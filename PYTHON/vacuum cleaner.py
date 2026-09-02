rooms = {'A':'Dirty','B':'Dirty'}

location = 'A'

while True:

    print("Location:", location)
    print("Room Status:", rooms)

    if rooms[location] == "Dirty":
        print("Cleaning", location)
        rooms[location] = "Clean"

    if location == 'A':
        location = 'B'
    else:
        location = 'A'

    if rooms['A']=="Clean" and rooms['B']=="Clean":
        break

print("\nAll Rooms Clean")
