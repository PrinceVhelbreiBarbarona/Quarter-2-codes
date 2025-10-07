#Learning activity 7.2

dis =  float(input("Enter the distance in kilemeters: "))
rate = float(input("Enter the rate per kilometer(₱): "))
def cost(dis, rate):
     total = dis * rate
     return total
print("The total cost is ₱", cost(dis, rate))