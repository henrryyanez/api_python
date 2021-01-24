
import pandas as pd
import numpy as np
import re

import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
from nltk import word_tokenize
from nltk.corpus import stopwords

# HY
from .models import Validator
from .views import *
from rest_framework.response import Response

from .apps import PredictionConfig

def validador(texto, restante):

	test = [texto]
	test = pd.DataFrame(test, columns=['text'])

	#Texto sin caracteres especiales
	text_SC = [ re.sub('[^A-Za-z0-9\s]|\s+?([a-zA-Z]{1})\s+',' ', str(t)) for t in test.text]
	test['text2'] = text_SC

	#Analisis de business
	li=[]
	for t in test.text.tolist():
		if re.search('money',str(t)):
			li.append(1)
		else:
			li.append(0)
		
	test['money'] = np.array(li)

	##Tokenizacion sin stopwords
	stopwords_english = set(stopwords.words('english')) 

	lo = []

	for t in test.text2:
		word_tokens = nltk.word_tokenize(str(t), language='english')
		filtered_sentence = []
		stop_words = []
		text_ssw = ''
		for w in word_tokens: 
			if w not in stopwords_english:
				filtered_sentence.append(w)
				text_ssw = text_ssw + " " + w
			else:
				stop_words.append(w)
		filtered_sentence = list(dict.fromkeys(filtered_sentence))    
		lo.append(len(stop_words))

	test['Q_StopWords'] = np.array(lo)

	#Cantidad de veces que figura www
	li=[]
	for t in test.text.tolist():
		li.append(len(re.findall("z*",str(t))))
		    
	test['Q_zzz'] = np.array(li)

	###################################### Implementacion de Countvectorizer#####################################

	real_vectorizer = PredictionConfig.real_vectorizer
	test_X = real_vectorizer.transform(test.text)

	CV = pd.DataFrame(test_X.toarray())

	x=test[['money','Q_StopWords','Q_zzz']]
	X= pd.concat([x,CV], axis=1, join='outer')

	###MODELOS DE CLASIFICACION

	model = PredictionConfig.model

	if model.predict(X)[0]	== 1:
		return {"result":"SPAM","status":"ok", "restante": restante}
	else:
		return {"result":"HAM","status":"ok", "restante": restante}