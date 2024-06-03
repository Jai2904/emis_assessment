
def format_medication_request_response(data):
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
        medication_codeable_concept = get_nested_value(data, ["medicationCodeableConcept", "text"])
        subject = get_nested_value(data, ["subject", "reference"])
        encounter = get_nested_value(data, ["encounter", "reference"])
        authored_on = data.get("authoredOn")
        requester = get_nested_value(data, ["requester", "display"])

        fields = (id, status, intent, medication_codeable_concept, subject, encounter, authored_on, requester)

        return fields

    except Exception as e:
        print("Error occurred in format_medication_request_response: ", e)