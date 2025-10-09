# Prime Intellect - CLI & SDKs

Monorepo for Prime Intellect's Python packages: CLI tools and SDKs for managing GPU compute resources, sandboxes, and inference.

## Packages

### [`prime`](./packages/prime/)
[![PyPI](https://img.shields.io/pypi/v/prime)](https://pypi.org/project/prime/)

**Command-line tool + SDK for managing GPU infrastructure on Prime Intellect.**

**Main Features:**
- **Authentication** - Secure login and API key management
- **GPU Pods** - Deploy, manage, and SSH into GPU instances
- **Sandboxes** - Remote code execution environments
- **Inference** - OpenAI-compatible chat completions
- **Availability** - Browse available GPU types and configurations

```bash
uv tool install prime

# Get started
prime login
prime availability list --gpu H100
prime pods create --gpu A100 --count 2
prime sandbox create --image python:3.11
```

**Use this for the complete Prime Intellect experience** - full CLI + Python SDK.

[→ Full Documentation](./packages/prime/)

---

### [`prime-sandboxes`](./packages/prime-sandboxes/)
[![PyPI](https://img.shields.io/pypi/v/prime-sandboxes)](https://pypi.org/project/prime-sandboxes/)

**Lightweight standalone SDK for managing remote code execution environments (sandboxes).**

```bash
uv pip install prime-sandboxes
```

```python
from prime_sandboxes import APIClient, SandboxClient, CreateSandboxRequest

client = APIClient(api_key="...")
sandbox = SandboxClient(client)
```

**Use this if you only need sandboxes** - minimal dependencies, ~50KB installed.

[→ Full Documentation](./packages/prime-sandboxes/)

---

## Quick Start

### For CLI Users

```bash
# Install
uv tool install prime

# Authenticate
prime login

# Browse available GPUs
prime availability list --gpu H100

# Deploy a GPU pod
prime pods create --gpu A100 --count 1

# Create a remote sandbox
prime sandbox create --image python:3.11

# Run inference
prime inference chat "Explain quantum computing"
```

### For Sandbox SDK Users

```python
# Lightweight - install only sandboxes SDK
uv pip install prime-sandboxes

from prime_sandboxes import APIClient, SandboxClient, CreateSandboxRequest

client = APIClient(api_key="your-api-key")
sandbox_client = SandboxClient(client)

sandbox = sandbox_client.create(CreateSandboxRequest(
    name="my-sandbox",
    docker_image="python:3.11-slim",
    cpu_cores=2,
    memory_gb=4,
))

sandbox_client.wait_for_creation(sandbox.id)
result = sandbox_client.execute_command(sandbox.id, "python --version")
print(result.stdout)
```

## Repository Structure

```
prime-cli/
├── packages/
│   ├── prime/               # Full CLI + all SDKs
│   ├── prime-sandboxes/     # Standalone sandboxes SDK
│   └── prime-core/          # Shared HTTP client & config (internal, not published)
├── examples/                # Example scripts
├── .github/workflows/       # CI/CD
├── pyproject.toml          # uv workspace configuration
└── README.md               # This file
```

### Package Architecture

- **`prime`** - Published CLI + full SDK
  - Depends on both `prime-core` and `prime-sandboxes`
  - Published with bundled core functionality

- **`prime-sandboxes`** - Published standalone SDK
  - Depends on `prime-core` during development
  - Published with bundled core functionality

- **`prime-core`** - Internal package containing shared `APIClient` and `Config` code
  - Single source of truth during development
  - Used via uv workspace (not published to PyPI)
  - Both `prime-sandboxes` and `prime` reference it locally

## Documentation

- [prime CLI Docs](./packages/prime/README.md)
- [prime-sandboxes SDK Docs](./packages/prime-sandboxes/README.md)
- [Examples](./examples/)

## Contributing

Contributions welcome! This is a monorepo with independent packages managed via uv workspace.

### Quick Start for Development

```bash
# 1. Clone and install
git clone https://github.com/PrimeIntellect-ai/prime-cli
cd prime-cli
uv sync

# 2. You're ready! Run examples:
uv run python examples/sandbox_demo.py

# 3. Use the CLI:
uv run prime --help

# 4. Run tests:
uv run pytest packages/prime-sandboxes/tests
```

That's it! All packages are installed in editable mode. Edit any code and changes are immediately available.

### Development Setup Options

**Option 1: Root-level development (recommended)**

Work on all packages with a unified environment:

```bash
# Install all packages + dev dependencies at root
uv sync --all-extras

# Now you can work on any package - they all share prime-core
# Run tests for specific packages:
uv run pytest packages/prime-sandboxes/tests
uv run pytest packages/prime/tests

# Run examples
uv run python examples/sandbox_demo.py

# Use the CLI directly
uv run prime --help
```

**Option 2: Package-specific development**

Work on individual packages independently:

```bash
# For prime-sandboxes
cd packages/prime-sandboxes
uv sync --all-extras
uv run pytest

# For prime CLI
cd packages/prime
uv sync --all-extras
uv run pytest
uv run prime --help
```

### Virtual Environment Management

- **Root venv** (`uv sync` at root): Includes all packages (prime-core, prime-sandboxes, prime) in one environment. Best for general development and cross-package work.

- **Package venvs** (`uv sync` in package dir): Each package gets its own venv with only its dependencies. Best for isolated testing and package-specific work.

- **Switching contexts**: Just `cd` to the directory you want and run `uv run <command>`. uv automatically uses the correct venv.

### Running Examples Locally

```bash
# From root (using root venv)
uv run python examples/sandbox_demo.py

# From sandboxes package (using package venv)
cd packages/prime-sandboxes
uv run python ../../examples/sandbox_demo.py
```

### Building for PyPI

When building packages for publication to PyPI, use the provided build scripts that handle bundling `prime-core`:

```bash
# Build prime-sandboxes for PyPI
cd packages/prime-sandboxes
./build_for_pypi.sh

# Build prime for PyPI
cd packages/prime
./build_for_pypi.sh
```

**How it works:**
- **Development**: Workspace uses `prime-core` as shared dependency (single source of truth)
- **Distribution**: Build scripts bundle `prime-core` code into wheels using hatchling's `force-include`
- **Result**: Published packages are self-contained with no `prime-core` dependency

The build scripts:
1. Temporarily remove `prime-core` from dependencies
2. Build wheel with `uv build` (hatchling auto-bundles code via `force-include`)
3. Restore original `pyproject.toml`

This approach follows industry standards (similar to NumPy, SciPy) and is fully uv-aligned.

## License

MIT License - see [LICENSE](./LICENSE) file for details.

## Links

- [Website](https://primeintellect.ai)
- [Dashboard](https://app.primeintellect.ai)
- [API Docs](https://api.primeintellect.ai/docs)
- [Discord Community](https://discord.gg/primeintellect)
