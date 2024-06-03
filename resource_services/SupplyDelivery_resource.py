
def format_supply_delivery_response(data):
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
        type = get_nested_value(data, ["type", "coding", 0, "display"])
        supplied_quantity = get_nested_value(data, ["suppliedItem", "quantity", "value"])
        supplied_item = get_nested_value(data, ["suppliedItem", "itemCodeableConcept", "text"])
        occurrence_datetime = data.get("occurrenceDateTime")

        fields = (id, status, type, supplied_quantity, supplied_item, occurrence_datetime)

        return fields

    except Exception as e:
        print("Error occurred in format_supply_delivery_response: ", e)