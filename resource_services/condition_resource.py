def format_condition_response(data):
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
        clinical_status = get_nested_value(data, ["clinicalStatus", "coding", "code"])
        verification_status = get_nested_value(data, ["verificationStatus", "coding", "code"])
        category = get_nested_value(data, ["category", "coding", "display"])
        code = get_nested_value(data, ["code", "text"])
        subject = get_nested_value(data, ["subject", "reference"])
        encounter = get_nested_value(data, ["encounter", "reference"])
        onset_date_time = data.get("onsetDateTime")
        abatement_date_time = data.get("abatementDateTime")
        recorded_date = data.get("recordedDate")

        fields = (id, clinical_status, verification_status, category, code, subject, encounter, onset_date_time,
                  abatement_date_time, recorded_date)

        return fields

    except Exception as e:
        print("Error occurred condition_resource : ", e)
