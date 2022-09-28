import math
import matplotlib.pyplot as plt

print("Hello! Weclome to the number grapher!")
print("-------------------------------------")

num_points: int = int(input("Enter number of points to display: "))
a = float(input("Enter x_min: "))
b = float(input("Enter y_min: "))
func = input("Enter a function to display (sin, cos, or tan: ")

if func == "sin":
    nums = []
    for i in range(num_points):
        step = (b-a) / num_points
        nums.append(math.sin(i * step + a))

elif func == "cos":
    nums = []
    for i in range(num_points):
        step = (b-a) / num_points
        nums.append(math.sin(i * step + a))

else:
    nums = []
    for i in range(num_points):
        step = (b-a) / num_points
        nums.append(math.tan(i * step + a))

plt.plot(nums)
plt.show()
