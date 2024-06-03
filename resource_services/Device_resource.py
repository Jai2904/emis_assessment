def format_device_response(data):
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
        distinct_identifier = data.get("distinctIdentifier")
        manufacture_date = data.get("manufactureDate")
        expiration_date = data.get("expirationDate")
        lot_number = data.get("lotNumber")
        serial_number = data.get("serialNumber")
        device_name = get_nested_value(data, ["deviceName", 0, "name"])
        device_type = get_nested_value(data, ["type", "coding", 0, "display"])
        type = get_nested_value(data, ["type", "text"])

        fields = (id, status, distinct_identifier, manufacture_date, expiration_date, lot_number,
                  serial_number, device_name, device_type, type)

        return fields

    except Exception as e:
        print("Error occurred in format_device_response: ", e)
