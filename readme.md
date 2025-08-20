# 🧠 NeuroEvolution Game 🚀

A captivating game that combines manual play with neural evolution to master obstacle navigation! This project showcases the power of evolutionary algorithms in training neural networks without traditional supervised learning.

<p align="center">
  <img src="https://github.com/Amirbehnam1009/NeuroEvolution-Game/assets/117163007/78c53398-6751-4176-9f4c-1ca679fd4ccb" width="400" alt="Game Demo">
  <img src="https://github.com/Amirbehnam1009/NeuroEvolution-Game/assets/117163007/ef895cc6-3f35-4867-9598-15314fed2e78" width="325" alt="Neural Evolution">
</p>

## 📖 About

> Developed under the supervision of [Prof. Mohammad Mehdi Ebadzadeh](https://scholar.google.com/citations?user=080Y_lUAAAAJ&hl=en)  
> Spring 2022 🎓

This project demonstrates neuroevolution - using genetic algorithms to train neural networks that can successfully play a game by navigating through obstacles. The AI learns through generations of selection, crossover, and mutation.

## 🎮 Game Modes

### 🕹️ Manual Mode
- Control your character using the **spacebar**
- Test your reflexes and timing skills
- Navigate through increasingly difficult obstacles

### 🧠 Neural Evolution Mode
- Watch as 300 AI players learn through generations
- Neural networks process game state to make jumping decisions
- Survival of the fittest: best performers pass their genes to next generations

## 🛠️ Tools & Technologies

- **Python 3** 🐍
- **NumPy** for efficient matrix operations
- **Custom neural network implementation** from scratch
- **Evolutionary algorithms** for training without backpropagation

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Amirbehnam1009/NeuroEvolution-Game.git
   cd NeuroEvolution-Game
2. **Run the game**:
   ```bash
   python game.py
   ```
3. **Select your mode**:

* Choose option 1 for Manual Mode 🕹️

* Choose option 2 for Neural Evolution Mode 🧠
  
# 🔬 Technical Implementation
## 🧠 Neural Network Architecture (nn.py)
* Custom implementation of feedforward neural networks

* Configurable layers and neurons

* Sigmoid activation function: f(x) = 1 / (1 + e^(-x))

* Random weight initialization

## 🎯 Decision Making (play.py)
* Input parameters: distance to obstacles, player velocity, etc.

* Output: jump decision (left, right, or no jump)

* Real-time processing of game state

## ⚡ Evolutionary Algorithm (evolution.py)
* **Population size**: 300 players per generation

* **Fitness function**: Distance traveled

* **Selection methods**:

    * Fitness-proportional selection (Roulette Wheel)

    * Stochastic Universal Sampling (SUS)

    * Q-Tournament selection

* **Genetic operators**:

    * Crossover: combining neural network weights of parents

    * Mutation: introducing random changes to weights

## 📊 Survivor Selection
* Multiple strategies implemented:

    * Sort by fitness (elitism) 

    * Roulette wheel selection

    * Stochastic Universal Sampling (SUS)

    * Q-Tournament selection
## 📁 Project Structure
``` bash
NeuroEvolution-Game/
├── game.py          # 🎮 Main game orchestrator and UI
├── evolution.py     # ⚡ Evolution class managing generations
├── nn.py           # �🧠 Neural network implementation
├── player.py       # 👤 Player class with neural network
├── variables.py    # 📊 Shared variables and constants
└── assets/         # 🖼️ Game assets (images, etc.)
```
## 🔧 Key Components
### 🎮 game.py
* Main game loop and rendering

* Mode selection interface

* Game state management

### ⚡ evolution.py
* **Evolution** class managing the evolutionary process

* Population initialization and management

* Fitness evaluation and selection mechanisms

* Generation of new populations through crossover and mutation

### 🧠 nn.py
* **NeuralNetwork** class with configurable architecture

* Forward propagation implementation

* Weight and bias management

### 👤 player.py
* **Player** class representing game entities

* Neural network integration for AI players

* Physics and movement handling

## 🔬 The Science Behind It
### Neuroevolution Basics
Unlike traditional neural networks that use backpropagation, this project employs evolutionary algorithms to train the networks. The process mimics natural selection:

1. **Initialization**: Create population with random neural networks

2. **Evaluation**: Test each network's performance (fitness)

3. **Selection**: Choose best performers as parents

4. **Reproduction**: Create new generation through crossover and mutation

5. **Iteration**: Repeat process until satisfactory performance is achieved

## Neural Network Architecture
The AI players use neural networks with this structure:

* **Input layer**: Game state parameters (obstacle distances, velocities, etc.)

* **Hidden layers**: Process information (configurable size)

* **Output layer**: Decision to jump left, right, or not jump

### 📈 Performance Metrics
* **Fitness**: Measured by distance traveled

* **Generations**: Number of evolutionary cycles

* **Success rate**: Percentage of players completing the course

* **Convergence**: Improvement rate across generations
## 🎯 Future Enhancements
* Graphical visualization of neural network decisions

* Real-time fitness graphs across generations

* Additional obstacle types and game mechanics

* Hyperparameter optimization interface

* Export/import of trained models

* Multi-objective optimization (speed vs. survival)
