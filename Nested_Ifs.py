# Nested Decisions

#Task 1 Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
       print("You found a boat!")
elif place == "cave":
    hunt = input("light a torch or proceed in the dark?")
    if hunt == "light a torch":
        print("There's a tiger Ruuuun!")
    elif hunt == "proceed in the dark":
        print("It's too dark to keep going")

# # Task 3 Default Path

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass    
elif place == "cave":
    hunt = input("light a torch or proceed in the dark?")
    if hunt == "light a torch":
        print("There's a tiger Ruuuun!")
    elif hunt == "proceed in the dark":
        print("It's too dark to keep going")
    else:
        pass
        
# Quick Decisions

# Task 1 Code Correction

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Task 2 Catering Choices

user = input("Would you be interested in vegetarian food?")
print("Veggie Delight Caterers") if user == "yes" else print("Gourmet Meals Caterers")