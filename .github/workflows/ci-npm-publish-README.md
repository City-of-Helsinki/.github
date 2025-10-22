# 📦 Reusable NPM Publish workflow

This reusable workflow is part of the City of Helsinki's GitHub Actions setup, specifically designed to provide an opinionated and consistent npm package publishing process for City of Helsinki's Node.js projects.

## 🌟 Key Features

- **Latest npm**: Automatically upgrades to the latest npm version for best compatibility.
- **Flexible Package Managers**: Supports npm, yarn, and pnpm with configurable commands.
- **Automated Testing**: Runs project tests before publishing (can be skipped if needed).
- **Build Process**: Builds the package before publishing.
- **Trusted Publishers**: Uses npm's trusted publisher feature with provenance for secure publishing.
- **Configurable Access**: Supports both public and restricted package publishing.

## 📋 Requirements for Projects Using the Workflow

- **package.json** with proper `name`, `version`, and `repository` fields.
- **repository** field in `package.json` must match the GitHub repository URL for provenance verification.
- **npm trusted publisher** must be configured on npm for the package (for automated publishing).
- **Build and test scripts** defined in `package.json` (e.g., `build`, `test`).

### 🧶 Package Manager Commands

The workflow uses configurable commands for different package managers:

**Default Yarn Commands:**
- **yarn --frozen-lockfile**: Install dependencies
- **yarn test**: Run tests
- **yarn build**: Build the package

**Alternative npm Commands:**
- **npm ci**: Install dependencies
- **npm run test**: Run tests
- **npm run build**: Build the package

## 📚 Usage Instructions

To use this reusable workflow, create a project-specific workflow file in your `.github/workflows` directory. Ensure the `uses` value is set to `City-of-Helsinki/.github/.github/workflows/ci-npm-publish.yml@main`. The workflow is typically triggered by release tags.

### Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `node-version` | Node.js version to use | No | `20` |
| `package-manager` | Package manager to use (`npm`, `yarn`, `pnpm`) | No | `npm` |
| `registry-url` | npm registry URL | No | `https://registry.npmjs.org` |
| `app-dir` | Directory containing package.json | No | `.` |
| `install-command` | Command to install dependencies | No | Auto-detected |
| `test-command` | Command to run tests | No | Auto-detected |
| `build-command` | Command to build the package | No | Auto-detected |
| `publish-command` | Command to publish the package | No | Auto-detected |
| `skip-tests` | Skip running tests | No | `false` |
| `use-ci-build` | Use build artifacts from CI workflow | No | `false` |

### 📄 Example usage (`<own project>/.github/workflows/npm-publish.yml`)

```yaml
name: npm publish

on:
  push:
    tags:
      - 'v*.*.*'  # Trigger on version tags

jobs:
  publish:
    uses: City-of-Helsinki/.github/.github/workflows/ci-npm-publish.yml@main
    with:
      node-version: '22'
      package-manager: 'npm'
      install-command: 'npm ci'
      test-command: 'npm run test:ci'
      build-command: 'npm run build'
```

### 📄 Advanced example with custom commands

```yaml
name: npm publish

on:
  push:
    tags:
      - 'my-package-v*.*.*'

jobs:
  publish:
    uses: City-of-Helsinki/.github/.github/workflows/ci-npm-publish.yml@main
    with:
      node-version: '18'
      package-manager: 'pnpm'
      install-command: 'pnpm install --frozen-lockfile'
      test-command: 'pnpm run test:coverage'
      build-command: 'pnpm run build:production'
      access: 'public'
```

### 📄 Quick publish without tests

```yaml
name: npm publish (no tests)

on:
  push:
    tags:
      - 'hotfix-v*.*.*'

jobs:
  publish:
    uses: City-of-Helsinki/.github/.github/workflows/ci-npm-publish.yml@main
    with:
      skip-tests: true
```

## 🔒 Security Features

- **Trusted Publishers**: Uses npm's trusted publisher feature for secure, token-free publishing.
- **Provenance**: Automatically generates and publishes provenance attestations.
- **OIDC Authentication**: Uses OpenID Connect for secure authentication with npm.

## Prerequisites

1. **Repository Configuration**: Your package.json must include a proper `repository` field for npm provenance to work:
   ```json
   {
     "repository": {
       "type": "git",
       "url": "git+https://github.com/owner/repo.git"
     }
   }
   ```

2. **npm Trusted Publishers**: Configure trusted publishers in your npm package settings:
   - Go to your package on npmjs.com
   - Navigate to Settings > Publishing access
   - Add GitHub Actions as trusted publisher with your repository details

## Build Artifact Integration

This workflow can reuse build artifacts from the `ci-node.yml` workflow to avoid rebuilding:

1. Set `use-ci-build: true` when calling this workflow
2. Ensure the CI workflow runs first using `needs` dependency
3. Set `skip-tests: true` since tests already ran in CI

**Example Combined Workflow:**
```yaml
jobs:
  ci:
    uses: ./.github/workflows/ci-node.yml
    
  publish:
    needs: ci
    uses: ./.github/workflows/ci-npm-publish.yml
    with:
      use-ci-build: true
      skip-tests: true
```
