from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(1, 1)

qc.h(0)        # Put qubit 0 into superposition
qc.z(0)        # Apply a Z gate (flips phase of |1⟩)
qc.h(0)        # Hadamard again to interfere paths

qc.measure(0, 0) 

simulator = Aer.get_backend('qasm_simulator')
compiled = transpile(qc, simulator)
qobj = assemble(compiled)
result = simulator.run(qobj).result()

counts = result.get_counts()
print("Phase kickback interference results:", counts)
plot_histogram(counts)
plt.show()
