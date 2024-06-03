
def format_medication_administration_response(data):
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
        medication_display = get_nested_value(data, ["medicationCodeableConcept", "text"])
        subject_reference = data.get("subject", {}).get("reference")
        context_reference = data.get("context", {}).get("reference")
        effective_date_time = data.get("effectiveDateTime")
        reason_reference = get_nested_value(data, ["reasonReference", 0, "reference"])

        fields = (id, status, medication_display, subject_reference, context_reference,
                  effective_date_time, reason_reference)

        return fields

    except Exception as e:
        print("Error occurred in format_medication_administration_response: ", e)