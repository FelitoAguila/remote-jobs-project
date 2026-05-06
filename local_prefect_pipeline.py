from prefect import flow, task
import dlt
from pipeline.sources import jobicy_source
from pipeline.config import BIGQUERY_DESTINATION

@task(log_prints=True)
def load_jobicy_data(destination: str):
    pipeline = dlt.pipeline(
        pipeline_name="remote_jobs",
        destination=destination,
        dataset_name="remote_jobs_data",
    )

    load_info = pipeline.run(jobicy_source())
    print(load_info)
    return load_info

@flow(log_prints=True, name="remote-jobs-pipeline")
def main(destination: str = BIGQUERY_DESTINATION):

    remote_works_workflow = load_jobicy_data(destination)
    return remote_works_workflow

if __name__ == "__main__":
    main.serve()