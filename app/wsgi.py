import socket
from flask import Flask


app = Flask(__name__)

container_id = socket.gethostname()
@app.route("/")
def home():
    return f"{container_id}: Hello, this is a simple flask application running in docker :)"


if __name__ == "__main__":
    app.run(debug=True)

