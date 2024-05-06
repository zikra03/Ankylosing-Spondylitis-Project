# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle 

# loading the saved models
AS_model = pickle.load(open('C:/Users/Zikra/AS project/AS_model (3).sav', 'rb')) 

input_data = (1,40,1,10,9,10,1,1,0,1) # changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)
# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = AS_model.predict(input_data_reshaped)
print(prediction)
if (prediction[0] == 0):
  print('The person does not have AS')
else:
  print('The person has AS')