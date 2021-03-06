import pandas as pd
import pickle
import csv
import sys
import os
import io
import bjoern
import bottle
from bottle import run, request, post, get

# adds the model.py path to the list
model_path = os.path.dirname(os.getcwd())
if 'MODEL_PATH' in os.environ:
    model_path = os.environ['MODEL_PATH']

sys.path.insert(0,model_path)

import model

@get('/ping')
def ping():
    return "Ok"

@post('/invocations')
def invoke():
    # load image from POST and convert it to json
    try:
        print(f"request received: \n\t content size = {request.content_length}\n\t content type = {request.content_type}")
        req = request.body

        data = pd.read_csv(req, sep=',', low_memory=False, error_bad_lines=False)
        print(f"request received: dataframe size = {data.shape}")
        predictions = model.predict(data, model_path)
        print(f"request received: prediction done!")
        
        return predictions.to_csv(sep=',', index=False)
    except Exception as e:
        print(f"Error: {str(e)}" )
        print("Unexpected error:", sys.exc_info())
        return bottle.HTTPResponse(status=500)
    

if __name__ == '__main__':
    
    if len(sys.argv) == 2 and ( not sys.argv[1] in [ "serve", "train"] ):
        raise Exception("Invalid argument: you must inform 'train' for fake training mode or 'serve' predicting mode") 

    train = len(sys.argv) == 2 and (sys.argv[1] == "train")
    
    if train:
        print("copy local model")
        try:
            os.makedirs('/opt/ml/model/', exist_ok=True)
            shutil.copy2('/opt/program/model.pkl', '/opt/ml/model/model.pkl')
        except Exception as e:
            print(e)
            
                
        print( "Fake training completed" )
    else:
        print("Server started")
        if 'PORT' in os.environ: 
            port = int(os.environ['PORT'])
        else:
            port = 8080
        
        print(f"Port: {port}")
        print(f"Model path: {model_path}")
        bjoern.run(bottle.app(), "0.0.0.0", port)
        
        
