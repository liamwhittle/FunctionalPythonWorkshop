from typing import Callable
from math import tan, pi

def clip_function_0_1(func: Callable):
    def clipped_function(*args, **kwargs):
        ret = func(*args, **kwargs)
        return min(1, max(0, ret))
    return clipped_function


clipped_tan = clip_function_0_1(tan)

if __name__ == "__main__":
    x = pi/2.1
    print(f"tan({x}) = {tan(x)}")
    print(f"clippped_tan({x}) = {clipped_tan(x)}")

    x = pi/0.9
    print(f"tan({x}) = {tan(x)}")
    print(f"clippped_tan({x}) = {clipped_tan(x)}")