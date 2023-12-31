import sys
import numpy as np
import re
import math
import time
from qiskit.circuit import QuantumCircuit
from qiskit.synthesis import generate_basic_approximations
from qiskit.transpiler.passes import SolovayKitaev
from qiskit.quantum_info import Operator

def count_cnots(circuit):
    cnot_count = 0
    for instr, qargs, cargs in circuit.data:
        if instr.name == 'cx':
            cnot_count += 1
    return cnot_count

def count_ops(circuit):
    count = 0
    for instr, qargs, cargs in circuit.data:
        if instr.name != '':
            count += 1
    return count

def sk_decomp(arr, qubit):


    op = Operator(arr)

    qc = QuantumCircuit(qubit)
    qc.unitary(op, list(range(int(qubit))), label="original gate")

    print("\nOriginal circuit:")
    print(qc.draw())

    basis = ["h", "s", "t", "z", "tdg", "sdg", "cx", "cz"]
    approx = generate_basic_approximations(basis, depth=3)

    skd = SolovayKitaev(recursion_degree=2, basic_approximations=approx)
    start_time = time.time()
    discretized = skd(qc)
    execution_time = time.time() - start_time

    print("\nDiscretized circuit:")
    print(discretized.draw())


    cnot_count = count_cnots(discretized)
    gate_counts = count_ops(discretized)

    dict = {'time': execution_time, 'total_gate': gate_counts, 'cnot_gate': cnot_count, 'error': np.linalg.norm(Operator(discretized).data - Operator(arr).data)}
    print(dict)


    return dict

   


