from typing import Dict, Any

def add_search_tag(tag: str):
    def mapper(record: dict) -> dict:
        record = dict(record)
        record["search_tag"] = tag
        return record
    return mapper