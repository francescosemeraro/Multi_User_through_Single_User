import numpy as np
import tensorflow as tf 
import keras
import matplotlib.pyplot as plt
import tensorflow_probability
from data_instance import Dataset
import pickle

tfd = tensorflow_probability.distributions


#Load dataset
dataset=pickle.load(open('example_dataset.pickle','rb'))
a = dataset.get_size()

'''#@title SGCN layer
#from https://github.com/kdkalvik/ST-GCN/blob/master/model/stgcn.py


REGULARIZER = tf.keras.regularizers.l2(l=0.0001) # to reduce the weights of the layers close to zero, to reduce overfitting
INITIALIZER = tf.keras.initializers.VarianceScaling(scale=2.,
                                                    mode="fan_out", 
                                                    distribution="truncated_normal") #scales input according to a uniform distribution whose std depends on the number of tensor weights in output
class SGCN(tf.keras.Model):
  """The basic module for applying a spatial graph convolution.
    Args:
        filters (int): Number of channels produced by the convolution
        kernel_size (int): Size of the graph convolving kernel
    Shape:
        - Input[0]: Input graph sequence in :math:`(N, C, T, V)` format
        - Input[1]: Input graph adjacency matrix in :math:`(K, V, V)` format
        - Output[0]: Output graph sequence in :math:`(N, out_channels, T, V)` format
        - Output[1]: Graph adjacency matrix for output data in :math:`(K, V, V)` format
        where
            :math:`N` is a batch size
            :math:`K` is the spatial kernel size
            :math:`T` is a length of the sequence
            :math:`V` is the number of graph nodes
            :math:`C` is the number of incoming channels
"""
  def __init__(self, filters, kernel_size=3):
      super().__init__()
      self.kernel_size = kernel_size
      self.conv = tf.keras.layers.Conv2D(filters*kernel_size,
                                          kernel_size=1,
                                          padding='same',
                                          kernel_initializer=INITIALIZER,
                                          data_format='channels_first',
                                          kernel_regularizer=REGULARIZER)

  # N, C, T, V
  def call(self, x, A, training):
      x = self.conv(x)

      N = tf.shape(x)[0]
      C = tf.shape(x)[1]
      T = tf.shape(x)[2]
      V = tf.shape(x)[3]

      x = tf.reshape(x, [N, self.kernel_size, C//self.kernel_size, T, V])
      x = tf.einsum('nkctv,kvw->nctw', x, A)
      return x, A


#Hyper-parameters

SGCN_LAYER_SIZE = 64
SGCN_KERNEL_SIZE = 9
INPUT_REPRESENTATION_SIZE = 32
NUMBER_OF_FRAMES= 26
BATCH_SIZE = 100
FEATURE_SIZE = 10

encoder = keras.Sequential()
encoder.add(SGCN(filters=SGCN_LAYER_SIZE, kernel_size=SGCN_KERNEL_SIZE))
encoder.add(SGCN(filters=SGCN_LAYER_SIZE, kernel_size=SGCN_KERNEL_SIZE))
encoder.add(SGCN(filters=SGCN_LAYER_SIZE, kernel_size=SGCN_KERNEL_SIZE))
encoder.add(SGCN(filters=SGCN_LAYER_SIZE, kernel_size=SGCN_KERNEL_SIZE))
encoder.add(tf.keras.layers.AveragePooling2D(pool_size=(2, 2)))
encoder.add(keras.layers.Dense(40))
encoder.add(keras.layers.Activation('relu'))

decoder = keras.Sequential()
decoder.add(keras.layers.Dense(2*INPUT_REPRESENTATION_SIZE))
decoder.add(keras.layers.Dense(2*INPUT_REPRESENTATION_SIZE))
decoder.add(keras.layers.Dense(4*INPUT_REPRESENTATION_SIZE))
decoder.add(keras.layers.Dense(8*INPUT_REPRESENTATION_SIZE))

prior_mean = tf.zeros(shape=(BATCH_SIZE, INPUT_REPRESENTATION_SIZE), dtype=tf.float32)
prior_log_scale = tf.zeros(shape=(BATCH_SIZE, INPUT_REPRESENTATION_SIZE), dtype=tf.float32)

prior_distribution = tfd.Independent(distribution=tfd.Normal(loc=prior_mean, scale=tf.exp(prior_log_scale)), reinterpreted_batch_ndims=1)

est_mean=tf.compat.v1.get_variable("mean",shape=(BATCH_SIZE,INPUT_REPRESENTATION_SIZE),dtype=tf.float32,initializer=tf.initializers.random_uniform)
est_scale=tf.compat.v1.get_variable("scale",shape=(BATCH_SIZE,INPUT_REPRESENTATION_SIZE),dtype=tf.float32,initializer=tf.initializers.random_uniform)

variational_posterior = tfd.Independent(distribution=tfd.Normal(loc=est_mean, scale=est_scale), reinterpreted_batch_ndims=1)

def bound_terms(data_batch, variational_posterior, decoder_fn):

  sample_from_var_post=variational_posterior.sample()
  likelihood_term= tf.log(decoder_fn(sample_from_var_post).prob(data_batch))
  # Reduce mean over the batch dimensions
  likelihood_term = tf.reduce_sum(likelihood_term,[1,2])
  likelihood_term = tf.reduce_mean(likelihood_term)

  kl_term=tfp.distributions.kl_divergence(variational_posterior,prior) 
  # Reduce over the batch dimension.
  kl_term = tf.reduce_mean(kl_term)
  
  # Return the terms in the optimization objective in (1.1) description
  return likelihood_term, kl_term

data_var = tf.Variable(
    tf.ones(shape=(BATCH_SIZE, NUMBER_OF_FRAMES, FEATURE_SIZE, 3), dtype=tf.float32), 
    trainable=False)

data_assign_op = tf.compat.v1.assign(data_var, real_data)

likelihood_term, kl_term = bound_terms(data_var, variational_posterior, decoder)
train_elbo = likelihood_term - kl_term
loss=-train_elbo

# Variational variable optimizer
variational_vars_optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.05)

#variational_vars_optimizer = tf.train.AdamOptimizer(0.1, beta1=0.9, beta2=0.9) #used to answer question 1.1.2.ii 

variational_vars = [est_mean,est_scale] # list of variational variables

# Just to check
print('Variational vars" {}'.format(variational_vars))
variational_vars_update_op = variational_vars_optimizer.minimize(
      loss, var_list=variational_vars)


# Decoder optimizer
decoder_optimizer = tf.train.AdamOptimizer(0.001, beta1=0.9, beta2=0.9)
decoder_vars = tf.get_collection(
    tf.GraphKeys.TRAINABLE_VARIABLES, scope=DECODER_VARIABLE_SCOPE)
print('Decoder vars" {}'.format(decoder_vars))
decoder_update_op = decoder_optimizer.minimize(loss, var_list=decoder_vars)

tf.trainable_variables()
'''