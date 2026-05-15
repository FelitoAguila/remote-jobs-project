# How to run flows on Prefect Managed infrastructure

Link to Prefect documentation: https://docs.prefect.io/v3/how-to-guides/deployment_infra/managed

## Qick guide and setup

In the Hobby tier (free), you only have access to Prefect Managed work pools. This means that Prefect handles the infrastructure and code execution for you.

So, this is how I deployed my pipeline:

1. Create a new work pool of type Prefect Managed in the UI or the CLI. I used the CLI:

- ``prefect work-pool create my-managed-pool --type prefect:managed``

Now, you need to create a deployment. You can do it using the flow ``deploy`` method as in ``managed-execution.py``. 


