import numpy as np
import csv
import os
import pandas as pd
import pickle
default_model_path = '/opt/ml'

model_cache = {}

def load_model(algorithm, model_path):
    if model_cache.get(algorithm) is None:
        model_filename = os.path.join(model_path, 'model.pkl')
        with open(model_filename, newline='') as file:
            model_cache[algorithm] = pickle.load(open(model_filename, 'rb'))
    
    return model_cache[algorithm]


def __read_csv_list(filename):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        return list(reader)[0]
        
    return []

predictors_cache = {}

def load_predictors(algorithm, model_path):
    if predictors_cache.get(algorithm) is None:
        predictors_filename = os.path.join(model_path, 'predictors.csv')
        predictors_cache[algorithm] = __read_csv_list(predictors_filename)
            
    return predictors_cache[algorithm]

to_cat_cache = {}

def load_to_cat(algorithm, model_path):
    if to_cat_cache.get(algorithm) is None:
        to_cat_filename = os.path.join(model_path, 'to_cat.csv')
        to_cat_cache[algorithm] = __read_csv_list(to_cat_filename)
            
    return to_cat_cache[algorithm]


def predict(data, model_path = default_model_path):
    algorithm = "algorithm_catboost"
    
    model = load_model(algorithm, model_path)
    predictors = load_predictors(algorithm, model_path)
    to_cat = load_to_cat(algorithm, model_path)
    
    if data.shape[0] == 0:
        return pd.DataFrame()

    for x in to_cat:
        data[x] = data[x].astype(str)

    y_pred_probs = model.predict_proba( data[predictors].values )
    probabilities = [item[1] for item in y_pred_probs]
    data['pd'] = probabilities
    
    
    return data
