Maze = [["#","#","#","#","#","#","#"],
        ["#"," "," ","#"," ","E","#"],
        ["#","#"," ","#"," ","#","#"],
        ["#"," "," "," "," "," ","#"],
        ["#","S","#","#","#","#","#"]]

def print_maze():
    for row in Maze:
        for cell in row:
            print(cell, end="")
        print()

print_maze()

GFlag = True
while GFlag:
    print("Use U, L, D, R to move. Your goal is to reach the Exit (E)! ")
    found = False  
    for i in range(len(Maze)):
        for j in range(len(Maze[0])):
            if Maze[i][j] == "S":
                Current_position = [i, j]
                print(f"Current Position: {Current_position}")
                nextMove = input("Enter your move (U/L/D/R): ").upper()
                new_position = Current_position.copy()
                if nextMove == "U":
                    new_position[0] -= 1
                elif nextMove == "L":
                    new_position[1] -= 1
                elif nextMove == "D":
                    new_position[0] += 1
                elif nextMove == "R":
                    new_position[1] += 1
                else:
                    print("Invalid move! Please enter U, L, D, or R.")
                    found = True
                    break 
                if (0 <= new_position[0] < len(Maze)) and (0 <= new_position[1] < len(Maze[0])):
                    if Maze[new_position[0]][new_position[1]] == "#":
                        print("You hit a wall! Try another direction.")
                    elif Maze[new_position[0]][new_position[1]] == "E":
                        print("YOU WIN! You reached the Exit")
                        GFlag = False
                        break
                    else:
                        Maze[i][j] = " " 
                        Maze[new_position[0]][new_position[1]] = "S"
                else:
                    print("You can't move outside the maze!")

                found = True
                break
        if found:
            break
    print()
    print_maze()
