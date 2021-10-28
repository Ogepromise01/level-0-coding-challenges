def area_of_triagle(a, b, c):
    perimeter = a + b + c
    s = (a + b + c) / 2  #calculates the semiperimeter
    area = ((s * (s - a) * (s - b) * (s - c)))**(1/2)
    print(area)
area_of_triagle(2, 3, 4)  

