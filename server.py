from flask import Flask, render_template
import datetime 


app = Flask(__name__)

@app.route('/') 
def hello():
    return 'Hello Worldskills! v1'

@app.route('/dog')
def dog():
    return render_template('dog.html')

@app.route('/healthcheck')
def healthckeck():
    now = datetime.datetime.now()
    return {"status": "healthy", "logs": {"time": str(now)}}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)