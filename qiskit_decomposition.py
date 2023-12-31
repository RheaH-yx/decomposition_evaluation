import sys
import numpy as np
import re
import math
import time
import qiskit
from qiskit.circuit import QuantumCircuit
from qiskit.quantum_info import Operator
from qiskit import transpile

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


def qiskit_decomp(arr, qubit):
    op = Operator(arr)

    qc = QuantumCircuit(qubit)
    qc.unitary(op, list(range(int(qubit))), label="original gate")


    start_time = time.time()
    trans_qc = transpile(qc, basis_gates=['cx', 'u3', 'rz', 'ry'], optimization_level=2)

    # trans_qc = transpile(qc)
    execution_time = time.time() - start_time
    

    cnot_count = count_cnots(trans_qc)
    gate_counts = count_ops(trans_qc)


    return {'time': execution_time, 'total_gate': gate_counts, 'cnot_gate': cnot_count, 'error': np.linalg.norm(Operator(trans_qc).data - Operator(arr).data)}