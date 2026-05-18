Architecture
============

Infrintia has three runtime surfaces: the broker, the host agent, and the SDK.

Broker
------

The FastAPI broker owns user accounts, API keys, credit balances, model
metadata, host registration, job state, streaming, metrics, and billing.
Business logic lives in ``app.marketplace`` and route modules under
``app.routes`` keep the HTTP surface thin.

Job execution follows this flow:

1. A user submits a model or equation job.
2. The broker reserves estimated credits and selects the cheapest compatible
   idle host.
3. The host claims the job with its host token.
4. The host streams chunks back to the broker.
5. The broker relays chunks to the user through Server-Sent Events.
6. Completion captures the final cost and refunds excess reserved credits.

Host Agent
----------

The host agent detects CUDA, Apple MPS, or CPU capabilities and registers the
models it can serve. ``host_agent.runtime.HostRuntime`` owns backend selection
and delegates execution to HuggingFace, LangChain, or subprocess-isolated worker
backends.

Worker isolation is handled by ``host_agent.worker_manager.WorkerManager``. Each
model can run in its own virtual environment, which lets hosts keep model
dependencies isolated and optionally warm between jobs.

SDK
---

``sdk.compute.ComputeClient`` and ``sdk.compute.AsyncComputeClient`` wrap broker
HTTP endpoints for user-facing workflows: credits, key rotation, model listing,
job submission, polling, cancellation, and token streaming.

Deployment
----------

The production shape targets Google Cloud Run for the broker, Cloud SQL for
PostgreSQL, Memorystore for Redis, Artifact Registry for images, and Secret
Manager for sensitive configuration.
