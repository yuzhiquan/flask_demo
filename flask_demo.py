import json

from flask import Flask, request, jsonify
from redis import Redis
from rq import Queue

from tasks import write_log_file

q = Queue(connection=Redis())
app = Flask(__name__)


@app.route('/ping')
def hello_world():
	return 'pong'


@app.route("/api/v1/log", methods=["GET", "POST"])
def log_storage():
	if request.is_json:
		q.enqueue(write_log_file, json.dumps(request.json), "flask_demo_test.log")
	return jsonify({"err": "", "msg": "succ"})


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8090)
