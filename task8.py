def num_cov(num):
    hour_value = num // 60
    if hour_value == 1:
        print(hour_value, "hour")
    else:
        print(hour_value, "hours")
    min_value = num % 60
    if min_value == 1:
        print(min_value, "min")
    else:
        print(min_value, "mins")
   
num = 71    
num_cov(num)
