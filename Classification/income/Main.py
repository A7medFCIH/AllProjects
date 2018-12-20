import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf

def stringToOnehot(df, colName):
    df[colName] = df[colName].astype('category')
    df[colName] = df[colName].cat.codes
    onehotMatrix = pd.get_dummies(df[colName])
    names = []
    for catCode in onehotMatrix:
        names.append(colName + str(catCode))
    
    onehotMatrix.columns = names
    del df[colName]
    df = df.join(onehotMatrix)
    return df

def getAccuracy(output, label):
    n = len(label)
    result = output == label
    acc = np.sum(result)/n
    return acc[0]

cols = ['age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race',
        'sex', 'capital-gain', 'capital-loss', 'hours-per-week',
        'native-country', 'income']
data1 = pd.read_csv('adult.data', names=cols)
data2 = pd.read_csv('adult.test', names=cols)
data = pd.concat([data1, data2], ignore_index=True)

label = data.loc[:, ['income']]
label = label == ' >50K'
del data['income']

categorical = ['workclass', 'education', 'marital-status', 'occupation',
          'relationship', 'race', 'sex', 'native-country']

quantitative = ['age', 'fnlwgt', 'education-num', 
                'capital-gain', 'capital-loss', 'hours-per-week']
for column in categorical:
    data = stringToOnehot(data, column)
means = []
stds = []
for column in quantitative:
    mean =  data[column].mean()
    std = data[column].std()
    means.append(mean)
    stds.append(std)
    data[column] = (data[column] - mean) / std

trainData = data[:][:-1000]
trainLabel = label[:][:-1000]
testData = data[:][-1000:]
testLabel = label[:][-1000:]

del data, data1, data2, cols, label, categorical

X = tf.placeholder(shape=[None, trainData.shape[1]], dtype=tf.float32)
Y = tf.placeholder(shape=[None, 1], dtype=tf.float32)

layer1 = tf.layers.dense(X, 7, tf.nn.relu)
output = tf.layers.dense(layer1, 1, tf.nn.sigmoid)

loss = tf.losses.sigmoid_cross_entropy(multi_class_labels=Y, logits=output)
optimizer = tf.train.AdamOptimizer(.001).minimize(loss)



steps = []
trainLosses = []
testLosses = []
previousLoss = [1000] #  to check overfit
accuracy = []
epochs = 7700
showEvery = 10

np.random.seed(7)
tf.set_random_seed(7)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(epochs):
        _, trainLoss = sess.run([optimizer, loss], feed_dict={X:trainData, Y:trainLabel})
        testLoss, out = sess.run([loss, output], feed_dict={X:testData, Y:testLabel})
        accuracy.append(getAccuracy(np.round(out), testLabel))
        steps.append(i+1)
        trainLosses.append(trainLoss)
        testLosses.append(testLoss)
        if i > 0:
            previousLoss.append(testLosses[i-1])
        if i % showEvery == 0:
            print(trainLoss)
            print(testLoss)
            print()
            

print('Accuracy = ' + str(accuracy[epochs-1]))
print('Accuracy = ' + str(max(accuracy)))
plt.scatter(x=steps, y=trainLosses, s=.1, label='Train')
plt.scatter(x=steps, y=testLosses, s=.1, label='Test')
plt.legend()
plt.show()
