from restaurant import *
 
order = {
    
    "items": []
    
}
 
##################################################
food = loadFood() # lists > 0 ...

while True:
    option = printMenu()
    
    if option == 0:
        break
    
    if option == 1:
        printFood(food)
        input("Hit enter to continue")
        
    if option == 2:
        selected_i = int(input("Which item: ")) -1 
        print(f"You've selected <<{food[selected_i]['name']} >> ")
        quantity = int(input("How many: "))
        price_per_item = quantity * food[selected_i]['price']['amount']
        
        if  food[selected_i]["avail"] >= quantity:
            print(f"{food[selected_i]['name']} is choosen")  
            print(
                f"<<{food[selected_i]['name']}>> x {quantity} = {price_per_item:8.2f}{food[selected_i]['price']['currency']}"
            )
            if input("Confirm your order(yes/no): ") == "yes":
                order["items"].append({
                    "name": food[selected_i]['name'],
                    "quantity": quantity,
                    "total": {
                        "amount": price_per_item,
                        "currency": food[selected_i]['price']['currency']
                    }
                })
        else:
            print(f"Stock of {food[selected_i]['name']}: {food[selected_i]["avail"]}")        
            input("Hit Enter to continue")
            
    if option == 3:
        sum = 0
        
        for i in order["items"]:
            print(i)
            sum += i["total"]["amount"]
            
        print("Total: ", sum, "MDL")
        input("Hit Enter to continue")