# tests/test_converters/test_morse_alpha.py
import pytest
from src.converters.morse_alpha import morse_to_alpha
from src.mappings.morse_map import TEXT_MAP

def test_single_word():
    # Simple Morse word
    assert morse_to_alpha("... --- ...") == "SOS"

def test_multiple_words():
    # Sentence with slash-separated words
    morse = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    expected = "HELLO WORLD"
    assert morse_to_alpha(morse) == expected

def test_numbers_and_punctuation():
    # Including numbers and supported punctuation
    morse = "- . ... - / .---- ..--- ...--"
    expected = "TEST 123"
    assert morse_to_alpha(morse) == expected

def test_extra_spaces():
    # Ensure extra spaces do not break decoding
    morse = ".... . .-.. .-.. ---   /   .-- --- .-. .-.. -.."
    expected = "HELLO WORLD"
    assert morse_to_alpha(morse) == expected

def test_unsupported_sequence():
    # Characters not in TEXT_MAP should raise ValueError
    unsupported_morse = "... --- ... / ....--"  # '....--' likely unsupported
    with pytest.raises(ValueError):
        morse_to_alpha(unsupported_morse)
