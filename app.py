import numpy as np
from flask import Flask, request, jsonify, render_template
import model

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	
	corpus = [x for x in request.form.values()]
	
	corpus = model.preprocess_text(corpus)
	output = model.predict(corpus)
    
	return render_template('index.html', prediction_text='Similarity is {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

	data = request.get_json(force=True)
	corpus =[]
	corpus.append(data['text1'])
	corpus.append(data['text2'])
    
	corpus = model.preprocess_text(corpus)
	output = model.predict(corpus)
	
	return "similarity is "+ str(output) +". "
    
    
if __name__ == "__main__":
    app.run(debug=True)