def rest():
 
 for i in range(item): 
   item=int(input("enter the number of item you want:")) 
while True:
     
    item_name=input("enter the item you want:")
    quantity=int(input("enter the quantity you want for it:"))    
    price=int(input("enter the price:"))
    if item_name=="done":
      break
    tip=int(input("enter the amount of tips you want to give:"))
    total_bill=0
    bill= total_bill + price*quantity
    taxRate=10.0
    total_cost=bill+taxRate*tip
    print("total bill is:",total_cost)
rest()

