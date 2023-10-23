num=int(input("Enter Number :"))

if num>0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is a negative number")

age=int(input("Enter Age to vote:"))
if age>=18 and age<=80:
    print("You are elligible to vote")
else:
    print("You cannot vote beccause you are a minor/old")