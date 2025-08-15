# tests/test_validators/test_morse_valid.py
import pytest
from morse_transcriber.validators.morse_valid import is_valid_morse
from morse_transcriber.mappings.morse_map import TEXT_MAP


# Valid Morse code tests
# -----------------------------
def test_valid_single_letter():
    assert is_valid_morse(".") is True      # E
    assert is_valid_morse("-") is True      # T

def test_valid_word():
    # SOS = ... --- ...
    assert is_valid_morse("... --- ...") is True

def test_valid_multiple_words():
    # HELLO WORLD = .... . .-.. .-.. --- / .-- --- .-. .-.. -..
    morse_text = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    assert is_valid_morse(morse_text) is True

def test_valid_with_extra_spaces():
    morse_text = ".... .  .-.. .-.. --- / .-- --- .-. .-.. -.."
    assert is_valid_morse(morse_text) is True  # Extra space between letters is ignored

# Invalid Morse code tests
# -----------------------------
def test_invalid_character_raises():
    with pytest.raises(ValueError):
        is_valid_morse("... --- ... $")  # $ is invalid

def test_invalid_sequence_raises():
    with pytest.raises(ValueError):
        is_valid_morse("... --- ... .....-")  # .....- is not in TEXT_MAP

def test_invalid_word_separator():
    # Missing spaces around slash should still be fine if sequences exist
    morse_text = "...---.../...---..."
    with pytest.raises(ValueError):
        is_valid_morse(morse_text)


# Edge cases
# -----------------------------
def test_empty_string_is_valid():
    assert is_valid_morse("") is True

def test_only_slash():
    assert is_valid_morse("/") is True

def test_only_spaces():
    assert is_valid_morse("   ") is True
