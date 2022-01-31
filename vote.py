#voting
age=int(input("enter your age"))
citizenship=str(input("enter your citizenship"))
if age>=18 and citizenship == "kenyan":
  print ("can vote")
else:
  print("cannot vote")