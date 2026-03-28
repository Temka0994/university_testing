# Contributing to ToDo Application

Thank you for considering contributing! This document outlines the guidelines for reporting issues, suggesting improvements, and submitting code changes.

## Reporting Bugs / Requesting Features

Use the [GitHub Issues](https://github.com/Temka0994/university_testing/issues) page to report bugs or propose new features.

- **Bugs**: Provide a clear description, steps to reproduce, expected vs. actual behaviour, and any error messages.
- **Features**: Explain the use case and how it would benefit the app.

## How to Contribute Code

1. **Fork** the repository to your own GitHub account.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/your-username/university_testing.git
   cd university_testing
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes**, following the code style (see below).
5. **Add or update tests** if necessary.
6. **Run the tests** to ensure everything passes:
   ```bash
   python -m unittest discover tests
   ```
7. **Commit your changes** with a clear commit message (see guidelines below).
8. **Push** your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
9. Open a **pull request** against the `main` branch of the original repository.

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code.
- Use meaningful variable and function names.
- Keep functions small and focused.
- Add docstrings for public functions and classes.

## Testing

- New features should include unit tests.
- Existing tests must continue to pass.
- Place tests in the `tests/` directory with names starting with `test_`.

## Commit Message Guidelines

- Use the present tense (“Add feature” not “Added feature”).
- Use the imperative mood (“Fix bug” not “Fixes bug”).
- Keep the first line under 50 characters.
- Optionally add a more detailed description after a blank line.

Example:
```
Add completion status to tasks

- Add 'completed' field to task model
- Update list view to show completed tasks differently
- Add unit tests for new functionality
```

## Pull Request Checklist

- [ ] Code follows the style guide.
- [ ] Tests have been added/updated and pass.
- [ ] Commit messages are clear and follow the guidelines.
- [ ] The PR description explains what has been changed and why.

## Questions?

If you have any questions, feel free to open an issue or reach out to the maintainer.

Thank you for contributing!

---

Both files assume the repository has a `tests/` folder and that `main.py` is the entry point. If your actual code differs (e.g., you have a GUI or a different structure), you can easily adapt the text. The screenshot placeholders should be replaced with actual images (e.g., in a `docs/` folder).
