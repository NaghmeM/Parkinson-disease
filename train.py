
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier



df=pd.read_csv("Parkinsson disease.csv")
df.rename (columns = ({
'MDVP:Fo(Hz)':'Av_vocal_freq',
'MDVP:Fhi(Hz)': 'Max_vocal_freq' ,
'MDVP:Flo(Hz)':'Min_vocal_freq',
'MDVP:Jitter(%)':'Jitter_%_freq','MDVP:Jitter(Abs)':'Jitter_Abs_freq','MDVP:RAP':'RAP_freq','MDVP:PPQ':'PPQ_freq','Jitter:DDP' :'DDP_freq',
'MDVP:Shimmer':'Shimmer_Amp','MDVP:Shimmer(dB)':'Shimmer_dB','Shimmer:APQ3':'APQ3_Amp','Shimmer:APQ5':'APQ5_Amp','MDVP:APQ':'APQ_Amp','Shimmer:DDA':'DDA_Amp',
'DFA':'Signal_scale'}),inplace=True)
df.drop('name' , axis = 1 ,inplace = True)
X = df.drop("status", axis=1)
y = df["status"]
transform = preprocessing.StandardScaler()
X_scaled = transform.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=1)

model = KNeighborsClassifier(algorithm='auto', n_neighbors=1, p=2)
model.fit(X_train, y_train) 


def predict(X , model):
    X = transform.fit_transform(X)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred


output_file = 'model.pkl'
with open(output_file, 'wb') as f_out:
    pickle.dump(model, f_out)

print(f'The model is saved to {output_file}')