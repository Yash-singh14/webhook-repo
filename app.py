from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from flask_cors import CORS
import datetime
import os

app = Flask(__name__)
CORS(app)

# MongoDB Connection
try:
    client = MongoClient("mongodb://localhost:27017/")  # Or MongoDB Atlas URL
    db = client["webhook_db"]
    collection = db["events"]
    print("✅ Connected to MongoDB")
except Exception as e:
    print("❌ MongoDB connection failed:", e)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        event = request.headers.get('X-GitHub-Event')

        if event == "push":
            collection.insert_one({
                "type": "push",
                "author": data["pusher"]["name"],
                "to_branch": data["ref"].split("/")[-1],
                "timestamp": datetime.datetime.utcnow()
            })

        elif event == "pull_request":
            pr = data["pull_request"]
            collection.insert_one({
                "type": "pull_request",
                "author": pr["user"]["login"],
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "merged": pr["merged"],
                "timestamp": datetime.datetime.utcnow()
            })

        return "Webhook received", 200
    except Exception as e:
        print("❌ Error processing webhook:", e)
        return "Webhook error", 500

@app.route('/get-events', methods=['GET'])
def get_events():
    try:
        events = list(collection.find().sort("timestamp", -1))
        for e in events:
            e["_id"] = str(e["_id"])
        return jsonify(events)
    except Exception as e:
        print("❌ Error fetching events:", e)
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
