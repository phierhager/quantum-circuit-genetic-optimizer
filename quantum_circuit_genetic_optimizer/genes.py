import random
import numpy as np
from typing import Any
from quantum_circuit_genetic_optimizer.structures import GeneSegment_T, Gene_T, CircuitGene

    
def create_random_circuit_gene(num_qubits: int, possible_cnot_pairs: Gene_T, 
                                entanglement_chance: float = 0.75) -> CircuitGene:
    """Create a random gene with a chance of including entanglement."""
    gene = [random.choice(possible_cnot_pairs) if np.random.rand()< entanglement_chance else None for _ in range(2 * num_qubits)]
    return CircuitGene(gene=gene)
    

def perform_crossover(circuit_gene_1: CircuitGene, circuit_gene_2: CircuitGene, possible_cnot_pairs: Gene_T, 
                      crossover_probability: float = 0.6) -> Gene_T:
    """Generate a child gene using crossover logic."""
    return CircuitGene(gene=[
        select_gene_segment_from_parents(gene_segment_1, gene_segment_2, possible_cnot_pairs, crossover_probability)
        for gene_segment_1, gene_segment_2 in zip(circuit_gene_1.gene, circuit_gene_2.gene)
    ])


def select_gene_segment_from_parents(gene_segment_1: GeneSegment_T, gene_segment_2: GeneSegment_T,
                              possible_cnot_pairs: Gene_T,
                              crossover_probability: float) -> Any:
    """Select which parent's gene or random mutation to inherit."""
    probability = random.random()
    if probability < crossover_probability / 2:
        return gene_segment_1
    elif probability < crossover_probability:
        return gene_segment_2
    elif probability < crossover_probability + (1 - 0.2) * (1 - crossover_probability):
        return random.choice(possible_cnot_pairs)
    else:
        return None


def mutate_circuit_gene(circuit_gene: CircuitGene, possible_cnot_pairs: Gene_T, 
                        mutation_probability: float = 0.5) -> CircuitGene:
    """Perform mutation on the circuit gene."""
    return CircuitGene(gene = [mutate_gene_segment(segment, possible_cnot_pairs, mutation_probability) for segment in circuit_gene])

    
def mutate_gene_segment(segment: GeneSegment_T, possible_cnot_pairs: Gene_T, 
                        mutation_probability: float) -> GeneSegment_T:
    """Mutate a single gene segment based on defined probabilities."""
    if segment is not None:
        return mutate_segment(segment, possible_cnot_pairs, mutation_probability)
    else:
        return mutate_none_segment(possible_cnot_pairs, mutation_probability)


def mutate_segment(segment: GeneSegment_T, possible_cnot_pairs: Gene_T,
                            mutation_probability: float, randomized_probability: float = 0.2) -> GeneSegment_T:

    probability = random.random()
    if probability < mutation_probability:
        return (segment[1], segment[0])  # Flip
    elif probability <= min(1, mutation_probability + randomized_probability):
        return random.choice(possible_cnot_pairs)  # Randomize
    else:
        return None


def mutate_none_segment(possible_cnot_pairs: Gene_T, mutation_probability: float) -> GeneSegment_T:
    probability = random.random()
    if probability < mutation_probability:
        return random.choice(possible_cnot_pairs) 
    else:
        return None