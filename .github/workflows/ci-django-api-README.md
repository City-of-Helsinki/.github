# 🚀 Reusable CI workflow for Django APIs

This reusable workflow is part of the City of Helsinki’s GitHub Actions setup, specifically designed to provide an opinionated and consistent CI process for City of Helsinki’s Django API projects.

## 🌟 Key Features

- **Commit Linting**: Enforces commit message standards using [commitlint](https://commitlint.js.org/).
- **Code Style Checks**: Verifies code style and formatting using [pre-commit](https://pre-commit.com/).
- **Automated Testing**: Runs project tests using [pytest](https://docs.pytest.org/en/stable/).
- **Code Quality Analysis**: Performs a [SonarQube Cloud](https://sonarcloud.io/) scan.

## 📋 Requirements for Projects Using the Workflow

- **commitlint** [config file](https://commitlint.js.org/reference/configuration.html#config-via-file) is present in the root of the project.
- **pre-commit** is set up with a `.pre-commit-config.yaml` file in the root of the project.
- **pytest** is used for testing, and tests can be run with `pytest` from the root of the project.
- **SonarQube Cloud** is configured with `SONAR_TOKEN` set in the repository secrets.
- `requirements.txt` and `requirements-dev.txt` are used for Python dependencies.

## 📚 Usage Instructions

To use this reusable workflow, create a project-specific workflow file in your `.github/workflows` directory. Ensure the `uses` value is set to `City-of-Helsinki/.github/.github/workflows/ci-django-api.yml@main` and `secrets` is set to `inherit`. Also provide the following inputs as needed:

### 🛑 Required Inputs

- **`python-version`** (string): Specifies the Python version to use in the workflow.
- **`postgres-major-version`** (number): Specifies the PostgreSQL major version (allowed values: `13`, `14`, `17`).

### 🔶 Optional Inputs

- **`use-postgis`** (boolean): Set to `true` to enable the PostGIS extension. Default is `false`.
- **`extra-commands`** (string): Additional setup commands or checks to execute before running tests. Can be used to set environment variables: `echo "EXTRA_TEST_ENV_VAR=test" >> $GITHUB_ENV`.

### 📄 Example usage (`<own project>/.github/workflows/ci.yml`)

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

jobs:
  common:
    uses: City-of-Helsinki/.github/.github/workflows/ci-django-api.yml@main
    secrets: inherit
    with:
      python-version: 3.12
      postgres-major-version: 17
      use-postgis: true
      extra-commands: |
        echo "EXTRA_TEST_ENV_VAR=test" >> $GITHUB_ENV
        pip install extra-test-package
        python manage.py extra_check
