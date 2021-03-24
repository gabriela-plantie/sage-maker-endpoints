# README

This repo shows how to deploy models using docker and/or aws or heroku.

1) Deploying an __AWS__ built in algorithm.

I took the example from: 

https://github.com/krishnaik06/AWS-SageMaker/blob/master/Untitled2.ipynb

And updated it using:

+ https://sagemaker.readthedocs.io/en/stable/overview.html

+ https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#client


Running everything on AWS from local jupyter notebook.

Requirements:

+ `sagemaker`==2.29.0
+ aws client

2) Create __Docker__ with model (model.py, app.py and Dockerfile) and deploy it on __Heroku__
You can use Postman to test the app.
   

3) Create __Docker__ with a model and deploy it on __AWS__

I took the example from:
https://github.com/aws-samples/sagemaker-byo-catboost-container-demo/blob/master/Catboost_container_for_SageMaker.ipynb


4) Custom docker endpoint on AWS to train model

