# DevConnect - Mini Social Feed 🌐

DevConnect is a simple **social feed web app** built using **FastAPI** + **Jinja2**. Users can post short messages and see them instantly on the homepage.

🚀 Live Demo: [https://connect-m6dm.onrender.com](https://connect-m6dm.onrender.com)

---

## ✨ Features
- 📝 Post messages instantly via a form.
- 💾 Stores messages in memory (you can extend to use DB).
- 🎨 Responsive frontend using basic HTML, CSS, and JavaScript.
- ⚡ FastAPI-powered backend with HTML templating.
- 🌀 Deployed on [Render](https://render.com).

---

## 🛠 Tech Stack
| Frontend     | Backend   | Deployment | Template Engine |
|--------------|-----------|------------|-----------------|
| HTML, CSS, JS | FastAPI   | Render     | Jinja2          |

---

## 📁 Project Structure

```

backend/
├── main.py                  # FastAPI app
├── templates/               # HTML pages
│   ├── index.html
│   └── new\_post.html
├── static/                  # CSS and JS files
│   ├── style.css
│   └── main.js
├── requirements.txt         # Python dependencies
└── render.yaml              # Render deployment config

````

---

## 🚀 Local Development

### Prerequisites:
- Python 3.8+
- `pip` installed

### Setup:
bash
# Clone the repo
git clone https://github.com/Jahnavi-9741/devconnect.git
cd devconnect/backend

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload


Then visit 👉 `http://127.0.0.1:8000` in your browser.

---

## 🌍 Deployment on Render

This app is deployed on [Render](https://render.com). To redeploy:

1. Push changes to `main` branch on GitHub.
2. Render auto-triggers deployment using `render.yaml`.

---

## 🤝 Contributing

Want to enhance this? Open an issue or pull request! You can:

* Add a database (e.g., SQLite or PostgreSQL)
* Add user authentication
* Add session-based message storage

---

## 📜 License

MIT License. Feel free to use and modify.

---

### 💡 Made with 💻 by Jahnavi Reddy




