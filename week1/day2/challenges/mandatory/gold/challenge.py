matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

message = ''
in_symbol_sequence = False
first_letter_found = False  

for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        char = matrix[row][col]
        if char.isalpha():
            if in_symbol_sequence and first_letter_found:
                message += ' '
            message += char
            in_symbol_sequence = False
            first_letter_found = True
        else:
            in_symbol_sequence = True

print(message)
