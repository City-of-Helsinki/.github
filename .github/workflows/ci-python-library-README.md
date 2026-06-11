# Reusable CI workflow for Python libraries

This reusable workflow is part of the City of Helsinki's GitHub Actions setup, specifically designed to provide an opinionated and consistent CI process for City of Helsinki's Python library projects.

## Key Features

- **Commit Linting**: Enforces commit message standards using [commitlint](https://commitlint.js.org/).
- **Code Style Checks**: Verifies code style and formatting using [pre-commit](https://pre-commit.com/).
- **Automated Testing**: Runs project tests across multiple Python versions using [hatch](https://hatch.pypa.io/).
- **Code Quality Analysis**: Performs a [SonarQube Cloud](https://sonarcloud.io/) scan.

## Requirements for Projects Using the Workflow

- **commitlint** [config file](https://commitlint.js.org/reference/configuration.html#config-via-file) is present in the root of the project.
- **pre-commit** is set up with a `.pre-commit-config.yaml` file in the root of the project.
- **hatch** is used for testing, with a `pyproject.toml` that defines the test environments.
- **SonarQube Cloud** is configured with `SONAR_TOKEN` and `GITHUB_TOKEN` set in the repository secrets.

## Usage Instructions

To use this reusable workflow, create a project-specific workflow file in your `.github/workflows` directory. Set the `uses` value to `City-of-Helsinki/.github/.github/workflows/ci-python-library.yml@main` and provide the following inputs and secrets as needed:

### Required Inputs

- **`python-matrix`** (string): Python versions to use in the test matrix. Must be an array inside a string, e.g. `"['3.12', '3.13']"`.

### Optional Inputs

- **`python-version`** (string): Python version to use for pre-commit checks. Defaults to `"3.x"`.
- **`enable-sonar`** (boolean): Whether to run the SonarQube Cloud Scan job after tests. Defaults to `true`.
- **`commitlint-config-file`** (string): Path to the commitlint config file. If not set, commitlint uses its default config discovery.
- **`pre-commit-config-file`** (string): Path to `.pre-commit-config.yaml`. If empty, pre-commit uses its default discovery (file in repository root).

### Secrets

- **`sonar-token`**: Token for SonarQube Cloud Scan. Required if `enable-sonar` is `true`.
- **`github-token`**: `GITHUB_TOKEN` for SonarQube Cloud PR decoration. Required if `enable-sonar` is `true`.

### Example usage (`<own project>/.github/workflows/ci.yml`)

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  common:
    uses: City-of-Helsinki/.github/.github/workflows/ci-python-library.yml@main
    secrets:
      sonar-token: ${{ secrets.SONAR_TOKEN }}
      github-token: ${{ secrets.GITHUB_TOKEN }}
    with:
      python-matrix: "['3.10', '3.11', '3.12', '3.13', '3.14']"
```
