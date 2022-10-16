def find_position(some_maze):
    position = []
    for current_row in range(len(some_maze)):
        for el in some_maze[current_row]:
            if el == 'k':
                position.append(current_row)
                position.append(some_maze[current_row].find('k'))
                return position


def next_free_spot(some_maze):
    free_spots = []
    for current_row in range(len(some_maze)):
        for el in range(len(some_maze[current_row])):
            tmp = []
            if some_maze[current_row][el] == ' ':
                tmp.append(current_row)
                tmp.append(el)
                free_spots.insert(0, tmp)
    return free_spots


def find_path(position, free, some_maze):
    is_blocked = True
    step = 0
    moves = 0

    while step < len(free):
        x1 = free[step][0]
        x2 = free[step][1]
        temp = [x1, x2]
        # moving left
        if temp[0] == position[0] and position[1] - temp[1] == 1:
            position = temp
            moves += 1
            free.pop(step)
            step = 0
        # moving right
        elif temp[0] == position[0] and temp[1] - position[1] == 1:
            position = temp
            moves += 1
            free.pop(step)
            step = 0
        # moving down
        elif temp[0] - position[0] == 1 and position[1] == temp[1]:
            position = temp
            moves += 1
            free.pop(step)
            step = 0
        # moving up
        elif position[0] - temp[0] == 1 and position[1] == temp[1]:
            position = temp
            moves += 1
            free.pop(step)
            step = 0
        else:
            step += 1
    if position[0] == 0 or position[0] == (len(some_maze) - 1) or position[1] == 0 or position[1] == len(some_maze[0]):
        return f'Kate got out in {moves + 1} moves'
    return f'Kate cannot get out'


rows = int(input())
maze = []
number_of_moves = 0
free_space = True
for row in range(rows):
    maze.append(input())
kate_position = find_position(maze)
next_free = next_free_spot(maze)
movement = find_path(kate_position, next_free, maze)
print(movement)
