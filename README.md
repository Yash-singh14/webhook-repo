# GitHub Webhook Listener – Developer Assessment (Atidan)

This project is part of the Atidan Developer Assessment. It is designed to listen to GitHub Webhook events (like Push, Pull Request, and Merge), store them in MongoDB, and display them on a live UI that updates every 15 seconds.

---

## 🚀 Features

- Receives GitHub Webhook events (`push`, `pull_request`)
- Extracts details like author, branches, and timestamp
- Saves events in MongoDB
- Displays activity in real time on the frontend
- Frontend updates every 15 seconds

---

## 🛠 Technologies Used

- **Python + Flask** – Backend API
- **MongoDB** – Database for storing events
- **HTML + JavaScript** – Frontend UI
- **Ngrok** – To expose local server to the internet
- **GitHub Webhooks** – To send repo events

---

## ⚠ Problem Faced & Solution

### ❌ Problem:
GitHub Webhooks require a public URL. Initially, we used:
http://127.0.0.1:5000/webhook


But GitHub responded with:
> "Payload URL is not supported because it isn't reachable over the public Internet."

### ✅ Solution:
We used **Ngrok** to tunnel our local Flask server to the public internet.

#### Steps:
1. Run Flask app locally: `python app.py`
2. In another terminal, start ngrok:
`ngrok http 5000`

3. Ngrok gives a public URL like:`https://your-ngrok-url.ngrok-free.app`
4. We used this URL in GitHub’s Webhook settings as: `https://your-ngrok-url.ngrok-free.app/webhook`

---

## 📂 Project Structure

webhook-repo/
├── app.py # Flask server logic
├── requirements.txt # Python dependencies
└── templates/
└── index.html # Frontend UI (auto-refreshes every 15s)


---

## 🧪 How to Run

### Prerequisites:
- Python 3
- MongoDB (local or Atlas)
- Ngrok

### Setup:

```bash
git clone https://github.com/yourusername/webhook-repo.git
cd webhook-repo
python -m venv venv
venv\Scripts\activate        # or source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## 🌐 Start Ngrok

To expose your local Flask server to GitHub:

```bash
ngrok http 5000
```
This will generate a public URL like:
`https://your-ngrok-url.ngrok-free.app`

## ⚙️ Webhook Setup in GitHub

1. Go to **Settings > Webhooks** in your `action-repo`

2. Set the **Payload URL** to:https://your-ngrok-url.ngrok-free.app/webhook

3. Set **Content type** to:`application/json`

4. Select the events:
- ✅ Push
- ✅ Pull Requests

5. Click **“Add Webhook”** to save the configuration.

---

## 💻 Frontend UI

- Open in your browser:
- `http://localhost:5000/` **(for local testing)**
- `https://your-ngrok-url.ngrok-free.app` **(for live testing via ngrok)**

- The activity log updates every 15 seconds and displays messages like:
- `User pushed to main on [date]`
- `User submitted a pull request from [branch] to [main] on [date]`
- `User merged branch [branch] to main on [date]`

---

## 👨‍💻 Author

**Yash Singh Kushwaha** 
B.Tech in Artificial Intelligence and Machine Learning  
Final Year Student







