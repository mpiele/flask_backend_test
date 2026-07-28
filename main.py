from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/api/message")
def message_test():
    return {
        "text": "refresh test"
    }

if __name__ == "__main__":
    app.run(debug=True)