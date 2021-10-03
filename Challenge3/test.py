
di = {'a':{'b':{'c':'d'}}
def myprint(di):
    for k, v in d.items():
        if isinstance(v, dict):
            myprint(v)
        else:
            print("{0} : {1}".format(k, v))