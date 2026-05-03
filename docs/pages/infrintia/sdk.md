# Infrintia Python SDK

The Infrintia SDK provides `ComputeClient` and `AsyncComputeClient` for interacting with the Infrintia GPU compute marketplace from Python.

---

## Installation

```bash
pip install infrintia
```

---

## ComputeClient

Synchronous client for the Infrintia API.

### Initialization

```python
from infrintia import ComputeClient

client = ComputeClient(
    base_url="https://api.infrintia.crossgl.net",
    username="alice",
    password="secure-password-123"
)
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `base_url` | str | Yes | Infrintia API base URL |
| `username` | str | No | Username for authentication |
| `password` | str | No | Password for authentication |
| `api_key` | str | No | API key (alternative to username/password) |
| `timeout` | int | No | Request timeout in seconds (default: `60`) |

### Methods

#### `create_user(username, email, password)`

Create a new user account.

```python
user = client.create_user(
    username="alice",
    email="alice@example.com",
    password="secure-password-123"
)
```

**Returns:** `dict` with `user_id`, `username`, `email`, `credits`, `created_at`.

#### `get_me()`

Get the authenticated user's profile.

```python
profile = client.get_me()
print(f"Credits: {profile['credits']}")
```

#### `list_models()`

List all available models on the marketplace.

```python
models = client.list_models()
for m in models:
    print(f"{m['name']} — {m['min_price_per_token']} credits/token")
```

**Returns:** `list[dict]` with model metadata.

#### `list_hosts()`

List all active GPU hosts.

```python
hosts = client.list_hosts()
for h in hosts:
    print(f"{h['host_id']}: {h['gpu']} ({h['status']})")
```

#### `run_model(model, input_text, max_tokens=128, temperature=0.7)`

Submit an inference job.

```python
job = client.run_model(
    model="meta-llama/Llama-3-8B-Instruct",
    input_text="What is gravity?",
    max_tokens=256,
    temperature=0.7
)
print(f"Job {job['job_id']} — status: {job['status']}")
```

**Returns:** `dict` with `job_id`, `status`, `model`, `credits_reserved`.

#### `get_job(job_id)`

Get the status and details of a specific job.

```python
status = client.get_job("job_def456")
```

#### `list_jobs(status=None, limit=20, offset=0)`

List jobs for the authenticated user.

```python
jobs = client.list_jobs(status="completed", limit=10)
```

#### `stream_job(job_id)`

Stream results from a running job. Yields tokens as they are generated.

```python
for token in client.stream_job("job_def456"):
    print(token, end="", flush=True)
```

**Yields:** `str` — individual tokens.

#### `get_metrics()`

Get platform-wide metrics.

```python
metrics = client.get_metrics()
print(f"Active hosts: {metrics['active_hosts']}")
```

---

## AsyncComputeClient

Async version of ComputeClient for use with `asyncio`.

### Initialization

```python
from infrintia import AsyncComputeClient

client = AsyncComputeClient(
    base_url="https://api.infrintia.crossgl.net",
    username="alice",
    password="secure-password-123"
)
```

### Async Methods

All methods mirror `ComputeClient` but are `async`:

```python
import asyncio
from infrintia import AsyncComputeClient

async def main():
    client = AsyncComputeClient(
        base_url="https://api.infrintia.crossgl.net",
        username="alice",
        password="secure-password-123"
    )

    job = await client.run_model(
        model="meta-llama/Llama-3-8B-Instruct",
        input_text="Write a poem about silicon.",
        max_tokens=128
    )

    async for token in client.stream_job(job["job_id"]):
        print(token, end="", flush=True)
    print()

asyncio.run(main())
```

### Available Async Methods

| Method | Description |
|---|---|
| `await create_user(...)` | Create user account |
| `await get_me()` | Get authenticated user profile |
| `await list_models()` | List available models |
| `await list_hosts()` | List GPU hosts |
| `await run_model(...)` | Submit inference job |
| `await get_job(job_id)` | Get job status |
| `await list_jobs(...)` | List user's jobs |
| `async for token in stream_job(job_id)` | Stream job results |
| `await get_metrics()` | Get platform metrics |
