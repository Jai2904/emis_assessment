def format_allergy_intolerance_response(data):
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
        clinical_status = get_nested_value(data, ["clinicalStatus", "coding", 0, "code"])
        verification_status = get_nested_value(data, ["verificationStatus", "coding", 0, "code"])
        type = data.get("type")
        category = ', '.join(data.get("category", []))
        criticality = data.get("criticality")
        code = get_nested_value(data, ["code", "coding", 0, "display"])
        recorded_date = data.get("recordedDate")
        reactions_list = data.get("reaction", [])

        reactions = []
        for reaction in reactions_list:
            manifestation = get_nested_value(reaction, ["manifestation", 0, "text"])
            if manifestation:
                reactions.append(manifestation)

        fields = (id, clinical_status, verification_status, type, category, criticality,
                  code, recorded_date, reactions)

        return fields

    except Exception as e:
        print("Error occurred in format_allergy_intolerance_response: ", e)
