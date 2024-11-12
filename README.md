# NLP Flask Sentiment Analysis

This project uses the sentiment analysis model from Hugging Face to evaluate the sentiment of a text, classifying it as either positive or negative. It utilizes Flask to create a web app where you can test the model. The app also uses HTML and JavaScript for the front-end. Additionally, there is a test script to check if the `sentiment_analyzer` function works as expected.

You can run the project locally or use Docker to test it.


## Requirements

- Python 3.7+
- Docker (if using the Docker setup)
- Dependencies listed in `requirements.txt`

## Running Locally

1. **Open Terminal**

    Navigate to the project directory:
    ```bash
    cd ~/nlp_flask/nlp-flask
    ```

2. **Create and Activate Virtual Environment**

    Create a virtual environment:
    ```bash
    python3 -m venv env
    ```

    Activate the virtual environment:
    ```bash
    source env/bin/activate
    ```

3. **Install Dependencies**

    Install the required packages from `requirements.txt`:
    ```bash
    cd nlp_flask
    python3 -m pip install -r requirements.txt
    ```

4. **Run the Application**

    Start the Flask application:
    ```bash
    cd nlp_flask
    python3 app.py
    ```

5. **Testing the Application**

    You can test the sentiment analysis in two ways:

    **Using cURL**:
    ```bash
    curl "http://localhost:5001/sentimentAnalyzer?textToAnalyze=I%20love%20using%20python%21"
    ```

    **Using a Web Browser**:
    Open the URL in a browser:  
    [http://localhost:5001](http://localhost:5001)

---

## Running with Docker

1. **Open Docker**

    Make sure Docker is running on your system.

2. **Navigate to the Docker Directory**

    Navigate to the project’s Docker directory:
    ```bash
    cd ~/nlp_flask/nlp-flask/docker
    ```

3. **Build Docker Image**

    Build the Docker image and start the application:
    ```bash
    docker compose up --build
    ```

4. **Access the Application**

    Open a browser and go to [http://localhost:5001](http://localhost:5001).

5. **Shutdown Docker**

    To shut down the Docker containers:
    ```bash
    docker compose down
    ```

---

## Additional Commands

- **View Active Ports**:
    ```bash
    lsof -i -P -n | grep LISTEN
    ```

- **View Specific Port (5001)**:
    ```bash
    lsof -i :5001
    ```

- **Kill Process on Port**:
    Find the Process ID (PID) and kill it:
    ```bash
    kill -9 <PID>
    ```
