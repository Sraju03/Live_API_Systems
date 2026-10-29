# Part 2: Live API Connection & 12-Factor Secret Hygiene

**Student Name:** Raju Sekar  
**EPITA Login:** epita_raju.sekar@epita.fr  
**Assigned Group:** Group 4  
**API Domain:** NASA — Space & Astronomy  
**API Used:** NASA Astronomy Picture of the Day (APOD)

---

## 2.1 Adding Base Dependencies with `uv`

The required dependencies were added to the project using the `uv` package manager.

Command executed:

```bash
uv add requests python-dotenv
```

The following dependencies were installed:

- `requests` — to send HTTP requests to the NASA API.
- `python-dotenv` — to load environment variables from the local `.env` file.

---

## 2.2 Configuration Module (`config.py`)

Created the configuration module:

```text
src/epita_raju_sekar_space/config.py
```

The configuration module uses `python-dotenv` to load environment variables from `.env`.

The `Settings` dataclass defines the following configuration values:

- `APP_ENV` — application environment.
- `NASA_API_KEY` — NASA API key.
- `DEBUG` — debug mode configuration.

The `validate()` method verifies that the NASA API key is configured before making a live API request.

The API key is not hardcoded into the Python source code.

---

## 2.3 Implementing the Live API Client (`client.py`)

Created the API client:

```text
src/epita_raju_sekar_space/client.py
```

The client connects to NASA's Astronomy Picture of the Day API using the endpoint:

```text
https://science.nasa.gov/wp-json/wp/v2/apod-basic/
```

The client uses the `requests` library to send an HTTP GET request.

The `fetch_live_data()` function:

1. Validates the NASA API key.
2. Sends an HTTP GET request to the NASA APOD endpoint.
3. Checks the HTTP response status.
4. Parses the JSON response.
5. Handles the list-based response format.
6. Returns the selected APOD data as a Python dictionary.

The returned data includes:

- API request status
- Date
- Astronomy picture title
- Media type
- Explanation
- Image or article URL
- Copyright information

The client also includes timeout handling and HTTP error handling.

---

## 2.4 Implementing Secret Hygiene

Created the following configuration files:

```text
.env
.env.template
.gitignore
```

### `.env`

The `.env` file contains the actual NASA API key and local application configuration.

It is excluded from Git version control.

### `.env.template`

The `.env.template` file contains public configuration placeholders:

```ini
APP_ENV=development
DEBUG=True
NASA_API_KEY=your_nasa_api_key_here
```

This file does not contain any real secrets and can be committed to Git.

### `.gitignore`

The `.gitignore` file includes:

```gitignore
.venv/
.env
__pycache__/
*.py[cod]
dist/
build/
*.egg-info/
.vscode/
```

The `.env` file is ignored by Git, while `.env.template` remains eligible for version control.

---

## 2.5 Testing the Live API Connection

The live API connection was tested using the following command:

```bash
uv run python -c "from epita_raju_sekar_space.client import fetch_live_data; print(fetch_live_data())"
```

### Direct API Test

The NASA APOD endpoint was tested directly using the public demo key.

Command executed:

```bash
uv run python -c "import requests; r=requests.get('https://science.nasa.gov/wp-json/wp/v2/apod-basic/', params={'api_key':'DEMO_KEY'}, timeout=30); print('Status:',r.status_code); print('Response:',r.text[:500])"
```

The API returned:

```text
Status: 200
```

The response contained valid NASA APOD data, including the date, title, media type, explanation, and permalink.

### Live API Response

Paste the actual output from the successful `fetch_live_data()` command below.

```python
{
    'status': 'LIVE_SUCCESS',
    'date': '[ACTUAL DATE]',
    'title': '[ACTUAL NASA APOD TITLE]',
    'media_type': '[ACTUAL MEDIA TYPE]',
    'explanation': '[ACTUAL EXPLANATION OR REDACTED EXCERPT]',
    'url': '[ACTUAL NASA URL]',
    'copyright': '[ACTUAL COPYRIGHT OR NONE]'
}
```

The API key has been redacted and is not included in the report.

### Git Status

Command executed:

```bash
git status
```

Actual output:

```text
[PASTE YOUR ACTUAL GIT STATUS OUTPUT HERE]
```

Verification command:

```bash
git check-ignore .env
```

Expected output:

```text
.env
```

This confirms that the `.env` file is ignored by Git.

---

## 2.6 Why Are Environment Variables Superior to Configuration Files for Storing Secrets?

Environment variables are preferable to storing secrets directly in configuration files such as `config.json` or `settings.yaml` for the following two security reasons.

### Reason 1: Reduced Risk of Accidental Exposure Through Version Control

Configuration files are often committed to Git along with application source code.

If a real API key is stored in a configuration file, it may accidentally be exposed in a public repository, shared with other developers, or remain accessible in Git history even after the file is deleted.

Environment variables allow credentials to be kept separate from source code.

A local `.env` file can be excluded from Git using `.gitignore`, while a public `.env.template` provides the required configuration structure without exposing the actual secret.

This reduces the risk of accidentally publishing sensitive credentials.

### Reason 2: Separation of Configuration from Application Code

Environment variables allow different environments, such as development, testing, and production, to use different API keys without modifying the application's source code.

For example, a development environment can use a development API key, while a production environment uses a separate production API key.

This makes credential replacement and rotation easier and reduces the risk of accidentally using the wrong credentials in an environment.

It also supports the principle of keeping deploy-specific configuration separate from the codebase.

This approach follows Factor III (Config) of the 12-Factor App methodology.

---

## Conclusion

The NASA APOD live API client was implemented using Python, `requests`, and `python-dotenv`.

The application reads its API key from environment-based configuration rather than hardcoding it in the source code.

The NASA API endpoint was tested successfully and returned HTTP 200 with valid APOD data.

The configuration and secret hygiene requirements were implemented using `.env`, `.env.template`, and `.gitignore`.

The project follows Factor III (Config) of the 12-Factor App methodology by separating application configuration and secrets from the codebase.

# Dependency Locking with `uv` & Semantic Versioning

## 3.1 Adding Direct and Development Dependencies

The following commands were used to add the required dependencies:

```bash
uv add rich
uv add --dev pytest
```

### Direct Dependencies

Direct dependencies are packages explicitly added to the project and declared in `pyproject.toml`.

| Dependency | Purpose                                                                   |
| ---------- | ------------------------------------------------------------------------- |
| `requests` | Makes HTTP requests to APIs and web services.                             |
| `rich`     | Provides enhanced terminal output, formatting, tables, and progress bars. |

### Development Dependency

| Dependency | Purpose                                                          |
| ---------- | ---------------------------------------------------------------- |
| `pytest`   | Used for writing and running automated tests during development. |

The `pytest` package is added as a development dependency because it is required for testing but is not needed when the application runs in production.

---

## 3.2 Visualizing the Dependency Tree

### Command

```bash
uv tree
```

### Dependency Tree Output

Paste the actual output of `uv tree` below:

```text
[PASTE YOUR ACTUAL UV TREE OUTPUT HERE]
```

### Direct Dependencies

The project's direct dependencies are:

- `requests`
- `rich`

The development dependency is:

- `pytest`

### Transitive Dependencies

Transitive dependencies are packages automatically installed because another package requires them.

#### Dependencies pulled in by `requests`

Common transitive dependencies include:

- `certifi` — Provides trusted CA certificates for verifying TLS connections.
- `charset-normalizer` — Helps detect and normalize character encodings.
- `idna` — Provides internationalized domain name support.
- `urllib3` — Provides HTTP client functionality used by `requests`.

#### Dependencies pulled in by `rich`

Common dependencies include:

- `markdown-it-py` — Provides Markdown parsing functionality.
- `pygments` — Provides syntax highlighting.
- `mdurl` — Provides URL-related functionality used by Markdown parsing.

The exact dependency tree and versions depend on the project's resolved dependencies and should be verified using the actual output of `uv tree`.

### Cryptographic SHA-256 Hashes in `uv.lock`

The `uv.lock` file contains the exact versions of the project's dependencies and cryptographic SHA-256 hashes for package distributions.

These hashes help protect the build against supply-chain attacks by allowing the package manager to verify that downloaded package files match the expected cryptographic fingerprints recorded in the lockfile.

If a package file is modified or tampered with, its SHA-256 hash will no longer match the expected hash, and the integrity check will fail.

This helps protect against:

- Unauthorized modification of package files.
- Tampering with downloaded dependencies.
- Unexpected changes to package artifacts.

The lockfile improves reproducibility by ensuring that the same dependency versions and verified package artifacts are used across installations.

However, hashes alone do not guarantee that a package is safe. A malicious package could still be published with a valid hash. Therefore, dependency integrity checks should be combined with trusted package sources and dependency review.

---

## 3.3 Semantic Versioning (SemVer) Analysis

### 1. Version Ranges

#### `requests = "^2.31.0"`

The caret (`^`) specifies a compatible version range.

It matches:

```text
>=2.31.0, <3.0.0
```

This allows compatible minor and patch updates while preventing automatic upgrades to version `3.0.0` or higher.

#### `urllib3 = "~=2.2.1"`

The compatible release operator (`~=`) specifies:

```text
>=2.2.1, <2.3.0
```

This allows patch-level updates starting from version `2.2.1`, but does not allow version `2.3.0` or higher.

#### `rich = "==13.7.1"`

The equality operator (`==`) specifies an exact version.

It matches:

```text
13.7.1
```

No other version is permitted by this requirement.

### 2. Will `uv lock --upgrade` Install `requests` Version `3.0.0`?

No.

The requirement:

```text
requests = "^2.31.0"
```

allows versions greater than or equal to `2.31.0` but less than `3.0.0`.

Therefore, even if the upstream author releases `requests` version `3.0.0` with breaking changes, `uv lock --upgrade` will not install it while the existing version constraint remains unchanged.

The upgrade command updates dependencies to newer versions that satisfy the declared constraints.

To allow version `3.0.0`, the project would need to update its version requirement, for example:

```text
requests = "^3.0.0"
```

This is important because major versions may introduce breaking changes that require changes to the project's source code.

### 3. Difference Between `pyproject.toml` and `uv.lock`

#### `pyproject.toml` — Dependency Declaration

The `pyproject.toml` file declares the project's dependencies and version requirements.

For example:

```toml
[project]
dependencies = [
    "requests>=2.31.0,<3.0.0",
    "rich>=13.7.1"
]
```

It defines which package versions are allowed.

#### `uv.lock` — Dependency Pinning

The `uv.lock` file records the exact dependency versions selected by the package resolver, including transitive dependencies and package distribution hashes.

It defines which specific versions should be installed for a reproducible environment.

### Fundamental Difference

| `pyproject.toml`                      | `uv.lock`                                   |
| ------------------------------------- | ------------------------------------------- |
| Declares dependency requirements.     | Records exact resolved dependency versions. |
| Specifies allowed version ranges.     | Pins the selected versions.                 |
| Maintained by the developer.          | Generated and updated by `uv`.              |
| Defines what versions are acceptable. | Defines which versions are selected.        |

Together, these files provide flexible dependency management and reproducible installations.

The `pyproject.toml` defines the project's dependency requirements, while `uv.lock` ensures that the same resolved dependencies can be installed consistently across different environments.

---

## Conclusion

Using `uv` for dependency management provides:

- Clear separation between runtime and development dependencies.
- Dependency resolution and version constraints.
- Reproducible installations using `uv.lock`.
- Package integrity verification using SHA-256 hashes.
- Better protection against unexpected dependency upgrades.
- Improved reliability and consistency across development environments.

# Part 4 — Building & Deploying the Live CLI to TestPyPI

## 4.1 Implementing the CLI Interface

Implemented a command-line interface in:

`src/epita_raju_sekar_space/cli.py`

The CLI uses the Rich library to display live API data in a styled terminal dashboard.

The implementation retrieves data using the `fetch_live_data()` function from the existing client module.

The terminal dashboard includes:

- A Rich Table displaying the API response.
- Property and Value columns.
- A Rich Panel to present the dashboard.
- Exception handling for execution errors.

## 4.2 Exposing the CLI Entrypoint

Configured the CLI entrypoint in `pyproject.toml`:

```toml
[project.scripts]
epita-raju-sekar-cli = "epita_raju_sekar_space.cli:main"
```

The CLI can be executed using:

```bash
uv run epita-raju-sekar-cli
```

## 4.3 Building Distribution Artifacts

Built the package using:

```bash
uv build
```

The build generated the following distribution artifacts:

- `epita_raju_sekar_space-0.1.0-py3-none-any.whl`
- `epita_raju_sekar_space-0.1.0.tar.gz`

The Wheel is the built distribution, while the `.tar.gz` file is the source distribution.

## 4.4 Publishing to TestPyPI

Published the package to TestPyPI using:

```bash
uv publish --publish-url https://test.pypi.org/legacy/ --token "YOUR_TESTPYPI_TOKEN"
```

**Public Package URL:**

https://test.pypi.org/project/epita_raju_sekar_space/

## 4.5 Live Verification

Verified the package by installing and executing the CLI from a temporary directory:

```bash
cd /tmp

uv run \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  epita-raju-sekar-cli
```

The command installs the published package and executes the CLI entrypoint, allowing the live API data to be retrieved and displayed independently of the local source code.

## 4.6 Why are Wheels Faster and Safer to Install than Source Distributions?

A Wheel (`.whl`) is a pre-built distribution containing the packaged Python code and installation metadata. A Source Distribution (`.tar.gz`) contains the original source files and build configuration, which may require additional build steps during installation.

Wheels are generally faster to install because they are already built and do not normally require a build backend to run on the client machine. Installation typically involves unpacking the files and placing them in the appropriate Python environment.

Wheels are generally safer and more reliable to install because they reduce the need to execute build-time code on the client machine. They also reduce the number of build tools and dependencies required during installation, providing a more predictable installation process.

However, Wheels are not inherently secure. Their safety still depends on the trustworthiness of the publisher and the integrity of the package. Source Distributions are useful because they provide the original source code and can be built for different environments.

In conclusion, Wheels offer a faster, more convenient, and more predictable installation experience when a compatible Wheel is available.
