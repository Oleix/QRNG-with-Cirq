# ===============================
# QISKIT QRNG with Benchmarking
# ===============================
import time
from qiskit import QuantumCircuit
from qiskit_aer import Aer

# Number of random bits
num_bits = 20

# Start benchmarking for Qiskit
qiskit_start = time.time()

# Create quantum circuit
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# Backend and run
backend = Aer.get_backend('qasm_simulator')
sim_start = time.time()
job = backend.run(qc, shots=num_bits)
counts = job.result().get_counts()
sim_end = time.time()

# Build bitstring
random_bits_qiskit = ""
for outcome, count in counts.items():
    random_bits_qiskit += outcome * count
random_bits_qiskit = random_bits_qiskit[:num_bits]
random_number_qiskit = int(random_bits_qiskit, 2)

# End benchmarking
qiskit_end = time.time()

print("=== QISKIT QRNG ===")
print("Random bits:", random_bits_qiskit)
print("Random number:", random_number_qiskit)
print(f"Simulation time: {sim_end - sim_start:.6f} seconds")
print(f"Total execution time: {qiskit_end - qiskit_start:.6f} seconds\n")


# ===============================
# CIRQ QRNG with Benchmarking
# ===============================
import cirq

# Start benchmarking for Cirq
cirq_start = time.time()

# Pick a qubit
qubit = cirq.GridQubit(0, 0)

# Create circuit
circuit = cirq.Circuit(
    cirq.H(qubit),                # Hadamard gate for superposition
    cirq.measure(qubit, key='m')  # Measurement
)
print("Cirq Circuit:")
print(circuit)

# Simulate
simulator = cirq.Simulator()
sim_start_cirq = time.time()
result = simulator.run(circuit, repetitions=num_bits)
sim_end_cirq = time.time()

# Extract bitstring
measurements = result.measurements['m']
random_bits_cirq = ''.join(str(bit[0]) for bit in measurements)
random_number_cirq = int(random_bits_cirq, 2)

# End benchmarking
cirq_end = time.time()

print("\n=== CIRQ QRNG ===")
print("Random bits:", random_bits_cirq)
print("Random number:", random_number_cirq)
print(f"Simulation time: {sim_end_cirq - sim_start_cirq:.6f} seconds")
print(f"Total execution time: {cirq_end - cirq_start:.6f} seconds")