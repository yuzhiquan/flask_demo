import json,os

from flask import Flask, request, jsonify
from redis import Redis
from rq import Queue

from tasks import write_log_file
from init_log import log

q = Queue(connection=Redis())
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
@app.route('/ping')
def hello_world():
	return 'pong'


@app.route("/api/v1/log", methods=["GET", "POST"])
def log_storage():
	if request.is_json:
                print json.dumps(request.json,indent=4)
		q.enqueue(write_log_file, json.dumps(request.json), "flask_demo_test.log")
	return jsonify({"err": "", "msg": "succ"})

@app.route("/api/v1/photo", methods=["GET","POST"])
def save_photo():
    if request.method == "POST":
        img=request.files.get("image")
        log.info(dir(img))
        img.save("./static/photo/"+img.filename)
        return jsonify({"msg":"succ"})
    elif request.method == "GET":
        return jsonify({"msg":"list"})


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8090)
