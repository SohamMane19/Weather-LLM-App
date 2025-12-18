# Weather LLM App

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Node.js](https://img.shields.io/badge/Node.js-18-green.svg)](https://nodejs.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A web application that allows users to ask natural language queries about weather. It uses **FastAPI** for the backend, **LangChain + OpenRouter API** for LLM processing, and a **React** frontend for user interaction. The app integrates with **OpenWeather API** to fetch live weather data.

---

## 📂 Project Structure

```
weather-llm-app/
├── backend/
│   ├── main.py          # FastAPI entrypoint
│   ├── agent.py         # Query handling & agent logic
│   ├── tools.py         # Weather API tool
│   ├── api_keys.txt     # Optional file to store API keys
│   └── requirements.txt # Python dependencies
├── frontend/
│   ├── package.json
│   ├── package-lock.json
│   ├── public/
│   └── src/             # React source files
├── venv/                # Python virtual environment
├── scripts.txt          # Notes or helper scripts
└── README.md
```

---

## ✨ Features

- Ask natural language queries about weather in any city.
- LLM-powered reasoning using **LangChain**.
- Live weather updates fetched from **OpenWeather API**.
- React frontend with user-friendly interface.

---

## ⚡ Setup Instructions

### Backend Setup (FastAPI)

1. **Clone the repository**:

```bash
git clone <repo-url>
cd weather-llm-app
```

2. **Create & activate Python virtual environment**:

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. **Install backend dependencies**:

```bash
pip install -r backend/requirements.txt
```

4. **Set Environment Variables**:

You need **OpenWeather API Key** and **OpenRouter API Key**. Set them in your shell:

```bash
export OPENWEATHER_API_KEY="your_openweather_api_key"
export OPENROUTER_API_KEY="your_openrouter_api_key"
```

For Windows (PowerShell):

```powershell
$env:OPENWEATHER_API_KEY="your_openweather_api_key"
$env:OPENROUTER_API_KEY="your_openrouter_api_key"
```

5. **Run the backend server**:

```bash
cd backend
uvicorn main:app --reload
```

- Backend will run at: `http://127.0.0.1:8000`

---

### Frontend Setup (React)

1. **Navigate to frontend folder**:

```bash
cd frontend
```

2. **Install Node.js dependencies**:

```bash
npm install
```

3. **Start the React development server**:

```bash
npm start
```

- Frontend will run at: `http://localhost:3000`

---

## 📝 Usage

1. Open the frontend URL (`http://localhost:3000`) in a browser.
2. Type a query about weather, e.g.:  
   `"What is the current weather in Pune?"`
3. Submit and wait for the LLM-powered agent to respond with live weather info.

---

## ⚠️ Notes

- Ensure both backend and frontend servers are running simultaneously.
- Make sure your API keys are valid and have active usage limits.
- The system uses LangChain agent, which may sometimes hit iteration limits depending on query complexity.
- For issues with weather fetching, check your OpenWeather API key and network connectivity.

---

## 🛠 Dependencies

**Backend**:

- Python 3.12
- FastAPI
- Uvicorn
- Requests
- LangChain
- OpenRouter API

**Frontend**:

- Node.js 18+
- React
- Axios
- Additional libraries from `package.json`

---

## 📜 License

This project is licensed under the MIT License.

