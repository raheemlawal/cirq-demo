import cirq

# Define four line qubits. NamedQubits would also work, however this demonstrates a more succint syntax.
q = cirq.LineQubit.range(4)

# Define a list of operations.
ops = [cirq.H(q[0]), cirq.H(q[1]), cirq.CNOT(q[1], q[2]), cirq.CNOT(q[0], q[3]), cirq.H(q[1])]

# Create a circuit from the list of operations.
print("Circuit:\n")
print(cirq.Circuit(ops))