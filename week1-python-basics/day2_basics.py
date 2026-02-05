import os
import csv
import json
# print(os.getcwd())


def cleaned_data(data):
  cleaned=[]
  for record in data:
    if(record["age"] is not None):
      cleaned.append(record)

  return cleaned

data = [ {"name": "Kunal", "age": 25}, {"name": "Rahul", "age": None}, {"name": "Amit", "age": 30} ]

# print(cleaned_data(data))

# with open("notes.txt", "r", encoding="utf-8") as file:
#   for line in file:
#     print(line.strip())

# with open("industry.csv", "r") as file:
#   rows= csv.reader(file)
#   for row in rows:
#     print(row)

# with open("demo.csv", "w", newline="") as file:
#   write= csv.writer(file)
#   write.writerow(["Name","Age","Ph Number"])
#   write.writerow(["Kunal",23,"992"])

# with open("demo.csv","r") as file:
#   read= csv.DictReader(file)
#   for row in read:
#     print(row["Name"], row["Age"])

data={
  "Name" : "Kunal",
  "Age": 23
}

# with open("profile.json","w") as file:
#   json.dump(data,file, indent=4)

# with open("profile.json","r") as file:
#   read= json.load(file)

# print(read["Age"])

# with open("demo.csv","a") as file:
#   nextst= csv.writer(file)
#   nextst.writerow(["Shreya",21,"88"])

# with open("demo.csv","r",newline="") as file:
#   rows= csv.DictReader(file)

#   for row in rows:
#     row["Age"]=int(row["Age"])

#   print(type(row["Age"]))

with open("profile.json", "r") as file:

  print(json.load(file))

data["skills"]= ["Python","Git"]

# with open("profile.json","w") as file:
#   json.dump(data,file,indent=4)

# with open("profile.json", "r") as file:

#   print(json.load(file))

data["skills"].append("Docker")

with open("profile.json","w") as file:
  json.dump(data,file,indent=4)

with open("profile.json", "r") as file:

  print(json.load(file))
