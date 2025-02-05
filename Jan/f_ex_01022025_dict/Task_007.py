
dict = {"a":231, "b":11, "c": 1, "d":3}

dict2= {"a":222, "b":12, "c": 2123, "d":0}

def get_max(dict):
    return max(dict.values())

def get_min(dict):
    return min(dict.values())

def sort_dict(dict):
    return sorted(dict.values())

print(sort_dict(dict))
print (get_max(dict))
print (get_min(dict2))

#get_max_min(dict2)


