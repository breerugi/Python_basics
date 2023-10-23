class fruits:
    def __init__(self, type, price, color):
        self.type = type
        self.price = price
        self.color = color

    def onyesha(self):
        print(f"I like eating {self.type} and it costs {self.price}, color being {self.color}")


# creating object
myobj = fruits("banana", "Ksh.20", "yellow")
myobj2 = fruits("berries", "Ksh.40", "red")
myobj3 = fruits("apples", "Ksh.30", "green")

myobj.onyesha()
myobj2.onyesha()
myobj3.onyesha()
