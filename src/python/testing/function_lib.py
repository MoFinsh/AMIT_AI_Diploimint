def valuesFun(dict):                            #colecting values from dictionaries
    val = []
    for values in dict.values():
        val.append(values)
   
    return val  

# creat list function

def creat_list():
    x=int(input("please enter the list length: "))

    list_1 = []

    for i in range(x):
        num = int(input(f"Enter number {i+1}"))
        list_1.append(num)

    print(list_1)