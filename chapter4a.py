"""Analyzing Neural Time Series Data
% Python code for Chapter 4 script A -- converted from original Matlab by Andrew Rose (and ChatGPT)
% Original Matlab code by Mike X Cohen
% 
% This code accompanies the book, titled "Analyzing Neural Time Series Data" 
% (MIT Press). Using the code without following the book may lead to confusion, 
% incorrect data analyses, and misinterpretations of results. 
% Mike X Cohen and Andrew Rose assume no responsibility for inappropriate or incorrect use of this code. 
"""
import numpy as np

# --- Variables, Part I ---

# Assigning basic values to variables
mike = 10
bob = 20

# Mathematical operations with variables
print(mike + bob)
print((mike + bob) / (mike - bob))

# Strings and concatenation
mike = "mike"
mikes_full_name = mike + " cohen"
mikes_two_fav_numbers = [7, 23]

# Checking variable types and sizes
print(type(mike))
print(len(mike))
print(len(mikes_full_name))

# --- Variables, Part II ---

# Lists (similar to MATLAB cells)
var1 = []
var1.append([1, 2, 3, 4, 5, 6, 7])
var1.append("hello world")
var1.append([1, 3, 6, 7, 4, 3, 5, 6, 7, 87, 76, 43, 4, 5, 6, 767])
print(var1[2])

# Dictionaries (similar to MATLAB structures)
ANTS = {}
ANTS["name"] = "mike"
ANTS["position"] = "author"
ANTS["favorite_toothpaste_flavor"] = "cinnamon"
ANTS["number_of_watches"] = 18
ANTS["favorite_color"] = [0.8, 0.1, 0.8]

# List of dictionaries
ANTS_list = [
    ANTS,
    {
        "name": "Your name here",
        "position": "reader",
        "favorite_toothpaste_flavor": "bratworst",
        "number_of_watches": 1,
        "favorite_color": [1, 1, 1],
    },
]

print(ANTS_list[0]["number_of_watches"])
print([ants["favorite_toothpaste_flavor"] for ants in ANTS_list])

# --- Functions ---
print(np.random.permutation(4))  # Randperm equivalent
print(np.mean([1, 3, 2, 4, 3, 5, 4, 6]))  # Mean function
permuted_integers = np.random.permutation(4)
print(permuted_integers)

# Combining functions
[max_value, max_value_index] = max(np.random.permutation(int(np.random.rand() * 10)))

# --- Indexing ---
twinkies = np.random.rand(10, 10)
the_twinkie_i_will_eat = twinkies[3, 7]  # 0-based indexing in Python

# Colon operator equivalent
print(np.arange(1, 11))
print(np.arange(1, 11, 2))
twinkies_i_will_eat = twinkies[3:8, 1:7]

# Sizes and lengths
print(twinkies.shape)
print(len(twinkies))
print(np.prod(twinkies.shape))

# --- For-loops ---
for counting_variable in range(1, 11):
    print(counting_variable)

# Nested loops
product_matrix = np.zeros((5, 7))
for i in range(5):
    for j in range(3, 7):
        product_matrix[i, j] = (i + 1) * (j + 1)  # 0-based indexing

# --- If-statements ---
if 4 > 5:
    print("Something has gone awry in the universe")
else:
    print("Whew! Everything" "s normal.")

# Switch/Case can be implemented using dictionaries or if-elif chains in Python
for counting_variable in range(1, 11, 2):
    if counting_variable == 1:
        suffix = "st"
    elif counting_variable == 2:
        suffix = "nd"
    elif counting_variable == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(
        f"The {counting_variable}{suffix} iteration value times 2 divided by 3 and added to 7 is {counting_variable * 2/3 + 7}."
    )

# --- Boolean (true/false) ---
print(5 == 5)
print(5 == 4)
fourIsFive = 4 == 5
print(fourIsFive)

# Tilde equivalent is "not"
print(not (1 == 1))
print(not (4 > 3))
print(not (4 < 3))

# repmat equivalent in Python using numpy.tile
mat = np.random.rand(4, 10)
mean_over_time = np.mean(mat, axis=1).reshape(-1, 1)
mean_over_time_repmat = np.tile(mean_over_time, (1, mat.shape[1]))
mat_mean_corrected = mat - mean_over_time_repmat
