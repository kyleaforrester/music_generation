#!/usr/bin/env python3
import numpy as np

class Network(object):

    def __init__(self, sizes):
        self.sizes = sizes

    def initialize_weights(self):
        self.weights = [np.random.randn(y, x+1)/np.sqrt(x) for x, y in zip(self.sizes[:-1], self.sizes[1:])]

    def sgd(self, training_data, epochs, mini_batch_size, 
