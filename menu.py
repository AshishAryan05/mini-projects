menu = {
    "Pasta" : 60,
    "Noodles" : 50,
    "Coffee": 90,
    "Burger" : 70,
    "Pizza" : 95
}
print("Welcome To My Restaurant😊")
print("Pasta: Rs.60\nNoodles: Rs.50\nCoffee: Rs.90\nBurger: Rs.70\nPizza: Rs.95")

ord_total = 0
item_1 = input("Enter the name of item you want to order :  ")
if item_1 in menu:
    ord_total += menu[item_1]
    print(f"Your Ordered item {item_1} has been added to your Order! ") 
else :
    print("Please order something else we can serve you!")
another_ord = input("Do you want to add another item?  (Yes/No)   ")
if another_ord == "Yes":
              item_2 = input("Enter the name of second item : ")
              if item_2 in menu :
                     ord_total += menu[item_2]
                     print(f"Item {item_2} has been added to order! ")
              else :
                     print(f"Ordered item {item_2} is not Available!") 
print(f"The total amount of your order to pay is  Rs.{ord_total}")  
print("Thank You for Visiting!!!")                         