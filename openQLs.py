import sys  
# sys.path.append('/home/rhea_huang/anaconda3/lib/python3.10/site-packages')

sys.path.append('/home/rhea_huang/OpenQL/pybuild')
import openql as ql
import os
import numpy as np
import math
import re
import qiskit
import time
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from qiskit.quantum_info import Operator


def convert_qasm(openql_qasm, nqubits):
    with open(openql_qasm, 'r') as f:
      openql_lines = f.readlines()

    gate_map = {
        'rx': 'rx',
        'ry': 'ry',
        'rz': 'rz',
        'x': 'x',
        'y': 'y',
        'z': 'z',
        'h': 'h',
        's': 's',
        'sdg': 'sdg',
        't': 't',
        'tdg': 'tdg',
        'cnot': 'cx'
    }

    qiskit_lines = []
    qiskit_lines.append('OPENQASM 2.0;\n')
    qiskit_lines.append('include "qelib1.inc";\n')
    qiskit_lines.append('qreg q[' + str(nqubits) + '];\n')
    # Define regular expression pattern to match
    pattern = re.compile(r'(\w+)\s+q\[([0-9]+)\],\s*(-?[0-9]+\.?[0-9]*)')
    for i in range(len(openql_lines)):
        if openql_lines[i].startswith('pragma') or openql_lines[i].startswith('.newKernel') or openql_lines[i].startswith('version 1.2') or openql_lines[i].startswith('# Generated by OpenQL') or openql_lines[i].isspace():
            continue
        line = pattern.sub(lambda m: '{}({}) q[{}]'.format(gate_map[m.group(1)], m.group(3), m.group(2)), openql_lines[i])
        line = line.replace("cnot", "cx")
        line = line.replace('\n', ';\n')
        line = line.replace('    ', '')
        
        qiskit_lines.append(line)

    return ''.join(qiskit_lines)


def openQL_decomp(arr, nqubits):


    print("Matrix to be factorized:\n",arr)
    op = Operator(arr)

    qc = QuantumCircuit(nqubits)
    qc.unitary(op, list(range(int(nqubits))), label="original gate")

    print("\nOriginal circuit:")
    print(qc.draw())
    print("\n")


    # ------------start decomposing------------------------

    curdir = "./"
    ql.set_option('output_dir', os.path.join(curdir, 'output'))
    ql.set_option('log_level', 'LOG_ERROR')
    ql.set_option('mapper', 'minextendrc')
    ql.set_option('mapusemoves', 'yes')
    ql.set_option('mapreverseswap', 'yes')
    ql.set_option('mappathselect', 'all')
    ql.set_option('maplookahead', 'all')
    ql.set_option('maprecNN2q', 'yes')
    ql.set_option('mapselectmaxlevel', '10')
    ql.set_option('mapselectmaxwidth', 'all')
    


    platf = ql.Platform.from_json('test_platform', {
            "hardware_settings": {
                "qubit_number": 2,
                "cycle_time": 100000
            },
            "instructions": {
                "y90": {
                    "prototype": ["U:qubit"],
                    "duration_cycles": 100
                },
                "ym90": {
                    "prototype": ["U:qubit"],
                    "duration_cycles": 100
                },
                "cz": {
                    "prototype": ["U:qubit", "U:qubit"],
                    "duration_cycles": 1000
                },
                "cnot": {
                    "prototype": ["U:qubit", "U:qubit"],
                    "duration_cycles": 1000,
                    "decomposition": {
                        "name": "to_cz",
                        "into": "ym90 op(1); cz op(0), op(1); skip 1; y90 op(1)"
                    }
                }
            }
        })
    
    platf = ql.Platform('none')
    program = ql.Program('example', platf, nqubits)
    kernel = ql.Kernel('newKernel', platf, nqubits)

    compiler = ql.Compiler('compiler1')
    vector_matrix = [complex(x) for x in arr.flatten()]
    start_time = time.time()
    u1 = ql.Unitary("testname",vector_matrix)
    u1.decompose()
    kernel.gate(u1, range(0, nqubits))
    program.add_kernel(kernel)
    program.compile()

    qiskit_string = convert_qasm("./output/example.qasm", nqubits)
    # Load the QASM file
    qasm_string = qiskit_string

    # Create a quantum circuit from the QASM string
    qc = QuantumCircuit.from_qasm_str(str(qasm_string))
    execution_time = time.time() - start_time


    print("\nDiscretized circuit:")
    print(qc.draw())

    print("Error:", np.linalg.norm(Operator(qc).data - Operator(arr).data))

    def count_cnots(circuit):
        cnot_count = 0
        for instr, qargs, cargs in circuit.data:
            if instr.name == 'cx':
                cnot_count += 1
        return cnot_count

    cnot_count = count_cnots(qc)
    print("Number of CNOT gates:", cnot_count)

    print(f"Aggregated decomposition time: {execution_time:.5f} seconds")