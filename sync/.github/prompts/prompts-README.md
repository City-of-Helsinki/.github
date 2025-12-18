# Common prompts for GitHub Copilot

This directory contains common prompts for GitHub Copilot.
Note that the common prompts are synced from City-of-Helsinki/.github repository, and any changes made here will be overwritten.

## Usage

All prompt files that are names *.prompt.md will be available as a slack command in the Github Copilot chat.

For example, to update the Django API documentation, you can run the command `/update-django-apidocs`.

If you want any new prompts to be synced to other repositories, you can add the prompt files to the `sync/.github/prompts/` directory in City-of-Helsinki/.github repository and they will be synced to the other repositories. If you want to sync to more repositories, you can add the repository names to the `.github/sync.yml` file in City-of-Helsinki/.github repository.

## Prompts

### update-django-apidocs.prompt.md

This prompt is used to add or update the Django API documentation.

This command will setup and update the Django API documentation using the drf-spectacular library.
