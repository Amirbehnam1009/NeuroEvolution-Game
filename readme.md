# NeuroEvolution Game

In this project, the game is designed to operate in two distinct modes: manual and neural evolution. The primary objective of the game is to navigate through obstacles along the path. In manual mode, players control the game using the spacebar. Upon running the game.py file, you'll encounter the main interface. Opting for the first choice initiates manual mode gameplay, while the second choice launches the game into the realm of neural evolution.

<p align="center">
  <img src="https://github.com/Amirbehnam1009/NeuroEvolution-Game/assets/117163007/78c53398-6751-4176-9f4c-1ca679fd4ccb"/ " width="400" > 
  <img src="https://github.com/Amirbehnam1009/NeuroEvolution-Game/assets/117163007/ef895cc6-3f35-4867-9598-15314fed2e78"/ " width="325" > 
</p>

## About

> Under The Supervision of [Prof.Mohammad Mehdi Ebadzadeh](https://scholar.google.com/citations?user=080Y_lUAAAAJ&hl=en)

> Spring 2022


## Tools

- Python

## How to Run
    $ game.py


## Problem Description

To enable the evolution of a game through neural networks, a neural network architecture is necessary to process vital decision-making parameters and produce corresponding outputs, simulating actions such as pressing the space button. Unlike conventional neural network training, there's a lack of training data for backpropagation, leading to the utilization of evolutionary algorithms.

In the game, numerous players (e.g., 300) equipped with neural networks initialized with random weights and biases navigate obstacles. Over time, players with superior performance advance to subsequent generations following principles of evolution, with crossover and mutation iteratively enhancing overall performance.

## Implementation

### Neural Network Implementation (nn.py)

- Initialize a neural network class with neuron counts per layer.
- Implement an activation function like sigmoid.
- Define a forward function to process input and return output neurons.

### Decision-making Parameters and Neural Network Architecture Selection (play.py)

- Select an appropriate architecture class for the project.
- Implement the think function to generate neural network output based on input vector, influencing left and right jumps.

### Survivor Selection (evolution.py)

- In neural evolution mode, 300 players undergo scenarios where fitness increases with traveled distance.
- Implement survivor selection methods such as sorting by fitness, roulette wheel, SUS, and Q-tournament.

### Parent Selection and Generation of New Organisms (evolution.py)

- Select survivors to serve as parents for generating the next generation.
- Implement the generate_new_population function to return an array of descendants.
- Ensure children differ from parents using the clone_player function to maintain fitness and neural network parameters.



## Project Structure

This repository contains the following files, organized to streamline the development and understanding of the project:

- **game.py**: Responsible for orchestrating the game process, including gameplay mechanics and interactions.
- **evolution.py**: Houses the `Evolution` class, which manages the evolution of creatures across generations.
- **nn.py**: Defines the neural network architecture and implements the feedforward mechanism.
- **player.py**: Encapsulates the `Player` class, facilitating the creation and management of player entities within the game scene.
- **variables.py**: Centralizes public variables shared across multiple files, promoting maintainability and coherence within the project.

