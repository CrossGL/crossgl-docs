Host Agent
==========

GPU owners run the host agent to sell compute capacity to the broker.

Start an agent against a local broker:

.. code-block:: bash

   BROKER_URL=http://127.0.0.1:8000 python -m host_agent.agent

Start against a deployed broker with a pre-issued token:

.. code-block:: bash

   BROKER_URL=https://broker.example.com \
   HOST_TOKEN=host-token-value \
   python -m host_agent.agent

Registration
------------

If ``HOST_TOKEN`` is unset, the agent:

1. Detects CUDA, Apple MPS, or CPU capabilities.
2. Builds a supported model list from available memory.
3. Submits a host registration payload.
4. Stores the returned token in memory for the current process.

Generate a registration payload without starting the polling loop:

.. code-block:: bash

   python -m host_agent.print_gpu_registration

Execution backends
------------------

``huggingface``
   Runs Transformers directly in the host process.

``langchain``
   Uses LangChain's HuggingFace pipeline integration.

``worker``
   Runs models through subprocess-managed virtual environments for dependency
   isolation.

Operational settings
--------------------

``POLL_INTERVAL``
   Seconds between heartbeat and job polling iterations.

``PRELOAD_MODELS``
   Comma-separated model names to warm before the polling loop starts.

``HF_HOME``
   Defaults to ``./hf_cache`` when backends load HuggingFace models.
