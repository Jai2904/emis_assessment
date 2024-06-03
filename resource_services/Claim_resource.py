def format_claim_response(claim_json):
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

        # Using the provided get_nested_value function to extract variables
        id = get_nested_value(claim_json, ["id"])
        status = get_nested_value(claim_json, ["status"])
        type = get_nested_value(claim_json, ["type", "coding", "code"])
        use = get_nested_value(claim_json, ["use"])
        patient = get_nested_value(claim_json, ["patient", "display"])
        billable_period_start = get_nested_value(claim_json, ["billablePeriod", "start"])
        billable_period_end = get_nested_value(claim_json, ["billablePeriod", "end"])
        created = get_nested_value(claim_json, ["created"])
        provider = get_nested_value(claim_json, ["provider", "display"])
        priority = get_nested_value(claim_json, ["priority", "coding", "code"])
        facility = get_nested_value(claim_json, ["facility", "display"])
        diagnosis = get_nested_value(claim_json, ["diagnosis", "diagnosisReference", "reference"])
        insurance = get_nested_value(claim_json, ["insurance", "coverage", "display"])
        total_value = get_nested_value(claim_json, ["total", "value"])

        # Creating a tuple with all the extracted variables
        fields = (id, status, type, use, patient, billable_period_start, billable_period_end, created,
                  provider, priority, facility, diagnosis, insurance, total_value)

        return fields

    except Exception as e:
        print("Error occurred claim_resource : ", e)
