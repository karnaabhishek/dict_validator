n = int(input('Enter number of elements'))
generic_dict = {}
for i in range(n):
    key = input("Enter Key:")
    a = int(input("Enter datatype: 1 for string: 2 for integer: 3 for boolean: 4 for float:"))
    if (a==1):
        value = input("Enter Value")
    elif (a==2):
        value = int(input("Enter Value"))
    elif (a==3):
        value = bool(input("Enter Value"))
    elif (a==4):
        value = float(input("Enter Value"))
    else:
        raise Exception("Invalid Data")

    generic_dict[key] = value

rules = {"max_length":20, "min_length":2, "max_value":1000, "min_value":0, "boolean": True}

def validator(dict, rules):
    flag = True
    for i in dict.keys():
        if (isinstance(dict[i], int) and not(dict[i]<rules["max_value"] and dict[i]>rules["min_value"])):
            flag = False
            break
        elif (isinstance(dict[i], float) and not(dict[i]<rules["max_value"] and dict[i]>rules["min_value"])):
            flag = False
            break
        elif (isinstance(dict[i], str) and not(len(dict[i])<rules["max_length"] and len(dict[i])>rules["min_length"])):
            flag = False
            break
        elif (isinstance(dict[i], bool) and not(dict[i]==True)):
            flag = False
            break
        
    return flag
print(validator(generic_dict, rules))

    




