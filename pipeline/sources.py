from typing import Any, Optional

import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources
from pipeline.config import (
    ROLES,
    BASE_URL,
    TABLE_NAME,
    PATH,
    NUMBER_OF_JOBS
)
from pipeline.transformers import add_search_tag

@dlt.source(name="jobicy")
def jobicy_source() -> Any:
    config: RESTAPIConfig = {
        
        "client": {
            "base_url": BASE_URL,
        },

        "resource_defaults": {
            "primary_key": "id",
            "write_disposition": "merge",
            "table_name": TABLE_NAME,
        },

        "resources": [
            {
                "name": f"{role['role'].replace(' ', '_')}_jobs",
                "endpoint": {
                    "path": PATH,
                    "params": {
                        "tag": role["tag"],
                        "count": NUMBER_OF_JOBS
                    }
                },
            }
            for role in ROLES
        ]
    }

    resources = [
        resource.add_map(add_search_tag(role["tag"]))
        for role, resource in zip(ROLES, rest_api_resources(config))
    ]

    yield from resources
