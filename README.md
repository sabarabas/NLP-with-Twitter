# Tomatoes

## Project structure

This projects follows a directory structure similar to the [cookiecutter data science framework](https://cookiecutter-data-science.drivendata.org/).

## Setup project

To quickly setup the environment, we'll use [uv](https://docs.astral.sh/uv/), an extremely fast state-of-the-art Python package and project manager, written in Rust.

Install it with:

```bash
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# or Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then, install the Python 3.12 with:
```bash
uv python install 3.12
```

Create and activate the environment with:
```bash
uv venv
source .venv/bin/activate # macOS / Linux
```

Finally, install the packages with:
```bash
uv pip install -r requirements.txt
```