marks=float(input("enter your marks:"))
if marks < 0 or  marks > 100:
    print("invalid marks")   
elif marks >= 90 :
      grade="A"
elif marks >= 75:
         grade="B"
elif marks >= 60: 
         grade="c"
elif marks >= 40:
         grade="D"
         print("your grade is:",grade)
else:
        grade="F"
        if marks<30:
             print("very poor performance")
marks=int(input("enter your marks:"))
if marks < 0 or marks > 100:
      print("invalid marks! enter between 0 and 100.")
else:
      if marks >=90:
            grade="A"
      elif marks >= 75 and marks < 90:
            grade="B"
      elif marks >= 60 and marks < 75:
            grade="C"
      elif marks >=40 and marks < 60:
            grade="D"
      else:
            grade="F"
            if marks < 30:
                  print("very poor performance")

      print("your gradde is:",grade)          
   