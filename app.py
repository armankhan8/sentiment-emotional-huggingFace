from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Initialize the Hugging Face models
sentiment_analyzer = pipeline("sentiment-analysis")
emotion_analyzer = pipeline("zero-shot-classification")

@app.route('/', methods=['GET', 'POST'])
def analyze_text():
    result = None
    if request.method == 'POST':
        input_text = request.form['inputText']
        analysis_type = request.form['analysis_type']
        
        if analysis_type == 'sentiment':
            # Perform sentiment analysis
            result = sentiment_analyzer(input_text)
            result = f"Sentiment: <strong>{result[0]['label']}</strong> (Confidence: {round(result[0]['score']*100, 2)}%)"
        
        elif analysis_type == 'emotion':
            # Perform emotion detection (using zero-shot classification as an example)
            candidate_labels = ['joy', 'anger', 'fear', 'sadness', 'surprise']
            result = emotion_analyzer(input_text, candidate_labels)
            
            # Create a list of emotions sorted by score
            sorted_emotions = sorted(zip(result['labels'], result['scores']), key=lambda x: x[1], reverse=True)
            
            result_text = "<strong>Emotions detected:</strong><br>"
            for label, score in sorted_emotions:
                result_text += f"<strong>{label.capitalize()}:</strong> {round(score * 100, 2)}% <br>"
            result = result_text

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
