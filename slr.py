def slr():
    while True:
        print("We recommend an SLR camera")
        print("Do you currently own Nikon or Canon lenses? [Y/n]")
        user_lens = input("> ")
        if user_lens.lower() == "y":
            print("Nikon or Canon?")
            lens_quest = input("> ")
            if lens_quest.lower() == "nikon":
                print("Good news! Almost every current Nikon SLR is compatible!")
                break
            elif lens_quest.lower() == "canon":
                print("If your lenses were made before 1987,",
                "you will have to buy new lenses, in which case",
                "we recommend either a Nikon or Canon SLR.")
                break
            else:
                print("That is not a valid option. Enter Nikon or Canon.")
        elif user_lens.lower() == "n":
            print("Flip a coin: Canon and Nikon are both great.")
            break
        else:
            print("That is not a valid choice. Please enter Y or N.")
slr()
