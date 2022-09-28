from typing import List, Dict, Tuple, Union

def listFunction1(a: List, b: Dict, c: Tuple[List, Dict]) -> Union[int, float]:
    pass

def listFunction2(a: list) -> int:
    pass

if __name__ == "__main__":

    # note the form the type annotations are listed 
    print(f"listFunction annotations: {listFunction1.__annotations__}")
    print(f"listFunction annotations: {listFunction1.__annotations__}")
    
    print("Calling function with bad types... ")

    # running these functions with incorrect types does nothing...
    listFunction1(None, 1, 10)
    listFunction2(None)