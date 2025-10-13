apptitude=int(input("enter a apptitude mark"))
gd=int(input("enter a GD value"))
tech=int(input("enter a technical mark"))
hr=int(input(" HR round mark"))      
total=apptitude+gd+tech+hr

if total>=390:
    print ("eligible for 30000 salary")
elif total>=380:
    print("eligible for 28000 salary")
elif total>=370:
    print("eligible for 25000 salary")
elif total>=350:
    print("eligible for 20000 salary")
else:
    print("not eligible")

