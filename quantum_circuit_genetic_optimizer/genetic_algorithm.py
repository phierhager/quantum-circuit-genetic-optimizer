from qiskit.quantum_info import SparsePauliOp
from qiskit_algorithms.optimizers import COBYLA
from typing import Any
from tqdm import tqdm
from quantum_circuit_genetic_optimizer.genes import (
    CircuitGene,
    create_random_circuit_gene,
    perform_crossover,
    mutate_circuit_gene,
)
from quantum_circuit_genetic_optimizer.circuit_helpers import (
    construct_quantum_circuit,
    generate_cnot_pairs,
)
from quantum_circuit_genetic_optimizer.vqe import execute_vqe
from quantum_circuit_genetic_optimizer.structures import Gene_T


def compute_population_fitness(
    population: list[CircuitGene],
    hamiltonian: SparsePauliOp,
    optimizer: Any,
    num_layers: int,
    num_qubits: int,
    print_progress: bool = True,
) -> None:
    """Calculate the fitness of the population."""
    enumerator = tqdm(population) if print_progress else population
    for gene in enumerator:
        gene.fitness = evaluate_fitness(
            num_layers, num_qubits, gene, hamiltonian, optimizer
        )


def evaluate_fitness(
    num_layers: int,
    num_qubits: int,
    gene: Gene_T,
    hamiltonian: SparsePauliOp,
    optimizer: Any,
) -> float:
    """Calculate the fitness score of an individual based on the Hamiltonian."""
    quantum_circuit = construct_quantum_circuit(num_layers, num_qubits, gene)
    result = execute_vqe(hamiltonian, quantum_circuit, optimizer)
    return result.eigenvalue.real


def run_genetic_algorithm(
    hamiltonian: SparsePauliOp,
    optimizer: Any,
    population_size: int = 100,
    num_generations: int = 5,
    num_layers: int = 2,
    crossover_probability: float = 0.6,
    mutation_probability: float = 0.5,
    entanglement_chance: float = 0.75,
) -> None:
    """Execute the genetic algorithm for optimizing quantum circuits."""
    num_qubits = hamiltonian.num_qubits
    possible_cnot_pairs = generate_cnot_pairs(num_qubits)

    population = [
        create_random_circuit_gene(num_qubits, possible_cnot_pairs, entanglement_chance)
        for _ in range(population_size)
    ]

    for generation in range(num_generations):
        print(f"\n-- Generation {generation + 1} --")
        compute_population_fitness(
            population, hamiltonian, optimizer, num_layers, num_qubits
        )
        population.sort(key=lambda x: x.fitness)
        best_gene = population[0]
        print(f"Best fitness: {best_gene.fitness}, by {best_gene.gene}")

        new_population = []
        for i in range(0, population_size, 2):
            if i + 1 < population_size:
                child_gene = perform_crossover(
                    population[i],
                    population[i + 1],
                    possible_cnot_pairs,
                    crossover_probability,
                )
                new_population.append(
                    mutate_circuit_gene(
                        child_gene, possible_cnot_pairs, mutation_probability
                    )
                )
        population = new_population
        population_size = len(population)
        if population_size < 2:
            break
