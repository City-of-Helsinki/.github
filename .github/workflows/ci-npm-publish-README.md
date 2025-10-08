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

### 🔶 Optional Inputs

- **`node-version`** (string): Node.js version to use. Default: `'22'`.
- **`package-manager`** (string): Package manager to use (npm, yarn, pnpm). Default: `'yarn'`.
- **`install-command`** (string): Command to install dependencies. Default: `'yarn --frozen-lockfile'`.
- **`test-command`** (string): Command to run tests. Default: `'yarn test'`.
- **`build-command`** (string): Command to build the package. Default: `'yarn build'`.
- **`skip-tests`** (boolean): Skip running tests. Default: `false`.
- **`registry-url`** (string): npm registry URL. Default: `'https://registry.npmjs.org/'`.
- **`access`** (string): Package access level (public, restricted). Default: `'public'`.

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
      node-version: '20'
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

## 🛠️ Setup Requirements

1. **Configure npm trusted publisher** for your package:
   - Go to your package on npmjs.com
   - Add trusted publisher with:
     - Organization: `City-of-Helsinki`
     - Repository: `<your-repo-name>`
     - Workflow: `<your-workflow-filename>.yml`
     - Environment: (leave blank)

2. **Ensure package.json repository field** matches your GitHub repository:
   ```json
   {
     "repository": {
       "type": "git", 
       "url": "https://github.com/City-of-Helsinki/<your-repo-name>"
     }
   }
   ```

3. **Set up proper tagging** in your release process (e.g., using release-please or manual tagging).
