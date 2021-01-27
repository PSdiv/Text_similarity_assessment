# import required packages
import re
import numpy as np
from collections import Counter
import math
import string


# Contraction Map
CONTRACTION_MAP = {
"ain't": "is not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how is",
"I'd": "I would",
"I'd've": "I would have",
"I'll": "I will",
"I'll've": "I will have",
"I'm": "I am",
"I'm" : "I am",
"I've": "I have",
"i'd": "i would",
"i'd've": "i would have",
"i'll": "i will",
"i'll've": "i will have",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so as",
"that'd": "that would",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what'll've": "what will have",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"when's": "when is",
"when've": "when have",
"where'd": "where did",
"where's": "where is",
"where've": "where have",
"who'll": "who will",
"who'll've": "who will have",
"who's": "who is",
"who've": "who have",
"why's": "why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you would",
"you'd've": "you would have",
"you'll": "you will",
"you'll've": "you will have",
"you're": "you are",
"you've": "you have"
}

# Function for expanding contractions from the given text
def expand_contractions(text, contraction_mapping=CONTRACTION_MAP):

    contractions_pattern = \
        re.compile('({})'.format('|'.join(contraction_mapping.keys())),
                   flags=re.IGNORECASE | re.DOTALL)

    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = \
            (contraction_mapping.get(match) if contraction_mapping.get(match) else contraction_mapping.get(match.lower()))
        expanded_contraction = first_char + expanded_contraction[1:]
        return expanded_contraction

    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", '', expanded_text)
    return expanded_text

def preprocess_text(corpus):
    # Expand Contractions and remove punctuations
    corpus = [expand_contractions(x).translate(str.maketrans('', '', string.punctuation)) for x in corpus]
    new_corpus =[]
    for line in corpus:
        new_line =[]
        for word in line.split():
            new_line.append(word.lower())
        new_corpus.append(" ".join(new_line))    
    return new_corpus 
    
    

# Metric for similarity calculation
def cosine_sim(a, b):
    cos_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    return cos_sim

# Inverse Document frequency calculation for words
def InverseDocumentfrequency(corpus, unique_words):
    idf_dict = {}
    N = len(corpus)
    for i in unique_words:
        count = 0
        for sen in corpus:
            if i in sen.split():
                count = count + 1
            idf_dict[i] = math.log((1 + N) / (count + 1)) + 1
    return idf_dict

# Generating vocabulary and IDF values for words in the corpus
def fit(whole_data):
    unique_words = set()
    if isinstance(whole_data, (list, )):
        for x in whole_data:
            for y in x.split():
                if len(y) < 2:
                    continue
                unique_words.add(y)
        unique_words = sorted(list(unique_words))
        vocab = {j:i for i,j in enumerate(unique_words)}
        Idf_values_of_all_unique_words=InverseDocumentfrequency(whole_data,unique_words)
    return vocab, Idf_values_of_all_unique_words
# Function for normalizing tf-idf vectors 
def normalized(a, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2 == 0] = 1
    return a / np.expand_dims(l2, axis)

# Creating TF-IDF vectors for each sentence 
def transform(dataset, vocabulary, idf_values):
    sparse_matrix = np.zeros((len(dataset), len(vocabulary)),
                             dtype=np.float64)
    for row in range(0, len(dataset)):
        number_of_words_in_sentence = Counter(dataset[row].split())
        for word in dataset[row].split():
            if word in list(vocabulary.keys()):
                tf_idf_value = number_of_words_in_sentence[word] \
                    / len(dataset[row].split()) * idf_values[word]
                sparse_matrix[row, vocabulary[word]] = tf_idf_value

    #  print("NORM FORM\n",normalize(sparse_matrix, norm='l2', axis=1, copy=True, return_norm=False))
    #  print("NORM FORM\n",normalized(sparse_matrix))

    output = normalized(sparse_matrix)
    return output

def predict(corpus):
    
    Vocabulary, idf_of_vocabulary = fit(corpus)
    final_output = transform(corpus,Vocabulary,idf_of_vocabulary)
    output = round(cosine_sim(final_output[0],final_output[1]), 2)
    return output
    
    
    
    
    
    
    
    
    
    
    
