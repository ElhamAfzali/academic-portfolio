## sum of threee numbers

def max_3_numbers(a, b, c):
  if a >= b and a >=c:
    return a
  elif b>=a and b>=c:
    return b
  else:
    return c
      
x = max_3_numbers(10, -200, 3)
print(x)

## sum_of_all_numbers

def sum_of_all_numbers(*args):
  summ = 0
  for number in args:
    summ += number
  return summ
  
list = [1, 2, 3, 4, 50]
x = sum_of_all_numbers(*list)
print(x)


## multiply all numbers

def multiply_all_numbers(*args):
  multy = 1
  for number in args:
    multy *= number
    
  return multy
  
list = (8, 2, 3, -1, 7)
print(multiply_all_numbers(*list))


