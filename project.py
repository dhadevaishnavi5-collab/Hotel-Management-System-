#define the menu of restarant
menu={
    'pizza':80,
    'pasta':50,
    'coffee':50,
    'nudals':70,
    'burger':60
}
#greet
print('welcome to python restarant')
print("pizza: Rs80\npasta:Rs50 \ncoffee: Rs50\nnudals: Rs70\nburger: Rs60")
order_total=0
#80+80=160 N
item_1=input("enter the name of item you want to order=")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item{item_1} is not available yet!")


another_order=input('Do you want to add another item?  yes/no')
if another_order=="yes":
    item_2=input("enter the nampizzae of second item=")
    if item_2  in menu :
        order_total += menu[item_2]
        print(f"item {item_2} has been added to your order")
    else:
        print(f"ordered item {item_2} is not available!")
    
print(f"the total amount of items to pay is {order_total}")

