from prefect import flow, task
import dlt
from pipeline.sources import jobicy_source
from prefect_gcp import GcpCredentials


def make_bq_destination():
    #get service account info
    gcp = GcpCredentials.load("gcp-creds")
    creds = gcp.service_account_info.get_secret_value() or {}
    #get project id
    project = creds.get("project_id")
    #create a bigquery destination
    return dlt.destinations.bigquery(credentials=creds, project_id=project)


@task(log_prints=True)
def load_jobicy_data(bq_dest: dlt.destinations.bigquery):
    pipeline = dlt.pipeline(
        pipeline_name="remote_jobs",
        destination=bq_dest,
        dataset_name="remote_jobs_data",
    )

    load_info = pipeline.run(jobicy_source())
    print(load_info)
    return load_info

@flow(log_prints=True, name="remote-jobs-pipeline")
def main():
    #create bigquery destination
    bq_dest = make_bq_destination()
    remote_works_workflow = load_jobicy_data(bq_dest)
    return remote_works_workflow

if __name__ == "__main__":
    main()