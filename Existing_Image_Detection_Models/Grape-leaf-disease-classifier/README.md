# grapeleaf-disease-classifier-flaskapp

## Introduction
This flask-app is an implementation of the Grape-leaf disease Image classifier.
This app exposes an API to use this image classifier to identify the disease of the grape leaf.

### Prerequisites
Ohter than configuration files, the trained-model should be present in the project folder. Download trained-model from  [Trained-model for leaf-disease-classifier](https://drive.google.com/open?id=1Hstw29i4Ccg0KqhB3wlhnd0W2_3qxlsT).</br>
```lable.pkl``` file has class-labels of the disease-types.

### Deployment
```manifest.yml```, ```requirements.txt```, ```runtime.txt``` and ```Procfile``` are the files which contains deployment and dependencies configurations.
For deploying this app on cloud foundry use: ```cf push```

### Testing the API
To use this API make a POST call from rest-client with the input file.
The body of the post call should contain ```key: file``` and ```value:``` should be uploaded file.
Append ```/disease``` to the app's URL to make a call to this API, otherwise it will not work.
