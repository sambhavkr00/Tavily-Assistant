# CuriousAI

A smart assistant capable of searching and crawling the internet. This project is a full-stack application with a Python backend and a SAP Fiori/UI5 frontend, designed to be deployed as standalone applications.

## Local Development

### Backend

The backend is a Python-based application using the FastAPI framework. It leverages LangChain and the Tavily APIs for its core functionality.

#### Prerequisites

- Python 3.6+
- Pip

#### Setup and Running

1.  **Navigate to the backend directory:**
    ```bash
    cd curious-ai-backend
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
5.  **Create a `.env` file** in the `curious-ai-backend` directory and add your Tavily and Google API keys:
    ```
    TAVILY_API_KEY="your_tavily_api_key"
    GOOGLE_API_KEY="your_google_api_key"
    ```
6.  **Run the application:**
    ```bash
    uvicorn app.main:app --reload
    ```

The backend will be running at `http://127.0.0.1:8000`.

### Frontend

The frontend is a SAP Fiori/UI5 application.

#### Prerequisites

- Node.js
- npm

#### Setup and Running

1.  **Navigate to the frontend directory:**
    ```bash
    cd curious-ai-frontend
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

## Cloud Foundry Deployment (Standalone)

This project is designed to be deployed to Cloud Foundry as two separate, standalone applications.

### 1. Deploy the Backend

1.  **Navigate to the backend directory:**
    ```bash
    cd curious-ai-backend
    ```
2.  **Deploy to Cloud Foundry:**
    ```bash
    cf push curious-ai-backend --random-route
    ```
3.  **Set Environment Variables:**
    ```bash
    cf set-env curious-ai-backend GOOGLE_API_KEY "your_google_api_key"
    cf set-env curious-ai-backend TAVILY_API_KEY "your_tavily_api_key"
    ```
4.  **Restage the Application:**
    ```bash
    cf restage curious-ai-backend
    ```
5.  **Get the Backend URL:** Note the URL for the deployed backend application.

### 2. Deploy the Frontend

1.  **Update the Backend URL:**
    - Open `curious-ai-frontend/webapp/controller/App.controller.js`.
    - Replace `<your-backend-url>` with the actual URL of your deployed backend.
2.  **Build the Frontend:**
    - Navigate to the `curious-ai-frontend` directory.
    - Run `npm install` and then `npm run build`.
3.  **Deploy the Frontend:**
    - Deploy the contents of the `curious-ai-frontend/dist` directory to a static file hosting service (e.g., Netlify, Vercel, or Cloud Foundry with a staticfile buildpack).
