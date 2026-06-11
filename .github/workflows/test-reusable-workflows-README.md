# 🧪 Reusable Workflow Tests

This workflow tests the reusable workflows in this repository to ensure they work correctly before changes are merged.

## When it runs

Triggered automatically on pull requests that modify workflow files or test fixtures.

## Test fixtures

The `.github/workflow-test-fixtures/` directory contains minimal project stubs used as test subjects for the reusable workflows:

- **`django-api/`** — pip-based Django project fixture for `ci-django-api.yml`
- **`django-api-uv/`** — uv-based Django project fixture for `ci-uv-django-api.yml`
- **`node-yarn/`** — yarn-based Node.js fixture for `ci-node.yml`
- **`node-pnpm/`** — pnpm-based Node.js fixture for `ci-pnpm-node.yml`
