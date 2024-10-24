from qiskit.quantum_info import SparsePauliOp
from qiskit_algorithms.optimizers import COBYLA
from quantum_circuit_genetic_optimizer.genetic_algorithm import (
    run_genetic_algorithm,
)


def main():
    # Define problem parameters
    hamiltonian = SparsePauliOp.from_list(
        [("ZZ", 1.0), ("XX", 1.0)]
    )  # Example Hamiltonian for 2 qubits
    optimizer = COBYLA(maxiter=100)

    # Genetic Algorithm hyperparameters
    population_size = 100
    num_generations = 10
    crossover_probability = 0.8
    mutation_probability = 0.75
    entanglement_chance = 0.75

    # Run the genetic algorithm
    run_genetic_algorithm(
        hamiltonian=hamiltonian,
        optimizer=optimizer,
        population_size=population_size,
        num_generations=num_generations,
        crossover_probability=crossover_probability,
        mutation_probability=mutation_probability,
        entanglement_chance=entanglement_chance,
    )


if __name__ == "__main__":
    main()
