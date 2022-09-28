import numpy as np
import time
from functools import partial

"""
The purpose of this file is to compare the runtime speeds of
three different implementations of matrix multiplication.
Your job is to make this code more elegant - i.e. it should do the exact
same thing as it currently does, but be:
    - easier to read
    - more extensible
    - beautiful
"""


def loopy_matmul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    assert a.shape[1] == b.shape[0]
    out_arr = np.zeros((a.shape[0], b.shape[1]))
    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            out_arr[i][j] = sum(a[i, :] * b[:, j])
    return out_arr


def functional_matmul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    assert a.shape[1] == b.shape[0]
    return np.array(list([np.array(list(map(lambda col: sum(row * col), b.T))) for row in a]))


def np_matmul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    assert a.shape[1] == b.shape[0]
    return np.matmul(a, b)


if __name__ == "__main__":
    # create some random data
    a = np.random.random((200, 300))
    b = np.random.random((300, 100))

    t = time.time()
    r1 = loopy_matmul(a, b)
    print(f"loopy_matmul took: {round(time.time() - t, 4)} seconds")

    t = time.time()
    r2 = functional_matmul(a, b)
    print(f"functional_matmul took: {round(time.time() - t, 4)} seconds")

    t = time.time()
    r3 = np_matmul(a, b)
    print(f"np_matmul took: {round(time.time() - t, 4)} seconds")

    # assert the returned arrays are identical

    print(f"Error between first two approaches = {np.sum(abs(r1 - r2))}")
    print(f"Error between second two approaches = {np.sum(abs(r2 - r3))}")
