
def format_care_plan_response(data):
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
        intent = data.get("intent")
        subject = get_nested_value(data, ["subject", "reference"])
        encounter = get_nested_value(data, ["encounter", "reference"])
        period_start = get_nested_value(data, ["period", "start"])
        period_end = get_nested_value(data, ["period", "end"])

        for each in data.get("category"):
            category = each.get("text")

        fields = (id, status, intent, category, subject, encounter, period_start, period_end)

        return fields

    except Exception as e:
        print("Error occurred in format_care_plan_response: ", e)
