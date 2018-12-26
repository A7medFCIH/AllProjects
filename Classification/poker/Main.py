import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

import categoricalToOnehot
import normalizeStandardize
import dataSlicing

colNames = []
categorical = []
for i in range(5):
    colNames.append('Suit' + str(i+1))
    categorical.append(colNames[-1])
    colNames.append('Rank' + str(i+1))
colNames.append('label')

dataSource1 = 'http://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data'
dataSource2 = 'http://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-testing.data'
# Read The Data
df1 = pd.read_csv(dataSource1, names=colNames)
df2 = pd.read_csv(dataSource2, names=colNames)

dataset = pd.concat([df1, df2], ignore_index=True)

# Split the Data
testPercentage = 0.01
splittedData = dataSlicing.spiltData(dataset, testPercentage)
(trainData, trainLabel), (testData, testLabel) = splittedData


# processing The Data
columnsEncoding = {} # Help in Test
columnsNames = {}

for columnName in categorical:
    trainData, columnsEncoding[columnName], columnsNames[columnName] = categoricalToOnehot.categoriesToOnehot(trainData, columnName)
    testData = categoricalToOnehot.encode(testData, columnName, columnsEncoding[columnName], columnsNames[columnName])

columnName = 'label'
trainLabel, columnsEncoding[columnName], columnsNames[columnName] = categoricalToOnehot.categoriesToOnehot(trainLabel, columnName)
testLabel = categoricalToOnehot.encode(testLabel, columnName, columnsEncoding[columnName], columnsNames[columnName])

batches = dataSlicing.batching(trainData, trainLabel, 2**12)


# Building the model
X = tf.placeholder(tf.float32, [None, trainData.shape[1]])
Y = tf.placeholder(tf.float32, [None, trainLabel.shape[1]])

layer1 = tf.layers.dense(X, 64, tf.nn.relu)
layer2 = tf.layers.dense(layer1, 32, tf.nn.relu)
layer3 = tf.layers.dense(layer2, 28, tf.nn.relu)
output = tf.layers.dense(layer3, 10, tf.nn.softmax)

loss = tf.losses.softmax_cross_entropy(onehot_labels=Y, logits=output)
_, accuracy = tf.metrics.accuracy(labels=Y, predictions=tf.round(output))
currentStep = tf.placeholder(tf.int32, [])
learningRate = tf.train.inverse_time_decay(.001, decay_rate=.027, global_step=currentStep, decay_steps=1)
optimizer = tf.train.AdamOptimizer(learningRate).minimize(loss)

steps = []
trainLosses = []
testLosses = []
previousLoss = [1000] #  to check overfit
epochs = 1000
showEvery = 10

np.random.seed(1)
tf.set_random_seed(1)


with tf.Session() as sess:
    sess.run(tf.local_variables_initializer())
    sess.run(tf.global_variables_initializer())
    for i in range(epochs):
      for batch in batches.values():
        trainData, trainLabel = batch
        _, trainLoss = sess.run([optimizer, loss], feed_dict={X:trainData, Y:trainLabel, currentStep:(i+1)})
      testLoss, testAccuracy = sess.run([loss, accuracy], feed_dict={X:testData, Y:testLabel})
      steps.append(i+1)
      trainLosses.append(trainLoss)
      testLosses.append(testLoss)
      if i > 1:
        previousLoss.append(testLosses[i-1])
      if i % showEvery == 0:
        print(i, '\t', trainLoss,'\t', testLoss,'\t', testAccuracy * 100)