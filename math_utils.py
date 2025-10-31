def find_max_number(num1, num2, num3):
    if(num1 > num2) and (num1 > num3):
     return num1
    elif (num2 > num3):
     return num2
    else:
      return num3
        
def find_mean(num1, num2, num3):
     x = num1 + num2 + num3
       return(x/3)

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    y = num1 - mean
    w = num2 - mean
    v = num3 - mean
    t = y**2 + w**2 + v**2
      return(mean,(t/3)**0.5)

