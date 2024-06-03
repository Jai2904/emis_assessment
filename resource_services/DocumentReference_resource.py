
def format_doc_reference_response(data):
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
        type = get_nested_value(data, ["type", "coding", "display"])
        category = get_nested_value(data, ["category", "coding", "display"])
        subject = get_nested_value(data, ["subject", "reference"])
        date = data.get("date")
        author = get_nested_value(data, ["author", "display"])
        custodian = get_nested_value(data, ["custodian", "display"])
        content = get_nested_value(data, ["content", "attachment", "data"])
        context = get_nested_value(data, ["context", "encounter", "reference"])
        context_period_start = get_nested_value(data, ["context", "period", "start"])
        context_period_end = get_nested_value(data, ["context", "period", "end"])

        fields = (id, status, type, category, subject, date, author, custodian, content, context, context_period_start,
                  context_period_end)

        return fields

    except Exception as e:
        print("Error occurred format_doc_reference_response : ", e)