import numpy as np


class NeuralNetwork:

    def __init__(self, layer_sizes):
        """
        Neural Network initialization.
        Given layer_sizes as an input, you have to design a Fully Connected Neural Network architecture here.
        :param layer_sizes: A list containing neuron numbers in each layers. For example [3, 10, 2] means that there are
        3 neurons in the input layer, 10 neurons in the hidden layer, and 2 neurons in the output layer.
        """
        self.layer_sizes = layer_sizes        
        self.weight_1, self.weight_2 = [np.random.normal(size=(n, m)) for n, m in zip(layer_sizes[1:], layer_sizes[:-1])]
        self.bias_1, self.bias_2 = [np.zeros((n, 1)) for n in layer_sizes[1:]]

    def activation(self, x):
        """
        The activation function of our neural network, e.g., Sigmoid, ReLU.
        :param x: Vector of a layer in our network.
        :return: Vector after applying activation function.
        """
        return 1 / (1 + np.exp(-x))

    def forward(self, x):
        """
        Receives input vector as a parameter and calculates the output vector based on weights and biases.
        :param x: Input vector which is a numpy array.
        :return: Output vector
        """
        x = np.reshape(x, (self.layer_sizes[0], 1))
        return self.activation(np.dot(self.weight_2, self.activation(np.dot(self.weight_1, x) + self.bias_1)) + self.bias_2)
