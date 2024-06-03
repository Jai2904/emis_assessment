
def format_immunization_response(data):
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
        vaccine = get_nested_value(data, ["vaccineCode", "text"])
        patient = get_nested_value(data, ["patient", "reference"])
        encounter = get_nested_value(data, ["encounter", "reference"])
        occurrence_date_time = data.get("occurrenceDateTime")
        primary_source = data.get("primarySource")
        location = get_nested_value(data, ["location", "display"])

        fields = (id, status, vaccine, patient, encounter, occurrence_date_time, primary_source, location)

        return fields

    except Exception as e:
        print("Error occurred in format_immunization_response: ", e)