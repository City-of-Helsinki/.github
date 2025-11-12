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

```yaml
name: Create release & publish to PyPI
# If ran manually, e.g. with ref set to "refs/tags/v1.2.3", set the run name to "Publish refs/tags/v1.2.3".
run-name: ${{ inputs.ref && format('Publish {0}', inputs.ref) || null }}

on:
  push:
    branches:
      - main
  # Run daily to keep the release PR date current
  schedule:
    - cron: '1 0 * * *'
  workflow_dispatch:
    inputs:
      ref:
        description: "The branch, tag or SHA to publish."
        required: true
        type: string

jobs:
  release-please:
    uses: City-of-Helsinki/.github/.github/workflows/release-please.yml@main
    permissions:
      contents: write
      pull-requests: write
    with:
        include-component-in-tag: false

  build:
    needs:
      - release-please
    uses: City-of-Helsinki/.github/.github/workflows/build-python-dists.yml@main
    with:
        ref: ${{ inputs.ref }}
    # Run build job if a release was created or a ref was specified (i.e. workflow was invoked manually)
    if: ${{ needs.release-please.outputs.release_created || inputs.ref }}

  publish-to-pypi:
    name: Publish to PyPI
    runs-on: ubuntu-latest
    needs:
      - build
    # Run publish job if an artifact was uploaded
    if: ${{ needs.build.outputs.artifact_name }}
    environment:
      name: pypi
      url: https://pypi.org/p/<package-name>
    permissions:
      id-token: write  # mandatory for trusted publishing
    steps:
    - name: Download all the dists
      uses: actions/download-artifact@018cc2cf5baa6db3ef3c5f8a56943fffe632ef53 # v6.0.0
      with:
        name: ${{ needs.build.outputs.artifact_name }}
        path: dist/
    - name: Publish distribution to PyPI
      uses: pypa/gh-action-pypi-publish@ed0c53931b1dc9bd32cbe73a98c7f6766f8a527e # v1.13.0
```

[gh-action-pypi-publish#trusted-publishing]: https://github.com/pypa/gh-action-pypi-publish/blob/987f11e872eb5ca67aad6a4fe531bd3089142c60/README.md#trusted-publishing
