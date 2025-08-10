"""Morse code mapping for morse-transcriber."""

"""Constants for Morse code symbols."""
MORSE_SYMBOLS = ['.', '-', '/']

"""Morse code mapping for Latin alphabet and digits."""
ALPHA_MAP = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..' }

NUMERIC_MAP = {
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.' }

PUNCTUATION_MAP = {
        ',': '--..--',
        '.': '.-.-.-',
        '?': '..--..',
        '!': '-.-.--',
        ':': '---...',
        ';': '-.-.-.',
        "'": '.----.',
        '-': '-....-',
        '_': '..--.-',
        '(': '-.--.',
        ')': '-.--.-',
        '"': '.-..-.',
        '=': '-...-',
        '+': '.-.-.',
        '@': '.--.-.' }

SPACE_MAP = {
        ' ': '/' ,  # Space is represented by a slash in Morse code
        '\n': '/'  # Newline is also represented by a slash
        }

"""Combined mapping for all characters."""
MORSE_MAP = {**ALPHA_MAP, **NUMERIC_MAP, **PUNCTUATION_MAP, **SPACE_MAP}


"""Reverse mapping for Morse code to characters."""
TEXT_MAP = {}


"""function to create reverse mapping from Morse code to characters."""
def _build_inverse_map(forward_map):
    """Builds a reverse mapping from Morse code to characters."""
    inverse_map = {}
    for char, morse in forward_map.items():
        if morse not in inverse_map:
            inverse_map[morse] = char
        else:
            # Handle cases where multiple characters map to the same Morse code
            inverse_map[morse] += f'/{char}'
    return inverse_map

# Build the reverse mapping
TEXT_MAP = _build_inverse_map(MORSE_MAP)