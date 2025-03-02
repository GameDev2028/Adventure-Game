import time

def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)

def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.")

def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        else:
            print_pause("Sorry, I don't understand.")

def house(items):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a fairie.")
    print_pause("Eep! This is the wicked fairie’s house!")
    print_pause("The fairie attacks you!")

    if "sword" not in items:
        print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")
    else:
        print_pause("As the fairie moves to attack, you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")

    fight_or_flight(items)

def cave(items):
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword with you.")
        items.append("sword")
    print_pause("You walk back out to the field.")

def fight_or_flight(items):
    choice = valid_input("Would you like to (1) fight or (2) run away? ", ["1", "2"])
    if choice == "1":
        if "sword" in items:
            print_pause("As the fairie moves to attack, you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
            print_pause("But the fairie takes one look at your shiny new toy and runs away!")
            print_pause("You have rid the town of the fairie. You are victorious!")
        else:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the wicked fairie.")
            print_pause("You have been defeated!")
    elif choice == "2":
        print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
        field(items)

def field(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = valid_input("(Please enter 1 or 2.) ", ["1", "2"])
    if choice == "1":
        house(items)
    elif choice == "2":
        cave(items)
        field(items)

def play_game():
    items = []
    intro()
    field(items)

if __name__ == "__main__":
    play_game()