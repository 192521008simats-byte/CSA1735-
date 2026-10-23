room = {"A": 1, "B": 1}
position = "A"

while 0 in room.values():
    if room[position] == 1:
        print(position, "is Dirty")
        room[position] = 0
        print(position, "Cleaned")

    position = "B" if position == "A" else "A"

print("All rooms are clean")
