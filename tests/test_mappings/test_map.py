# tests/test_mappings/test_map.py
import pytest
from src.mappings.morse_map import MORSE_MAP, TEXT_MAP

def test_basic_letter_mapping():
    # Test a few letters
    assert MORSE_MAP['A'] == '.-'
    assert MORSE_MAP['Z'] == '--..'
    # Reverse mapping
    assert TEXT_MAP['.-'] == 'A'
    assert TEXT_MAP['--..'] == 'Z'

def test_numeric_mapping():
    # Numbers
    assert MORSE_MAP['0'] == '-----'
    assert MORSE_MAP['5'] == '.....'
    # Reverse mapping
    assert TEXT_MAP['-----'] == '0'
    assert TEXT_MAP['.....'] == '5'

def test_punctuation_mapping():
    # Punctuation
    assert MORSE_MAP[','] == '--..--'
    assert MORSE_MAP['?'] == '..--..'
    # Reverse mapping
    assert TEXT_MAP['--..--'] == ','
    assert TEXT_MAP['..--..'] == '?'

def test_space_mapping():
    # Spaces and newline
    assert MORSE_MAP[' '] == '/'
    assert MORSE_MAP['\n'] == '/'
    # Reverse mapping contains both ' ' and '\n'
    assert ' ' in TEXT_MAP['/']
    assert '\n' in TEXT_MAP['/']


def test_all_morse_reverse_exists():
    # Every Morse code in MORSE_MAP should exist in TEXT_MAP
    for char, morse in MORSE_MAP.items():
        assert morse in TEXT_MAP

def test_conflict_handling():
    # If multiple characters map to same Morse, TEXT_MAP should contain '/'
    # In your current mapping, ' ' and '\n' both map to '/', so TEXT_MAP['/'] should include both
    assert '/' in TEXT_MAP
    assert ' ' in TEXT_MAP['/'] or '\n' in TEXT_MAP['/']
