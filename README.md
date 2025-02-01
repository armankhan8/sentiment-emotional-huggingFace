# Sentiment Analysis and Emotion Detection
A web-based application that performs Sentiment Analysis and Emotion Detection on user-inputted text using pre-trained models from Hugging Face's transformers library. The application uses Flask as the backend framework to provide real-time results for sentiment and emotional analysis.

# Features
Sentiment Analysis: Classifies text as positive, negative, or neutral.
Emotion Detection: Detects emotions such as joy, sadness, anger, fear, and surprise.
Easy-to-use interface for inputting text and getting results instantly.

# Technologies Used
Python (Flask framework)
Hugging Face Transformers (for sentiment and emotion detection models)
JavaScript (for frontend functionality)
HTML/CSS (for frontend layout and design)
Requirements
Python 3.7+

# Install required dependencies using pip:

pip install -r requirements.txt

requirements.txt:
flask==2.0.1
transformers==4.9.2
torch==1.9.0


Project Setup
Clone the repository:
git clone https://github.com/yourusername/sentiment-emotion-analysis.git
cd sentiment-emotion-analysis

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows


Install the dependencies:
pip install -r requirements.txt

Run the Flask app:
python app.py
Open the app in your browser at http://127.0.0.1:5000/.

How It Works
Sentiment Analysis:

The user inputs a text in the textarea.
The user clicks the "Sentiment Analysis" button, which sends the text to the backend (Flask app) via a POST request.
The Flask backend processes the text using a pre-trained Hugging Face model (e.g., BERT or DistilBERT).
The result is returned to the frontend and displayed as positive, negative, or neutral.
Emotion Detection:

The user inputs text and clicks the "Emotion Detection" button.
The text is sent to the backend, where it is analyzed by an emotion detection model.
The application returns the detected emotions and their confidence scores (e.g., joy, sadness, anger, etc.) as a percentage.

Example Input & Output
Sentiment Analysis:
Input: "I am so happy with the product! Totally worth the money."
Output: Positive Sentiment
Emotion Detection:
Input: "I feel so lonely and sad today."
Output:
yaml
Copy
Edit
Emotions detected:
- Sadness: 85%
- Joy: 10%
- Fear: 3%
