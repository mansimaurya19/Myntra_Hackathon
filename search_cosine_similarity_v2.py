# -*- coding: utf-8 -*-
"""Search_cosine_similarity_v2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-ROMrzb5YZ3DCP5hcBkscAA0jmXz5Ymn
"""

import pandas as pd
import numpy as np
import re
import operator
import nltk 
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer

#nltk.download('punkt')
#nltk.download('wordnet')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('stopwords')

#df = pd.read_csv('/content/Myntra_dataset.csv')

df = pd.read_csv('Myntra_dataset.csv')
df.sample(5)

df['total_info'] = df['dominant_color'] + str(' ') +	df['product_type'] + str(' size ') + df['size']

df['total_info'] = df['total_info'].apply(lambda x: str(x).translate(str.maketrans('', '', string.punctuation)).lower())

df['size'] = df['size'].apply(lambda x: (str(x.lower())))

product = list(df['total_info'])

from sklearn.feature_extraction.text import TfidfVectorizer
import operator
## Create Vocabulary
vocabulary = set()
for doc in product:
    vocabulary.update(doc.split(' '))
vocabulary = list(vocabulary)
# Intializating the tfIdf model
tfidf = TfidfVectorizer(vocabulary=vocabulary)
# Fit the TfIdf model
tfidf.fit(product)
# Transform the TfIdf model
tfidf_tran=tfidf.transform(product)

def gen_vector_T(tokens):
  Q = np.zeros((len(vocabulary)))    
  x= tfidf.transform(tokens)
  
  for token in tokens[0].split(','):
      
      try:
          ind = vocabulary.index(token)
          Q[ind]  = x[0, tfidf.vocabulary_[token]]
      except:
          pass
  return Q

def cosine_sim(a, b):
    cos_sim = np.dot(a, b) / (np.linalg.norm(a)*np.linalg.norm(b))
    return cos_sim

def cosine_similarity_T(k, query):

    size = ''
    preprocessed_query = re.sub("\W+", " ", query.lower()).strip()
    preprocessed_query = ' '.join([word for word in preprocessed_query.split(' ')[2:]])
    words = preprocessed_query.split()
    if 'size' in words:
      size = words[words.index('size') + 1].lower()
    tokens = word_tokenize(str(preprocessed_query))
    d_cosines = []
    
    query_vector = gen_vector_T(tokens)
    for d in tfidf_tran.A:
        d_cosines.append(cosine_sim(query_vector, d))
                    
    out = np.array(d_cosines).argsort()[-k:][::-1]
    d_cosines.sort()
    df1 = pd.DataFrame()
    for i,index in enumerate(out):
        df1.loc[i,'unique_id'] = df['uniq_id'][index]
        df1.loc[i,'product_id'] = df['product_id'][index]
        df1.loc[i,'title'] = df['title'][index]
        df1.loc[i,'images'] = df['images'][index]
        df1.loc[i, 'dominant_color'] = df['dominant_color'][index]
        df1.loc[i,'size'] = df['size'][index]
        df1.loc[i,'product_type'] = df['product_type'][index]
    for j,simScore in enumerate(d_cosines[-k:][::-1]):
        df1.loc[j,'Score'] = simScore
    if size != '':
      return df1[df1['size']==size]
    else:
      return df1

#print(cosine_similarity_T(20, 'show me saree size onesize'))

#cosine_similarity_T(20, 'search for red kurta size L')

