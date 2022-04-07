#Tipuri de date primitive
#Numbers

x = 3
print(type(x))  # Afiseaza "<class 'int'>"
print(x)  # Afiseaza "3"
print(x + 1)  # Adunare; Afiseaza "4"
print(x - 1)  # Scadere; Afiseaza "2"
print(x * 2)  # Inmultire; Afiseaza "6"
print(x ** 2)  # Exponential; Afiseaza "9"
x += 1
print(x)  # Afiseaza "4"
x *= 2
print(x)  # Afiseaza "8"
y = 2.5
print(type(y))  # Afiseaza "<class 'float'>"
print(y, y + 1, y * 2, y ** 2)  # Afiseaza "2.5 3.5 5.0 6.25"

# Bool

t = True
f = False
print(type(t))  # Afiseaza "<class 'bool'>"
print(t and f)  # Logical AND; Afiseaza "False"
print(t or f)  # Logical OR; Afiseaza "True"
print(not t)  # Logical NOT; Afiseaza "False"
print(t != f)  # Logical XOR; Afiseaza "True"

# String

hello = 'hello' # Un string se declara intre ghilimele simple
world = "world" # sau intre ghilimele duble
print(hello) # Afiseaza "hello"
print(len(hello)) # Lungimea sirului de caracter; Afiseaza 5
hw = hello + ' ' + world # Concatenare
print(hw) # Afiseaza "hello world"
hw12 = '%s %s %d' % (hello, world, 12) # sprint - formatarea
# sirurilor de caractere

print(hw12) # Afiseaza "hello world 12"
s = "hello"
print(s.capitalize()) # Afiseaza "Hello"
print(s.upper()) # Afiseaza "HELLO"

print(s.replace('l', '(ell)'))  # Inlocuieste toate instantele
                                # primului argument cu al doilea
                                # argument,Afiseaza "he(ell)(ell)o"
print(' hello world '.strip() ) # Sterge spatiile albe
                                # de la inceput si sfarsit;
                                # Afiseaza "hello world"


#Colectii
#Liste

xs = [3, 1, 2]  # Creaza o lista
print(xs, xs[2])  # Afiseaza "[3, 1, 2] 2"
print(xs[-1])  # Indicii negativi numara de la sfarsitul listei; Afiseaza "2"

xs[2] = 'foo'  # Listele pot contine elemente de tipuri diferite
print(xs)  # Afiseaza "[3, 1, 'foo']"
xs.append('bar')  # Adaugare la sfarsitul listei
xs += ['foobar']  # Adaugare la sfarsitul listei
print(xs)  # Afiseaza "[3, 1, 'foo', 'bar', 'foobar' ]"

x = xs.pop()  # Elimina si returneaza ultimul element al listei
y = xs.pop(-1) # Elimina si returneaza elementul de pe pozitia i din lista
print(x, y, xs) # Afiseaza "foobar bar [3, 1, 'foo']"


#Slicing - putem accesa o sublista a unei liste

nums = list(range(5))  # range(n) este o functie care creeaza o lista de intregi, pornind de la 0 pana la n-1, iar range(a, b), creaza o lista cu numere intregi de la [a, b-1]

print(nums)  # Afiseaza "[0, 1, 2, 3, 4]"
print(nums[2:4])  # Acceseaza o sublista de la indicele 2 la 4 (exclusiv); Afiseaza "[2, 3]"

print(nums[2:])  # Acceseaza o sublista de la indicele 2 la sfarsitul listei ; Afiseaza "[2,3,4]"
print(nums[:2])  # Acceseaza o sublista de la inceputul listei pana la indicele 2 (exclusive); Afiseaza "[0, 1]"

print(nums[:])  # Acceseaza lista; Afiseaza "[0,1,2,3,4]"
print(nums[:-1])  # Acceseaza lista de la primul pana la penultimul element; Afiseaza "[0,1,2,3]"

nums[2:4] = [8, 9]
print(nums)  # Afiseaza "[0, 1, 8, 9, 4]"
numbers = list(range(5, 10))  # Numerele de la 5 la 9 (inclusiv)
nums_reverse = numbers[::-1]  # Parcurgem lista de la ultimul element pana la primul.
print(nums_reverse)  # Afiseaza "[9, 8, 7, 6, 5]"


Bucle

animals = ['cat', 'dog', 'monkey']
for animal in animals: print(animal)  # Afiseaza "cat", "dog", "monkey", fiecare pe cate o linie.

animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals): print('#%d: %s' % (idx + 1, animal))  # Afiseaza "#1: cat", "#2: dog", "#3: monkey", fiecare pe cate o linie.

X = [1, 2, 3, 4, 5]
Y = [9, 8, 7]
# inmultim listele element cu element (element wise)
xy_dot = [a * b for (a, b) in zip(X, Y)]  # se formeaza perechi cu al i-lea element din prima lista si al i-lea din a doua lista
print(xy_dot)  # Afiseaza [9, 16, 21]


#List comprehension

nums = [0, 1, 2, 3, 4]
squares = []
for x in nums: squares.append(x ** 2)
print(squares) # Afiseaza [0, 1, 4, 9, 16]

nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares) # Afiseaza [0, 1, 4, 9, 16]

nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares) # Afiseaza "[0, 4, 16]"

bool_list = [True, False, True, True, False]
num_list = [x * 1 for x in bool_list]
print(num_list) # Afiseaza [1, 0, 1, 1, 0]


#Dictionare

d = {'cat': 'cute', 'dog': 'furry'} # Creaza un dictionar
print(d['cat'])  # Acceseaza o valoare in functie de cheia din dictionar. Afiseaza "cute"
print('cat' in d)  # Verifica daca in dictionar exista cheia; Afiseaza "True"
d['fish'] = 'wet'  # Adauga o noua pereche in dictionar
print(d['fish'])  # Afiseaza "wet"
print(d['monkey'])  # KeyError: cheia 'monkey' nu exista in dictionar
print(d.get('monkey', 'N/A'))  # Acceseaza o valoare din dictionar pe baza cheii, iar daca nu exista se returneaza valoarea default 'N/A'; Afiseaza "N/A"
print(d.get('fish', 'N/A'))  # Afiseaza "wet"
del d['fish']  # Sterge elementul din dictionar
print(d.get('fish', 'N/A'))  # "fish" nu mai este cheie; Afiseaza "N/A"

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d: legs = d[animal]
print('A %s has %d legs' % (animal, legs))
# Afiseaza "A person has 2 legs", "A cat has 4 legs", "A spider has 8 legs"
# Afisam cheile din dictionar
for key in d.keys(): print(key)
# Afiseaza spider, person, cat cate o cheie pe un rand.
# Afisam valorile din dictionar
for value in d.values(): print(value)
# Afiseaza 8, 4, 2 cate un numar pe un rand.

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items(): print('A %s has %d legs' % (animal, legs))
# Afiseaza "A person has 2 legs", "A cat has 4 legs", "A spider has 8 legs"


#Dictionar comprehension

nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square) # Afiseaza "{0: 0, 2: 4, 4: 16}"


#Set - colectie neordonata de elemente distincte

animals = {'cat', 'dog'}
print('cat' in animals) # Verifica daca un element se afla
# in set; Afiseaza "True"
print('fish' in animals) # Afiseaza "False"
animals.add('fish') # Adauga un element in set
print('fish' in animals) # Afiseaza "True"
print(len(animals)) # Numarul elementelor in set; Afiseaza "3"
animals.add('cat') # Adaugarea unui element care deja
# exista in set, nu are niciun efect
print(len(animals)) # Afiseaza "3"
animals.remove('cat') # Elimina un element din set
print(len(animals)) # Afiseaza "2"
# operatii cu multimi
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# reuniunea
print(A | B) # Afiseaza {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))
# intersectia
print(A & B) # Afiseaza {4, 5}
print(A.intersection(B))
# diferenta
print(A - B) # Afiseaza {1, 2, 3}
print(A.difference(B))
# diferenta simetrica - elementele din reuniune care nu sunt in intersectie
print(A ^ B) # Afiseaza {1, 2, 3, 6, 7, 8}
A.symmetric_difference(B)


#Set comprehension

from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print(nums) # Afiseaza "{0, 1, 2, 3, 4, 5}"


#Tupluri

#Creaza un dictionar cu chei de tip tuple
d = {(x, x + 1): x for x in range(10)}
t = (5, 6)  # Creaza un tuple
print(type(t))  # Afiseaza "<class 'tuple'>"
print(d[t])  # Afiseaza "5"
print(d[(1, 2)])  # Afiseaza "1"
t2 = ('cat', 5, 6)  # Creaza un tuple
print(t2[0])  # Afiseaza "cat"
# Creaza o lista de tuple
list_tuples = [('cat', 5, 6), ('dog', 8, 1)]
print(len(list_tuples))  # Afiseaza "2"
print(list_tuples[1][0])  # Afiseaza "dog"


#Functii

def sign(x):
    if x > 0: return 'positive'
    elif x < 0: return 'negative'
    else: return 'zero'
for x in [-1, 0, 1]: print(sign(x))
# Afiseaza "negative", "zero", "positive"

def hello(name, loud=False):
    if loud: print('HELLO, %s!' % name.upper())
    else: print('Hello, %s' % name)
hello('Bob') # Afiseaza "Hello, Bob"
hello('Fred', loud=True) # Afiseaza "HELLO, FRED!"

def my_function(first_list, second_list):
    if(len(first_list) == 0 or len(second_list) == 0): raise ValueError('Lists must not be empty!')
    min_first = min(first_list)
    min_second = min(second_list)
    if (min_first not in second_list or min_second in first_list) and len(first_list) != len(second_list): return True
    else: return False
first_list = [1, 2, 3, 4]
second_list = [0, 1, 3]
print(my_function(first_list, second_list)) # Afiseaza False
first_list = [-1, 1, 2, 3, 4]
second_list = [0, 1, 3]
print(my_function(first_list, second_list)) # Afiseaza True
first_list = [1, 2, 3, 4]
second_list = [0, 1, 3, 9]
print(my_function(first_list, second_list)) # Afiseaza False
first_list = [1, 2, 3, 4]
second_list = []
print(my_function(first_list, second_list)) # ValueError: Lists must not be empty!

import random # importul pachetului
def two_rand_nums():
    a = random.randint(0, 5)
    b = random.randint(0, 5)
    while(a == b):
        print('a == b')
        b = random.randint(0, 5)
        return a, b
print(two_rand_nums())

class Greeter:
    # Constructor
    def init(self, name):
        self.name = name  # Crearea unei instante
# Metoda
def greet(self, loud=False):
    if loud: print('HELLO, %s!' % self.name.upper())
    else: print('Hello, %s' % self.name)
g = Greeter('Fred')  # Construieste un obiect de tipul Greeter
g.greet()
# Apeleaza metoda greet(); Afiseaza "Hello, Fred"
g.greet(loud=True)
#Apeleaza metoda greet(); Afiseaza "HELLO, FRED!"