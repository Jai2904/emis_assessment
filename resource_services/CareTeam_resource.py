def format_care_team_response(data):
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
        subject = get_nested_value(data, ["subject", "reference"])
        encounter = get_nested_value(data, ["encounter", "reference"])
        period_start = get_nested_value(data, ["period", "start"])
        period_end = get_nested_value(data, ["period", "end"])
        reason_code = get_nested_value(data, ["reasonCode", 0, "text"])
        managing_organization = get_nested_value(data, ["managingOrganization", 0, "display"])

        fields = (id, status, subject, encounter, period_start, period_end, reason_code, managing_organization)

        return fields

    except Exception as e:
        print("Error occurred in format_care_team_response: ", e)
