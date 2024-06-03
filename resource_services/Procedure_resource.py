def format_procedure_response(data):
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
        code = get_nested_value(data, ["code", "text"])
        subject = get_nested_value(data, ["subject", "reference"])
        encounter = get_nested_value(data, ["encounter", "reference"])
        performed_period_start = get_nested_value(data, ["performedPeriod", "start"])
        performed_period_end = get_nested_value(data, ["performedPeriod", "end"])
        location = get_nested_value(data, ["location", "display"])

        fields = (id, status, code, subject, encounter, performed_period_start, performed_period_end,
                  location)

        return fields

    except Exception as e:
        print("Error occurred in format_procedure_response: ", e)
