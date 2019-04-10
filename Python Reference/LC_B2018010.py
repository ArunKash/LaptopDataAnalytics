# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:29:35 2019

@author: GIM
"""
## python
import pandas as pd
from collections import  Counter
import numpy as np
import string
from random import *
import scipy.stats as stat
from sklearn import datasets, linear_model, metrics 
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

import statsmodels.api as sm

import statsmodels.formula.api as smf

#Question 1


## Implementing Summation Function
data = {}
for x in range(1, 101):
    f = 0
    for n in range(1, 1000):
        func = np.round((np.e**-n)/(n**x), 5)
        f = f + func
    data.__setitem__(x, f)

print(data)


# Question 2

#C:\Users\GIM\Downloads\Datasets_for_the_exam\trees.csv
"""
out = pd.cut(d["Height"], bins=[0, 60, 70, 80, 90], include_lowest=False)
print(out)
d["Bin"] = out
"""
## Read a Data Set
d =  pd.read_csv(r'C:\Users\GIM\Downloads\Datasets_for_the_exam\trees.csv')
print(d.head())

## Making into Bins
out = pd.cut(d["Height"], bins=[0, 60, 70, 80, 90], include_lowest=False)
print(out)
d["Bin"] = out

## Creating a table
out = d.pivot_table(index= 'Bin', values='Girth')
print(out['Girth'])

## barplot by pivot table 
out.plot(kind="bar")

## Question 3

## Random Password Generation
import string
from random import *
N = 10
characters = string.ascii_letters + string.punctuation  + string.digits

Letter =  "".join(choice(string.ascii_letters) for x in range(randint(1, N)))
SPL =  "".join(choice(string.punctuation) for x in range(randint(1, N)))
Numbr =  "".join(choice(string.digits) for x in range(randint(1, N)))
password1 = Letter+ SPL+ Numbr
print (password1)

## Question 4

import random

step = random.randint(0,1)
times = [0]*11

def drunk_walk(x):
    "How drunk walks"
    #start at the middle times[5]
    x = step
    times[5] +=1
    position = 5
    P = times[position]
    while (times[0] or times[-1]) != 1:        
        if step == 0:
            position = position -1
            times[position] += 1
            print ("drunk steps to the left")
            print (times, position)
        else:
            position = position + 1
            times[position] += 1
            print ("drunk steps to the right")
            print (times, position)

sim = drunk_walk(step)
print (sim)



## Question 5
df = pd.read_csv(r'C:\Users\GIM\Downloads\Datasets_for_the_exam\carseats.csv')
##Sales~CompPrice+Income+Advertising+Price+ShelveLoc.Bad+ShelveLoc.Good+Age

### Making Dummy variables for columns to columns
for elem in df['ShelveLoc'].unique():
    df[str(elem)] = df['ShelveLoc'] == elem


## using Stats model to fit a linnear regession
smf_ols_fit = smf.ols(formula = 'Sales~CompPrice+Income+Advertising+Price+Bad+Good+Age', data = df).fit()


## Model Summary
print(smf_ols_fit.summary())

## generating dummy variables for data python

## Question 6 

intetractionModel = smf.ols(formula = 'Sales~CompPrice+Income+Advertising+Price+Bad+Good+Age+Advertising*Income', data = df).fit()
print(intetractionModel.summary())





#Q7 MAPE- Mean Average Percentage Error

    #splitting dataset in training and predicting dataset
"""split= sample.split(dummy1$Sales, SplitRatio = 0.7)
training_data= subset(dummy1, split=="TRUE")
predicting_data= subset(dummy1, split=="FALSE")

    #Applying Prediction Model on predicting dataset
prediction= predict(m6, predicting_data)
prediction
plot(predicting_data$Sales, type="l", col="green")
lines(prediction, type="l", col="blue")
"""
# splitting X and y into training and testing sets 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(df, df['Sales'], test_size=0.4, 
                                                    random_state=1) 

## On Testing Data
Model = smf.ols(formula = 'Sales~CompPrice+Income+Advertising+Price+Bad+Good+Age+Advertising*Income', data = X_test).fit()
print(Model.summary())

predictions = Model.predict(X_train)

print("MAPE is :\n")

np.mean(np.abs((y_train - predictions) / y_train)) * 100