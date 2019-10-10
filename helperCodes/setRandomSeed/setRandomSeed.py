import random
import numpy as np
import tensorflow as tf

mySeed = 42

random.seed(mySeed)
np.random.seed(mySeed)
tf.set_random_seed(mySeed)
