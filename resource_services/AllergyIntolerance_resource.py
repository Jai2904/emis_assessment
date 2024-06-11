import json

def format_allergy_intolerance_response(data):
    try:

        id = data.get("id")
        clinical_status = data.get('clinicalStatus', {}).get('coding', [{}])[0].get('code', '')
        verification_status = data.get('verificationStatus', {}).get('coding', [{}])[0].get('code', '')
        type = data.get("type")
        category = ', '.join(data.get("category", []))
        criticality = data.get("criticality")
        code = data.get('code', {}).get('text', '')
        recorded_date = data.get("recordedDate")
        reactions_list = data.get("reaction", [])

        reactions = {}
        for reaction in reactions_list:
            manifestation_display = reaction.get('manifestation', [{}])[0].get('text')
            severity = reaction.get("severity")
            if manifestation_display and severity:
                reactions[manifestation_display] = severity
        fields = (id, clinical_status, verification_status, type, category, criticality,
                  code, recorded_date, json.dumps(reactions))
        return fields

    except Exception as e:
        pass
        print("Error occurred in format_allergy_intolerance_response: ", e)
