from django.apps import AppConfig

#class ValidadoresConfig(AppConfig):
#    name = 'validadores'


#HY
import pandas as pd
import joblib
import pickle
import os

class MoviesConfig(AppConfig):
    name = 'movies'
    #pass


#HY
class PredictionConfig(AppConfig):
    name = 'prediction'

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CLASSIFIER_FOLDER = os.path.join(BASE_DIR, 'validadores/modelo/')
    CLASSIFIER_FILE = os.path.join(CLASSIFIER_FOLDER, "modelo")
    REAL_VECTOR = os.path.join(CLASSIFIER_FOLDER, "vocabulary.json")

    real_vectorizer = pickle.load(open(REAL_VECTOR, 'rb'))
    model = joblib.load(CLASSIFIER_FILE)