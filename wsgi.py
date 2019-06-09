from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World, this a test commit!"

if __name__ == "__main__":
    application.run()
