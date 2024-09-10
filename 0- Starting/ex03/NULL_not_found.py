import math

def NULL_not_found(object: any) -> int:
#your code here
    match object:
        case None:
            print("Nothing: None ", type(object))
            return 0
        case float() if math.isnan(object):
            print("Cheese: nan ", type(object))
            return 0
        case int() if object == 0:
            print("Zero: 0 ", type(object))
            return 0
        case str() if object == '':
            print("Empty: '' ", type(object))
            return 0
        case bool() if object == False:
            print("Fake: False ", type(object))
            return 0
        case _:
            print("Type not found")
    return 1