"""
Main CLI entry point for morse-transcriber.

Usage (interactive menu):
    morse-transcriber

Usage (one-shot conversion):
    morse-transcriber --text "HELLO WORLD"
    morse-transcriber --morse ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

Features:
- Convert plain text to Morse code.
- Convert Morse code to plain text.
- Validates input before conversion.
- Displays helpful error messages for invalid inputs.
"""

import argparse
import pyperclip
from morse_transcriber.validators.alpha_valid import is_valid_alpha
from morse_transcriber.validators.morse_valid import is_valid_morse
from morse_transcriber.converters.alpha_morse import alpha_to_morse
from morse_transcriber.converters.morse_alpha import morse_to_alpha

# ANSI colors
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"


def copy_to_clipboard(text: str):
    """copy given text to clipboard and notify the user."""
    try:
        pyperclip.copy(text)
        print(f"{CYAN}[copied to clipboard]{RESET}")
    except pyperclip.PyperclipException:
        print(f"{RED}[clipboard not available]{RESET}")


def run_interactive_menu():
    """Run the interactive CLI menu for conversions."""
    while True:
        print(f"\n{CYAN}morse-transcriber CLI{RESET}")
        print("1. text to morse")
        print("2. morse to text")
        print("3. terminate")

        choice = input(YELLOW + "enter choice (1/2/3): " + RESET).strip()

        if choice == "1":
            text = input(YELLOW + "enter text: " + RESET).strip()
            try:
                if not is_valid_alpha(text):
                    raise ValueError(
                        "Invalid text input. Only letters, numbers, and basic punctuation are allowed."
                    )
                result = alpha_to_morse(text)
                print(f"{GREEN}morse-code: {result}{RESET}")
                copy_to_clipboard(result)
            except ValueError as e:
                print(f"{RED}error: {e}{RESET}")

        elif choice == "2":
            morse = input(YELLOW + "enter morse-code: " + RESET).strip()
            try:
                if not is_valid_morse(morse):
                    raise ValueError(
                        "Invalid Morse code input. Only dots, dashes, spaces, and slashes are allowed."
                    )
                result = morse_to_alpha(morse)
                print(f"{GREEN}text: {result}{RESET}")
                copy_to_clipboard(result)
            except ValueError as e:
                print(f"{RED}error: {e}{RESET}")

        elif choice == "3":
            print(f"{CYAN}morse-transcriber terminated.{RESET}")
            break

        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")


def main():
    """Main entry point: parses arguments or runs interactive menu."""
    parser = argparse.ArgumentParser(description="Morse Code Converter CLI")
    parser.add_argument("--text", type=str, help="Convert text to Morse code")
    parser.add_argument("--morse", type=str, help="Convert Morse code to text")
    args = parser.parse_args()

    if args.text:
        try:
            if not is_valid_alpha(args.text):
                raise ValueError(
                    "Invalid text input. Only letters, numbers, and basic punctuation are allowed."
                )
            result = alpha_to_morse(args.text)
            print(f"{GREEN}{result}{RESET}")
            copy_to_clipboard(result)
        except ValueError as e:
            print(f"{RED}Error: {e}{RESET}")
        return

    if args.morse:
        try:
            if not is_valid_morse(args.morse):
                raise ValueError(
                    "Invalid Morse code input. Only dots, dashes, spaces, and slashes are allowed."
                )
            result = morse_to_alpha(args.morse)
            print(f"{GREEN}{result}{RESET}")
            copy_to_clipboard(result)
        except ValueError as e:
            print(f"{RED}Error: {e}{RESET}")
        return

    # If no arguments provided, fall back to interactive menu
    run_interactive_menu()


if __name__ == "__main__":
    main()
