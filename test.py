import numpy as np
import openQLs
import squander
import pickle
import qiskit_decomposition
import squander_test
import solovayKitaev

with open('array1.pkl', 'rb') as f:
    array1 = pickle.load(f)

cnt = 1
result1 = []
for arr in array1:
    # res = squander.squander_decomp(arr, 1)
    # res = qiskit_decomposition.qiskit_decomp(arr, 1)
    res = openQLs.openQL_decomp(arr, 1)
    # res = solovayKitaev.sk_decomp(arr, 1)
    # res = squander_test.decomp(arr,1)
    result1.append(res)

print(result1)


# with open('array2.pkl', 'rb') as f:
#     array2 = pickle.load(f)

# result2 = []
# for arr in array2:
#     # res = squander.squander_decomp(arr, 2)
#     # res = qiskit_decomposition.qiskit_decomp(arr, 2)
#     # res = openQLs.openQL_decomp(arr, 2)
#     res = squander_test.decomp(arr,2)
#     result2.append(res)

# print(result2)

# with open('array3.pkl', 'rb') as f:
#     array3 = pickle.load(f)

# result3 = []
# for arr in array3:
#     # res = squander.squander_decomp(arr, 3)
#     # res = squander_test.decomp(arr,3)
#     res = openQLs.openQL_decomp(arr, 3)
#     # res = qiskit_decomposition.qiskit_decomp(arr, 3)
#     result3.append(res)

# print(result3)


# with open('array4.pkl', 'rb') as f:
#     array4 = pickle.load(f)

# result4 = []
# for arr in array4:
#     # res = squander.squander_decomp(arr, 4)
#     # res = qiskit_decomposition.qiskit_decomp(arr, 4)
#     res = openQLs.openQL_decomp(arr, 4)
#     # res = squander_test.decomp(arr,4)
#     result4.append(res)

# print(result4)



# print(squander.squander_decomp(arr, 4))

# arr = np.array([[-0.30135952-0.2969337j,  -0.09458393+0.29470865j,  0.19503355+0.09349825j,
#   -0.12683525+0.14308173j,  0.05468918+0.21104936j,  0.00205269+0.09255788j,
#   -0.20356264+0.24344779j,  0.67823252+0.15832274j],
#  [ 0.13434474+0.03460422j, -0.25094058-0.29618077j, -0.18542389-0.35423408j,
#    0.12495183+0.08842006j,  0.1891406 +0.63333347j,  0.35918775+0.12109576j,
#    0.18767679-0.10901323j,  0.12999508+0.04684325j],
#  [-0.1248772 +0.20161248j,  0.06344657-0.32511372j, -0.23472003-0.17923089j,
#    0.25801068-0.51375464j, -0.08335464-0.06135044j, -0.06632993-0.29798398j,
#   -0.23445047+0.41320665j,  0.23987262+0.17073821j],
#  [-0.28803772+0.29870534j,  0.29805381-0.33377325j, -0.29423371+0.47530668j,
#   -0.32290997+0.11748652j,  0.01751811+0.08233211j,  0.24404623+0.07284783j,
#   -0.23510327-0.24437135j,  0.09908037+0.0156921j], 
#  [ 0.13394946-0.11346094j,  0.17723073+0.01472868j,  0.04003929+0.57723809j,
#    0.61110467-0.23467257j, -0.03818094+0.22074137j, -0.08304692+0.20429778j,
#    0.22957339-0.07398859j,  0.11698388-0.05955679j],
#  [ 0.2208503 -0.45654943j,  0.2141553 -0.5506009j,  -0.06957011-0.10736729j,
#   -0.01677442+0.19305135j,  0.27602507-0.32922489j, -0.22677875+0.21047313j,
#   -0.0007331 +0.01626563j,  0.22570869-0.0912691j],
#  [-0.35123932+0.08439261j, -0.02856438-0.07766086j,  0.06946184+0.12651418j,
#    0.01009632+0.06675746j,  0.47776412-0.02236026j, -0.06665383+0.21179157j,
#    0.29439067+0.39402295j, -0.35449652+0.43775307j],
#  [-0.15062691-0.36349225j,  0.16317138-0.17151636j,  0.08890364+0.11721663j,
#   -0.09174737+0.11124606j, -0.17362009+0.06417636j,  0.20062239-0.67511456j,
#    0.45864024+0.0278769j,  -0.01455828+0.07123067j]])

# print(squander.squander_decomp(arr, 3))