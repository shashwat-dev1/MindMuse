
# 🧠 MindMuse – 5-in-1 Creativity Tool

MindMuse is a web-based app that helps you generate creative project ideas, subtopics, pitches, and more using Cohere's AI APIs.

## 🎯 Features

✅ Generate 5 unique project ideas for any topic  
✅ Find related subtopics to expand research  
✅ Write a short elevator pitch automatically  
✅ Discover real-world problems in your chosen domain  
✅ Get project recommendations to build next  

## 🛠 Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- AI: Cohere NLP API

## 🚀 Live Demo

*(You can deploy using Replit or Render and put the link here)*

## 📂 Project Structure

```
MindMuse/
├── app.py            # Flask routes
├── cohere_api.py     # Cohere API calls
├── requirements.txt  # Python dependencies
├── Procfile          # Process declaration for deployment
├── static/
│   ├── style.css
│   └── bg.jpg
├── templates/
│   └── index.html
```

## 🖥️ Running Locally

1. Clone the repository:
   ```
   git clone https://github.com/shashwat-dev1/MindMuse.git
   cd MindMuse
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   python app.py
   ```
4. Open your browser at `http://127.0.0.1:5000`

## 🌐 Deployment

This project is ready to deploy on Render or Replit.

Create a `Procfile` with:
```
web: gunicorn app:app
```

## ✨ Future Enhancements

- Voice input
- Dark mode toggle
- Export to PDF
- User login & history

---

🙌 **Developed by Shashwat Jain and Ayushi Majumdar**
