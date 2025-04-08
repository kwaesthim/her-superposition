import numpy as np

def simulate_qubit():
    state = np.array([1, 1])  # Not normalized
    return np.dot(hadamard(), state)

def hadamard():
    # Error: Wrong dimensions
    return np.array([[1, 1], [-1, 1]])
