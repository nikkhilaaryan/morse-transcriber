"""
Module: text_validator
----------------------
Validates plain text input for Morse code conversion.

Rules:
- Only uppercase A–Z, digits 0–9, and supported punctuation are allowed.
- Spaces between words are allowed.
- Any unsupported character will cause a validation failure.

Returns:
- True if valid.
- Raises ValueError or returns False (depending on usage) if invalid.
"""
from src.converters.alpha_morse import alpha_to_morse
from src.mappings.morse_map import MORSE_MAP


def is_valid_alpha(text: str) -> bool:
    """
    Validates if the input text contains only valid characters for Morse code conversion.

    Args:
        text (str): The input text to validate.

    Returns:
        bool: True if the text is valid, False otherwise.
    
    Raises:
        ValueError: If the text contains unsupported characters.
    """
    for char in text.upper():
        if char == " ":  # spaces are fine
            continue
        if char not in MORSE_MAP:
            raise ValueError(f"Unsupported character in text: '{char}'")
    return True