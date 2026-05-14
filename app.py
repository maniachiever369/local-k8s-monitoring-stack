import os
from flask import Flask

app = Flask(__name__)

VERSION = os.environ.get("APP_VERSION", "1.0.0")
ENV = os.environ.get("APP_ENV", "Production")


@app.route("/health")
def health():
    return {"status": "healthy", "version": VERSION}, 200


@app.route("/")
def home():
    return f"<h1>[Live Server] Running Version: {VERSION} ({ENV} Environment)</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
