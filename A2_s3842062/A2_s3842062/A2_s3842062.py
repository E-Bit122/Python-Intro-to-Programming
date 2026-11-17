#COSC1519 Introduction to Programming
#A2 Programming Project
#Student name: Ethan Haberl
#Student number: s3842062
#Practical group teacher: Steven Korevaar

print("Hello there! welcome to the world of Cyberpunk 2078, the text-based game! \nMy name is Oak! People call me the Cyber Prof!\n")

#get player name
player_name = input("First, what is your name? ")
print("Right! So your name is ", player_name, "!\n", sep="")

#set up decklist and deck attacks, able to be changed here
decklist = ["NETWATCH NETDRIVER MK.V", "MILITEK PARALINE", "TETRATRONIC RIPPLER MK.4"]
#CHANGE ATTACK MOVES AND DAMAGE HERE
def get_deck(deck_name):
    #NETWATCH NETDRIVER MK.V
    netwatch = {"Overload": 40, "Breach": 35, "Quickhack": 20, "DDOS": 500}
    #MILITEK PARALINE
    militek = {"Steal Data": 30, "Short Circuit": 35, "Breach Protocol": 22, "Distract": 0.75}
    #TETRATRONIC RIPPLER MK.4
    tetratronic = {"Ultimate Quickhack": 50, "Remote Activation": 35, "Overload": 40, "Reboot Optics": 0.5}

    if deck_name == "NETWATCH NETDRIVER MK.V":
        deck = netwatch
    elif deck_name == "MILITEK PARALINE":
        deck = militek
    elif deck_name == "TETRATRONIC RIPPLER MK.4":
        deck = tetratronic
   
    return deck
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------

print("There are 3 Cyberdecks here! When i was young i used to have many more! \nIn my old age, I only have 3 left, but you can have one! Choose!\n")

#choose deck type, looper keeps loop running until turned off
#all loops have a try statement for non-integer inputs as well as an if statement for inputs outside of the range
looper = True
while looper == True:
    try:
        print("\t1 - NETWATCH NETDRIVER MK.V")
        print("\t2 - MILITEK PARALINE")
        decknumber = int(input("\t3 - TETRATRONIC RIPPLER MK.4\n"))

        if decknumber < 4 and decknumber > 0:
            deckname = decklist[decknumber - 1]
            looper = False
        else:
            print("Hey! That's not an option!\n")
    except:
        print("Listen kiddo, ya gotta put in an integer.\n")
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------

print("Very well, your very own Cyberpunk legend is about to unfold! \nA world of dreams and adventures with ", player_name, " and their mighty ", deckname, " awaits! Let's go!\n\n", sep="")
print("\tThe year is 2078, \n\tAfter a long day at work, you are finally home. \n\tYou are greeted by Jonny Goldhand, your dog, delighted to see you.")
print("\tThen, right when you get on your PC to play your favourite game ...\n")
print("Your Arasaka A2 is ringing, what do you do?")

#phone ringing response
looper = True
while looper == True:
    try:
        print("\t1. Ignore it and continue watching.")
        print("\t2. Smack the phone to make it stop.")
        phone_reaction = int(input("\t3. Answer the phone.\n"))

        if phone_reaction < 4 and phone_reaction > 0:
            if phone_reaction == 1:
                print("Your Arasaka A4 is ringing, what do you do?")
            elif phone_reaction == 2:
                print("You smack your phone. It keeps ringing. Why would you do that?\n")
            elif phone_reaction == 3:
                looper = False
        else:
            print("Oak's words echoed... \"Hey! That's not an option!\"\n")

    except:
        print("Oak's words echoed... \"Listen kiddo, ya gotta put in an integer\"\n")
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------


print("Hey ", player_name, "!!\n", sep="")
print("\tIt's Jackie!... \n\t\"I've got a little gig coming up and we need you hack the security system to get us in!")
print("\tCome on, it's gonna be easy, you in?\n")

#response to go on job, includes program ending function
#if program end is picked, if statement skips the rest of the code
looper = True
continue_program = True
while looper == True:
    try:
        print("\t1. Sure, I need the cash.")
        print("\t2. <Say Nothing>")
        response = int(input("\t3. No can do buddy... [end game]\n"))

        if response < 4 and response > 0:
            if response == 1:
                looper = False
            elif response == 2:
                print("Are ya there buddy?\n")
            elif response == 3:
                print("\t", player_name, ", you are a highly respected corpo and you thought better of jackie. \n\tYou have a social security number, you pay your taxes, and ...", sep="")
                print("\tYou sure as h*** aren't losing your job for some gig.\n")
                continue_program = False
                looper = False
        else:
            print("Oak's words echoed... \"Hey! That's not an option!\"\n")

    except:
        print("Oak's words echoed... \"Listen kiddo, ya gotta put in an integer\"\n")

   

#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------


#rest of code is skipped if continue program is false from previous section
if continue_program == True:

    print("\tSiiiick! Let's meet tonight at my place at my place 11 and then we can go smoke these pandejos.\n")
    print("\tYou finish your game get ready. You hop on your ARCH NAZARÉ bike and ride there.\n")
    print("\tAfter meeting with the team, you get onsite with them.\n\tWhile they move towards the front door, you remain in the back to support them.")
    print("\tTime to jack in to the building access point and try to hack it!\n")

    #gateway fight section, loops until gateway_health variable is equal to or below zero
    attacks = ["guess", "black ice", "DDOS"]
    gateway_health = 30
    while gateway_health > 0:
        try:
            print("The gateway health is now ", gateway_health, ", how do you attack it?", sep="")
            print("\t1. Guess the username / password.")
            print("\t2. Use a black ice attack.")
            attack = int(input("\t3. Throw a DDOS attack [one shot!]\n"))
                        
            if attack < 4 and attack > 0:
                        
                if attack == 1: #guess username/password
                    print("Jackie looks at you trying to enter 'admin/password'\n\"What the hell are you doing ", player_name, "!?!!?", sep="")
                    print("\"It's not the 20s, that won't be so easy!\n")
                    damage = 0
                elif attack == 2: #black ice
                    damage = 10
                elif attack == 3: #DDOS
                    damage = 500

                gateway_health -= damage
                print("You inflict", damage, "to the gateway.")

            else:
                print("Oak's words echoed... \"Hey! That's not an option!\"\n")

        except:
            print("Oak's words echoed... \"Listen kiddo, ya gotta put in an integer\"\n")

        
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------

    print("\nYou are now inside the building security system. \nYou stop all alarms and open the door for your team. \n...")
    print("While waiting for your team to take of the security personel, \nyou play a few games of Fate Sole/Order on your Arasaka A2")
    print("Your team is now in front of the safe boxes, you need to hack them on by one. \nTime to bring out your Cyberdeck.\n")

    #Fight using deck section
    #gets deck from get_deck function
    #uses nested loop to go through each box, only moving on once their health is 0
    #modifier is used for certain attacks that 'lower defence'

    deck = get_deck(deckname)
    for boxcount in range(0, 4):
        box_health = 100.0
        modifier = 1.0 #defence modifier
        deck_list = list(deck) #Gets the names of all attacks
        attack_input = 0 #declared here as used in two sections
        while box_health > 0:
            if boxcount == 0:
                box = "1x1"
            elif boxcount == 1:
                box = "1x2"
            elif boxcount == 2:
                box = "2x1"
            elif boxcount == 3:
                box = "2x2"

            print("You are in front of box", box)
            print("The box health point is ", box_health, ", what do you do?\n", sep="")
            try:
                print("\t1. ", deck_list[0])
                print("\t2. ", deck_list[1])
                print("\t3. ", deck_list[2])
                print("\t4. ", deck_list[3])
                attack_input = int(input(""))
                
            except:
                print("Oak's words echoed... \"Listen kiddo, ya gotta put in an integer\"\n")

            if attack_input < 5 and attack_input > 0:

                attack_name = deck_list[attack_input - 1] #attack name acquired
                damage = deck[attack_name] #damage calculated from deck dictionary

                if damage > 1:
                    box_health -= damage*modifier #damage modifier changes if a defence move is used
                    print("Nice!")
                    print("You inflict", damage*modifier, "damage to the safe.")
                    if box_health <= 0:
                        print("Nice! Safe", box, "has been opened!\n\n")
                else:
                    modifier += damage #adds to damage modifier
                    print("The box's defences has been lowered")
            else:
                print("Oak's words echoed... \"Hey! That's not an option!\"\n")
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------


    print("Phew! All the safes are now open. \nYou can relax...")
    input("<press enter>")
    print("Something is beeping in the background \n...")
    input("<press enter>")
    print("It is your police scanner \n... \nSomehow they have been warned and they are coming to get you!")
    input("<press enter>")
    print("The police are getting closer!")

    #Final section, waiting for police
    #only have 3 chances until game ends
    team_back = 0
    for chance in range(0, 3):
        print("The Police are getting closer!\nWhat do you do??\n\n")


        try:
            print("\t1. Leave the place now")
            print("\t2. Yell at your team to fall back")
            police_response = int(input("\t3. Enjoy your sweet sweet time, your team will be back soon and you're such a daredevil!\n"))
        except:
            print("Oak's words echoed... \"Listen kiddo, ya gotta put in an integer\"\n")


        if police_response < 4 and police_response > 0:

            if police_response == 1: #immediately exits
                print("You and", chance, "of your team members made it but",3-chance ,"did not\n")
                print("They won't forget that you abandoned them! Better leave the city!")
                break

            elif police_response == 2: #if clicked three times in a row, first if statement is triggered
                print("So far,", chance+1, "out of 3 have fallen back...")
                team_back += 1
                if chance == 2 and team_back == 3:
                    print("You're all here, but so are the police!\nBetter get out of here!")
                    print("You and the team are chased out of the city, never to return.")
                elif chance == 2:
                    print("You waited too long, the police are here.")
                    print("It's jail time for you!")

            elif police_response == 3: #does nothing until last iteration
                if chance == 2:
                    print("You waited too long, the police are here.")
                    print("It's jail time for you!")

    print("\t...\n\t...\n\t...\n\tCRIME NEVER PAYS\n")
print("███  ██   █  ██")
print("█    █ █  █  █ █")
print("██   █  █ █  █  █")
print("█    █   ██  █ █")
print("███  █    █  ██")


