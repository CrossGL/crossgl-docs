# Infrintia API Reference

Base URL: `https://api.infrintia.crossgl.net`

Authenticated endpoints require a `Bearer` token or Basic Auth credentials in the `Authorization` header.

---

## Public Endpoints

These endpoints require no authentication.

### GET /

Platform information and version.

**Response `200 OK`**

```json
{
  "name": "Infrintia Compute Marketplace",
  "version": "1.0.0",
  "docs": "https://crossgl.github.io/crossgl-docs/pages/infrintia/overview/"
}
```

### GET /health

Health check.

**Response `200 OK`**

```json
{
  "status": "healthy",
  "active_hosts": 24,
  "queued_jobs": 3
}
```

### GET /models

List all available models on the marketplace.

**Response `200 OK`**

```json
{
  "models": [
    {
      "name": "meta-llama/Llama-3-8B-Instruct",
      "available_hosts": 8,
      "min_price_per_token": 0.0001,
      "max_tokens": 4096
    }
  ]
}
```

### GET /hosts

List all registered hosts and their status.

**Response `200 OK`**

```json
{
  "hosts": [
    {
      "host_id": "host_xyz",
      "gpu": "NVIDIA A100 80GB",
      "status": "active",
      "models": ["meta-llama/Llama-3-8B-Instruct"],
      "price_per_token": 0.00012,
      "backend": "huggingface"
    }
  ]
}
```

### GET /metrics

Platform-wide metrics.

**Response `200 OK`**

```json
{
  "total_jobs_completed": 152340,
  "active_hosts": 24,
  "total_users": 1830,
  "avg_job_latency_ms": 3200
}
```

---

## User Endpoints

### POST /users

Create a new user account.

**Request Body:**

```json
{
  "username": "alice",
  "email": "alice@example.com",
  "password": "secure-password-123"
}
```

**Response `201 Created`**

```json
{
  "user_id": "usr_abc123",
  "username": "alice",
  "email": "alice@example.com",
  "credits": 100.0,
  "created_at": "2025-06-01T12:00:00Z"
}
```

### GET /users/me

Get the authenticated user's profile and credit balance.

**Authentication:** Required

**Response `200 OK`**

```json
{
  "user_id": "usr_abc123",
  "username": "alice",
  "credits": 87.50,
  "total_jobs": 42,
  "created_at": "2025-06-01T12:00:00Z"
}
```

### POST /run/model

Submit an inference job.

**Authentication:** Required

**Request Body:**

```json
{
  "model": "meta-llama/Llama-3-8B-Instruct",
  "input_text": "Explain quantum computing.",
  "max_tokens": 256,
  "temperature": 0.7
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `model` | string | Yes | Model identifier (from `GET /models`) |
| `input_text` | string | Yes | Input prompt |
| `max_tokens` | integer | No | Maximum tokens to generate (default: `128`) |
| `temperature` | float | No | Sampling temperature (default: `0.7`) |

**Response `202 Accepted`**

```json
{
  "job_id": "job_def456",
  "status": "queued",
  "model": "meta-llama/Llama-3-8B-Instruct",
  "credits_reserved": 2.56,
  "created_at": "2025-06-01T12:05:00Z"
}
```

### GET /jobs

List the authenticated user's jobs.

**Authentication:** Required

**Query Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `status` | string | Filter by status: `queued`, `running`, `completed`, `failed` |
| `limit` | integer | Results per page (default: `20`) |
| `offset` | integer | Pagination offset (default: `0`) |

**Response `200 OK`**

```json
{
  "jobs": [
    {
      "job_id": "job_def456",
      "model": "meta-llama/Llama-3-8B-Instruct",
      "status": "completed",
      "credits_used": 1.92,
      "created_at": "2025-06-01T12:05:00Z"
    }
  ],
  "total": 42
}
```

### GET /jobs/{id}/stream

Stream job results via Server-Sent Events (SSE).

**Authentication:** Required

**Response:** `text/event-stream`

```
data: {"token": "Quantum"}
data: {"token": " computing"}
data: {"token": " is"}
data: {"token": " a"}
data: [DONE]
```

Each event contains a single generated token. The stream ends with `[DONE]`.

---

## Host Endpoints

### POST /hosts/register

Register a new GPU host on the marketplace.

**Request Body:**

```json
{
  "gpu": "NVIDIA A100 80GB",
  "models": ["meta-llama/Llama-3-8B-Instruct"],
  "price_per_token": 0.00012,
  "backend": "huggingface",
  "endpoint_url": "https://my-gpu-host.example.com/infer"
}
```

**Response `201 Created`**

```json
{
  "host_id": "host_xyz",
  "status": "active",
  "api_key": "hk_live_xxxxxxxx"
}
```

### POST /hosts/heartbeat

Send a heartbeat to confirm the host is still active. Should be called every 30 seconds.

**Authentication:** Required (Host API key)

**Request Body:**

```json
{
  "host_id": "host_xyz",
  "gpu_utilization": 0.45,
  "available_models": ["meta-llama/Llama-3-8B-Instruct"]
}
```

**Response `200 OK`**

```json
{
  "status": "acknowledged"
}
```

### POST /hosts/next-job

Poll for the next available job assigned to this host.

**Authentication:** Required (Host API key)

**Request Body:**

```json
{
  "host_id": "host_xyz"
}
```

**Response `200 OK`** (job available)

```json
{
  "job_id": "job_def456",
  "model": "meta-llama/Llama-3-8B-Instruct",
  "input_text": "Explain quantum computing.",
  "max_tokens": 256,
  "temperature": 0.7
}
```

**Response `204 No Content`** — No jobs available.

---

## Admin Endpoints

These endpoints require admin-level authentication.

### GET /admin/users

List all users on the platform.

**Response `200 OK`**

```json
{
  "users": [
    {
      "user_id": "usr_abc123",
      "username": "alice",
      "credits": 87.50,
      "total_jobs": 42,
      "created_at": "2025-06-01T12:00:00Z"
    }
  ],
  "total": 1830
}
```

### GET /admin/hosts

List all registered hosts.

**Response `200 OK`**

```json
{
  "hosts": [
    {
      "host_id": "host_xyz",
      "gpu": "NVIDIA A100 80GB",
      "status": "active",
      "total_jobs_completed": 1240,
      "total_earnings": 148.80,
      "last_heartbeat": "2025-06-01T12:10:00Z"
    }
  ],
  "total": 24
}
```
