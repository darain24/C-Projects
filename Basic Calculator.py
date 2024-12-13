first=int(input("Enter 1st no:"))
second=int(input("Enter 2nd no:"))
operator=input("Select an operator (+,-,*,/,%)")
if operator=="+":
    print(first+second)
elif operator=="-":
    print(first-second)
elif operator=="*":
    print(first*second)
elif operator=="/":
    print(first/second)
elif operator=="%":
    print(first%second)
else:
    print("Invalid operator")