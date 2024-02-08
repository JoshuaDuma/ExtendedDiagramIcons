# Diagram Icons Extention
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
[![pypi version](https://badge.fury.io/py/ExtendedDiagramIcons.svg)](https://badge.fury.io/py/ExtendedDiagramIcons)
![contributors](https://img.shields.io/github/contributors/JoshuaDuma/ExtendedDiagramIcons)

<a href="https://www.buymeacoffee.com/joshuaduma" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>


This repo contains the python library used to create the pip package ExtendedDiagramIcons to extend the Diagrams package: [Diagrams GitHub Repository](https://github.com/mingrammer/diagrams).

## Current Builds
[![Stable Build Version](https://github.com/JoshuaDuma/ExtendedDiagramIcons/blob/main/docs/data/stable_build.svg)](https://github.com/JoshuaDuma/ExtendedDiagramIcons/tree/main)
[![Development Build Version](https://github.com/JoshuaDuma/ExtendedDiagramIcons/blob/dev/docs/data/development_build.svg)](https://github.com/JoshuaDuma/ExtendedDiagramIcons/tree/dev)

<!-- START_SECTION:InstallLatestDevelopment -->

- Install latest development build: `pip install ExtendedDiagramIcons==1.3.0.dev1`
    
<!-- END_SECTION:InstallLatestDevelopment -->
<!-- START_SECTION:InstallLatestStable -->

<!-- END_SECTION:InstallLatestStable -->

## Usage
This is intended to be used in a project that uses the diagrams python pip package as an extention of the available icons. To import the latest build of this library into your project use `pip install ExtendedDiagramIcons`.

## Requirement
- Python `3.9+`
- Requires the pip package `Diagrams``

## Testing

To run the unit tests use this command in the directory `python3 -m unittest discover tests`.

## Publish

To publish the latest version of this project use the following:

1. Install Twine: `pip install twine`
2. Build your package: `python setup.py sdist bdist_wheel`
3. To Upload your package, you will need your PyPI credentials (not avilable via CICD for security reasons): `twine upload dist/* -u __token__ -p <your-api-token>`

## Documentation

Use the references below to extend your diagrams. Example import: `from ExtendedDiagramIcons.diagrams.octopusdeploy.octopusdeploy import Octopus_Server_Node, Pipeline`.

<!-- START_SECTION:Documentation -->


## digitalocean



<img width="30" src="/resources/digitalocean/project.png" alt="Project" style="float: left; padding-right: 10px;" > **ExtendedDiagramIcons.digitalocean.Project**


## digitalocean.security



<img width="30" src="/resources/digitalocean/security/ssh_key.png" alt="Ssh_Key" style="float: left; padding-right: 10px;" > **ExtendedDiagramIcons.digitalocean.security.Ssh_Key**




## generic



<img width="30" src="/resources/generic/github.png" alt="Github" style="float: left; padding-right: 10px;" > **ExtendedDiagramIcons.generic.Github**

<img width="30" src="/resources/generic/jira.png" alt="Jira" style="float: left; padding-right: 10px;" > **ExtendedDiagramIcons.generic.Jira**

<img width="30" src="/resources/generic/report_portal.png" alt="Report_Portal" style="float: left; padding-right: 10px;" > **ExtendedDiagramIcons.generic.Report_Portal**

<img width="30" src="/resources/generic/software_engineer.png" alt="Software_Engineer" style="float: left; padding-right: 10px;" > **ExtendedDiagramIcons.generic.Software_Engineer**







## dnsproviders.namecheap



<img width="30" src="/resources/dnsproviders/namecheap/namecheap_api.png" alt="Namecheap_Api" style="float: left; padding-right: 10px;" > **ExtendedDiagramIcons.dnsproviders.namecheap.Namecheap_Api**

<img width="30" src="/resources/dnsproviders/namecheap/namecheap_domain.png" alt="Namecheap_Domain" style="float: left; padding-right: 10px;" > **ExtendedDiagramIcons.dnsproviders.namecheap.Namecheap_Domain**

<img width="30" src="/resources/dnsproviders/namecheap/provider.png" alt="Provider" style="float: left; padding-right: 10px;" > **ExtendedDiagramIcons.dnsproviders.namecheap.Provider**




## octopusdeploy



<img width="30" src="/resources/octopusdeploy/octopus_deploy.png" alt="Octopus_Deploy" style="float: left; padding-right: 10px;" > **ExtendedDiagramIcons.octopusdeploy.Octopus_Deploy**

<img width="30" src="/resources/octopusdeploy/octopus_server_node.png" alt="Octopus_Server_Node" style="float: left; padding-right: 10px;" > **ExtendedDiagramIcons.octopusdeploy.Octopus_Server_Node**

<img width="30" src="/resources/octopusdeploy/octopus_worker_node.png" alt="Octopus_Worker_Node" style="float: left; padding-right: 10px;" > **ExtendedDiagramIcons.octopusdeploy.Octopus_Worker_Node**

<img width="30" src="/resources/octopusdeploy/octopus_worker_pool.png" alt="Octopus_Worker_Pool" style="float: left; padding-right: 10px;" > **ExtendedDiagramIcons.octopusdeploy.Octopus_Worker_Pool**

<img width="30" src="/resources/octopusdeploy/pipeline.png" alt="Pipeline" style="float: left; padding-right: 10px;" > **ExtendedDiagramIcons.octopusdeploy.Pipeline**

<img width="30" src="/resources/octopusdeploy/release.png" alt="Release" style="float: left; padding-right: 10px;" > **ExtendedDiagramIcons.octopusdeploy.Release**



<!-- END_SECTION:Documentation -->

# Semantic Release

[![GitHub Actions](https://github.com/JoshuaDuma/ExtendedDiagramIcons/actions/workflows/dev.yml/badge.svg)](https://github.com/JoshuaDuma/ExtendedDiagramIcons/actions)
[![GitHub Actions](https://github.com/JoshuaDuma/ExtendedDiagramIcons/actions/workflows/main.yml/badge.svg)](https://github.com/JoshuaDuma/ExtendedDiagramIcons/actions)

## Continuous Integration (CI)

### GitHub Actions

We use GitHub Actions to automate our release workflows. The badge above indicates the status of our latest build.
# Semantic Versioning in Our Project

In our project, we adhere to [Semantic Versioning](https://semver.org/) to standardize version numbers and to convey meaning about the underlying code with each release. Below is an explanation of the prefixes we use in our commit messages and how they relate to our release strategy:

<!-- 
## Commit Prefixes

### 1. `feat:`

**Description:** A new feature for the user or a particular improvement to existing functionalities.  
**Example:** `feat: add new login button`  
**Effect:** Increments the *minor* version.  
**Branches:** Typically used on both `dev` and `release` branches.

### 2. `fix:`

**Description:** A bug fix that resolves an issue affecting the user.  
**Example:** `fix: resolve issue with login button not responding`  
**Effect:** Increments the *patch* version.  
**Branches:** Typically used on both `dev` and `release` branches.

### 3. `chore:`

**Description:** Simple changes that are not part of application logic or business features.  
**Example:** `chore: update dependencies`  
**Effect:** No version increment unless combined with other prefixes.  
**Branches:** Typically used on `dev` branch.

### 4. `docs:`

**Description:** Changes to documentation.  
**Example:** `docs: update API documentation`  
**Effect:** No version increment.  
**Branches:** Can be used on any branch.

### 5. `style:`

**Description:** Code changes that do not modify the logic or business features (e.g., formatting).  
**Example:** `style: reformat code`  
**Effect:** No version increment.  
**Branches:** Can be used on any branch.

### 6. `refactor:`

**Description:** Code changes that neither fix a bug nor add a feature.  
**Example:** `refactor: optimize code for performance`  
**Effect:** No version increment unless there is a significant change.  
**Branches:** Can be used on any branch.

### 7. `perf:`

**Description:** Changes that improve performance.  
**Example:** `perf: enhance query performance`  
**Effect:** May increment the *patch* version if significant.  
**Branches:** Typically used on both `dev` and `release` branches.

### 8. `test:`

**Description:** Adding or modifying tests.  
**Example:** `test: add unit tests for login functionality`  
**Effect:** No version increment.  
**Branches:** Can be used on any branch.

### 9. `BREAKING CHANGE:`

**Description:** A change that is not backward compatible and requires the user to change something about their setup.  
**Example:** `BREAKING CHANGE: migrate to new login system`  
**Effect:** Increments the *major* version.  
**Branches:** Typically used on `release` branch.

## Branches

### 1. `dev`

**Purpose:** Regular dev and feature additions happen here.  
**Versioning:** Automated version increments happen for *minor* and *patch* changes using the `feat:` and `fix:` prefixes.

### 2. `release/main`

**Purpose:** Stable and production-ready features are merged here.  
**Versioning:** *Major* version increments happen here using the `BREAKING CHANGE:` prefix.

#### main Branch

On the main branch, commits with prefixes `test`, `perf`, `refactor`, `style`, `docs`, or `chore` **will not trigger a deployment**. This ensures that only substantial changes, which either fix a bug or introduce a new feature, cause a deployment in the main environment.

By adhering to this strategy, we ensure consistency, predictability, and ease of understanding in our versioning and deployment process.

# Semantic Versioning Workflow

## dev (Pre-release) Branch

### Steps:

1. **Start:**
   - [No Commits]

2. **Commit: `feat: add new feature`**
   - [Generates Version & Tag: **1.1.0-dev.0**]

3. **Commit: `fix: resolve minor bug`**
   - [Generates Version & Tag: **1.1.0-dev.1**]

4. **Commit: `chore: update dependencies`**
   - [No Version Change: Remains **1.1.0-dev.1**]

5. **Merge into main:**
   - [Commits are merged, triggers a check for release in main branch]

---

## main (Release) Branch

### Steps:

1. **Start:**
   - [Current Version: **1.0.0**]

2. **Merge from dev (with `feat` & `fix` commits):**
   - [Checks Commits: Finds `feat:` & `fix:`, hence eligible for release]
   - [Generates Version & Tag: **1.1.0**]

---

## Explanation

- **dev Branch (Pre-release):**
  - New features (`feat:`) and bug fixes (`fix:`) increment the pre-release version.
  - Commits like `chore:`, `docs:`, etc. do not change the version.
  - Each commit or PR that changes the version generates a new pre-release tag like `1.1.0-dev.0`, `1.1.0-dev.1`, etc.

- **main Branch (Release):**
  - When changes are merged from `dev` to `main`, it checks for commits with `feat:` or `fix:` prefixes.
  - If found, it increments the appropriate version number (minor for `feat:` and patch for `fix`)
-->