
def format_encounter_response(resource):
    try:

        id = resource.get("id")
        status = resource.get("status")
        class_code = resource.get("class", {}).get("code")
        type = resource.get("type", [{}])[0].get("text")
        subject = resource.get("subject", {}).get("display")
        participant = resource.get("participant", [{}])[0].get("individual", {}).get("display")
        period_start = resource.get("period", {}).get("start")
        period_end = resource.get("period", {}).get("end")
        location = resource.get("location", [{}])[0].get("location", {}).get("display")
        service_provider = resource.get("serviceProvider", {}).get("display")

        fields = (id, status, class_code, type, subject, participant, period_start, period_end, location, service_provider)

        return fields

    except Exception as e:
        print("Error occurred encounter_resource : ", e)
