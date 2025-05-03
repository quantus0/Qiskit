from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1000)

result = job.result()
counts = result.get_counts(qc)
print("Measurement results:", counts)

plot_histogram(counts)
