def format_explanation_of_benefit_response(data):
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
        type = get_nested_value(data, ["type", "coding", "code"])
        use = data.get("use")
        patient = get_nested_value(data, ["patient", "reference"])
        billable_period_start = get_nested_value(data, ["billablePeriod", "start"])
        billable_period_end = get_nested_value(data, ["billablePeriod", "end"])
        created = data.get("created")
        insurer = get_nested_value(data, ["insurer", "display"])
        provider = get_nested_value(data, ["provider", "reference"])
        facility = get_nested_value(data, ["facility", "display"])
        outcome = data.get("outcome")
        insurance = get_nested_value(data, ["insurance", "coverage", "display"])
        total_amount = get_nested_value(data, ["total", "amount", "value"])

        fields = (id, status, type, use, patient, billable_period_start, billable_period_end, created, insurer,
                  provider, facility, outcome, insurance, total_amount)

        return fields

    except Exception as e:
        print("Error occurred in format_explanation_of_benefit_response: ", e)