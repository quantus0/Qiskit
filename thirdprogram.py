from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2) # 2-qubit quantum circuit with 2 classical bits

qc.h(0) # Create Superposition

qc.cx(0, 1) # Apply CNOT

qc.measure([0, 1], [0, 1]) # Measure both qubits

simulator = Aer.get_backend('qasm_simulator')
compiled = transpile(qc, simulator)
qobj = assemble(compiled)
result = simulator.run(qobj).result()

counts = result.get_counts()
print("Bell state measurement results:", counts)
plot_histogram(counts)
plt.show()
