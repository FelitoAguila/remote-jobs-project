import dlt
from pipeline.sources import jobicy_source

def load_jobicy_data(destination: str) -> None:
    pipeline = dlt.pipeline(
        pipeline_name="remote_jobs",
        destination=destination,
        dataset_name="remote_jobs_data",
    )

    load_info = pipeline.run(jobicy_source())
    print(load_info) 