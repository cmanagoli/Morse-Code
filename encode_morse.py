# Author: Chinmai Managoli

import sys as sys

# Morse code dictionary
char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}


def encode_morse(message):
    message = str(message)
    message = message.upper()
    try:
        for x in message:
            print(char_to_dots[x], end=" ") 
        print("\nMessage was encoded successfully")
    # Exceptions
    except KeyError:
        print("\n" + x + " is an invalid character")
    except:
        print("\nThere was an error")


if __name__ == "__main__":
    print("This program will encode a string into Morse. Unicode characters are not supported.")
    string = input("Enter the message to be encoded: ")
    encode_morse(string)
    sys.exit()

