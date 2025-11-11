# 🚀 Reusable CI workflow for Release Please

This reusable workflow is part of the City of Helsinki’s GitHub Actions setup and it provides a consistent Release process for City of Helsinki’s projects.

## 🌟 Key Features

- **Release PR**: Create PR for release.
- **Changelog**: Create changelog from git commits.
- **Version number**: Increase software version number. 

## 📋 Requirements for Projects Using the Workflow

- **Commits** must be written in the form of [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) 
- **release-please-config.json** configuration file for release-please.
- **.release-please-manifest.json** file to maintain version information.

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `include-component-in-tag` | If true, add prefix to tags and branches, allowing multiple libraries to be released from the same repository | No | `true` |

## Outputs

| Output | Description |
|--------|-------------|
| `release_created` | Whether a release was created or not |


## 📚 Usage Instructions

To use this reusable workflow, create a project-specific workflow file in your `.github/workflows` directory. 

City of Helsinki release please general [instructions](https://helsinkisolutionoffice.atlassian.net/wiki/spaces/DD/pages/8278966368/Releases+with+release-please).

### 📄 Example usage (`<own project>/.github/workflows/release-please.yml`)

```yaml
name: release-please
on:
  push:
    branches:
      - main
  # Run daily to keep the release PR date current
  schedule:
    - cron: '1 0 * * *'

permissions:
  contents: write
  pull-requests: write

jobs:
  common:
    uses: City-of-Helsinki/.github/.github/workflows/release-please.yml@main
