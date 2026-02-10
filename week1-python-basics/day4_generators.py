def count_up_to(max):
  current =1
  while current<=max:
    yield current
    current+=1

# for num in count_up_to(5):
#   print(num)

nums = (x*2 for x in range(10))

print(type(nums))

# for i in nums:
#   print(i)

def read_numbers():
  for i in range(10):
    yield i

def square_numbers(x):
  for i in x:
    yield i*i

pipeline = square_numbers(read_numbers())

# for num in pipeline:
#   print(num)

for num in square_numbers(5):
  print(num)