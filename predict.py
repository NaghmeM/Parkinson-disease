import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model.pkl'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

app = Flask('predict')

@app.route('/predict', methods=['POST'])



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)