# Infrintia Overview

**Infrintia** is a decentralized GPU compute marketplace that connects users who need inference compute with hosts who have idle GPUs. Submit a job, and Infrintia's broker automatically routes it to the cheapest available host — results stream back in real time.

---

## How It Works

```
User submits job → Broker finds cheapest host → Host runs inference → Results stream back
```

1. **Users** submit inference jobs through the API or Python SDK, specifying a model and input
2. **The Broker** matches the job to the cheapest available host based on price, capacity, and model availability
3. **Hosts** pick up jobs, run inference on their GPUs, and stream results back token-by-token
4. **Credits** are reserved upfront and settled after job completion

---

## Key Features

| Feature | Description |
|---|---|
| **Credit Reservation** | Credits are held before job execution and released on completion, preventing overspend |
| **Multi-Backend Support** | Hosts can run HuggingFace Transformers, LangChain pipelines, or custom Worker backends |
| **Live Token Streaming** | Results stream back token-by-token via Server-Sent Events (SSE) for real-time output |
| **12% Platform Fee** | Transparent platform fee applied to each job; the rest goes to the host |
| **Auto-Routing** | The broker automatically selects the cheapest host that supports the requested model |

---

## Architecture

### Components

- **API Server** — REST API for users and hosts, handles auth, job submission, and streaming
- **Broker** — Matches submitted jobs to available hosts based on price and capacity
- **Host Agent** — Runs on GPU machines, registers with the platform, picks up and executes jobs
- **Credit System** — Manages user balances, reservations, and settlements

### Job Lifecycle

1. User calls `POST /run/model` with model name and input
2. Broker reserves credits from user balance
3. Broker assigns job to the cheapest available host
4. Host pulls the job via `POST /hosts/next-job`
5. Host streams results back via the API
6. On completion, credits are settled and the host is paid

---

## Supported Backends

| Backend | Description |
|---|---|
| **HuggingFace** | Run any HuggingFace Transformers model directly |
| **LangChain** | Execute LangChain chains and agents |
| **Worker** | Custom inference backend — bring your own model server |

---

## Next Steps

- [Getting Started](getting-started.md) — Install the SDK and run your first job
- [API Reference](api-reference.md) — Full endpoint documentation
- [SDK Guide](sdk.md) — Python SDK reference
- [Hosting Guide](hosting.md) — Register as a GPU host and start earning
