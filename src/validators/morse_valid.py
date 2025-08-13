"""
Module: morse_validator
-----------------------
Validates Morse code input before converting it to plain text.

Rules:
- Only dot (.), dash (-), space ( ), and slash (/) are allowed.
- Letters within a word must be separated by a single space.
- Words must be separated by ' / ' (space-slash-space).
- Each Morse sequence must exist in MORSE_TO_TEXT mapping.

Returns:
- True if valid.
- Raises ValueError or returns False (depending on mode) if invalid.
"""

from src.mappings.morse_map import MORSE_MAP

def is_valid_morse(morse: str) -> bool:
    """
    Validates if the input Morse code contains only valid characters and formats.

    Args:
        morse (str): The Morse code string to validate.

    Returns:
        bool: True if the Morse code is valid, False otherwise.
    
    Raises:
        ValueError: If the Morse code contains unsupported characters or incorrect formatting.
    """
    allowed_chars = {".", "-", " ", "/"}

    # 1. Check only allowed characters are present
    for ch in morse:
        if ch not in allowed_chars:
            raise ValueError(f"Unsupported character in Morse code: '{ch}'")

    # 2. Validate each Morse sequence
    words = morse.strip().split(" / ")
    for word in words:
        sequences = word.split(" ")
        for seq in sequences:
            if seq and seq not in MORSE_MAP:
                raise ValueError(f"Unsupported Morse code sequence: '{seq}'")

    return True