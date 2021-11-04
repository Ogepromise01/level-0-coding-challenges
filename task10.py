def common_letters(str1, str2):
    s1 = set(str1)
    s2 = set(str2)
    com_let = s1 & s2 #intersection of str1 and str2
    print("Common Letters:", com_let)

common_letters("house", "computers")
