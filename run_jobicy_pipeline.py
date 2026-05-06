from pipeline import load
from pipeline.config import BIGQUERY_DESTINATION

if __name__ == "__main__":
    load.load_jobicy_data(BIGQUERY_DESTINATION)