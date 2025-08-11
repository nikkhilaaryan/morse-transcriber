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
    
    words = morse_code.strip().split(' / ')  # Split words by slashes
    decoded_words = []

    for morse_word in words:
        letters = morse_word.split(' ')  # Split letters by spaces
        decoded_letters = []
        for code in letters:
            if code in TEXT_MAP:
                decoded_letters.append(TEXT_MAP[code])
            else:
                raise ValueError(f"Unsupported Morse code sequence: '{code}'")
        decoded_words.append(''.join(decoded_letters))
    return ' '.join(decoded_words)  # Join words with spaces
