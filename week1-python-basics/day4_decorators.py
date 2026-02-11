def log(func):
  def wrapper(*args,**kwargs):
    print("Values ", args)
    result = func(*args)
    print("Result is ", result)
    return result
  return wrapper  

def greater_first(func):
  def wrapper(a,b):
    if(a<b):
      a,b=b,a
    return func(a,b)

  return wrapper

@log
@greater_first
def sub(a,b):
  return a-b

@log
@greater_first
def divide(a,b):
  return a/b

@log
def add(*args):
  sum=0
  for num in args:
    sum += num
  return sum

result1 = sub(2,4)
print(result1)

result2 = divide(2,4)
print(result2)

add(2,2,4,6,8)