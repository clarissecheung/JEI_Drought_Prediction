# -*- coding: utf-8 -*-
"""KNN_Drought_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hGu4bygSVBcwU30U2pIN5Un5uO6l_tka

Copyright (c) 2022 AIClub

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without 
limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of 
the Software, and to permit persons to whom the Software is furnished to do so, subject to the following 
conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO 
EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN 
AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
OR OTHER DEALINGS IN THE SOFTWARE.

Follow our courses - https://www.corp.aiclub.world/courses
"""

def launch_fe(dataset):
    import os
    import pandas as pd
    from io import StringIO
    import json
    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.feature_extraction import text
    import pickle
    from scipy import sparse
    MAX_TEXT_FEATURES = 200
    columns_list = ["score", "PRECTOT", "PS", "QV2M", "T2M", "T2MDEW", "T2MWET", "T2M_MAX", "T2M_MIN", "T2M_RANGE", "TS", "WS10M", "WS10M_MAX", "WS10M_MIN", "WS10M_RANGE", "WS50M", "WS50M_MAX", "WS50M_MIN", "WS50M_RANGE"]

    
    dataset = dataset[columns_list]
    num_samples = len(dataset)

    # Encode labels into numbers starting with 0
    label = "score"
    tmpCol = dataset[label].astype('category')
    dict_encoding = { label: dict(enumerate(tmpCol.cat.categories))}
    # Save the model
    model_name = "name"
    fh = open(model_name, "wb")
    pickle.dump(dict_encoding, fh)
    fh.close()

    label = "score"
    dataset[label] = tmpCol.cat.codes

    # Move the label column
    cols = list(dataset.columns)
    colIdx = dataset.columns.get_loc("score")
    print('colIdx ', colIdx)
    # Do nothing if the label is in the 0th position
    # Otherwise, change the order of columns to move label to 0th position
    if colIdx != 0:
        cols = cols[colIdx:colIdx+1] + cols[0:colIdx] + cols[colIdx+1:]
        dataset = dataset[cols]

    # split dataset into train and test
    train, test = train_test_split(dataset, test_size=0.2, random_state=42)

    # Write train and test csv
    train.to_csv('train.csv', index=False, header=False)
    test.to_csv('test.csv', index=False, header=False)
    column_names = list(train.columns)
def get_model_id():
    return "name"

from google.colab import drive
drive.mount('/content/drive', force_remount=True)
import numpy as np
import pandas as pd

import pandas as pd
# Launch FE
dataset = pd.read_csv('path')
launch_fe(dataset)

# import the library of the algorithm
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
# Load the test and train datasets
train = pd.read_csv('train.csv', skipinitialspace=True, header=None)
test = pd.read_csv('test.csv', skipinitialspace=True, header=None)
# Train the algorithm

for k in range(1,20):
  model = KNeighborsClassifier(n_neighbors=k)
  model.fit(train.iloc[:,1:], train.iloc[:,0])
  # calculate accuracy
  score = model.score(test.iloc[:, 1:], test.iloc[:, 0])
  # The value is returned as a decimal value between 0 and 1
  # converting to percentage
  accuracy = score * 100
  print('Accuracy of the model is: ', accuracy, ' for a K value of ', k)

def encode_confusion_matrix(confusion_matrix):
    import pickle
    encoded_matrix = dict()
    object_name = get_model_id()
    file_name = open(object_name, 'rb')
    dict_encoding = pickle.load(file_name)
    labels = list(dict_encoding.values())[0]
    for row_indx, row in enumerate(confusion_matrix):
        encoded_matrix[labels[row_indx]] = {}
        for item_indx, item in enumerate(row):
            encoded_matrix[labels[row_indx]][labels[item_indx]] = item
    return encoded_matrix

# Predict the class labels
y_pred = model.predict(test.iloc[:,1:])
# import the library to calculate confusion_matrix
from sklearn.metrics import confusion_matrix
# calculate confusion matrix
confusion_matrix = confusion_matrix(test.iloc[:,0], y_pred)
encoded_matrix = encode_confusion_matrix(confusion_matrix)
print('Confusion matrix of the model is: ', encoded_matrix)
# calculate accuracy
score = model.score(test.iloc[:, 1:], test.iloc[:, 0])
# The value is returned as a decimal value between 0 and 1
# converting to percentage
accuracy = score * 100
print('Accuracy of the model is: ', accuracy)

# fe_transform function traansforms raw data into a form the model can consume
print('Below is the prediction stage of the AI')
def fe_transform(data_dict, object_path=None):
    import os
    import pandas as pd
    from io import StringIO
    import json
    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.feature_extraction import text
    import pickle
    from scipy import sparse
    
    dataset = pd.DataFrame([data_dict])

    return dataset
def encode_label_transform_predict(prediction):
    import pickle
    encoded_prediction = prediction
    label = "score"
    object_name = "name"
    file_name = open(object_name, 'rb')
    dict_encoding = pickle.load(file_name)
    label_name = list(dict_encoding.keys())[0]
    encoded_prediction = \
        dict_encoding[label_name][int(prediction)]
    print(encoded_prediction)
def get_labels(object_path=None):
    label_names = []
    label_name = list(dict_encoding.keys())[0]
    label_values_dict = dict_encoding[label_name]
    for key, value in label_values_dict.items():
        label_names.append(str(value))

test_sample = {'PRECTOT': 59.1, 'PS': 85.325, 'QV2M': 49.615, 'T2M': 3.6899999999999977, 'T2MDEW': -3.2600000000000016, 'T2MWET': -2.860000000000001, 'T2M_MAX': 9.4, 'T2M_MIN': -3.629999999999999, 'T2M_RANGE': 14.945, 'TS': 4.684999999999999, 'WS10M': 8.365, 'WS10M_MAX': 10.685, 'WS10M_MIN': 6.745, 'WS10M_RANGE': 8.764999999999999, 'WS50M': 10.22, 'WS50M_MAX': 13.775, 'WS50M_MIN': 7.81, 'WS50M_RANGE': 11.205}
# Call FE on test_sample
test_sample_modified = fe_transform(test_sample)
# Make a prediction
prediction = model.predict(test_sample_modified)
encode_label_transform_predict(prediction)