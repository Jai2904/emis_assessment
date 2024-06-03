
def format_medication_response(data):
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
        code_text = get_nested_value(data, ["code", "text"])

        fields = (id, status, code_text)

        return fields

    except Exception as e:
        print("Error occurred in format_medication_response: ", e)