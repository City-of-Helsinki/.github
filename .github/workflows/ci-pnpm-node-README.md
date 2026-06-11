# 🚀 Reusable CI workflow for Node (pnpm)

This reusable workflow is part of the City of Helsinki’s GitHub Actions setup, specifically designed to provide an opinionated and consistent CI process for City of Helsinki’s **pnpm-based** Node projects.

This repository has two similar Node CI workflows on purpose:

- `ci-node.yml` is the general workflow for yarn-based projects.
- `ci-pnpm-node.yml` is the pnpm-specific workflow for projects that use `pnpm-lock.yaml`, pnpm install behavior, and pnpm commands.

Keeping both workflows allows projects to use the same CI structure while matching their package manager and lockfile strategy.

## 🌟 Key Features

- **Commit Linting**: Enforces commit message standards using [commitlint](https://commitlint.js.org/).
- **Build and Lint**: Build and verifies code style and formatting via pnpm.
- **Automated Testing**: Runs project tests via pnpm.
- **Code Quality Analysis**: Performs a [SonarQube Cloud](https://sonarcloud.io/) scan.

## 📋 Requirements for Projects Using the Workflow

- **commitlint** [config file](https://commitlint.js.org/reference/configuration.html#config-via-file) is present in the root of the project.
- **pnpm lockfile** (`pnpm-lock.yaml`) is present in the configured `working-directory`.
- **SonarQube Cloud** is configured with `SONAR_TOKEN` set in the repository or organization secrets.

### 🧶 pnpm Commands

- **build** the project.
- **lint** run [eslint](https://eslint.org/) or another lint tool.
- **test:coverage** runs project tests with coverage.

### 🪡 Optional pnpm Commands

- **typecheck** run tsc check
- **check-size** run browser bundle size limits check. The command is run if the `.size-limit.js` file is found in the app directory.
- **check-dist**: run ecmascript checks for build files. The command is run if the `.escheckrc` file is found in the app directory.

## 📚 Usage Instructions

To use this reusable workflow, create a project-specific workflow file in your `.github/workflows` directory. Ensure the `uses` value is set to `City-of-Helsinki/.github/.github/workflows/ci-pnpm-node.yml@main`. Also provide the following inputs and secrets as needed:

### 🛑 Required Inputs

- **`node-version`** (string): Specifies the Node version to use in the workflow.

### 🔶 Optional Inputs

- **`extra-commands`** (string): Additional setup commands or checks to execute before running tests. Can be used to set environment variables: `echo "EXTRA_TEST_ENV_VAR=test" >> $GITHUB_ENV`.
- **`typecheck`** (boolean): Run typecheck command. Default is `false`.
- **`working-directory`** (string): Repository working directory where to run pnpm installation and the tests jobs. Default is `.` (the repository root).
- **`app-directory`** (string): The subdirectory of the application where lint/build/tests are run. Default is **`working-directory`**.
- **`upload-artifacts`** (boolean): Set to true to upload build artifacts. Default is `false`.
- **`skip-sonar`** (boolean): Set to true to skip SonarQube checks. Default is `false`.
- **`skip-build`** (boolean): Set to true to skip the build phase. Default is `false`.
- **`ignore-scripts`** (boolean): Set to true to skip lifecycle scripts during install (`--ignore-scripts`). Default is `true`.
- **`pnpm-version`** (string): pnpm version to use (passed to `pnpm/action-setup`). If empty, the version is read from the `packageManager` field in `package.json`.
- **`commitlint-config-file`** (string): Path to the commitlint config file. If not set, commitlint uses its default config discovery.

### 🔑 Secrets

- **`SONAR_TOKEN`**: Token for SonarQube Cloud Scan. Required.

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
    uses: City-of-Helsinki/.github/.github/workflows/ci-pnpm-node.yml@main
    secrets:
      SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
    with:
      node-version: 24
    extra-commands: |
      echo "EXTRA_TEST_ENV_VAR=test" >> $GITHUB_ENV
```
