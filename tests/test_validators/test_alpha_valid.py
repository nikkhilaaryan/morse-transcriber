# tests/test_validators/test_alpha_valid.py
import pytest
from src.validators.alpha_valid import is_valid_alpha
from src.mappings.morse_map import MORSE_MAP


# Valid input tests
# ---------------------------------------
def test_valid_letters():
    assert is_valid_alpha("HELLO") is True
    assert is_valid_alpha("WORLD") is True

def test_valid_numbers():
    assert is_valid_alpha("12345") is True
    assert is_valid_alpha("9081726354") is True

def test_valid_punctuation():
    punctuation = ''.join([p for p in MORSE_MAP if p not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "])
    assert is_valid_alpha(punctuation) is True

def test_valid_mixed_text():
    assert is_valid_alpha("HELLO WORLD 123!") is True
    assert is_valid_alpha("SOS!") is True

def test_valid_with_spaces_only():
    assert is_valid_alpha(" ") is True
    assert is_valid_alpha("A B C") is True

# Invalid input tests
# -----------------------------------------
def test_invalid_lowercase():
    # Lowercase letters are valid because is_valid_alpha converts to upper
    assert is_valid_alpha("hello") is True

def test_invalid_character_raises():
    with pytest.raises(ValueError):
        is_valid_alpha("HELLO$")  # $ not in Morse map

def test_invalid_multiple_characters():
    invalid_text = "HELLO<>WORLD"  # < and > are not in Morse map
    with pytest.raises(ValueError):
        is_valid_alpha(invalid_text)

def test_empty_string():
    # Empty string is arguably valid
    assert is_valid_alpha("") is True
