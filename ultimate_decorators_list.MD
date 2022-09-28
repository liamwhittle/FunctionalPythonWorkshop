# Essential List of Decorators
**A list of decorators every python programmer should know**

### Custom Function Decorator Template
#### :thinking: What to use this for?
Use this template for any new functional decorator (a decorator which takes a function as argument
and returns a new, wrapped function.

:computer: usage:

```python
from functools import wraps
from typing import Callable

def my_decorator(func: Callable) -> Callable:
    """
    My decorator returns a wrapped version of the input func when used like so:
    @my_decorator
    def func():
        ...
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # pre-functionality
        ret_val = func(*args, **kwargs)
        # post-functionality
        return ret_val
    return wrapper
```

### `@numba.jit`
#### :thinking: what does it do?
JIT stands for Just In Time compilation. Any function you decorate with `numba.jit` will
compile at runtime to machine code and therefore be able to run a LOT faster.

##### Use for:

:white_check_mark: algorithms with lots of if statements, looping and control logic

##### Don't use for:

:no_entry_sign: any function using an external library which isn't numpy

:no_entry_sign: algorithms which could be vectorized with numpy or torch

:floppy_disk: from functools import wraps

:computer: usage:

```python
@numba.jit
def longest_increasing_sequence(arr: np.ndarray) -> int:
    """
    Decorate any function with numba.jit which only uses basic python features
    such as loops, control flow statements, fundamental types, and no extenral
    libraries except numpy.
    """
    max_seq_len = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            max_seq_len += 1
        else:
            max_seq_len = 0
    return max_seq_len
```

### `@property and @property.setter`
#### :thinking: what does it do?
Overloads the normal behavior of `self.variable`. For input validation and other post variable 
assignment functionality.

##### Use for:

:white_check_mark: important class attributes requiring input validation

##### Don't use for:

:no_entry_sign: every class variable ever. We don't need more code than we need.

:floppy_disk: part of the standard python library

:computer: usage:

```python
class EvenInt:
    def __init__(self, value):
        self.value = value
    
    @property
    def value(self):
        return self.value
    
    @value.setter
    def value(self, value: int):
        if value // 2 != 0:
            raise ValueError("Value must be even!")
        else:
            self.value = value
```
