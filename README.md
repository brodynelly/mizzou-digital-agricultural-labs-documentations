# PAAL Documentation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![CI](https://github.com/brodynelly/mizzou-digital-agricultural-labs-documentations/actions/workflows/ci.yml/badge.svg)](https://github.com/brodynelly/mizzou-digital-agricultural-labs-documentations/actions/workflows/ci.yml) ![MkDocs](https://img.shields.io/badge/MkDocs-Material-teal)

This repository contains the MkDocs source for the PAAL project. The documentation build validates the configured navigation and internal page references; it does not publish or deploy the site.

## Preview locally

Use Python 3.11 or newer and install the documented theme dependency:

~~~
python -m pip install "mkdocs-material>=9,<10"
mkdocs serve
~~~

Open the local address printed by the MkDocs server. To run the same check used in CI:

~~~
mkdocs build --strict
~~~

The strict build stops on warnings, including missing pages referenced by the configured navigation.

## Deployment notes

The pages describe the PAAL system, but this repository does not contain verified production deployment manifests or evidence for the Kubernetes, managed database, monitoring, or automatic rollback setup described in older text. See the deployment and recovery evidence page for source-backed boundaries and gaps. No production deployment is claimed by this repository.

## Contributing

Keep architecture and operational claims traceable to current source or reviewed evidence. Mark unverified procedures and assumptions clearly.
