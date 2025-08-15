# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2025-08-15
### Added
- Full MkDocs documentation with Material dark theme.
- Dedicated sections for:
  - Installation
  - Commands
  - Contributing
  - Changelog
- CLI help command: `morse-transcriber --help`.
- CLI version command: `morse-transcriber --version`.
- Clipboard support with `pyperclip` dependency.
- Interactive menu mode and one-shot argument mode.
- Strict validation for text and Morse code inputs.

### Changed
- Project restructured into `src/` layout for packaging best practices.
- Updated README with badges, detailed usage, and contribution guidelines.

### Removed
- Old incomplete documentation files from previous releases.

---

## [0.1.1] - 2025-08-14
### Fixed
- Minor bug fixes to conversion logic.
- Adjusted CLI argument parsing.

### Known Issues
- Clipboard functionality not working on some Linux distributions.
- Documentation incomplete.

---

## [0.1.0] - 2025-08-14
### Added
- Initial public release with basic:
  - Text → Morse conversion
  - Morse → Text conversion
- Basic CLI argument handling.

### Known Issues
- Missing input validation for unsupported characters.
- No automated testing implemented.

---

## [Unreleased]
- Features and fixes planned for the next update.
