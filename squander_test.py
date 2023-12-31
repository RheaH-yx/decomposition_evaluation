import numpy as np
import time
import random




import sys  
sys.path.append('/home/rhea_huang/anaconda3/envs/qgd/lib/python3.10/site-packages')

from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Operator
import numpy as np
from qiskit import execute
from qiskit import Aer
from scipy.stats import unitary_group

from qgd_python.utils import get_unitary_from_qiskit_circuit
from qgd_python.decomposition.qgd_N_Qubit_Decomposition_custom import qgd_N_Qubit_Decomposition_custom
from qgd_python.utils import get_unitary_from_qiskit_circuit
from qgd_python.decomposition.qgd_N_Qubit_Decomposition_adaptive import qgd_N_Qubit_Decomposition_adaptive as N_Qubit_Decomposition_adaptive
from qgd_python.decomposition.qgd_N_Qubit_Decomposition_custom import qgd_N_Qubit_Decomposition_custom as N_Qubit_Decomposition_custom
from qgd_python.decomposition.qgd_N_Qubit_Decomposition import qgd_N_Qubit_Decomposition as N_Qubit_Decomposition



## Qiskit backend for simulator
backend = Aer.get_backend('unitary_simulator')


# 
optimized_parameters_mtx = None
alpha_vec = None


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

def convert_to_two_qubit_gate(U):
	"""
	Convert a single-qubit gate represented by a 2x2 numpy matrix U
	into a 2-qubit gate represented by a 4x4 numpy matrix.
	"""
	# Create a dummy 2-qubit gate that applies U to the first qubit
	# and leaves the second qubit in the |0⟩ state.
	I = np.eye(2)
	U_tensor_I = np.kron(U, I)
	CNOT = np.array([[1, 0, 0, 0],
					 [0, 1, 0, 0],
					 [0, 0, 0, 1],
					 [0, 0, 1, 0]])
	gate = np.dot(np.dot(CNOT, U_tensor_I), CNOT)
	return gate
##
# @brief Call load precosntructed data for inerpolated optimization
# @param filename1 The filename containing the preconstructed optimizated parameters
# @param filename2 The filename containing the parameter values
def load_preconstructed_data( filename1, filename2 ):
	global alpha_vec
	global optimized_parameters_mtx

	optimized_parameters_mtx = np.loadtxt(filename1)
	alpha_vec = np.loadtxt(filename2)




##
# @brief Calcuates the distance between two unitaries according to Eq.(3) of Ref. ....
# @param Umtx1 The first unitary
# @param Umtx2 The second unitary
# @return Returns with the calculated distance
def get_unitary_distance( Umtx1, Umtx2 ):

	product_matrix = np.dot(Umtx1, Umtx2.conj().T)
	phase = np.angle(product_matrix[0,0])
	product_matrix = product_matrix*np.exp(-1j*phase)
	product_matrix = np.eye(len(Umtx1))*2 - product_matrix - product_matrix.conj().T
	distance =  (np.real(np.trace(product_matrix)))/2

	return distance



def create_custom_gate_structure_QX2(qbit_num):
	r"""
	This method is called to create custom gate structure for the decomposition 

	"""
## [import gates block]
	from qgd_python.gates.qgd_Gates_Block import qgd_Gates_Block


	# creating an instance of the wrapper class qgd_Gates_Block
	Gates_Block_ret = qgd_Gates_Block( qbit_num )
## [import gates block]

## [disentangle_qbit]
	disentangle_qbit = qbit_num - 1 
## [disentangle_qbit]

		

	for qbit in range(0, disentangle_qbit ):

## [create layer]
		# creating an instance of the wrapper class qgd_Gates_Block
		Layer = qgd_Gates_Block( qbit_num )
## [create layer]

		if qbit == 0:

			# add U3 gate to the block
			# Theta = True
			# Phi = False
			# Lambda = True      
			# Layer.add_U3( 0, Theta, Phi, Lambda )                 
			# Layer.add_U3( disentangle_qbit, Theta, Phi, Lambda ) 
			
			Layer.add_RZ( 0 ) 
			Layer.add_RY( 0 ) 

			Layer.add_RZ( disentangle_qbit ) 
			Layer.add_RY( disentangle_qbit ) 

			# add CNOT gate to the block
			Layer.add_CNOT( 0, disentangle_qbit)

		elif qbit == 1:

## [create gate struct]
			# add U3 gate to the block
			# Theta = True
			# Phi = False
			# Lambda = True      
			# Layer.add_U3( 0, Theta, Phi, Lambda )                 
			# Layer.add_U3( 1, Theta, Phi, Lambda ) 

			Layer.add_RZ( 0 ) 
			Layer.add_RY( 0 ) 

			Layer.add_RZ( 1 ) 
			Layer.add_RY( 1 ) 

			# add CNOT gate to the block
			Layer.add_CNOT( 0, 1)

## [create gate struct]

		elif qbit == 2:

			# # add U3 gate to the block
			# Theta = True
			# Phi = False
			# Lambda = True      
			# Layer.add_U3( 2, Theta, Phi, Lambda )                 
			# Layer.add_U3( disentangle_qbit, Theta, Phi, Lambda ) 

			Layer.add_RZ( 2 ) 
			Layer.add_RY( 2 ) 

			Layer.add_RZ( disentangle_qbit ) 
			Layer.add_RY( disentangle_qbit ) 

			# add CNOT gate to the block
			Layer.add_CNOT( 2, disentangle_qbit )

		 
## [add layer]
		Gates_Block_ret.add_Gates_Block( Layer )
## [add layer]


	return Gates_Block_ret

##
# @brief ???????????
# @return ???????????
def decomp(arr, qubit ):
	
	if (qubit == 1):
		arr = convert_to_two_qubit_gate(arr)
		qubit = 2
	op = Operator(arr)
	qc = QuantumCircuit(qubit)
	qc.unitary(op, list(range((qubit))), label="original gate")

	# qc = QuantumCircuit(nqubit)
	# qc.unitary(arr, list(range(int(nqubit))))
	# qc_orig = transpile(qc, optimization_level=3, basis_gates=['cx', 'u3'], layout_method='sabre')
	# Umtx_orig = get_unitary_from_qiskit_circuit( qc_orig )
	
	start_time = time.time()
	iteration_max = 10
	for jdx in range(iteration_max):
		cDecompose = N_Qubit_Decomposition( np.conj(arr).T)
		gate_structure = {4:create_custom_gate_structure_QX2(4), 3:create_custom_gate_structure_QX2(3), 2:create_custom_gate_structure_QX2(2)}
		cDecompose.set_Gate_Structure(gate_structure)
		cDecompose.set_Optimization_Tolerance( 1e-20 )

		# set the number of successive identical blocks in the optimalization of disentanglement of the n-th qubits
		cDecompose.set_Optimization_Blocks( 200 )

		# turning off verbosity
		cDecompose.set_Verbose( False )

		# starting the decomposition
		cDecompose.Start_Decomposition()

		qc_final = cDecompose.get_Quantum_Circuit()

		# get the unitary of the final circuit
		Umtx_recheck = get_unitary_from_qiskit_circuit( qc_final )

		# get the decomposition error
		decomposition_error =  get_unitary_distance(arr, Umtx_recheck)
		print('recheck decomposition error: ',decomposition_error)

		cDecompose = N_Qubit_Decomposition(np.conj(arr).T )


		if decomposition_error < 1e-5:
			# cDecompose.List_Gates()
			break

	if decomposition_error < 1e-5:
		
		execution_time = time.time() - start_time
		print("\nDiscretized circuit:")
		print(qc_final.draw())


		cnot_count = count_cnots(qc_final)
		gate_counts = count_ops(qc_final)
		# print("Number of CNOT gates:", cnot_count)

		# print(f"Aggregated decomposition time: {execution_time:.5f} seconds")
		dict = {'time': execution_time, 'total_gate': gate_counts, 'cnot_gate': cnot_count, 'error': decomposition_error}
		print(dict)
		return dict
	else:
		return None 


