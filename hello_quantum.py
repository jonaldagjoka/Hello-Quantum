#      from qiskit import QuantumCircuit, Aer, execute
#      from qiskit.visualization import plot_histogram
#      import matplotlib.pyplot as plt
# ... 
# ... # Build a quantum circuit with 1 qubit and 1 classical bit
# ... qc = QuantumCircuit(1, 1)
# ... qc.h(0)               # Apply Hadamard gate
# ... qc.measure(0, 0)      # Measure the qubit
# ... 
# ... # Simulate the circuit
# ... simulator = Aer.get_backend('qasm_simulator')
# ... job = execute(qc, simulator, shots=1024)
# ... result = job.result()
# ... 
# ... # Get and display results
# ... counts = result.get_counts(qc)
# ... print("Result:", counts)
# ... 
# ... # Plot the results
# ... plot_histogram(counts)
# ... plt.show()
