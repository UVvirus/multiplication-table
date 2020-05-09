number=float(input("Enter the number:"))

for i in range(1,10):
    value=i * number
    value=round(value,4)
    print(i,"*",number,"=",value)

print("======================================================")
for i in range(1,10):
    value = i ** number
    value=round(value,4)
    print(i, "**", number, "=", value)