def all_thing_is_obj(object: any) -> int:
    object_type: str = type(object)
    object_name: str = type(object).__name__.capitalize()

    if type(object) == str:
        print(f"{object} is in the kitchen : {object_type}")
    elif type(object) == int:
        print("Type not found")
    else:
        print(f"{object_name} : {type(object)}")
    return 42
