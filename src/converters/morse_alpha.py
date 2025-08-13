"""
Module: morse_alpha.py
Provided functionality: convert Morse code to plain text using TEXT_MAP from src/mappings/morse_map module.
Conversion Rules:
- Input: A string containing Morse code, where each character is separated by spaces and words are separated by slashes.
- Output: A string where each Morse code character is replaced by its plain text equivalent, with
  words separated by spaces.

  Unsupported Characters:
  - According to project policy, Morse code sequences not defined in TEXT_MAP will raise a ValueError.
  """

import re
from src.mappings.morse_map import TEXT_MAP

def morse_to_alpha(morse_code: str) -> str:
    """
    Converts a Morse code string to plain text.
    
    Args:
        morse_code (str): The input Morse code string to convert.
        
    Returns:
        str: The plain text representation of the input Morse code.
        
    Raises:
        ValueError: If the input contains Morse code sequences not defined in TEXT_MAP.
    """
    # Split words on slashes with optional spaces
    words = re.split(r'\s*/\s*', morse_code.strip())
    decoded_words = []

    for morse_word in words:
        letters = morse_word.split(' ')
        decoded_letters = []
        for morse_char in filter(None, letters):  # Skip empty splits
            if morse_char in TEXT_MAP:
                decoded_letters.append(TEXT_MAP[morse_char])
            else:
                raise ValueError(f"Unsupported Morse code sequence: '{morse_char}'")
        decoded_words.append(''.join(decoded_letters))

    return ' '.join(decoded_words)
