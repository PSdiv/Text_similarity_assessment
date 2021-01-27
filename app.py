import numpy as np
from flask import Flask, request, jsonify, render_template
import model
import string 

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	
	corpus = [model.expand_contractions(x).translate(str.maketrans('', '', string.punctuation)) for x in request.form.values()]
	print(corpus)
	new_corpus =[]
	for line in corpus:
		new_line =[]
		for word in line.split():
			new_line.append(word.lower())
		new_corpus.append(" ".join(new_line))	
	print(new_corpus)
	Vocabulary, idf_of_vocabulary = model.fit(new_corpus)
	final_output = model.transform(new_corpus,Vocabulary,idf_of_vocabulary)
	output = round(model.cosine_sim(final_output[0],final_output[1]), 2)
    
	return render_template('index.html', prediction_text='Similarity is $ {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

	data = request.get_json(force=True)
	corpus =[]
	corpus.append(model.expand_contractions(data['text1']))
	corpus.append(model.expand_contractions(data['text2']))
    
	print(corpus)
	
	Vocabulary, idf_of_vocabulary = model.fit(corpus)
	final_output = model.transform(corpus,Vocabulary,idf_of_vocabulary)
	output = round(model.cosine_sim(final_output[0],final_output[1]), 2)
	
    
	return "similarity is "+ str(output) +". "
    
    
if __name__ == "__main__":
    app.run(debug=True)