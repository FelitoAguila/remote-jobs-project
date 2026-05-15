from prefect import flow
from prefect.schedules import Cron

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/FelitoAguila/remote-jobs-project.git",
        entrypoint="pipeline/cloud_prefect_pipeline.py:main",
    ).deploy(
        name="remote-jobs-flow",
        work_pool_name="my-managed-pool",
        job_variables={
            "pip_packages": [
                "dlt[bigquery]>=1.0", 
                "prefect-gcp==0.6.2", 
                "google-cloud-bigquery"
            ]
        },
        # === Schedules ===
        # This will run the flow every day at 00:00 and 12:30 in the America/Argentina/Buenos_Aires timezone.
        schedules=[
            Cron("0 0 * * *",   timezone="America/Argentina/Buenos_Aires"),   # 00:00
            Cron("30 12 * * *", timezone="America/Argentina/Buenos_Aires"),  # 12:30
        ]
    )