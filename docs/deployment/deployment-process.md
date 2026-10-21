# Deployment and recovery evidence

This page records what can be supported by the public source currently linked for PAAL. It is a source review, not a record of a production deployment or recovery exercise.

## What the source shows

At the reviewed dashboard revision, the [Docker Compose configuration](https://github.com/brodynelly/mizzou-digital-agricultural-labs-dashboard/blob/51636e2cce352e313507087322f5cdf362396b78/docker-compose.yml) defines MongoDB, initialization and seed-admin tasks, a backend, a frontend, and an Nginx proxy on a Docker Compose network. It also defines named volumes for MongoDB and dependency directories.

The checked-in [Nginx configuration](https://github.com/brodynelly/mizzou-digital-agricultural-labs-dashboard/blob/51636e2cce352e313507087322f5cdf362396b78/nginx.conf) routes API and Socket.IO paths to the backend and other requests to the frontend. This is evidence of a local container topology and reverse-proxy routing.

## What is not verified

The checked-in configuration does not establish that the system runs in Kubernetes, uses a managed database or CDN, has staging and production environments, or has the monitoring and automatic rollback procedures described in earlier versions of this guide. The Compose configuration does not define container health checks. This source review did not start the application or connect to a database.

Do not treat the topology as a production security or availability assessment. The public repository's deployment claims need confirmation from an authorized operator before being presented as operational practice.

## Recovery work still needed

A repeatable recovery claim requires a separate disposable environment with synthetic data and a reviewed configuration that does not reuse tracked operational-looking key or database files. A future test should record:

1. Which synthetic dataset and application revision were used.
2. How a backup was created and restored into an isolated database.
3. Checksums or record counts before and after restore.
4. Health checks and rollback behavior that were actually exercised.
5. Any manual steps and known limitations.

No backup restore, health-check exercise, or rollback was performed for this documentation update.
