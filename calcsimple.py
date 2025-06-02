#basic calculator program
#asking for user request
number1=int(input("enter first number: "))
number2=int(input("enter second number: "))
operation =input("enter the operation(+,-,*,/")

#operations from the user input
if operation =="+":
  result=number1+number2
  print(result)
elif operation=="-":
  result=number1-number2
  print(result)
elif operation==*:
  result=number1*number2
  print(result)
elif operation=="/": # check for division by zero (0)
  if number2!=0:
  result=number1//number2
  print(result)
  else:
    print("error")
else:
  print("invalid operation")
