# Quantum Circuit Genetic Optimizer

This project implements a genetic algorithm to optimize quantum circuits using variational techniques. The optimizer is designed to minimize the energy of a Hamiltonian by evolving a population of quantum circuit genes through selection, crossover, and mutation operations.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)

## Features

- **Genetic Algorithm**: Utilizes a genetic algorithm to optimize quantum circuits.
- **Variational Quantum Eigensolver (VQE)**: Incorporates VQE for estimating the eigenvalues of Hamiltonians.
- **Circuit Representation**: Represents circuits using a gene-based structure, allowing for crossover and mutation operations.

## Requirements

- Python 3.12
- Qiskit
- Qiskit Algorithms
- tqdm
- Other dependencies as specified in `pyproject.toml`
- they can be installed with poetry (see below)

## Installation

To install the necessary dependencies, use Poetry for package management:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/quantum-circuit-genetic-optimizer.git
    cd quantum-circuit-genetic-optimizer
    ```

    Install Poetry (if not already installed):

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2. **Install dependencies**:

    ```bash
    poetry install
    ```

## Usage

To run the genetic algorithm for optimizing quantum circuits, use the run_genetic_algorithm function with the appropriate parameters:

```python
from qiskit.quantum_info import SparsePauliOp
from qiskit_algorithms.optimizers import COBYLA

# Define your Hamiltonian and optimizer
hamiltonian = SparsePauliOp.from_list([("Z", 0), ("ZZ", [0, 1])])
optimizer = COBYLA()

# Run the genetic algorithm
run_genetic_algorithm(
    hamiltonian=hamiltonian,
    optimizer=optimizer,
    population_size=100,
    num_generations=5,
    num_layers=2,
    crossover_probability=0.6,
    mutation_probability=0.5,
    entanglement_chance=0.75
)
```

## Function Descriptions

- run_genetic_algorithm: Executes the genetic algorithm for optimizing quantum circuits.
- compute_population_fitness: Calculates the fitness of the population based on the Hamiltonian.
- evaluate_fitness: Evaluates the fitness score of an individual gene.
- create_random_circuit_gene: Generates a random quantum circuit gene.
- perform_crossover: Performs crossover between two circuit genes.
- mutate_circuit_gene: Mutates a circuit gene to introduce variation.

## Code Structure

- quantum_circuit_genetic_optimizer/: Contains the main logic and algorithms for optimizing quantum circuits.
- genes.py: Functions for managing and manipulating circuit genes.
- circuit_helpers.py: Helper functions for constructing quantum circuits and generating CNOT pairs.
- vqe.py: Functions for executing the VQE algorithm.
- structures.py: Data structures used in the optimization process.