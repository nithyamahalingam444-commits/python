#program to read the temprature in centigrade and display
temp=int(input("Enter a Weather"))
if temp<0:
    print("Freezing Weather")
elif temp>0 and temp<=10:
    print("Very Cold Weather")
elif temp>10 and temp<=20:
    print("cold Weather")
elif temp>20 and temp<=30:
    print("Normal in temp")
elif temp>30 and temp<=40:
    print("Hot")
else:
    print("very hot")
