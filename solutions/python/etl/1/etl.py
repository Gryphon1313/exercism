def transform(legacy_data: dict) -> dict:
    return {value.lower(): key for key, values in legacy_data.items() for value in values}
