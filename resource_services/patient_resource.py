
def format_pat_response(resource):
    try:

        patient_id = resource.get("id")
        patient_name = " ".join(resource.get("name")[0].get("given")) + " " + resource.get("name")[0].get("family")
        patient_gender = resource.get("gender")
        patient_birthdate = resource.get("birthDate")
        marital_status = resource.get("maritalStatus", {}).get("text")
        address = resource.get("address", [{}])[0]
        city = address.get("city")
        state = address.get("state")
        country = address.get("country")
        line = address.get("line")

        mrn = None
        identifiers = resource.get("identifier", [])
        for identifier in identifiers:
            if identifier.get("type", {}).get("text") == "Medical Record Number":
                mrn = identifier.get("value")

        fields = (patient_id, patient_name, patient_gender, patient_birthdate, marital_status, city, state, country,
                  line[0], mrn)

        return fields

    except Exception as e:
        print("Error occurred Patient_resource : ", e)
