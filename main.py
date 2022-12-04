import json
from database import jobList
from flask import Flask, request, make_response

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

def ok(data):
  response = make_response(json.dumps(data), 200)
  response.headers['Content-Type'] = 'application/json'
  return response

def getFilteredJobsWithTags(jobList, tags):
  return [job for job in jobList if set(tags).issubset(set(job['tags']))]

@app.route('/jobs', methods=['GET'])
def get_jobs():
  tags = request.args.get('tags')
  if tags:
    return ok(getFilteredJobsWithTags(jobList, tags.split(',')))
  return ok(jobList)

app.run()
