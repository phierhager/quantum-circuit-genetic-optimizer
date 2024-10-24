import pytest
import random
import numpy as np
from quantum_circuit_genetic_optimizer.structures import (
    GeneSegment_T,
    Gene_T,
    CircuitGene,
)
from quantum_circuit_genetic_optimizer.genes import (
    create_random_circuit_gene,
    perform_crossover,
    mutate_circuit_gene,
    mutate_gene_segment,
    mutate_segment,
    mutate_none_segment,
)

# Test constants
NUM_QUBITS = 3
POSSIBLE_CNOT_PAIRS = [("q1", "q2"), ("q2", "q3"), ("q1", "q3")]
ENTANGLEMENT_CHANCE = 0.75


# Test for create_random_circuit_gene
def test_create_random_circuit_gene():
    circuit_gene = create_random_circuit_gene(
        NUM_QUBITS, POSSIBLE_CNOT_PAIRS, ENTANGLEMENT_CHANCE
    )

    assert isinstance(circuit_gene, CircuitGene)
    assert len(circuit_gene.gene) == 2 * NUM_QUBITS
    assert all(
        gene_segment is None or gene_segment in POSSIBLE_CNOT_PAIRS
        for gene_segment in circuit_gene.gene
    )


# Test for perform_crossover
def test_perform_crossover():
    gene1 = CircuitGene(gene=[("q1", "q2"), None, ("q2", "q3")])
    gene2 = CircuitGene(gene=[None, ("q1", "q3"), ("q1", "q2")])

    child_gene = perform_crossover(gene1, gene2, POSSIBLE_CNOT_PAIRS)

    assert isinstance(child_gene, CircuitGene)
    assert len(child_gene.gene) == len(gene1.gene)


# Test for mutate_circuit_gene
def test_mutate_circuit_gene():
    original_gene = CircuitGene(gene=[("q1", "q2"), None, ("q2", "q3")])
    mutated_gene = mutate_circuit_gene(
        original_gene, POSSIBLE_CNOT_PAIRS, mutation_probability=1.0
    )

    assert mutated_gene.gene != original_gene.gene


# Test for mutate_gene_segment
def test_mutate_gene_segment():
    segment = ("q1", "q2")
    mutated_segment = mutate_gene_segment(
        segment, POSSIBLE_CNOT_PAIRS, mutation_probability=1.0
    )

    assert mutated_segment != segment


# Test for mutate_none_segment
def test_mutate_none_segment():
    segment = None
    mutated_segment = mutate_none_segment(
        POSSIBLE_CNOT_PAIRS, mutation_probability=1.0
    )

    assert mutated_segment in POSSIBLE_CNOT_PAIRS or mutated_segment is None


# Test for mutate_segment
def test_mutate_segment():
    segment = ("q1", "q2")
    mutated_segment = mutate_segment(
        segment, POSSIBLE_CNOT_PAIRS, mutation_probability=1.0
    )

    assert mutated_segment != segment or mutated_segment in POSSIBLE_CNOT_PAIRS
