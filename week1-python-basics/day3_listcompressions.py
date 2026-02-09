# squares = [i*i for i in range(11)]
# print(squares)

# even = [n for n in range(50) if n%2==0]
# print(even)

multiply= lambda x,y: x * y

print(multiply(3,4))

nums= [1,2,3,4]

result= map(lambda x:x*2, nums)

print(list(result))