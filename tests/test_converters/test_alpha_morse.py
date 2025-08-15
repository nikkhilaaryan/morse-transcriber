# tests/test_converters/test_alpha_morse.py
import pytest
from morse_transcriber.converters.alpha_morse import alpha_to_morse
from morse_transcriber.mappings.morse_map import MORSE_MAP

def test_single_word():
    # Simple word
    assert alpha_to_morse("SOS") == "... --- ..."

def test_multiple_words():
    # Sentence with spaces
    text = "HELLO WORLD"
    expected = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    assert alpha_to_morse(text) == expected

def test_numbers_and_punctuation():
    # Including numbers and supported punctuation
    text = "TEST 123"
    expected = "- . ... - / .---- ..--- ...--"
    assert alpha_to_morse(text) == expected

def test_lowercase_input():
    # Ensure lowercase letters work
    assert alpha_to_morse("sos") == "... --- ..."

def test_unsupported_character():
    # Characters not in MORSE_MAP should raise ValueError
    with pytest.raises(ValueError):
        alpha_to_morse("HELLO#WORLD")  # '#' is likely unsupported
