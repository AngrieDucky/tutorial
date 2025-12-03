import json

@app.errorhandler(404)
async def not_found_error(error):
    return jsonify({"message": "Resource not found"}), 404

# print(int("-1"))
# & | !
if __name__ == "__main__":
    int_1: None = None
    a: dict = {"id": 0, "name": "a"}
    a: None|str = None
    str_a: str = json.dumps(a)
    print(f"{str_a}")
    still_a_string: str = '"this is a string"'
    print(type(str_a))
    b: bytes = str_a.encode("utf-8")
    print(b)
    # *args
    a: list = [1,2,3,4,4]
    b: tuple = (1,2,3,4)
    c: tuple = tuple(a)
    x: set = set(a)
    # **kwargs
    v: dict = {'A': 1, "B": 2}