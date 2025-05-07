#Exercise 3: From English to Morse
#Write a function that converts English text to Morse code and another one that does the opposite.
#Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

def english_to_morse(text):
    # Créer une chaîne vide qui va contenir le texte en morse
    morse_text = ''
    
    # Boucler sur chaque caractère du texte d'entrée
    for char in text:
        # Si le caractère est une lettre ou un chiffre, on l'ajoute au texte morse
        if char.upper() in MORSE_CODE_DICT:
            morse_text += MORSE_CODE_DICT[char.upper()] + ' '
        # Si ce n'est pas une lettre ou un chiffre (comme un espace), on l'ajoute tel quel
        else:
            morse_text += ' '
    # Retourner le texte morse
    return morse_text.strip()

def morse_to_english(code, original_text=None):
    # Dictionnaire inversé pour décoder le morse
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    
    # Décodage du code Morse en texte brut
    decoded_text = ''.join(reverse_dict.get(c, '') for c in code.split())

    if original_text:
        # Respecter la casse originale
        result = []
        for i, char in enumerate(decoded_text):
            if original_text[i].isupper():  # Comparer la casse du texte original
                result.append(char.upper())
            else:
                result.append(char.lower())
        return ''.join(result)
    else:
        return decoded_text

# Exemple d’utilisation :
texte_long = "The quick brown fox jumps over the lazy dog"
code_morse_long = english_to_morse(texte_long)
print("Texte vers Morse:", code_morse_long)

texte_decode_long = morse_to_english(code_morse_long, texte_long)
print("Morse vers texte:", texte_decode_long)