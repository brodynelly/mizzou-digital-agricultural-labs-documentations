# Getting started

This page helps you read or edit the documentation. It does not provide a verified application deployment recipe.

## Read the project documentation

Start with the [high-level architecture](architecture/high-level-system.md), then browse the frontend and backend pages from the navigation. The [deployment and recovery evidence](deployment/deployment-process.md) page records which infrastructure statements are supported by public source and which remain unverified.

## Preview documentation changes

Use Python 3.11 or newer. Install MkDocs Material, then run the local preview:

~~~
python -m pip install "mkdocs-material>=9,<10"
mkdocs serve
~~~

To run the CI build locally:

~~~
mkdocs build --strict
~~~

The strict build checks the configured navigation and local page links.

## Application setup is not verified here

The public application repository contains Docker and Nginx configuration, but its README and older documentation contain inconsistent setup instructions and production claims that are not confirmed by the checked-in deployment configuration. This documentation project does not start the application, connect to a database, or validate a backup or restore process.

Before attempting an application run, review the current source and use a disposable environment with synthetic data. Do not reuse tracked operational-looking data or key files.
