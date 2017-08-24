# define types of photography
photo_styles = [
"street", "portrait", "landscape", "photojournalism", "fine art",
"wildlife", "snapshot"
]

printed_list = ", ".join(photo_styles)

# recommend cameras, lenses, other gear depending on camera type.
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
                print("We recommend a rangefinder camera. ")
                break
            if pref.lower() == "portrait":
                print("We recommend a Mamiya RZ67. ")
                break
            if pref.lower() == "landscape":
                print("We recommend a 4x5 view camera. ")
                break
        else:
            print("That isn't an available option. Please choose from the list of"
            "available options: ")
            print(" ")
            user_pref()
            break

user_pref()




# return styles of photography based on user feedback
