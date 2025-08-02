# CuriousAI

A smart assistant capable of searching and crawling the internet. This project is a full-stack application with a Python backend and a SAP Fiori/UI5 frontend.

## Backend

The backend is a Python-based application using the FastAPI framework. It leverages LangChain and the Tavily API for its core functionality.

### Prerequisites

- Python 3.6+
- Pip

### Setup and Running

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```
2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment:**
    - **On Windows:**
      ```bash
      .\venv\Scripts\activate
      ```
    - **On macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```
4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Create a `.env` file** in the `backend` directory and add your Tavily and Google API keys:
    ```
    TAVILY_API_KEY="your_tavily_api_key"
    GOOGLE_API_KEY="your_google_api_key"
    ```
6.  **Run the application:**
    ```bash
    uvicorn app.main:app --reload
    ```

The backend will be running at `http://127.0.0.1:8000`.

## Frontend

The frontend is a SAP Fiori/UI5 application.

### Prerequisites

- Node.js
- npm

### Setup and Running

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```
2.  **Install the dependencies:**
    ```bash
    npm install
    ```
3.  **Run the application:**
    ```bash
    npm start
    ```

The frontend will be running at `http://localhost:8080`.
