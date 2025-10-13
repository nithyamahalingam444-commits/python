salary=int(input("Enter a salary"))
year=int(input("enter year"))
if year>5:
    bouns=salary*0.05
    print("bouns salary", bouns)
    print("bouns after salary", salary+bouns)
else:
    print ("no bouns")
