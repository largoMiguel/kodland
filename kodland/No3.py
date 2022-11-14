def valid_number(number):
    if 1 <= number <= 8:
        return False
    print("Posicion invalida")
    return True


column_a = int(input())  # columna A
while valid_number(column_a):
    column_a = int(input())  # columna A

row_a = int(input())  # fila A
while valid_number(row_a):
    row_a = int(input())  # fila A

column_b = int(input())  # columna B
while valid_number(column_b):
    column_b = int(input())  # columna B

row_b = int(input())  # fila B
while valid_number(row_b):
    row_b = int(input())  # fila B


def valid_movement():
    # Vertical
    if row_a == row_b:
        print("SI")
        return
    # Horizonatal
    if column_a == column_b:
        print("SI")
        return

        # Diagonal
    if (column_a + row_a) == (column_b + row_b):
        print("SI")
        return

        # Diagonal inversa
    if (column_a - column_b) == (row_a - row_b):
        print("SI")
        return

    print("NO")


valid_movement()
