import pandas as pd
import numpy as np
import math
#from tensorflow import keras

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
model = Sequential()
model.add(LSTM(128, input_shape=(1,10), return_sequences = True))
model.add(LSTM(128))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='tanh'))
model.add(Dense(1, activation='sigmoid'))
model.load_weights('model/model_oversampled250.h5')
#model = keras.models.load_model("model_oversampled250.h5")
def classify(x):
    if x <= 0.5:
        return 0
    else:
        return 1 

    
def sepsis(hr,o2sat,temp,sbp,map1,resp,gender,age,hospadmtime,iculos):
    X = [float(hr),float(o2sat),float(temp),float(sbp),float(map1),float(resp),float(gender),float(age),float(hospadmtime),float(iculos)]
    X_mean = [83.72276626338754, 96.83018891312972,36.61446499405063,123.04661877727092,82.62690784906772,18.90137532229274,61.64342324474379,0.5594506148353828,-51.84765965886919,39.01011503371678]
    X_std = [16.5302153248836,3.913998151342051,3.1449394226042457,24.17546288602834,16.42480213606982,4.791598816912431,16.48294561381705,0.4964591975794707,139.7649578409348,22.924640812712394]
    X = np.array(X)
    X_mean = np.array(X_mean)
    X_std = np.array(X_std)
    X=((X-X_mean)/X_std)
    X = X.reshape(1,1,10)
    y = model.predict(X)
    final_pred = np.array(list(map(classify, y)))
    return final_pred[0]