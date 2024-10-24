from qiskit import QuantumCircuit
from qiskit.primitives import Estimator
from qiskit.quantum_info import SparsePauliOp
from qiskit_algorithms import VQE, VQEResult
from qiskit_algorithms.optimizers import Optimizer

def execute_vqe(hamiltonian: SparsePauliOp, ansatz: QuantumCircuit, optimizer: Optimizer, estimator = Estimator()) -> VQEResult:
    """Execute VQE to compute the minimum eigenvalue of the Hamiltonian."""
    result = VQE(estimator=estimator, ansatz=ansatz, optimizer=optimizer).compute_minimum_eigenvalue(hamiltonian)
    return result