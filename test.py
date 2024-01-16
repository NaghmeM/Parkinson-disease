import requests
import json
import numpy as np

patient = {'Av_vocal_freq': 201.464, 'Max_vocal_freq': 210.565, 'Min_vocal_freq': 195.708, 'Jitter_%_freq': 0.00198, 'Jitter_Abs_freq': 1e-05, 'RAP_freq': 0.00106, 'PPQ_freq': 0.00115, 'DDP_freq': 0.00314, 'Shimmer_Amp': 0.01194, 'Shimmer_dB': 0.107, 'APQ3_Amp': 0.00586, 'APQ5_Amp': 0.0076, 'APQ_Amp': 0.00957, 'DDA_Amp': 0.01758, 'NHR': 0.00135, 'HNR': 31.732, 'RPDE': 0.344252, 'Signal_scale': 0.742737, 'spread1': -7.777685, 'spread2': 0.170183, 'D2': 2.447064, 'PPE': 0.05761}




url = 'http://localhost:9696/predict'
response = requests.post(url, json=patient)
result = response.json()

print(json.dumps(result, indent=2))