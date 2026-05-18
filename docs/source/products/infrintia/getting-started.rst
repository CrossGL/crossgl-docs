Getting Started
===============

Install the Infrintia package from a local checkout:

.. code-block:: bash

   git clone https://github.com/CrossGL/infrintia.git
   cd infrintia
   pip install -e ".[dev]"
   cp .env.example .env

Run the broker locally:

.. code-block:: bash

   python run_server.py

Start a host agent in another terminal. Without ``HOST_TOKEN``, the agent
auto-detects local hardware and registers itself with the broker.

.. code-block:: bash

   python -m host_agent.agent

Create a user and keep the returned API key:

.. code-block:: bash

   curl -s -X POST http://127.0.0.1:8000/users \
     -H "Content-Type: application/json" \
     -d '{"name":"researcher","initial_credits":20}'

Submit inference through the SDK:

.. code-block:: python

   from sdk.compute import ComputeClient

   client = ComputeClient("http://127.0.0.1:8000", api_key="YOUR_API_KEY")
   job = client.run_model(
       model_name="gpt2",
       prompt="Quantum tunneling is",
       estimated_runtime_seconds=60,
       max_new_tokens=80,
       backend="worker",
   )

   for event in client.stream_job(job["job_id"]):
       if event["type"] == "token":
           print(event["text"], end="", flush=True)

Core environment variables
--------------------------

``DATABASE_URL``
   SQLAlchemy async database URL. SQLite is used by default for development.

``REDIS_URL`` and ``REDIS_ENABLED``
   Enable Redis-backed caching, streaming, and rate limiting for distributed
   broker deployments.

``ADMIN_API_KEY``
   Required for admin endpoints such as forced job failure and host bans.

``BROKER_URL`` and ``HOST_TOKEN``
   Configure host agents that connect to a local or deployed broker.
