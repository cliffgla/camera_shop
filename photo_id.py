# define types of photography
photo_styles = [
"street", "portrait", "landscape", "photojournalism", "fine art",
"wildlife", "snapshot"
]

printed_list = ", ".join(photo_styles)

# recommend cameras, lenses, other gear depending on camera type.

def rangefinder():
    print("We recommend a rangefinder camera. ")

def slr():
    pass

def view_camera() :
    print("We recommend a 4x5 view camera. ")


def medium_format():
    print("We recommend a Mamiya RZ67. ")


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
                break
            if pref.lower() == "portrait":
                return medium_format()
                break
            if pref.lower() == "landscape":
                return view_camera()
                break
        else:
            print("That isn't an available option. Please choose from the list of"
            "available options: ")
            print(" ")
            user_pref()
            break

user_pref()




# return styles of photography based on user feedback
