# How to run flows on Prefect Managed infrastructure

Link to Prefect documentation: https://docs.prefect.io/v3/how-to-guides/deployment_infra/managed

## Qick guide and setup

In the Hobby tier (free), you only have access to Prefect Managed work pools. This means that Prefect handles the infrastructure and code execution for you.

So, this is how I deployed my pipeline:

### 1. **Create a new work pool of type Prefect Managed in the UI or the CLI. **

I used the CLI:
- ``prefect work-pool create my-managed-pool --type prefect:managed``

You only need to do this once in the Hobby tier because you can have one work pool.

2. Create a deployment using the flow ``deploy`` method or ``prefect.yaml``.
   
How to deploy flows with Python: https://docs.prefect.io/v3/how-to-guides/deployments/deploy-via-python
How to define deployments with YAML: https://docs.prefect.io/v3/how-to-guides/deployments/prefect-yaml

I used python, the script ``managed-execution.py`` has everything I need for my deployment. 


