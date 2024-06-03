def format_imaging_study_response(data):
    try:
        def get_nested_value(d, keys, default=None):
            for key in keys:
                if isinstance(d, list) and d:
                    d = d[0]
                if isinstance(d, dict):
                    d = d.get(key, default)
                else:
                    return default
            return d

        id = data.get("id")
        status = data.get("status")
        started = data.get("started")
        number_of_series = data.get("numberOfSeries")
        number_of_instances = data.get("numberOfInstances")
        procedure_code = get_nested_value(data, ["procedureCode", 0, "text"])
        location = get_nested_value(data, ["location", "display"])
        series_modality = get_nested_value(data, ["series", 0, "modality", "display"])
        series_body_site = get_nested_value(data, ["series", 0, "bodySite", "display"])
        instance_title = get_nested_value(data, ["series", 0, "instance", 0, "title"])

        fields = (id, status, started, number_of_series, number_of_instances, procedure_code, location,
                  series_modality, series_body_site, instance_title)

        return fields

    except Exception as e:
        print("Error occurred in format_imaging_study_response: ", e)
