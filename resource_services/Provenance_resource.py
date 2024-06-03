import json


def format_provenance_response(data):
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
        recorded = data.get("recorded")
        agents = data.get("agent", [])

        agent_details = {}

        for agent in agents:
            agent_type = get_nested_value(agent, ["type", "text"])
            who_display = get_nested_value(agent, ["who", "display"])
            on_behalf_of_display = get_nested_value(agent, ["onBehalfOf", "display"])
            agent_details[agent_type] = {"Name": who_display, "BehalfOf": on_behalf_of_display}

        fields = (id, recorded, json.dumps(agent_details))

        return fields

    except Exception as e:
        print("Error occurred in format_provenance_response: ", e)
