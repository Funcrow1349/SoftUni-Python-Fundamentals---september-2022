def dungeon_crawler(some_dungeon):
    health = 100
    bitcoins = 0
    best_room = 1
    dead = False
    for room in dungeons_rooms:
        current_room = room.split()
        command = current_room[0]
        number = int(current_room[1])
        if command == "potion":
            health += number
            if health >= 100:
                number -= health - 100
                health = 100
            print(f"You healed for {number} hp.")
            print(f"Current health: {health} hp.")
        elif command == "chest":
            bitcoins += number
            print(f"You found {number} bitcoins.")
        else:
            health -= number
            if health > 0:
                print(f"You slayed {command}.")
            else:
                print(f"You died! Killed by {command}.")
                dead = True
                break
        best_room += 1
    if not dead:
        print("You've made it!")
        print(f"Bitcoins: {bitcoins}")
        print(f"Health: {health}")
    else:
        print(f"Best room: {best_room}")


dungeons_rooms = input().split("|")
dungeon_crawler(dungeons_rooms)

