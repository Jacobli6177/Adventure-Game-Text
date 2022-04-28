# Adventure game

answer = input("Do you wat to play this text adventure game ?[Y/N]")

if answer == "Y":
    print("Now let's get started !!")
    answer = input("Would you like to explore the Jungle or the ocean? [Ocean/Jungle]")
    if answer == "Ocean":
        print("Let's get on the submarine!!!")
        answer = input("How deep would you like to go 1000ft or 10000ft[1000/10000]")
        if answer == 1000:
            print("You got it, Sir!")
        else:
            print("Your submarine crashed into the ground!! You lose!")

    else:
        print("Put on your equipments and Let's get going!!!")




else:
    print("Darn it. Come back Next time !!!")
