import json
import datetime
import asyncio
import time

def fun():
    time.sleep(10)
    print("hello")

async def funck():
    await asyncio.sleep(10, result='hello')

# loop = asyncio.get_event_loop()
# loop.run_forever(funck)
# loop.stop()

print("here")
# print(int("-1"))
# & | !
if __name__ == "__main__":
    print(__name__)
    # int_1: None = None
    # a: dict = {"id": 0, "name": "a"}
    # a: None|str = None
    # str_a: str = json.dumps(a)
    # print(f"{str_a}")
    # still_a_string: str = '"this is a string"'
    # print(type(str_a))
    # b: bytes = str_a.encode("utf-8")
    # print(b)
    # # *args
    # a: list = [1,2,3,4,4]
    # b: tuple = (1,2,3,4)
    # c: tuple = tuple(a)
    # x: set = set(a)
    # before = datetime.datetime.now()
    # print(a+b)
    # after = datetime.datetime.now()
    # print(after-before)
    # # **kwargs
    # v: dict = {'A': 1, "B": 2}
    # vr = fun()

    # asyncio.run(funck())
    
    class A:
        def __init__(self):
            pass
        
        def __repr__(self):
            return "this is a class"
        
    s = A()
    print(len("Константин константинович константиновский-оглы-байрам"))
    def decunstruct_ip(ip: str) -> int:
        """
        0.0.0.1 -> 1
        O(n) -> O(1)
        """
        pass
    