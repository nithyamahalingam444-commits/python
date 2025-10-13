quantity=int(input("Enter a quantity"))
price=int(input("enter a item price"))
total_cost=quantity*price

if total_cost>1000:
    discount=total_cost*0.10
    discount-=total_cost
    print("discount applied for 10%")
else:
    print("discount not applied")
print("total_cost",total_cost)
    
 
