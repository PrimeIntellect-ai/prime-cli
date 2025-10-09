<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/40c36e38-c5bd-4c5a-9cb3-f7b902cd155d">
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/6414bc9b-126b-41ca-9307-9e982430cde8">
    <img alt="Prime Intellect" src="https://github.com/user-attachments/assets/6414bc9b-126b-41ca-9307-9e982430cde8" width="312" style="max-width: 100%;">
  </picture>
</p>

---

<h3 align="center">
Prime Intellect CLI & SDKs
</h3>

---

<div align="center">

[![PyPI version](https://img.shields.io/pypi/v/prime?cacheSeconds=60)](https://pypi.org/project/prime/)
[![Python versions](https://img.shields.io/pypi/pyversions/prime?cacheSeconds=60)](https://pypi.org/project/prime/)
[![Downloads](https://img.shields.io/pypi/dm/prime)](https://pypi.org/project/prime/)

Command line interface and SDKs for managing Prime Intellect GPU resources, sandboxes, and environments.
</div>

## Quick Start

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install prime
uv tool install prime

# Authenticate
prime login

# List available GPU resources
prime availability list
```

## Features

- **Environments** - Access hundreds of verified environments on our community hub
- **GPU Resource Management** - Query and filter available GPU resources
- **Pod Management** - Create, monitor, and terminate compute pods
- **Sandboxes** - Easily run AI-generated code in the cloud
- **SSH Access** - Direct SSH access to running pods
- **Team Support** - Manage resources across team environments

## Installation

### Using uv (recommended)

First, install uv if you haven't already:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then install prime:

```bash
uv tool install prime
```

### Using pip

```bash
pip install prime
```

### Sandboxes SDK Only

If you only need the sandboxes SDK (lightweight, ~50KB):

```bash
uv pip install prime-sandboxes
```

See [prime-sandboxes documentation](./packages/prime-sandboxes/) for SDK usage.

## Usage

### Configuration

#### API Key Setup

```bash
# Interactive mode (recommended - hides input)
prime config set-api-key

# Non-interactive mode (for automation)
prime config set-api-key YOUR_API_KEY

# Environment variable (most secure for scripts)
export PRIME_API_KEY="your-api-key-here"
```

#### Other Configuration

```bash
# Configure SSH key for pod access
prime config set-ssh-key-path

# View current configuration
prime config view
```

**Security Note**: When using non-interactive mode, the API key may be visible in your shell history. For enhanced security, use interactive mode or environment variables.

### GPU Resources

```bash
# List all available GPUs
prime availability list

# Filter by GPU type
prime availability list --gpu-type H100_80GB

# Show available GPU types
prime availability gpu-types
```

### Pod Management

```bash
# List your pods
prime pods list

# Create a pod
prime pods create
prime pods create --id <ID>     # With specific GPU config
prime pods create --name my-pod # With custom name

# Monitor and manage pods
prime pods status <pod-id>
prime pods terminate <pod-id>
prime pods ssh <pod-id>
```

### Team Management

```bash
# List teams
prime teams list

# Set team context
prime config set-team-id
```

## Development

```bash
# Clone the repository
git clone https://github.com/PrimeIntellect-ai/prime-cli
cd prime-cli

# Set up workspace (installs all packages in editable mode)
uv sync

# Install CLI globally in editable mode
uv tool install -e packages/prime

# Now you can use the CLI directly
prime --help

# Run tests
uv run pytest packages/prime/tests
uv run pytest packages/prime-sandboxes/tests
```

All packages (prime-core, prime-sandboxes, prime) are installed in editable mode. Changes to code are immediately reflected.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links

- [Website](https://primeintellect.ai)
- [Dashboard](https://app.primeintellect.ai)
- [API Docs](https://api.primeintellect.ai/docs)
- [Discord Community](https://discord.gg/primeintellect)
