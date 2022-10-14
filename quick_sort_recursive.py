def f(list):
    if len(list) <= 1:
        return list

    a = []
    b = []
    for i in list:
        if i > list[1]:
            b.append(i)
        elif i < list[1]:
            a.append(i)
    return f(a) + [list[1]] + f(b)



# test = [5,10,12,2,6,1,3,11]
#
# print(f(test))
