# define types of photography
photo_styles = [
"street", "portrait", "landscape", "photojournalism", "fine art",
"wildlife", "snapshot"
]

rangefinders = [
"Leica", "Zeiss",
]

printed_list = ", ".join(photo_styles)

# recommend cameras, lenses, other gear depending on camera type.

def rangefinder():
    print("We recommend a rangefinder camera. What is your budget? "
    "Please enter a number between 1000 and 10,000")
    price = input("> ")
    print(price)
    if int(price) < 5000:
        print("We recommend Zeiss.")
    else:
        print("We recommend Leica.")

def slr():
    print("We recommend an SLR camera")
    print("Do you currently own Nikon or Canon lenses? [Y/n]")

def view_camera() :
    print("We recommend a 4x5 view camera. ")


def medium_format():
    print("We recommend a Mamiya. ")


# take user input to decide what kind of camera to buy
def user_pref():
    shopping = True
    while shopping:
        print(printed_list+"?")
        print(" ")
        pref = input("What kind of photography do you enjoy? ")
        print (pref)

        if pref.lower() in photo_styles:
            if pref.lower() == "street":
                return rangefinder()

            if pref.lower() == "portrait":
                return medium_format()
                break
            if pref.lower() == "landscape":
                return view_camera()
                break

            if pref.lower() =="photojournalism":
                return slr()

            if pref.lower() == "snapshot":
                print("You're smartphone is already a great snapshot camera.")
                break
        else:
            print("That isn't an available option. Please choose from the list of"
            "available options: ")
            print(" ")
            user_pref()
            break

user_pref()




# return styles of photography based on user feedback
