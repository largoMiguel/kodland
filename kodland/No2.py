number_lines = int(input("Ingresa el numero de lineas del poema: "))
poem = []
poem_print = []
vowels = ["A", "E", "I", "O", "U"]

number_vowels = 0
number_consonants = 0

for i in range(number_lines):
    message_input = "Ingrese la linea {} del poema: "
    input_line = input(message_input.format(i + 1))

    poem.append(input_line.strip().replace(" ", ""))
    poem_print.append(input_line)

for line in poem:
    for character in line:
        if character.upper() in vowels:
            number_vowels = number_vowels + 1
        if character.upper() not in vowels:
            number_consonants = number_consonants + 1

for line in poem_print:
    print(line)

message_vowels = "Numero de vocales: {}"
message_consonants = "Numero de consonantes: {}"
print(message_vowels.format(number_vowels))
print(message_consonants.format(number_consonants))