# 🚀 Reusable CI workflow for Node

This reusable workflow is part of the City of Helsinki’s GitHub Actions setup, specifically designed to provide an opinionated and consistent CI process for City of Helsinki’s Node projects.

## 🌟 Key Features

- **Commit Linting**: Enforces commit message standards using [commitlint](https://commitlint.js.org/).
- **Build and Lint**: Build and verifies code style and formatting via yarn.
- **Automated Testing**: Runs project tests via yarn.
- **Code Quality Analysis**: Performs a [SonarQube Cloud](https://sonarcloud.io/) scan.

## 📋 Requirements for Projects Using the Workflow

- **commitlint** [config file](https://commitlint.js.org/reference/configuration.html#config-via-file) is present in the root of the project.
- **SonarQube Cloud** is configured with `SONAR_TOKEN` set in the repository or organization secrets.

### 🧶 Yarn Commands

- **build** the project.
- **lint** run [eslint](https://eslint.org/) or another lint tool.
- **test:coverage** runs project tests with coverage.

## 📚 Usage Instructions

To use this reusable workflow, create a project-specific workflow file in your `.github/workflows` directory. Ensure the `uses` value is set to `City-of-Helsinki/.github/.github/workflows/ci-node.yml@main` and `secrets` is set to `inherit`. Also provide the following inputs as needed:

### 🛑 Required Inputs

- **`node-version`** (string): Specifies the Node version to use in the workflow.

### 🔶 Optional Inputs

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
    uses: City-of-Helsinki/.github/.github/workflows/ci-node.yml@main
    secrets: inherit
    with:
      node-version: 20
    extra-commands: |
      echo "EXTRA_TEST_ENV_VAR=test" >> $GITHUB_ENV
