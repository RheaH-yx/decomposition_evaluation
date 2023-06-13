## Decomposition Tools Comparison



### 1. Qiskit Solovay-Kitaev (for 1-qubit gate only)

#### **setup:**

```shell
$ pip install qiskit
```

**qule command:** 

`./qule --decomposition SK`

------

**Basis set:** ["h", "s", "t", "z", "tdg", "sdg", "cx", "cz"]

- This algorithm is unable to use custom gate ["rz", "ry", "cx"]

**Hyperparameter**: recursion_degree = 2

- recursion_degree: The recursion depth for the Solovay-Kitaev algorithm. A larger recursion depth increases the accuracy and length of the decomposition.

**Example output of a Hadmard gate:**

<img src=".\figure\sk_example.png" alt="sk_example" style="zoom:67%;" />





### 2. Qiskit (custom gates only work for qubit < 3)

#### **setup:**

```shell
$ pip install qiskit
```

**qule command:** 

`./qule --decomposition QISKIT`

------

**Default basis gate set:** u gate (Generic single-qubit rotation gate with 3 Euler angles) and CNOT ("cx") gate

**Custom basis gate:** ["rz", "ry", "cx"]

**Hyperparameter**: optimization_level = 0

- optimization_level: How much optimization to perform on the circuits. Higher levels generate more optimized circuits, at the expense of longer transpilation time.

  * 0: no optimization

  - 1: light optimization

  - 2: heavy optimization

  - 3: even heavier optimization

**Algorithm used for decomposition**: 

- For 4x4 unitary, TwoQubitBasisDecomposer is used. TwoQubitBasisDecomposer implements KAK decomposition method described in (https://arxiv.org/abs/0806.4015 ) by Drury and Love. This method uses optimal number of CNOT gates.

- For larger unitaries, Isometry class is used. This class implements the method introduced by Iten et al. in (https://arxiv.org/abs/1501.06911 ). This method achieves the theoretical lower bound on the number of used CNOT gates.

- This method works fine for default basis gate. However, when I tested the Qiskit transpiler on qubit>2 unitary gate (which I initialize with a matrix) to use custom basis gate["rz", "ry", "cx"] , it gives an error saying that it cannot find a path from source to target basis.



### 3. SQUANDER (Sequential Quantum Gate Decomposer)

**github link:** https://github.com/rakytap/sequential-quantum-gate-decomposer

#### **set-up:** 

- reference: https://codedocs.xyz/rakytap/sequential-quantum-gate-decomposer/

- conda virtual environment is highly recommended

  ```shell
  # Creating new python environment:
  $ conda create -n qgd
  
  # Activate the new anaconda environment
  $ conda activate qgd
  
  # Install required dependencies:
  $ conda install numpy scipy pip pytest scikit-build tbb-devel && conda install -c conda-forge gsl && pip install qiskit matplotlib
  
  # Install squander package
  $ pip install squander
  ```

- go to `\qule\src\Decomposition\squander.py` and change the sys path (line 12) to the location of squander. You can check the location of squander by `pip show squander`



**qule command:** 

`./qule --decomposition SQUANDER`

------

**Default basis gate set:** u gate (Generic single-qubit rotation gate with 3 Euler angles) and CNOT ("cx") gate

**Custom basis gate:** ["rz", "ry", "cx"]

**Hyperparameter**: set_tolerance = 1e-10

- set_tolerance: setting the tolerance of the optimization process at each layer. The final error of the decomposition would scale with the square root of this value.

**Example output of a 3-qubit gate:**

<img src=".\figure\squander_example.png" alt="squander_example" style="zoom:67%;" />





### 4. OpenQL

**github link:** https://github.com/QuTech-Delft/OpenQL

**Docs:** 

- https://openql.readthedocs.io/en/latest/old/passes/decomposition.html?highlight=decomposition
- https://repository.tudelft.nl/islandora/object/uuid:9c60d13d-4f42-4d8b-bc23-5de92d7b9600?collection=education

#### **set-up:** 

```shell
!pip install qutechopenql 
!pip install qiskit
```

#### **Developer setup**

please follow this link: https://github.com/QuTech-Delft/OpenQL/blob/develop/docs/developer/build.rst

**qule command:** 

`./qule --decomposition OPENQL`

------

**Default basis gate set:** ["rz", "ry", "cx"]

**Algorithm:** Quantum Shannon Decomposition (https://arxiv.org/pdf/2101.02993.pdf, p7)

**Example output:**

- `./qule --matrix_type rand --n 4 --method GDP --alpha 0.5 --num_tests 2 --decomposition OPENQL`

<img src=".\figure\openql_example.png" alt="openql_example" style="zoom:67%;" />





# Performance Comparison with Default Basis Gate Set

The below performance results were based on an average of 10 tests under fixed overall error tolerance level 10e-5.

| method         | #qubit | Mean  execution time in seconds | Number of  CNOT gates | Number of  total gates | error                |
| -------------- | ------ | ------------------------------- | --------------------- | ---------------------- | -------------------- |
| Solovay-Kitaev | 1      | 1.57005143165588                | 0                     | 20495                  | 8.34177592240033E-06 |
| Qiskit         | 1      | 0.00189499855041503             | 0                     | 1                      | 0                    |
| OpenQL         | 1      |                                 |                       |                        |                      |
| Squander       | 1      | 0.363046                        | 0                     | 4                      | 6.65E-08             |
| Qiskit         | 2      | 0.00149464607238769             | 0                     | 1                      | 0                    |
| OpenQL         | 2      |                                 |                       |                        |                      |
| Squander       | 2      | 0.13997                         | 3                     | 11                     | 4.29E-07             |
| Qiskit         | 3      | 0.0396940231323242              | 11                    | 33                     | 1.60007874197874E-14 |
| OpenQL         | 3      |                                 |                       |                        |                      |
| Squander       | 3      | 5.73619                         | 17                    | 54                     | 9.83E-07             |
| Qiskit         | 4      | 0.193830394744873               | 67                    | 193                    | 6.62474976918748E-14 |
| OpenQL         | 4      |                                 |                       |                        |                      |
| Squander       | 4      | 177.8239                        | 77                    | 235                    | 4.22E-06             |



# Performance Comparison with Custom Basis Gate Set

Same as above, the below performance results were based on an average of 10 tests under fixed overall error tolerance level 10e-5.

The custom basis gate set is ["rz", "ry", "cx"]

| method   | #qubit | Mean  execution time in seconds | Number of  CNOT gates | Number of  total gates | error                |
| -------- | ------ | ------------------------------- | --------------------- | ---------------------- | -------------------- |
| Qiskit   | 1      | 0.00234084129333496             | 0                     | 3                      | 5.80055992565347E-16 |
| OpenQL   | 1      |                                 |                       |                        |                      |
| Squander | 1      | 0.362069606781005               | 0                     | 9                      | 1.54E-09             |
| Qiskit   | 2      | 0.00629525184631347             | 3                     | 26                     | 4.88853738865987E-15 |
| OpenQL   | 2      |                                 |                       |                        |                      |
| Squander | 2      | 0.591429853439331               | 3                     | 18                     | 5.43E-09             |
| Qiskit   | 3      | /                               | /                     | /                      | /                    |
| OpenQL   | 3      |                                 |                       |                        |                      |
| Squander | 3      | 18.8654224395751                | 17                    | 89                     | 6.3385763082735E-09  |
| Qiskit   | 4      | /                               | /                     | /                      | /                    |
| OpenQL   | 4      |                                 |                       |                        |                      |
| Squander | 4      | 614.487759637832                | 77                    | 390                    | 3.92E-09             |





# Paper reference 

1. **Efficient decomposition of unitary matrices in quantum circuit compilers** (https://arxiv.org/abs/2101.02993 )

- This paper first compares the performance of different algorithms of unitary decomposition for 1 through 5-qubit gates. 
  - Algorithms include: Iterative unentangling, Recursive CSD, Quantum Shannon Decomposition

- OpenQL decomposition technique is based on Quantum Shannon Decomposition.

- The paper also compares OpenQL with Qubiter, which shows that OpenQL generates circuits with half the number of CNOT gates and a third of the total circuit length. In addition, OpenQL is also up to 10 times as fast.
