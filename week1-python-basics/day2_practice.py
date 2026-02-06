import csv

# with open(r"C:\Users\Kunal\OneDrive\Desktop\python\python-core\week1-python-basics\students.csv", "w",newline="") as file:
#   write= csv.writer(file)
#   write.writerow(["Name", "Age","score"])
#   write.writerow(["Kunal", 23,85])
#   write.writerow(["shreya", 21,80])
#   write.writerow(["nmis", 20,90])
#   write.writerow(["nnn", "40","95"])
#   write.writerow(["kkm", 30,75])

total_students =0
total_age=0
total_score=0
highest_score=0

with open("students.csv","r", newline="") as file:
  reader= csv.DictReader(file)

  for row in reader:
    age = int(row["Age"])
    score= int(row["score"])

    total_students+=1
    total_age+=age
    total_score+= score

    if(score>highest_score):
      highest_score=score

average_age= total_age/total_students
average_score= total_score/total_students

with open("summary.txt","w") as file:
  file.write(f"Total students: {total_students}\n")
  file.write(f"Average Age: {average_age}\n")
  file.write(f"Average Score: {average_score}\n")
  file.write(f"Highest score: {highest_score}\n")


print(total_students)
print(average_age)
print(average_score)
print(highest_score)
