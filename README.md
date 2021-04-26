[![aioneers_logo](etc/aioneers_logo.png)](https://aioneers.com/about/open-source-aio-data-science/)
![Python_Version](https://img.shields.io/badge/Python%20Version-3.7%20%7C%203.8-blue)
[![Documentation Status](https://readthedocs.org/projects/aioconnect/badge/?version=latest)](https://aioconnect.readthedocs.io/)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CONTRIBUTING.md)
[![Code of Conduct](https://img.shields.io/badge/Code%20of%20Conduct-Be%20kind%20to%20each%20other-yellow)](CODE_OF_CONDUCT.md)
[![License](https://img.shields.io/badge/License-MIT-brightgreen)](LICENSE)
[![aioneers](https://img.shields.io/badge/With%20love%20from-aioneers-blue)](https://aioneers.com/about/open-source-aio-data-science/)

# Our Motivation

At [**aioneers**](https://aioneers.com/), we place a lot of importance on giving back to our community.<br>
<br>
We operate in the field of supply chains, helping organizations close their supply chain performance gap whilst
retaining resilience and furthering sustainability. ([See our Manifesto](https://aioneers.com/about/why/)).<br>
<br>
We want a part of our work to be providing the supply chain data science community with open source,
free-to-use code for building applications. This will be accompanied by insightful explanations and tutorials,
so that data scientists across the world can achieve the same things we aim for; strengthened resilience, sustainability, and an optimized supply chain performance.<br>
<br>
We happily welcome contributions from anyone sharing the same goal, to build and spread better supply chain data science tools.<br>
<br>
We are dedicated to spending up to 5% of our time on sharing, exchanging and curating guides,
with the end goal of accelerating our community’s efforts to build a more sustainable world.
<br>
<br>
The documentation can be found here: [![Documentation Status](https://readthedocs.org/projects/aioconnect/badge/?version=latest)](https://aioconnect.readthedocs.io/en/latest/?badge=latest)

# Installation

## Usage of the package

Install the package with PyPI.

```
$ pip install aioconnect
```

## Clone the repository for users with direct access

git clone -b dev https://GITUSERNAME:PERSONALACCESSTOKEN@github.com/aioneers/aioconnect.git

Install the package locally:

```
$ pip install -e ./aioconnect
```

## Install and configure Azure CLI

For a lot of our functions we use the Azure CLI repository.

To install the current release, Azure CLI is necessary as a prerequisite: [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)

On Windows, the installation guide can be found here: [Windows az CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli)

On macOS the Azure CLI can be installed with Homebrew on a command line: [macOS az CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-macos)

```
$ brew update && brew install azure-cli
```

On Linux, the Azure CLI can be installed via apt: [Linux az CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux)

```
$ curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

Then the Azure CLI needs to be signed, which is easiest with this command (for all systems):

```
$ az login
```

# Contribution guidelines

First of all, thank you for considering contributing to this repository. Any contribution, from correcting a typo, forking the repo to adding another function or an insightful tutorial is very welcome.

**If you want to contribute to aioneers, be sure to review the
[contribution guidelines](CONTRIBUTING.md). This project adheres to aioneers'
[code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to
uphold this code.**

**We use [GitHub issues](https://github.com/aioneers/aio/issues) for
tracking requests and bugs and please direct specific questions to
[maintainer e-mail address](mailto:maintainer@@aioneers.com).**

# License

[![License](https://img.shields.io/badge/License-MIT-brightgreen)](LICENSE)
