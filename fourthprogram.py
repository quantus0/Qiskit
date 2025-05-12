from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a 2-qubit quantum circuit with 2 classical bits
qc = QuantumCircuit(2, 2)

qc.h(0)        # Put qubit 0 into superposition
qc.cx(0, 1)    # Entangle qubit 0 with qubit 1
qc.x(1)        # Apply X gate to qubit 1

qc.measure([0, 1], [0, 1])  # Measure both qubits

simulator = Aer.get_backend('qasm_simulator')
compiled = transpile(qc, simulator)
qobj = assemble(compiled)
result = simulator.run(qobj).result()

counts = result.get_counts()
print("Measurement results:", counts)
plot_histogram(counts)
plt.show()
