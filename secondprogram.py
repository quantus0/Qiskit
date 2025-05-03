from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create circuit
qc = QuantumCircuit(1, 1)
qc.h(0)               
qc.measure(0, 0)      

simulator = Aer.get_backend('qasm_simulator')
compiled = transpile(qc, simulator)
qobj = assemble(compiled)
result = simulator.run(qobj).result()

counts = result.get_counts()
print(counts)
plot_histogram(counts)
plt.show()
