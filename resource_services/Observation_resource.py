
def format_observation_response(data):
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
        category = get_nested_value(data, ["category", "coding", "display"])
        code = get_nested_value(data, ["code", "text"])
        subject = get_nested_value(data, ["subject", "reference"])
        encounter = get_nested_value(data, ["encounter", "reference"])
        effective_date_time = data.get("effectiveDateTime")
        issued = data.get("issued")
        value_quantity = get_nested_value(data, ["valueQuantity", "value"])
        value_unit = get_nested_value(data, ["valueQuantity", "unit"])

        fields = (id, status, category, code, subject, encounter, effective_date_time, issued, value_quantity,
                  value_unit)

        return fields

    except Exception as e:
        print("Error occurred in format_observation_response: ", e)