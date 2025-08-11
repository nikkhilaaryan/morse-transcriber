"""
Module: alpha_morse.py
Provided functionality: convert plain text to Morse code using MORSE_MAP from src/mappings/morse_map.py.
Conversion Rules: 
- Input: A string containing alphanumeric characters, punctuation, and spaces.
- Output: A string where each character is replaced by its Morse code equivalent, with words separated by slashes.

Unsupported Characters:
- According to project poilcy, characters not defined in MORSE_MAP will raise a ValueError.
"""

from src.mappings.morse_map import MORSE_MAP

def alpha_to_morse(text: str) -> str:
    """
    Converts a plain test string to Morse code.
    Args:
        text (str): The input string to convert.
        
    Returns:
        str: The Morse code representation of the input string.
        
    Raises:
        ValueError: If the input contains characters not defined in MORSE_MAP.
    """

    text = text.uppper()  # Convert to uppercase for consistency
    morse_words = []
    for words in text.split(" "):
        morse_chars = []
        for char in words:
            # Check if the character is in the Morse map
            if char in MORSE_MAP:
                morse_chars.append(MORSE_MAP[char])
            else:
                raise ValueError(f"Character '{char}' not defined in Morse code mapping.")
        
    return ' / '.join(morse_words)  # Join Morse code words with spaces



