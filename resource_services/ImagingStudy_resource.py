def format_imaging_study_response(data):
    try:
        id = data.get("id")
        status = data.get("status")
        started = data.get("started")
        number_of_series = data.get("numberOfSeries")
        number_of_instances = data.get("numberOfInstances")
        procedure_code = data.get("procedureCode", [{}])[0].get("text", "")
        location = data.get("location", {}).get("display", "")
        series_modality = data.get("series", [{}])[0].get("modality", {}).get("display", "")
        series_body_site = data.get("series", [{}])[0].get("bodySite", {}).get("display", "")
        instance_title = data.get("series", [{}])[0].get("instance", [{}])[0].get("title", "")

        fields = (id, status, started, number_of_series, number_of_instances, procedure_code, location,
                  series_modality, series_body_site, instance_title)

        return fields

    except Exception as e:
        print("Error occurred in format_imaging_study_response: ", e)