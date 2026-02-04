x=1000
y="kunal"
z= "100"


# print(f"my name is {y} and i have {x} rupees")

# print(x-int(z))

a =97
b=6

# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)

# t = "Python Developer"
# print(t[::-1])

name = "  kunal nikam  "

# print(name)
# print(name.strip())
# print(name.upper())
# print(name.lower())
# print(name.replace("kunal", "KUNAL"))
# print(name.split())

email = "kunalnikam1550@gmail.com"

username, domain_part = email.split("@")
domain, extention = domain_part.split(".")
# print(f"Username: {username}")
# print(f"Domain: {domain}")
# print(f"Extention: {extention}")

l2= [3,33,14,55,33,2,42,99,477,5394]
l1 = [1, 22,34,55, "Leo", "ben10",19]
l1.append("viper")
l1.insert(2, "Ronaldo")
l1.pop()
l2.sort()

# print(l1)
# print(l2)

l3=[]

for num in l2:
  if num %2 == 0:
    l3.append(num)

# print(l3)

names=("kunal", "messi","ronaldo")
# print(type(names))

a = {1, 2, 3}
b = {3, 4, 5}

# print(a | b)  # Union
# print(a & b)  # Intersection
# print(a - b)  # Difference
# print(b - a)

dict1= {
  "name": "Kunal",
  "age" : 23,
  "Roll no" : 40
}
# print(dict1["age"])
# dict1["Roll no"] = 41

# for x,y in dict1.items():
#   print(f"{x}={y}")

a = 10
b = a
a = 20

# print(a)
# print(b)

list1 = [1, 2, 3]
list2 = list1

list1.append(4)

# print(list1)
# print(list2)

import copy

list1 = [1, 2, 3]
list2 = list1.copy()        # shallow copy

list1.append(4)

# print(list1)
# print(list2)

l1= [1,1,10,2,3,9,4,4,5,6,7,7,7,8]

unique= list(set(l1))
unique_preserve_order= dict.fromkeys(l1)
unique2= list(unique_preserve_order)

# print(l1)
# print(unique_preserve_order)
# print(unique2)

example= "Data Engineering"
reverse= example[::-1]
# print(reverse)

def demo(s):
  freq={}
  for i in s:
    freq[i]=freq.get(i,0)+1
  return freq

demo_string= input("Enter your string: ")
print(demo(demo_string))