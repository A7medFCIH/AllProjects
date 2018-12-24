import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

import normalizeStandardize
import categoricalToOnehot

dataset = pd.read_csv('reg_train.csv')
importantColumns = ['season', 'yr', 'mnth', 'hr', 'holiday',
                    'weekday', 'workingday', 'weathersit', 'temp',
                    'atemp', 'hum', 'windspeed','casual', 'registered',
                    'cnt']
categorical = ['season', 'mnth', 'hr', 'weekday', 'weathersit']
quantitative = ['yr', 'temp', 'atemp', 'hum', 'windspeed',
                'casual', 'registered']

# split The Data
dataset = dataset[importantColumns]
testSize = 3903
trainData = dataset.iloc[:-testSize, :-1]
trainLabel = dataset.iloc[:-testSize, [-1]]
testData = dataset.iloc[-testSize:, :-1]
testLabel = dataset.iloc[-testSize:, [-1]]

# processing the Data
columnsEncoding = {} # Help in Test
columnsNames = {}
mean = 0
std = 0

for columnName in categorical:
    trainData, columnsEncoding[columnName], columnsNames[columnName] = categoricalToOnehot.categoriesToOnehot(trainData, columnName)
    testData = categoricalToOnehot.encode(testData, columnName, columnsEncoding[columnName], columnsNames[columnName])
    
trainData, mean, std = normalizeStandardize.standardize(trainData, quantitative)
testData = normalizeStandardize.adaptStandardize(testData, quantitative, mean, std)

# Building the model
X = tf.placeholder(tf.float32, [None, trainData.shape[1]])
Y = tf.placeholder(tf.float32, [None, trainLabel.shape[1]])

layer1 = tf.layers.dense(X, 64, tf.nn.relu)
layer2 = tf.layers.dense(layer1, 32, tf.nn.relu)
layer3 = tf.layers.dense(layer2, 8, tf.nn.relu)
output = tf.layers.dense(layer3, 1, tf.nn.relu)

loss = tf.losses.huber_loss(labels=Y, predictions=output)
optimizer = tf.train.AdamOptimizer(.001).minimize(loss)

steps = []
trainLosses = []
testLosses = []
previousLoss = [1000] #  to check overfit
epochs = 7000
showEvery = 10

np.random.seed(7)
tf.set_random_seed(7)

with tf.Session() as sess:
    sess.run(tf.local_variables_initializer())
    sess.run(tf.global_variables_initializer())
    for i in range(epochs):
        _, trainLoss = sess.run([optimizer, loss], feed_dict={X:trainData, Y:trainLabel})
        testLoss = sess.run(loss, feed_dict={X:testData, Y:testLabel})
        steps.append(i+1)
        trainLosses.append(trainLoss)
        testLosses.append(testLoss)
        if i > 0:
            previousLoss.append(testLosses[i-1])
        if i % showEvery == 0:
            print(trainLoss)
            print(testLoss)
            print()
            
            # size of scatter = 1 / (epochs/1000)
dotSize = 1 / (epochs/1000)
plt.scatter(x=steps, y=trainLosses, s=dotSize, label='Train')
plt.scatter(x=steps, y=testLosses, s=dotSize, label='Test')
plt.legend()
plt.show()

