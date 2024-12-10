def key_args(**key_args):
    return key_args


result = key_args(name="Subrota", age=23, city="Joypurhat")

print(result.get("name"), result.get("age"), result.get("city"))
