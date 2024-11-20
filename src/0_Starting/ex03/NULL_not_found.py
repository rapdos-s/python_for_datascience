def NULL_not_found(object: any) -> int:
    object_name: str = ""
    object_type: str = type(object)

    if object_type == type(None):
        object_name = "Nothing"
    elif object_type == float and object != object:
        object_name = "Cheese"
    elif object_type == int and object == 0:
        object_name = "Zero"
    elif object_type == str and object == "":
        object_name = "Empty"
    elif object_type == bool and object == False:
        object_name = "Fake"
    else:
        print("Type not Found")
        return 1

    print(f"{object_name}: {object} {object_type}")
    return 0
