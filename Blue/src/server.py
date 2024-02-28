from flask import Flask
import datetime 


app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello Worldskills!'

@app.route("/healthcheck")
def healthcheck():
    now = datetime.datetime.now()
    return {"status": "healthy", "logs": {"time": str(now)}}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
