from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    # 0.0.0.0 allows the web app platform to route traffic to this app.
    # Use the PORT environment variable when the platform provides one.
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
