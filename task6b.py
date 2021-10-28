def maximum(tup):
    max_num = 0
    for x in tup:
        if x > max_num:
           max_num = x
    print(max_num)

tup = (1, 2, 3)
tup = list(tup)  #convert tuple to list inorder to add numbers
tup.extend([14, 60, 4]) #add multiple numbers to list
tup = tuple(tup)

maximum(tup)
