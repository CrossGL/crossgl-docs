Broker API
==========

The broker exposes FastAPI routes grouped by responsibility. Local development
serves OpenAPI at ``/docs`` and ``/openapi.json``.

Users and API keys
------------------

``POST /users``
   Create a user with optional initial credits.

``GET /users/me``
   Return the authenticated user profile.

``POST /users/credits``
   Add credits to the authenticated account.

``POST /users/rotate-key``
   Rotate the default API key and return the new key.

Jobs
----

``POST /run/model``
   Submit a model inference job.

``POST /run/equation``
   Submit a structured equation job.

``GET /jobs/{job_id}``
   Read job status, metadata, and output when available.

``GET /jobs/{job_id}/stream``
   Stream Server-Sent Events for tokens and terminal job state.

``POST /jobs/{job_id}/cancel``
   Cancel a queued or running job.

Hosts
-----

``POST /hosts/register``
   Register a host and its model capabilities.

``POST /hosts/heartbeat``
   Keep a host online and update its status.

``POST /hosts/next-job``
   Atomically claim the next compatible queued job.

``POST /hosts/jobs/{job_id}/chunk``
   Publish a generated token or text chunk.

``POST /hosts/complete-job/{job_id}``
   Complete a job and finalize billing.

``POST /hosts/fail-job/{job_id}``
   Fail a job and refund reserved credits.

Catalog and discovery
---------------------

``GET /models``
   List registered model specifications.

``GET /models/{model_name}``
   Inspect a single registered model.

``GET /hosts``
   Discover public host capacity and filter by model or status.

Operations
----------

``GET /metrics``
   Prometheus metrics for jobs, hosts, runtime, and cost.

``/admin/*``
   Admin-only endpoints protected by ``x-admin-key``.
