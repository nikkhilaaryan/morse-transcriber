# Command Reference

This section describes how to use **morse-transcriber** from the command line.  
The tool supports both **interactive mode** (menu-driven) and **one-shot mode** (direct commands).

---

## 1. Interactive Mode

Interactive mode is useful when performing multiple conversions in a single session.

**Command:**
```bash
morse-transcriber
```
Example session"
```
morse-transcriber CLI
1. text to morse
2. morse to text
3. morse-transcriber terminated.
enter choice (1/2/3): 1
enter text: SOS
morse-Code: ... --- ...
```
**Notes**:
* The program will keep running until you choose Exit.
* Input is validated before conversion.
* Output is automatically copied to the clipboard (if pyperclip is installed).


## 2. One-Shot Argument Mode

Convert Text to Morse Code
Command:
```bash
morse-transcriber --text "SOS"
```
```
Expected Output: ... --- ...
```
Convert Morse Code to Text
Command:
```bash
morse-transcriber --morse "... --- ..."
```
```
Expected Output: SOS
```
## Important Commands
1. Show Help
Displays all available options and usage instructions.
    ```bash
    morse-transcriber --help
    ```

2. Show Version
Displays the currently installed version of morse-transcriber.
    ```bash
    morse-transcriber --version
    ```
## Tips

- Wrap your input in quotes to avoid shell parsing issues.
- Use interactive mode for quick multiple conversions.
- Use one-shot mode in scripts or automation tasks.



