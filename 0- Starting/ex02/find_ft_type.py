def all_thing_is_obj(object: any) -> int:
#your code here
    if type(object) is list:
        print("List : <class 'list'>")
    elif type(object) is tuple:
        print("Tuple : <class 'tuple'>")
    elif type(object) is set:
        print("Set : <class 'set'>")
    elif type(object) is dict:
        print("Dict : <class 'dict'>")
    elif type(object) is str:
        print(object, "is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
    return 42