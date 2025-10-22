# 🐍 Reusable PyPI Publish workflow

This reusable workflow is part of the City of Helsinki's GitHub Actions setup, specifically designed to provide an opinionated and consistent PyPI package publishing process for City of Helsinki's Python projects.

## 🌟 Key Features

- **Flexible Python Versions**: Configurable Python version support.
- **Automated Testing**: Runs project tests before publishing (can be skipped if needed).
- **Build Process**: Builds Python packages using the standard `build` module.
- **Dual Authentication**: Supports both API tokens and trusted publishers for secure publishing.
- **Dependency Management**: Optional requirements file installation for complex dependencies.
- **Modern Tools**: Uses latest Python setup and build tools.

## 📋 Requirements for Projects Using the Workflow

- **pyproject.toml**, **setup.py** or **setup.cfg** for package configuration.
- **Source code** in a standard Python package structure.
- **Test suite** (pytest recommended) if running tests.
- **PyPI account** and either API token or trusted publisher setup.

### 🧪 Testing Requirements

**Default test command:** `python -m pytest`

### 📦 Build Requirements

**Default build command:** `python -m build .`

The workflow uses Python's standard `build` module which supports:
- **Both formats** (recommended)
- **Wheel packages** (.whl files)
- **Source distributions** (sdist)

## 📚 Usage Instructions

To use this reusable workflow, create a project-specific workflow file in your `.github/workflows` directory. Ensure the `uses` value is set to `City-of-Helsinki/.github/.github/workflows/ci-pypi-publish.yml@main`. The workflow is typically triggered by release tags.

### 🔶 Optional Inputs

- **`python-version`** (string): Python version to use. Default: `'3.9'`.
- **`test-command`** (string): Command to run tests. Default: `'python -m pytest'`.
- **`skip-tests`** (boolean): Skip running tests. Default: `false`.
- **`build-command`** (string): Command to build the package. Default: `'python -m build .'`.
- **`requirements-file`** (string): Requirements file for dependencies. Default: `''` (none).
- **`use-trusted-publisher`** (boolean): Use trusted publisher instead of API token. Default: `false`.

### 🔐 Optional Secrets

- **`PYPI_API_TOKEN`**: PyPI API token (not required if using trusted publisher).

### 📄 Example usage with Trusted Publisher

```yaml
name: PyPI Publish (Trusted Publisher)

on:
  release:
    types: [published]

jobs:
  publish:
    uses: City-of-Helsinki/.github/.github/workflows/ci-pypi-publish.yml@main
    with:
      python-version: '3.12'
      use-trusted-publisher: true
      requirements-file: 'requirements-dev.txt'
```

### 📄 Example usage with API Token (`<own project>/.github/workflows/pypi-publish.yml`)

```yaml
name: PyPI Publish

on:
  push:
    tags:
      - 'v*.*.*'  # Trigger on version tags

jobs:
  publish:
    uses: City-of-Helsinki/.github/.github/workflows/ci-pypi-publish.yml@main
    secrets:
      PYPI_API_TOKEN: ${{ secrets.PYPI_API_TOKEN }}
    with:
      python-version: '3.12'
      test-command: 'pytest --cov'
```

### 📄 Advanced example with custom setup

```yaml
name: PyPI Publish

on:
  push:
    tags:
      - 'release-*'

jobs:
  publish:
    uses: City-of-Helsinki/.github/.github/workflows/ci-pypi-publish.yml@main
    secrets:
      PYPI_API_TOKEN: ${{ secrets.PYPI_API_TOKEN }}
    with:
      python-version: '3.12'
      test-command: 'python -m pytest tests/ --verbose'
      build-command: 'python -m build . --wheel'
      requirements-file: 'requirements.txt'
```

### 📄 Quick publish without tests

```yaml
name: PyPI Publish (No Tests)

on:
  workflow_dispatch:  # Manual trigger

jobs:
  publish:
    uses: City-of-Helsinki/.github/.github/workflows/ci-pypi-publish.yml@main
    secrets:
      PYPI_API_TOKEN: ${{ secrets.PYPI_API_TOKEN }}
    with:
      skip-tests: true
```

## 🔒 Authentication Methods

### 🛡️ Trusted Publisher Method (Recommended)

1. **Configure on PyPI**:
   - Go to your project on PyPI
   - Add trusted publisher with:
     - Publisher: GitHub
     - Owner: `City-of-Helsinki`
     - Repository: `<your-repo-name>`
     - Workflow: `<your-workflow-filename>.yml`
     - Environment: (optional)

2. **Use in workflow**:
   ```yaml
   with:
     use-trusted-publisher: true
   ```

### 🔑 API Token Method (Traditional)

1. **Generate API token** on PyPI:
   - Go to PyPI Account Settings
   - Create new API token for your project
   - Copy the token (starts with `pypi-`)

2. **Add token to GitHub secrets**:
   - Repository Settings → Secrets and variables → Actions
   - Add secret named `PYPI_API_TOKEN`
   - Paste your PyPI token

3. **Use in workflow**:
   ```yaml
   secrets:
     PYPI_API_TOKEN: ${{ secrets.PYPI_API_TOKEN }}
   ```

## 🚀 Supported Build Systems

#TODO
 - To be defined and tested
