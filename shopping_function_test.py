inventory = {

"Nikon": 800,
"Leica": 5000,
"Zeiss": 2000,
"Mamiya":1000,
"View Camera": 1000

}

cart ={}



def loop_cart():
    print("What camera do you want?")
    shopper = input("> ")
    for key, value in inventory.items():
        if shopper.title() == key:
            cart.update({key:value})
    print(cart)



#cart()

loop_cart()
