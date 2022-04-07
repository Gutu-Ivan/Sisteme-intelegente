import numpy as np
import matplotlib.pyplot as plt

#Numpy
#initializați folosind o listă din Python
a = np.array([1, 2, 3])
print(a)
print(type(a))  # tipul obiectului a => <class 'numpy.ndarray'>
print(a.dtype)  # tipul elementelor din a => int32
print(a.shape)  # tuple continand lungimea lui a pe fiecare dimensiune => (3,)
print(a[0])  # acceseaza elementul avand indexul 0 => 1
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)  # => (2, 3)
print(b[0][2])  #=>3
print(b[0, 2])  #=>3
c = np.asarray([[1, 2], [3, 4]])
print(type(c))  # => <class 'numpy.ndarray'>
print(c.shape)  # => (2, 2)


#creați folosind funcții din NumPy
zero_array = np.zeros((3, 2))  # creeaza un vector continand numai 0
print(zero_array)  # => [[0. 0.]
                       # [0. 0.]
                       # [0. 0.]]
ones_array = np.ones((2, 2))  # creeaza un vector continand numai 1
print(ones_array) # => [[1. 1.]
                     # [1. 1.]]
constant_array = np.full((2, 2), 8) # creeaza un vector constant
print(constant_array) # => [[8 8]
                          # [8 8]]
identity_matrix = np.eye(3) # creeaza matricea identitate de dimensiune 3x3
print(identity_matrix) # => [[1. 0. 0.]
                           # [0. 1. 0.]
                           # [0. 0. 1.]]
random_array = np.random.random((1,2))
print(random_array)  # creeaza un vector cu valori aleatoare uniform distribuite intre [0, 1) => ex: [[0.00672748 0.12277961]]
mu, sigma = 0, 0.1
gaussian_random = np.random.normal(mu, sigma, (3,6))  # creeaza un vector cu valori random cu distributie Gaussiana de medie mu si deviatie standard sigma
first_5 = np.arange(5)  # creeaza un vector continand primele 5 numere naturale
print(first_5) # => [0 1 2 3 4]

#Indexare
#Slicing
array_to_slice = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
slice = array_to_slice[:, 0:3]  # luam toate liniile si coloanele 0, 1, 2
print(slice)  # =>[[1 2 3]
                 # [567]
                 # [ 9 10 11]]
# !! modificarea slice duce automat la modificarea array_to_slice
print(array_to_slice[0][0])  # => 1
slice[0][0] = 100
print(array_to_slice[0][0])  # => 100
# pentru a nu se intampla acest lucru submultimea poate fi copiata
slice_copy = np.copy(array_to_slice[:, 0:3])
slice_copy[0][0] = 100
print(slice_copy[0][0])  # => 100
print(array_to_slice[0][0])  # => 1

slice_1 = array_to_slice[2:3, :]
print(slice_1)  # => [[ 9 10 11 12]]
slice_2 = array_to_slice[2, :]
print(slice_2)  #=>[9101112] # returnarea tuturor elementelor intr-un array 1D:
slice_1d = np.ravel(slice_1)
print(slice_1d)  #=>[9101112] # dimensiunea vectorilor poate fi modificata folosind functia
np.reshape reshaped_array = np.reshape(array_to_slice, (2, 6))
print(reshaped_array) # => [[ 1 2 3 4 5 6]
                          # [7 8 9101112]]

#Folosind vectori de întregi:
print(array_to_slice[[0,0], [1,3]]) # afiseaza elementele de pe pozitiile
# [0,1] si [0,3] => [2 4]

#Folosind vectori de valori bool:
# Vrem sa afisam toate elementele mai mari decat 10 din array_to_slice
bool_idx = (array_to_slice > 10)  # rezulta o matrice de aceeasi dimensiune cu
                                  # array_to_slice in care fiecare element consta
                                  # intr-o valoare bool astfel:
                                  # True, daca elementul corespunzatoe din
                                  # array_to_slice > 10
                                  # False, daca elementul corespunzatoe din
                                  # array_to_slice <= 10
print(bool_idx)  # => [[ True False False False]
                 # [False False False False]
                 # [False False True True]]
print(array_to_slice[bool_idx])  # => [100 11 12]
                                 # Operatia se poate face si direct:
print(array_to_slice[array_to_slice > 10])  # => [100 11 12]

#Functii matematice:
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
            #Suma element cu element => [[ 6.0 8.0]
            #[ 10.0 12.0]]
print(x + y)
print(np.add(x, y))
            # Diferenta element cu element => [[ -4.0 -4.0]
            # [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))
            # Produs element cu element => [[ 5.0 12.0]
            # [ 21.0 32.0]]
print(x * y)
print(np.multiply(x, y))
            # Impartire element cu element => [[ 0.2 0.33333333]
            # [ 0.42857143 0.5]]
print(x / y)
print(np.divide(x, y))
print(np.sqrt(x))
            # Ridicare la putere
my_array = np.arange(5)
powered = np.power(my_array, 3)
print(powered)  #=>[0 1 8 27 64]

#Produs scalar:
x = np.array([[1, 2],[3, 4]])
y = np.array([[5, 6],[7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])  # vector x vector => 219
print(v.dot(w))
print(np.dot(v, w))  # matrice x vector => [29 67]
print(np.matmul(x, v))  # matrice x matrice => [[19 22]  # [43 50]]
print(np.matmul(x, y))

#Operatii pe matrici:
my_array = np.array([[1, 2, 3], [4, 5, 6]]) # [[1, 2, 3],
                                            # [4, 5, 6]]
print(my_array.T) # => [[1, 4],
                  # [2, 5],
                  # [3, 6]]
                  # inversa unei matrici
my_array = np.array([[1., 2.], [3., 4.]])
print(np.linalg.inv(my_array))  # => [[-2. , 1. ], [ 1.5, -0.5]]

#Functii care realizeaza operatii pe o anumita dimensiune
x = np.array([[1, 2],[3, 4]])
# suma pe o anumita dimensiune
print(np.sum(x)) # Suma tuturor elementelor => 10
print(np.sum(x, axis=0)) # Suma pe coloane => [4 6]
print(np.sum(x, axis=1)) # Suma pe linii => [3 7]
# putem specifica si mai multe axe pe care sa se faca operatia:
print(np.sum(x, axis=(0, 1))) # Suma tuturor elementelor => 10

# media pe o anumita dimensiune
y = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 2, 3,
4], [5, 6, 7, 8]]])
print(y.shape) # => (3, 2, 4)
print(y) # => [[[1 2 3 4]
# [5 6 7 8]]
# [[1 2 3 4]
# [5 6 7 8]]
# [[1 2 3 4]
# [5 6 7 8]]]
print(np.mean(y, axis=0)) # => [[1. 2. 3. 4.]
# [5. 6. 7. 8.]]
print(np.mean(y, axis=1)) # => [[3. 4. 5. 6.]
# [3. 4. 5. 6.]
# [3. 4. 5. 6.]]
# indexul elementului maxim pe fiecare linie
z = np.array([[10, 12, 5], [17, 11 ,19]])
print(np.argmax(z, axis=1)) # => [1 2]

#Broadcasting
# Vrem sa adunam un vector (v) la fiecare linie a unei matrici (m)
m = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = m + v
print(y) # => [[ 2 2 4]
         # [5 5 7]
         # [8 8 10]
         # [11 11 13]]

#Exercitii
#a
images = np.array([np.load(r"images/car_{idx}.npy".format(idx=i)) for i in range(9)])
print(images)

#b
suma = np.sum(images)
print(suma)

#c
each_sum = np.sum(images, axis=(1,2))
print(each_sum)

#d
print(np.argmax(np.sum(images, axis=(1,2))))

#e
from skimage import io
# mean_image = np.mean(images, axis=0)
io.imshow(mean_image.astype(np.uint8))
io.show()

#f
deviation = np.std(images)
print(deviation)

#g
normalization = (images - mean_image) / np.std(images)
print(normalization)

#h
cropped = images[:, 200:301, 290:401]
plt.imshow(images[7].astype(np.uint), cmap='gray')
plt.imshow(cropped[7].astype(np.uint), cmap='gray')