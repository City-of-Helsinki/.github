# 🚀 Reusable CI workflow for .NET apps

This reusable workflow is part of the City of Helsinki's GitHub Actions setup, specifically designed to provide an opinionated and consistent CI process for City of Helsinki's .NET projects.

## 🌟 Key Features

- **Automated Testing**: Builds the app and runs tests via `dotnet test`, collecting code coverage with [dotnet-coverage](https://learn.microsoft.com/dotnet/core/additional-tools/dotnet-coverage).
- **Code Quality Analysis**: Performs a [SonarQube Cloud](https://sonarcloud.io/) scan using the collected coverage report.
- **Dependency Review**: Scans dependency changes in pull requests for known vulnerabilities using [GitHub's dependency review action](https://github.com/actions/dependency-review-action).

## 📋 Requirements for Projects Using the Workflow

- `dotnet build` and `dotnet test` work without extra arguments from the project's working directory (i.e. a solution or project file can be discovered automatically).
- **SonarQube Cloud** project configuration is present in `SonarQube.Analysis.xml` at the root of the calling repository. It must include `sonar.projectKey`, `sonar.organization`, and `sonar.cs.vscoveragexml.reportsPaths` pointing at the generated `coverage.xml`. The workflow passes the project key and organization through the scanner's required command-line arguments. `SONAR_TOKEN` must be set in the repository secrets.

## 📚 Usage Instructions

To use this reusable workflow, create a project-specific workflow file in your `.github/workflows` directory. Ensure the `uses` value is set to `City-of-Helsinki/.github/.github/workflows/ci-dotnet.yml@main`. Also provide the following inputs and secrets as needed:

### � Optional Inputs

- **`dotnet-version`** (string): Specifies the .NET SDK version to use, e.g. `10.0.x`. Default is `10.0.x`.
- **`working-directory`** (string): Repository subdirectory where to build, test and run the SonarQube Cloud scan. Default is repository root.
- **`extra-commands`** (string): Additional setup commands or checks to execute before building and testing. Can be used to set environment variables: `echo "EXTRA_TEST_ENV_VAR=test" >> $GITHUB_ENV`.
- **`skip-sonar`** (boolean): Set to `true` to skip the SonarQube Cloud scan. Default is `false`.

### 🔑 Secrets

- **`SONAR_TOKEN`**: Token for SonarQube Cloud Scan. Required unless `skip-sonar` is `true`.

### 📄 Example usage (`<own project>/.github/workflows/ci.yml`)

The example uses the following workflow settings:

- **`concurrency`**: Ensures that only the latest workflow run for each branch or pull request is kept running. An in-progress run is cancelled when a newer run starts.
- **`permissions`**: Grants the workflow read access to repository contents and write access to pull requests, which is required for reporting workflow results.

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

permissions:
  contents: read
  pull-requests: write

jobs:
  common:
    uses: City-of-Helsinki/.github/.github/workflows/ci-dotnet.yml@main
    secrets:
      SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
    with:
      dotnet-version: "10.0.x"
      extra-commands: |
        echo "EXTRA_TEST_ENV_VAR=test" >> $GITHUB_ENV
```
