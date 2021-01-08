# Submission for the Emerging technologies project 2020
### How to run:
#### Web service:
set FLASK_APP=webservice.py
python -m flask run
#### Docker container
docker build -t power-predictions-image
docker run --name power-predictions-container -d -p 5000:5000 power-predictions-image
#### Model
Open the PowerPredictions.ipynb file and read through it. There is a graph of the predictions for power based on the model that was trained.

### Limitations:
I was unable to get the model to predict the power in my web server so the web server takes in a speed value and spits out a power value that is made up.
