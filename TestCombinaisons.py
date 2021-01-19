import itertools




# Driver Function
if __name__ == "__main__":

    list1 = ['a1','a2','a3']
    list2 = ['b1', 'b2', 'b3']

    l=[list1, list2]

    for x in itertools.product(list1, list2):
        print(x)