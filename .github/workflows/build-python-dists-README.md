# Build Python Distribution Packages Workflow

A reusable GitHub Actions workflow for building Python distribution packages (wheels and source distributions) using the standard Python `build` module.

## Overview

This workflow provides a standardized way to build Python packages across different repositories. It supports customizable build commands, dependency installation, and artifact storage.

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `artifact-name` | Name of the artifact to upload | No | `"python-package-dist"` |
| `artifact-path` | Path/pattern for files to include in artifact | No | `"dist/"` |
| `build-command` | Command(s) to build the package | No | `"python3 -m build"` |
| `dependencies-command` | Command(s) to install build dependencies | No | `"python3 -m pip install --user build"` |
| `python-version` | Python version to use for building | No | `"3.x"` |
| `ref` | Branch, tag, or SHA to checkout | No | (uses default branch) |

## Outputs

| Output | Description |
|--------|-------------|
| `artifact_name` | Name of the uploaded artifact (empty if no artifact was created) |

## Features

- **Standardized Build Process**: Uses Python's standard `build` module for creating distribution packages
- **Flexible Python Versions**: Supports any Python version available in GitHub Actions
- **Customizable Commands**: Override build and dependency installation commands as needed
- **Artifact Storage**: Automatically uploads built packages as GitHub Actions artifacts
- **Security**: Uses pinned action versions and disables credential persistence

## Requirements

Your repository should have:
- A valid Python package structure with `setup.py`, `setup.cfg`, or `pyproject.toml`
- Build configuration that works with the `python -m build` command

## Usage

### Basic usage

```yaml
name: Build package

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    uses: City-of-Helsinki/.github/.github/workflows/build-python-dists.yml@main
```

### Full workflow using release-please and PyPI with trusted publishing

> [!NOTE]
> At the time of writing, trusted publishing cannot be used from within a reusable workflow.
> In other words, this means that the other parts workflow can be reusable workflows, but the
> publishing part in particular **must** be non-reusable.
> [See gh-action-pypi-publish's README for more information.](gh-action-pypi-publish#trusted-publishing)

For a complete release and publish workflow, refer to [pypi-publish.yml](../../sync/.github/workflows/pypi-publish.yml). It adds a `workflow_dispatch` trigger with the following inputs, allowing the release and publish steps to be run manually for a specific ref:

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `ref` | The branch, tag or SHA to publish. E.g. main, refs/tags/v1.0.0, aeb2839. | Yes | - |
| `skip-build` | Skip artifact build and publish, i.e. run release-please only. | No | `false` |

[gh-action-pypi-publish#trusted-publishing]: https://github.com/pypa/gh-action-pypi-publish/blob/987f11e872eb5ca67aad6a4fe531bd3089142c60/README.md#trusted-publishing
