file=open("data.txt","w")
data=input("enter some text:")
file.write(data)
file.close()
file=open("data.txt","r")
content=file.read()
print(content)
file.close()
file=open("data.txt","a")
more_data=input("enter text to append:")
file.write("\n"+more_data)
file.close()
try:
    file=open("data.txt","r")
    print(file.read())
    file.close()
except fileNotFoundError:
    print("file not found!")
import csv
file=open("students.csv","w",newline="")
writer=csv.writer(file)
writer.writerow(["ID","Name","Marks"])
writer.writerow([1,"Alice",85])
writer.writerow([2,"Bob",90])
writer.writerow([3,"charlie",78])
file.close()
file=open("students.csv","r")
reader=csv.reader(file)
for row in reader:
    print(row)
    file.close
with open("data.txt","r")as file:
    print(file.read())
