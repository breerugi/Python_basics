# list are ordered mutable
fruits=["Mangoes","Oranges","Bananas","Apples"]
fruits.sort()
num=[11,3,7,0,14,4,-3,2]
num.sort()
num[3]=9
rep=num*2
print(len(num))


print(fruits)
fruits[1]= "Watermelon"
print(f"I love eating {fruits[1]}")
print(num)
print(rep)


# tuple
cars=("Toyota","Mercedes","Nissan","Toyota")
print(cars)
print(cars[0])
tup=cars*3
print(tup)
print(tup.count("Toyota"))


# sets
days={"Monday","Tuesday","Wednesday","Thursday","Friday"}
print(days)


# dictionaries

staff_details={"Name":"Brenda","Age":"22","Company":"eMobilis","Gender":"Female","Salary":"64782738"}
print(staff_details)
print(f"Name : %s" %staff_details["Name"])
print(f"Gender : %s" %staff_details["Gender"])
print(f"Age : %s" %staff_details["Age"])
print(f"Company : %s" %staff_details["Company"])