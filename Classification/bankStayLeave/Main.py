import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

import categoricalToOnehot
import normalizeStandardize

dataset = pd.read_csv('Churn_Modelling.csv')

importantColumns = ['CreditScore', 'Geography', 'Gender', 'Age',
                    'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
                    'IsActiveMember', 'EstimatedSalary', 'Exited']

categorical = ['Geography']
quantitative = ['CreditScore', 'Age', 'Tenure', 'Balance',
                'NumOfProducts', 'EstimatedSalary']

# processing
dataset = dataset[importantColumns]
dataset['Gender'] = dataset['Gender'] == dataset['Gender'][0]
for column in categorical:
    dataset, _, _ = categoricalToOnehot.categoriesToOnehot(dataset, column)

dataset, _, _ = normalizeStandardize.standardize(dataset, quantitative)
label = dataset.loc[:, ['Exited']]
del dataset['Exited']

testSize = 1000
trainData = dataset.iloc[:-testSize, :]
trainLabel = label.iloc[:-testSize, :]
testData = dataset.iloc[-testSize:, :]
testLabel = label.iloc[-testSize:, :]

# Building the model
X = tf.placeholder(tf.float32, [None, trainData.shape[1]])
Y = tf.placeholder(tf.bool, [None, trainLabel.shape[1]])

layer1 = tf.layers.dense(X, 8, tf.nn.relu)
layer2 = tf.layers.dense(layer1, 6, tf.nn.relu)
output = tf.layers.dense(layer2, 1, tf.nn.sigmoid)

loss = tf.losses.sigmoid_cross_entropy(multi_class_labels=Y, logits=output)
accuracy,  accuracyOp= tf.metrics.accuracy(labels=Y, predictions=tf.round(output))
optimizer = tf.train.AdamOptimizer(.001).minimize(loss)

steps = []
trainLosses = []
testLosses = []
previousLoss = [1000] #  to check overfit
epochs = 1200
showEvery = 10

np.random.seed(7)
tf.set_random_seed(7)

with tf.Session() as sess:
    sess.run(tf.local_variables_initializer())
    sess.run(tf.global_variables_initializer())
    for i in range(epochs):
        _, trainLoss = sess.run([optimizer, loss], feed_dict={X:trainData, Y:trainLabel})
        testLoss, acc = sess.run([loss, accuracyOp], feed_dict={X:testData, Y:testLabel})
        steps.append(i+1)
        trainLosses.append(trainLoss)
        testLosses.append(testLoss)
        if i > 0:
            previousLoss.append(testLosses[i-1])
        if i % showEvery == 0:
            print(trainLoss)
            print(testLoss)
            print(acc)
            print()
            
            # size of scatter = 1 / (epochs/1000)
dotSize = 1 / (epochs/1000)
plt.scatter(x=steps, y=trainLosses, s=dotSize, label='Train')
plt.scatter(x=steps, y=testLosses, s=dotSize, label='Test')
plt.legend()
plt.show()

