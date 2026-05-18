Python SDK
==========

The SDK exposes synchronous and asynchronous clients over the broker API.

Synchronous client
------------------

.. code-block:: python

   from sdk.compute import ComputeClient

   client = ComputeClient("http://127.0.0.1:8000", api_key="YOUR_API_KEY")
   models = client.list_models()

   job = client.run_model(
       model_name="gpt2",
       prompt="Explain shader compilation in one paragraph.",
       estimated_runtime_seconds=30,
   )

   final = client.wait_for_job(job["job_id"])

Streaming tokens
----------------

.. code-block:: python

   for event in client.stream_job(job["job_id"]):
       if event["type"] == "token":
           print(event["text"], end="", flush=True)
       elif event["type"] in {"completed", "failed", "cancelled"}:
           print(event)

Asynchronous client
-------------------

.. code-block:: python

   import asyncio
   from sdk.compute import AsyncComputeClient

   async def main() -> None:
       client = AsyncComputeClient("http://127.0.0.1:8000", api_key="YOUR_API_KEY")
       try:
           job = await client.run_model("gpt2", "CrossGL is")
           print(await client.get_job(job["job_id"]))
       finally:
           await client.close()

   asyncio.run(main())

Client responsibilities
-----------------------

The clients handle request headers, JSON payloads, job polling, cancellation,
model catalog reads, and SSE parsing. They intentionally leave retries,
application-level prompt management, and output persistence to calling code.
