'''
Dependencies
'''
from flask import Flask, request, render_template
from src.SentimentAnalysis.sentiment_analisys import sentiment_analyzer

app = Flask(__name__)


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    '''
    This code receives the text from the HTML interface and runs sentiment analysis over it using
    sentiment_analyzer() function. The output returned shows the label and its confidence score for
    the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)

    # Extract the label and score from the response
    label = response[0]['label']  # Assuming response is a list
    score = response[0]['score']   # Assuming response is a list

    # Check if label / score is None
    if label is None:
        return "Invalid input! Please try again"

    # Return a formatted string with the sentiment label and score
    return f"The given text has been identified as {label} with a score of {score}."


@app.route("/")
def render_index_page():
    '''
    This function initiates the rendering of the main application page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
