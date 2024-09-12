# Contributing to Emoji Mood Tracker

## Branching Strategy

- `main`: The main branch contains production-ready code.
- `develop`: The development branch for integrating features.
- `feature/`: Feature branches for new features or enhancements.
- `bugfix/`: Bugfix branches for fixing issues.
- `release/`: Release branches for preparing new production releases.

## Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` A new feature
- `fix:` A bug fix
- `docs:` Documentation only changes
- `style:` Changes that do not affect the meaning of the code (white-space, formatting, etc)
- `refactor:` A code change that neither fixes a bug nor adds a feature
- `perf:` A code change that improves performance
- `test:` Adding missing tests or correcting existing tests
- `chore:` Changes to the build process or auxiliary tools and libraries

Example: `feat: add mood trend visualization`

## Pull Requests

1. Create a new branch from `develop` for your feature or bugfix.
2. Make your changes and commit them using the commit message conventions.
3. Push your branch and create a Pull Request against the `develop` branch.
4. Fill out the PR template with details about your changes.
5. Request a review from at least one team member.
6. Once approved, merge your PR using the "Squash and merge" option.

## Code Style

- Follow PEP 8 guidelines for Python code.
- Use 4 spaces for indentation.
- Maximum line length is 120 characters.
- Use meaningful variable and function names.

## Testing

- Write unit tests for new features and bug fixes.
- Ensure all tests pass before submitting a PR.
- Aim for at least 80% code coverage.

## Documentation

- Update README.md with any new features or changed functionality.
- Keep inline code comments up-to-date and meaningful.
- Document new functions and classes using docstrings.

## Review Process

- Reviewers should check for code quality, test coverage, and adherence to project conventions.
- Address all comments and suggestions from reviewers.
- Resolve any merge conflicts before requesting a re-review.

Remember, these conventions are meant to improve our workflow and code quality. Thank you for your contributions!