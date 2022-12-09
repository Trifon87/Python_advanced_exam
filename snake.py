directions = {
    "up": [-1, 0],
    "right": [0, 1],
    "down": [1, 0],
    "left": [0, -1]
}

n = int(input())
food_counter = 0
matrix = []
snake = []

for i in range(n):
    line = list(input())
    if "S" in line:
        snake = [i, line.index("S")]
    matrix.append(line)

while True:

    command = input()
    new_row = snake[0] + directions[command][0]
    new_col = snake[1] + directions[command][1]
    new_pos = [new_row, new_col]

    if 0 <= new_row < n and 0 <= new_col < n:
        if matrix[new_row][new_col] == "-":
            matrix[snake[0]][snake[1]] = '.'
            matrix[new_row][new_col] = 'S'
            snake = new_row, new_col
        if matrix[new_row][new_col] == "*":
            food_counter += 1
            matrix[snake[0]][snake[1]] = '.'
            matrix[new_row][new_col] = 'S'
            snake = new_row, new_col
        if matrix[new_row][new_col] == "B":
            matrix[snake[0]][snake[1]] = '.'
            matrix[new_row][new_col] = '.'
            for row in range(len(matrix)):
                for col in range(len(matrix)):
                    if matrix[row][col] == "B":
                        snake = row, col
                        matrix[row][col] = 'S'
                        snake = row, col
        if food_counter == 10:
            print(f"You won! You fed the snake.")
            print(f"Food eaten: {food_counter}")
            [print("".join(row)) for row in matrix]
            break
    else:
        matrix[snake[0]][snake[1]] = '.'
        print("Game over!")
        print(f"Food eaten: {food_counter}")
        [print("".join(row)) for row in matrix]
        break