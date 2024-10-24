import pytest
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from quantum_circuit_genetic_optimizer.structures import Gene_T, CnotPair_T
from quantum_circuit_genetic_optimizer.circuit_helpers import (
    generate_cnot_pairs,
    add_ry_rz_to_circuit,
    apply_cnot_operations,
    construct_quantum_circuit,
)


def test_generate_cnot_pairs():
    # Test for num_qubits = 2
    result = generate_cnot_pairs(2)
    expected = [(0, 1), (1, 0)]
    assert result == expected

    # Test for num_qubits = 3
    result = generate_cnot_pairs(3)
    expected = [(0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1)]
    assert result == expected

    # Test for num_qubits = 1 (should be empty)
    result = generate_cnot_pairs(1)
    expected = []
    assert result == expected


def test_add_ry_rz_to_circuit():
    circuit = QuantumCircuit(2)
    add_ry_rz_to_circuit(circuit, num_qubits=2, layer=0)

    # Check that RY and RZ gates are added
    assert circuit.size() == 4  # Two qubits, two gates each

    # Check gate types
    gate_types = [
        gate[0].name for gate in circuit.data
    ]  # Get the names of the gates
    assert "rz" in gate_types
    assert "ry" in gate_types


def test_apply_cnot_operations():
    circuit = QuantumCircuit(2)
    gene = [(0, 1), (1, 0), None]  # Example CNOT operations
    apply_cnot_operations(circuit, gene)

    # Check that CNOT gates were added correctly
    assert circuit.size() == 2  # Only two CNOT gates should be added
    assert circuit.data[0][0].name == "cx"
    assert circuit.data[1][0].name == "cx"


def test_construct_quantum_circuit():
    num_layers = 1
    num_qubits = 2
    gene = [(0, 1), (1, 0)]  # Example gene
    circuit = construct_quantum_circuit(num_layers, num_qubits, gene)

    # Check circuit size
    assert circuit.size() == 6  # 2 RY + 2 RZ + 2 CNOT (1 layer)

    # Check that the gates are added in the correct order
    assert circuit.data[0][0].name == "rz"
    assert circuit.data[1][0].name == "ry"
    assert circuit.data[2][0].name == "rz"
    assert circuit.data[3][0].name == "ry"
