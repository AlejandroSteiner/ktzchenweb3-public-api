# Contributing to KtzchenWeb3

Thank you for your interest in contributing to KtzchenWeb3! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Community](#community)

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct:

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive feedback
- Respect differing viewpoints and experiences

## Getting Started

### Prerequisites

- Git
- Node.js 18+ (for JavaScript SDK)
- Python 3.9+ (for Python SDK)
- A KtzchenWeb3 API key for testing

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/YOUR_USERNAME/ktzchenweb3-public-api.git
cd ktzchenweb3-public-api
```

3. Add the upstream remote:

```bash
git remote add upstream https://github.com/ktzchenweb3/ktzchenweb3-public-api.git
```

## How to Contribute

### Reporting Bugs

Before creating a bug report:

1. Check existing issues to avoid duplicates
2. Collect relevant information:
   - API endpoint affected
   - Expected vs actual behavior
   - Request/response examples
   - Error messages

Create a new issue with the **Bug Report** template.

### Suggesting Features

We welcome feature suggestions! Before submitting:

1. Check if the feature has already been requested
2. Consider if it aligns with the project's goals
3. Think about the implementation approach

Create a new issue with the **Feature Request** template.

### Documentation Improvements

Documentation improvements are always welcome:

- Fix typos or unclear explanations
- Add examples
- Improve API documentation
- Translate documentation

### Code Contributions

We accept contributions for:

- SDK improvements
- New examples
- Bug fixes
- Performance improvements
- Test coverage

## Development Setup

### JavaScript SDK

```bash
cd sdk
npm install
npm run build
npm test
```

### Python SDK

```bash
cd sdk
pip install -e ".[dev]"
pytest
```

### Running Examples

```bash
# Set your API key
export KTZCHENWEB3_API_KEY="your_api_key"

# Run JavaScript examples
cd examples/javascript
node basic-usage.js

# Run Python examples
cd examples/python
python basic_usage.py
```

## Pull Request Process

1. **Create a branch** from `main`:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

2. **Make your changes** following our style guidelines

3. **Write/update tests** for your changes

4. **Update documentation** if needed

5. **Commit your changes** with clear messages:

```bash
git commit -m "feat: add support for new network"
# or
git commit -m "fix: handle timeout errors correctly"
```

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Test changes
- `chore:` - Maintenance tasks

6. **Push to your fork**:

```bash
git push origin feature/your-feature-name
```

7. **Open a Pull Request** against the `main` branch

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] Documentation updated if needed
- [ ] Commit messages follow conventions
- [ ] PR description explains the changes

## Style Guidelines

### JavaScript/TypeScript

- Use ES6+ features
- Use `const`/`let` instead of `var`
- Use async/await for async operations
- Use JSDoc comments for public functions
- Follow ESLint configuration

```javascript
/**
 * Get gas fees for a network
 * @param {string} network - Network identifier
 * @returns {Promise<GasFeesResponse>}
 */
async function getGasFees(network) {
  // Implementation
}
```

### Python

- Follow PEP 8
- Use type hints
- Use docstrings (Google style)
- Maximum line length: 88 characters (Black)

```python
def get_gas_fees(network: str) -> Dict[str, Any]:
    """
    Get gas fees for a network.
    
    Args:
        network: Network identifier (e.g., 'ethereum_mainnet')
        
    Returns:
        Gas fees data including slow, standard, fast prices
        
    Raises:
        KtzchenWeb3Error: If the API request fails
    """
    # Implementation
```

### Documentation

- Use clear, concise language
- Include code examples
- Keep examples up to date
- Use proper Markdown formatting

## Community

- **Discord**: [Join our community](https://discord.gg/ktzchenweb3)
- **Twitter**: [@ktzchenweb3](https://twitter.com/ktzchenweb3)
- **Email**: contributors@ktzchenweb3.io

### Getting Help

If you need help:

1. Check the documentation
2. Search existing issues
3. Ask on Discord
4. Open a new issue

## Recognition

Contributors are recognized in:

- README.md contributors section
- Release notes
- Our website's contributors page

Thank you for contributing to KtzchenWeb3!
