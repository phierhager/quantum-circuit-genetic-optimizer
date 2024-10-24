from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from quantum_circuit_genetic_optimizer.structures import Gene_T, CnotPair_T

def generate_cnot_pairs(num_qubits: int) -> CnotPair_T:
    """Generate possible CNOT pairs between qubits."""
    connections = []
    
    for i in range(num_qubits - 1):
        for j in range(i + 1, num_qubits):
            connections.append((i, j))
            connections.append((j, i))

    return connections
    
def add_ry_rz_to_circuit(quantum_circuit: QuantumCircuit, num_qubits: int, layer: int):
    """Add RZ and RY rotations to every qubit."""
    for j in range(num_qubits):
        quantum_circuit.rz(Parameter(f"θ_rz_{layer}_{j}"), j)
        quantum_circuit.ry(Parameter(f"θ_ry_{layer}_{j}"), j)


def apply_cnot_operations(quantum_circuit: QuantumCircuit, cnot_gene: Gene_T):
    """Apply CNOT operations based on the provided gene segment."""
    for connection in cnot_gene:
        if connection is not None:
            quantum_circuit.cx(*connection)
            
def construct_quantum_circuit(num_layers: int, num_qubits: int, gene: Gene_T) -> QuantumCircuit:
    """Construct the quantum circuit based on the gene."""
    quantum_circuit = QuantumCircuit(num_qubits)
    for i in range(num_layers):
        add_ry_rz_to_circuit(quantum_circuit, num_qubits, layer=i)
        apply_cnot_operations(quantum_circuit, gene)
    return quantum_circuit