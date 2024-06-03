
def format_diagnostic_report_response(data):
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
        code = get_nested_value(data, ["code", "coding", "display"])
        subject = get_nested_value(data, ["subject", "reference"])
        encounter = get_nested_value(data, ["encounter", "reference"])
        effective_date_time = data.get("effectiveDateTime")
        issued = data.get("issued")
        performer = get_nested_value(data, ["performer", "display"])
        presented_form = get_nested_value(data, ["presentedForm", "data"])

        fields = (id, status, category, code, subject, encounter, effective_date_time, issued, performer, presented_form)

        return fields

    except Exception as e:
        print("Error occurred format_diagnostic_report_response : ", e)