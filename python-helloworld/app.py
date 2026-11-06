from flask import Flask
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('helllo success')
    return "Hello World!"
@app.route("/status")
def status():
    app.logger.info('fetch success')
    return {"status":"Ok-healthy"},200
@app.route("/metrics")
def metrics():
    app.logger.info('metri success')
    return {"UserCount":140,"UserCountActive":23,"status":"success"},200


if __name__ == "__main__":

    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0',)
