import sys
import numpy as np
import re
import math
import time
from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import SGate, HGate, SdgGate, TGate, TdgGate, ZGate, XGate, YGate
from qiskit.transpiler.passes.synthesis import SolovayKitaev
from qiskit.quantum_info import Operator
from qiskit.synthesis.discrete_basis.generate_basis_approximations import (
    generate_basic_approximations,
)
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

    basic_approximations = generate_basic_approximations(basis_gates=[HGate(), SGate(), TGate(), ZGate(), TdgGate(), SdgGate(), XGate(), YGate()], depth=10)
    skd = SolovayKitaev(recursion_degree=5, basic_approximations = basic_approximations)
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

   


