import sys
import os
import numpy as np
import re
import math
from qiskit import transpile, QuantumRegister
from qiskit.circuit import QuantumCircuit, QuantumRegister, CircuitInstruction
from qiskit.quantum_info import Operator
import time

import sys  
sys.path.append('/home/rhea_huang/anaconda3/envs/qgd/lib/python3.10/site-packages')

#decomposition classes
from qgd_python.decomposition.qgd_N_Qubit_Decomposition_adaptive import qgd_N_Qubit_Decomposition_adaptive as N_Qubit_Decomposition_adaptive
from qgd_python.decomposition.qgd_N_Qubit_Decomposition_custom import qgd_N_Qubit_Decomposition_custom as N_Qubit_Decomposition_custom
from qgd_python.decomposition.qgd_N_Qubit_Decomposition import qgd_N_Qubit_Decomposition as N_Qubit_Decomposition
from qgd_python.decomposition.qgd_N_Qubit_Decomposition_custom import qgd_N_Qubit_Decomposition_custom
from qgd_python.utils import get_unitary_from_qiskit_circuit
from qgd_python.gates.qgd_Gates_Block import qgd_Gates_Block

import numpy as np

# def convert_to_two_qubit_gate(U):
#     """
#     Convert a single-qubit gate represented by a 2x2 numpy matrix U
#     into a 2-qubit gate represented by a 4x4 numpy matrix.
#     """
#     # Create a dummy 2-qubit gate that applies U to the first qubit
#     # and leaves the second qubit in the |0⟩ state.
#     I = np.eye(2)
#     U_tensor_I = np.kron(U, I)
#     CNOT = np.array([[1, 0, 0, 0],
#                      [0, 1, 0, 0],
#                      [0, 0, 0, 1],
#                      [0, 0, 1, 0]])
#     gate = np.dot(np.dot(CNOT, U_tensor_I), CNOT)
#     return gate


# def count_cnots(circuit):
#     cnot_count = 0
#     for instr, qargs, cargs in circuit.data:
#         if instr.name == 'cx':
#             cnot_count += 1
#     return cnot_count

# def count_ops(circuit):
#     count = 0
#     for instr, qargs, cargs in circuit.data:
#         if instr.name != '':
#             count += 1
#     return count

# def create_custom_gate_structure_lin_3qubit(self, layer_num=2):
#         """
#         Add layers to disentangle the 3rd qubit from the others
#         linear chain with IBM native operations
#         """
#         from qgd_python.gates.qgd_Gates_Block import qgd_Gates_Block

#         qbit_num = 3

#         # creating an instance of the wrapper class qgd_Gates_Block
#         Gates_Block_ret = qgd_Gates_Block( qbit_num )


#         for idx in range(0,layer_num,2):

#             # creating an instance of the wrapper class qgd_Gates_Block
#             Layer = qgd_Gates_Block( qbit_num )

#             Layer.add_RZ( 2 ) 
#             Layer.add_RY( 2 ) 
            

#             Layer.add_RZ( 1 ) 
#             Layer.add_RY( 1 ) 
            

#             # add CNOT gate to the block
#             Layer.add_CNOT( 1, 2)

#             Gates_Block_ret.add_Gates_Block( Layer )


#             # creating an instance of the wrapper class qgd_Gates_Block
#             Layer = qgd_Gates_Block( qbit_num )

#             Layer.add_RZ( 1 ) 
#             Layer.add_RY( 1 ) 
            

#             Layer.add_RZ( 0 ) 
#             Layer.add_RY( 0 ) 
            

#             # add CNOT gate to the block
#             Layer.add_CNOT( 0, 1)

#             Gates_Block_ret.add_Gates_Block( Layer )



#         return Gates_Block_ret



# def create_custom_gate_structure_lin_2qubit(self, layer_num=1, Gates_Block_ret=None):
#         """
#         Add layers to disentangle the final 2 qubits
#         linear chain with IBM native operations
#         """

#         from qgd_python.gates.qgd_Gates_Block import qgd_Gates_Block


#         qbit_num = 2

#         if Gates_Block_ret == None:
#             # creating an instance of the wrapper class qgd_Gates_Block
#             Gates_Block_ret = qgd_Gates_Block( qbit_num )


#         for idx in range(layer_num):

#             # creating an instance of the wrapper class qgd_Gates_Block
#             Layer = qgd_Gates_Block( qbit_num )

#             Layer.add_RZ( 1 ) 
#             Layer.add_RY( 1 ) 
            

#             Layer.add_RZ( 0 ) 
#             Layer.add_RY( 0 ) 
            

#             # add CNOT gate to the block
#             Layer.add_CNOT( 0, 1)

#             Gates_Block_ret.add_Gates_Block( Layer )



#         return Gates_Block_ret


# def create_custom_gate_structure_finalyzing(self, qbit_num = 3, Gates_Block_ret=None):
#         """
#         Rotating qubits into state |0>
#         """

#         from qgd_python.gates.qgd_Gates_Block import qgd_Gates_Block



#         if Gates_Block_ret == None:
#             # creating an instance of the wrapper class qgd_Gates_Block
#             Gates_Block_ret = qgd_Gates_Block( qbit_num )


#         for idx in range(qbit_num):

#             # creating an instance of the wrapper class qgd_Gates_Block
#             Layer = qgd_Gates_Block( qbit_num )

#             Layer.add_RZ( idx ) 
#             Layer.add_RY( idx ) 
           
#             Gates_Block_ret.add_Gates_Block( Layer )



#         return Gates_Block_ret


# def squander_decomp(arr, qubit):

#     orig_arr = arr
#     if (qubit == 1):
#         arr = convert_to_two_qubit_gate(arr)
#         qubit = 2
#     op = Operator(arr)
#     qc = QuantumCircuit(qubit)
#     qc.unitary(op, list(range((qubit))), label="original gate")

#     print("\nOriginal circuit:")
#     print(qc.draw())
#     print("\n")



#     # start decomposing....

#     # create custom gate structure for the decomposition
#     gate_structure = create_custom_gate_structure_lin_3qubit(14)
#     gate_structure = create_custom_gate_structure_lin_2qubit( gate_structure)
#     gate_structure = create_custom_gate_structure_finalyzing( gate_structure)

#     # creating an instance of the C++ class
#     cDecompose = qgd_N_Qubit_Decomposition_custom(np.conj(arr).T, initial_guess="random" )

#     # adding custom gate structure to the decomposition
#     cDecompose.set_Gate_Structure( gate_structure )


#     # creating a class to decompose the 
#     # cDecompose = N_Qubit_Decomposition(np.conj(arr).T )

#     # setting the verbosity of the decomposition
#     cDecompose.set_Verbose( 4 )

#     # setting the debugfile name. If it is not set, the program will not debug. 
#     # cDecompose.set_Debugfile("debug.txt")

#     # setting the tolerance of the optimization process. The final error of the decomposition would scale with the square root of this value.
#     cDecompose.set_Optimization_Tolerance( 1e-40 )

#     # set the number of block to be optimized in one shot
#     # cDecompose.set_Optimization_Blocks( 200 )
#     start_time = time.time()
#     # starting the decomposition
#     cDecompose.Start_Decomposition()

#     # list the decomposing operations
#     cDecompose.List_Gates()

#     # get the decomposing operations
#     quantum_circuit = cDecompose.get_Quantum_Circuit()
#     execution_time = time.time() - start_time

#     # if (qubit == 1):
#     #     print(quantum_circuit.qubits[1])

#     print("\nDiscretized circuit:")
#     # print the quantum circuit
#     print(quantum_circuit)

#     cnot_count = count_cnots(quantum_circuit)
#     gate_counts = count_ops(quantum_circuit)

#     dict = {'time': execution_time, 'total_gate': gate_counts, 'cnot_gate': cnot_count, 'error': np.linalg.norm(Operator(quantum_circuit).data - Operator(arr).data)}
#     print(dict)


#     return dict

def convert_to_two_qubit_gate(U):
    I = np.eye(2)
    U_tensor_I = np.kron(U, I)
    CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    gate = np.dot(np.dot(CNOT, U_tensor_I), CNOT)
    return gate

# Count CNOT gates in a circuit
def count_cnots(circuit):
    cnot_count = 0
    for instr, qargs, cargs in circuit.data:
        if instr.name == 'cx':
            cnot_count += 1
    return cnot_count

# Count total operations in a circuit
def count_ops(circuit):
    return len(circuit.data)

# Create a custom gate structure for 2-qubit systems
def create_custom_gate_structure_2qubit(layer_num=1):
    Gates_Block_ret = qgd_Gates_Block(2)
    for _ in range(layer_num):
        Layer = qgd_Gates_Block(2)
        Layer.add_RZ(1)
        Layer.add_RY(1)
        Layer.add_RZ(0)
        Layer.add_RY(0)
        Layer.add_CNOT(0, 1)
        Gates_Block_ret.add_Gates_Block(Layer)
    return Gates_Block_ret

# Decompose a gate using the SQUANDER method
def squander_decomp(arr, qubit):
    original_qubit = qubit  # Store the original number of qubits

    # Convert 1-qubit gate to 2-qubit gate if necessary
    if qubit == 1:
        arr = convert_to_two_qubit_gate(arr)
        qubit = 2  # Update the number of qubits after conversion

    # Create the quantum circuit with the correct number of qubits
    qc = QuantumCircuit(qubit)
    qc.unitary(Operator(arr), list(range(qubit)), label="original gate")

    # Create custom gate structure for decomposition
    gate_structure = create_custom_gate_structure_2qubit(layer_num=2)

    # Initialize and configure the decomposition
    cDecompose = N_Qubit_Decomposition_custom(np.conj(arr).T, initial_guess="random")
    cDecompose.set_Gate_Structure(gate_structure)
    cDecompose.set_Verbose(4)
    cDecompose.set_Optimization_Tolerance(1e-40)

    start_time = time.time()
    cDecompose.Start_Decomposition()
    quantum_circuit = cDecompose.get_Quantum_Circuit()
    execution_time = time.time() - start_time

    # Calculate metrics
    cnot_count = count_cnots(quantum_circuit)
    gate_counts = count_ops(quantum_circuit)
    error = np.linalg.norm(Operator(quantum_circuit).data - Operator(arr).data)

    results_dict = {'time': execution_time, 'total_gate': gate_counts, 'cnot_gate': cnot_count, 'error': error}

    # Additional check to ensure correct qubit indexing
    if original_qubit == 1:
        print("Inspecting decomposed circuit for 1-qubit gate converted to 2-qubit gate")
        for instr, qargs, cargs in quantum_circuit.data:
            print(instr, qargs)  # Check each instruction and its qubit indices

    return results_dict







