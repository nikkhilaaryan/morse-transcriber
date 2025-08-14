# tests/test_interfaces/test_cli.py
import pytest
from unittest import mock
from src.interfaces.cli import main, run_interactive_menu, copy_to_clipboard
from src.converters.alpha_morse import alpha_to_morse
from src.converters.morse_alpha import morse_to_alpha


# Test copy_to_clipboard
# -----------------------------
def test_copy_to_clipboard(monkeypatch):
    copied = {}
    def fake_copy(text):
        copied['text'] = text
    monkeypatch.setattr("pyperclip.copy", fake_copy)
    copy_to_clipboard("HELLO")
    assert copied['text'] == "HELLO"


# Test main CLI with --text argument
# -----------------------------
@mock.patch("builtins.print")
@mock.patch("src.interfaces.cli.copy_to_clipboard")
def test_text_argument(mock_copy, mock_print, monkeypatch):
    monkeypatch.setattr("sys.argv", ["morse-transcriber", "--text", "SOS"])
    main()
    expected = alpha_to_morse("SOS")
    mock_print.assert_any_call(f"\033[92m{expected}\033[0m")
    mock_copy.assert_called_once_with(expected)


# Test main CLI with --morse argument
# -----------------------------
@mock.patch("builtins.print")
@mock.patch("src.interfaces.cli.copy_to_clipboard")
def test_morse_argument(mock_copy, mock_print, monkeypatch):
    monkeypatch.setattr("sys.argv", ["morse-transcriber", "--morse", "... --- ..."])
    main()
    expected = morse_to_alpha("... --- ...")
    mock_print.assert_any_call(f"\033[92m{expected}\033[0m")
    mock_copy.assert_called_once_with(expected)


# Test interactive menu exit (choice 3 exits)
# -----------------------------
@mock.patch("builtins.input", side_effect=["3"])
@mock.patch("builtins.print")
def test_interactive_menu_exit(mock_print, mock_input):
    run_interactive_menu()
    mock_print.assert_any_call("\033[96m" + "morse-transcriber terminated." + "\033[0m")


# Test interactive menu invalid choice
# -----------------------------
@mock.patch("builtins.input", side_effect=["invalid", "3"])
@mock.patch("builtins.print")
def test_interactive_menu_invalid_choice(mock_print, mock_input):
    run_interactive_menu()
    mock_print.assert_any_call("\033[91mInvalid choice. Please try again.\033[0m")
