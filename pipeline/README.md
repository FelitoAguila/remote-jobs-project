# How to run flows on Prefect Managed infrastructure

Link to Prefect documentation: https://docs.prefect.io/v3/how-to-guides/deployment_infra/managed

## Qick guide and setup

In the Hobby tier (free), you only have access to Prefect Managed work pools. This means that Prefect handles the infrastructure and code execution for you.

So, this is how I deployed my pipeline:

### 1. Create a new work pool of type Prefect Managed in the UI or the CLI. 

I used the CLI:
- ``prefect work-pool create my-managed-pool --type prefect:managed``

You only need to do this once in the Hobby tier because you can have one work pool.

### 2. Create a deployment using the flow ``deploy`` method or ``prefect.yaml``.
   
I used python, the script ``managed-execution.py`` has all the instructions that I want for this pipeline. So, I need to run it to create the deployment. 

Before running the script, verify that you are talking to Prefect Cloud. You should be authenticated to your workspace. To check it, run in your terminal:
- ``prefect profile ls``: list and see which is active
- ``prefect profile use prefect-cloud``: switch to prefect cloud.

Then you can run your python script in your terminal:
- ``python managed-execution.py``

That should make it, at this point you can see the deployment from the UI, run it, etc.

Additional resources:
- **How to deploy flows with Python**: https://docs.prefect.io/v3/how-to-guides/deployments/deploy-via-python
- **How to define deployments with YAML**: https://docs.prefect.io/v3/how-to-guides/deployments/prefect-yaml


## Next steps

Now your deployment is ready. You can modify and run ``managed-execution.py`` to add/edit/remove dependencies, schedule, parameters, etc. 