# 🚀 Reusable CI workflow for Release Please

This reusable workflow is part of the City of Helsinki’s GitHub Actions setup and it provides a consistent Release process for City of Helsinki’s projects.

## 🌟 Key Features

- **Release PR**: Create PR for release.
- **Changelog**: Craete changelog from git commit.
- **Version number**: Increase software version number. 

## 📋 Requirements for Projects Using the Workflow

- **Commits** must be written in the form of [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) 
- **release-please-config.json** configuration file for release-please.
- **.release-please-manifest.json** file to maintain version information.
- **token** is using `GITHUB_TOKEN` set in the repository secrets.

## 📚 Usage Instructions

To use this reusable workflow, create a project-specific workflow file in your `.github/workflows` directory. Ensure the `uses` value is set to `City-of-Helsinki/.github/.github/workflows/release-pleasee.yml@main` and `secrets` is set to `inherit`. 

City of Helsinki release please general [instructions](https://helsinkisolutionoffice.atlassian.net/wiki/spaces/DD/pages/8278966368/Releases+with+release-please).

### 📄 Example usage (`<own project>/.github/workflows/release-please.yml`)

```yaml
name: release-please
on:
  push:
    branches:
      - main
  schedule:
    - cron: '1 0 * * *'

permissions:
  contents: write
  pull-requests: write

jobs:
  common:
    uses: City-of-Helsinki/.github/.github/workflows/release-please.yml@main
