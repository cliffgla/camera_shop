inventory = {

"Nikon": 800,
"Leica": 5000,
"Zeiss": 2000,
"Mamiya":1000,
"View Camera": 1000

}


cart = {}

def add_to_cart():
    print("Which item would you like to add to cart")
    cart_add = input("> ")
    if cart_add.lower() == "nikon":
        cart.update(inventory[0])
    print(cart)

def cart_total():
    total = 0
    for key, value in cart.items():
        total += value
    print(total)

def shopping():
    while True:
        print("What would you like to buy?")
        buy = input("> ")
        if buy.lower() in inventory.keys():
            print("Testing 123")

#add_to_cart()

#cart_total()

shopping()
