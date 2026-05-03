# Hosting Guide

Earn credits by registering your GPU as a host on the Infrintia compute marketplace. When users submit inference jobs, the broker routes them to available hosts — you run the computation and get paid.

---

## Requirements

- A machine with one or more NVIDIA GPUs (CUDA-capable)
- Python 3.9+
- Stable internet connection
- Sufficient VRAM for the models you want to serve

---

## Register as a Host

### 1. Install the Infrintia host agent

```bash
pip install infrintia[host]
```

### 2. Register your machine

```python
from infrintia.host import HostAgent

agent = HostAgent(
    api_url="https://api.infrintia.crossgl.net",
    gpu="NVIDIA A100 80GB",
    models=["meta-llama/Llama-3-8B-Instruct"],
    price_per_token=0.00012,
    backend="huggingface"
)

registration = agent.register()
print(f"Host ID: {registration['host_id']}")
print(f"API Key: {registration['api_key']}")
```

The registration response includes a `host_id` and `api_key` — store the API key securely. You'll need it for all subsequent host operations.

### 3. Start serving

```python
agent.serve()
```

This starts an event loop that:

1. Sends heartbeats every 30 seconds
2. Polls for new jobs via `POST /hosts/next-job`
3. Runs inference on assigned jobs
4. Streams results back to the platform

---

## Auto-Detection

The host agent automatically detects:

- **GPU model and VRAM** via `nvidia-smi`
- **Available models** based on installed backends and cached weights
- **System resources** (CPU, RAM, disk) for capacity reporting

You can override any auto-detected value in the `HostAgent` constructor.

---

## Backends

Choose the backend that matches your setup:

### HuggingFace (default)

Runs models using HuggingFace Transformers. Models are downloaded and cached automatically.

```python
agent = HostAgent(
    api_url="https://api.infrintia.crossgl.net",
    backend="huggingface",
    models=["meta-llama/Llama-3-8B-Instruct"],
    price_per_token=0.00012
)
```

### LangChain

Execute LangChain chains and agents.

```python
agent = HostAgent(
    api_url="https://api.infrintia.crossgl.net",
    backend="langchain",
    models=["custom-chain-v1"],
    price_per_token=0.0002
)
```

### Worker (Custom)

Point to your own inference server. Useful for custom models, quantized weights, or vLLM/TGI backends.

```python
agent = HostAgent(
    api_url="https://api.infrintia.crossgl.net",
    backend="worker",
    endpoint_url="http://localhost:8000/generate",
    models=["my-custom-model"],
    price_per_token=0.00015
)
```

---

## Earnings

- Hosts are paid per token generated, at the `price_per_token` they set during registration
- The platform takes a **12% fee**; the remaining 88% is credited to the host
- Earnings accumulate in the host's credit balance and can be withdrawn

### Example

If you set `price_per_token=0.00012` and generate 1,000,000 tokens:

- Gross: 120.00 credits
- Platform fee (12%): 14.40 credits
- Net earnings: **105.60 credits**

---

## Monitoring

Check your host's status and earnings:

```python
from infrintia import ComputeClient

client = ComputeClient(
    base_url="https://api.infrintia.crossgl.net",
    api_key="hk_live_xxxxxxxx"
)

hosts = client.list_hosts()
for h in hosts:
    if h["host_id"] == "host_xyz":
        print(f"Status: {h['status']}")
        print(f"Jobs completed: {h['total_jobs_completed']}")
```

---

## Best Practices

- **Set competitive pricing** — check `GET /hosts` to see current market rates
- **Keep your host online** — missed heartbeats mark your host as inactive
- **Use fast storage** — model loading speed affects job pickup latency
- **Monitor GPU utilization** — the heartbeat reports utilization to the broker for smart routing
