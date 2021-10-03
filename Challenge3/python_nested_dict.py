
dictonary = {'a':{'b':{'c':'d'}}}

def nested_dict_values(dict_obj):
    for value in dict_obj.values():
        if isinstance(value, dict):
            for v in  nested_dict_values(value):
                yield v
        else:
            yield value
            
for value in nested_dict_values(dictonary):
    print(value)
