import json
import os
import datetime

from cloud_db import Patient, Encounter, Condition, DiagnosticReport, DocumentReference, Claim, ExplanationOfBenefit, \
    Observation, Procedure, Immunization, MedicationRequest, CareTeam, CarePlan, ImagingStudy, Medication, \
    MedicationAdministration, Provenance, AllergyIntolerance, Device, SupplyDelivery

from resource_services.AllergyIntolerance_resource import format_allergy_intolerance_response
from resource_services.CarePlan_resource import format_care_plan_response
from resource_services.CareTeam_resource import format_care_team_response
from resource_services.Claim_resource import format_claim_response
from resource_services.condition_resource import format_condition_response
from resource_services.Device_resource import format_device_response
from resource_services.diagnostic_report_resource import format_diagnostic_report_response
from resource_services.DocumentReference_resource import format_doc_reference_response
from resource_services.encounter_resource import format_encounter_response
from resource_services.ExplanationOfBenefit_resource import format_explanation_of_benefit_response
from resource_services.ImagingStudy_resource import format_imaging_study_response
from resource_services.Immunization_resource import format_immunization_response
from resource_services.Medication_resource import format_medication_response
from resource_services.MedicationAdministration_resource import format_medication_administration_response
from resource_services.MedicationRequest_resource import format_medication_request_response
from resource_services.Observation_resource import format_observation_response
from resource_services.patient_resource import format_pat_response
from resource_services.Procedure_resource import format_procedure_response
from resource_services.Provenance_resource import format_provenance_response
from resource_services.SupplyDelivery_resource import format_supply_delivery_response

# Initialize the objects for each table class
patient = Patient()
encounter = Encounter()
condition = Condition()
diagnosticReport = DiagnosticReport()
documentReference = DocumentReference()
claim = Claim()
explanationOfBenefit = ExplanationOfBenefit()
observation = Observation()
procedure = Procedure()
immunization = Immunization()
medicationRequest = MedicationRequest()
careTeam = CareTeam()
carePlan = CarePlan()
imagingStudy = ImagingStudy()
medication = Medication()
medicationAdministration = MedicationAdministration()
provenance = Provenance()
allergyIntolerance = AllergyIntolerance()
device = Device()
supplyDelivery = SupplyDelivery()

# Set the path for data set
cur_path = os.path.dirname(__file__)
json_dir = os.path.relpath('data', cur_path)

# Initialize the formatted bulk data set
patient_resource_list = []
encounter_resource_list = []
condition_resource_list = []
diagnostic_report_resource_list = []
DocumentReference_resource_list = []
Claim_resource_list = []
ExplanationOfBenefit_resource_list = []
Observation_resource_list = []
Procedure_resource_list = []
Immunization_resource_list = []
MedicationRequest_resource_list = []
CareTeam_resource_list = []
CarePlan_resource_list = []
ImagingStudy_resource_list = []
Medication_resource_list = []
MedicationAdministration_resource_list = []
Provenance_resource_list = []
AllergyIntolerance_resource_list = []
Device_resource_list = []
SupplyDelivery_resource_list = []

'''
# -------- Get distinct resource types ---------
resource_types = []

# Iterate over each file in the directory
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        with open(file_path, 'r', errors='ignore') as f:
            fhir_data = json.load(f)

    response_list = fhir_data.get('entry', [])
    for item in response_list:
        if item['search']['mode'] == 'match':
            if item['resourceType'] not in resource_types:
                resource_types.append(item['resourceType'])

print(resource_types)
'''

print('Start!')
print(datetime.datetime.now())

# Iterate over each file in the directory
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        with open(file_path, 'r', errors='ignore') as f:
            fhir_data = json.load(f)

    response_list = fhir_data.get('entry', [])

    for item in response_list:

        if item['resource']['resourceType'] == 'Patient':
            patient_resource_list.append(format_pat_response(item['resource']))
        if item['resource']['resourceType'] == 'Encounter':
            encounter_resource_list.append(format_encounter_response(item['resource']))
        if item['resource']['resourceType'] == 'Condition':
            condition_resource_list.append(format_condition_response(item['resource']))
        if item['resource']['resourceType'] == 'DiagnosticReport':
            diagnostic_report_resource_list.append(format_diagnostic_report_response(item['resource']))
        if item['resource']['resourceType'] == 'DocumentReference':
            DocumentReference_resource_list.append(format_doc_reference_response(item['resource']))
        if item['resource']['resourceType'] == 'Claim':
            Claim_resource_list.append(format_claim_response(item['resource']))
        if item['resource']['resourceType'] == 'ExplanationOfBenefit':
            ExplanationOfBenefit_resource_list.append(format_explanation_of_benefit_response(item['resource']))
        if item['resource']['resourceType'] == 'Observation':
            Observation_resource_list.append(format_observation_response(item['resource']))
        if item['resource']['resourceType'] == 'Procedure':
            Procedure_resource_list.append(format_procedure_response(item['resource']))
        if item['resource']['resourceType'] == 'Immunization':
            Immunization_resource_list.append(format_immunization_response(item['resource']))
        if item['resource']['resourceType'] == 'MedicationRequest':
            MedicationRequest_resource_list.append(format_medication_request_response(item['resource']))
        if item['resource']['resourceType'] == 'CareTeam':
            CareTeam_resource_list.append(format_care_team_response(item['resource']))
        if item['resource']['resourceType'] == 'CarePlan':
            CarePlan_resource_list.append(format_care_plan_response(item['resource']))
        if item['resource']['resourceType'] == 'ImagingStudy':
            ImagingStudy_resource_list.append(format_imaging_study_response(item['resource']))
        if item['resource']['resourceType'] == 'Medication':
            Medication_resource_list.append(format_medication_response(item['resource']))
        if item['resource']['resourceType'] == 'MedicationAdministration':
            MedicationAdministration_resource_list.append(format_medication_administration_response(item['resource']))
        if item['resource']['resourceType'] == 'Provenance':
            Provenance_resource_list.append(format_provenance_response(item['resource']))
        if item['resource']['resourceType'] == 'AllergyIntolerance':
            AllergyIntolerance_resource_list.append(format_allergy_intolerance_response(item['resource']))
        if item['resource']['resourceType'] == 'Device':
            Device_resource_list.append(format_device_response(item['resource']))
        if item['resource']['resourceType'] == 'SupplyDelivery':
            SupplyDelivery_resource_list.append(format_supply_delivery_response(item['resource']))

if patient_resource_list:
    patient.insertPatientRecord(patient_resource_list)

if encounter_resource_list:
    encounter.insertEncounterRecord(encounter_resource_list)

if diagnostic_report_resource_list:
    diagnosticReport.insertDiagnosticReportRecord(diagnostic_report_resource_list)

if DocumentReference_resource_list:
    documentReference.insertDocumentReferenceRecord(DocumentReference_resource_list)

if Claim_resource_list:
    claim.insertClaimRecord(Claim_resource_list)

if ExplanationOfBenefit_resource_list:
    explanationOfBenefit.insertExplanationOfBenefitRecord(ExplanationOfBenefit_resource_list)

if Observation_resource_list:
    observation.insertObservationRecord(Observation_resource_list)

if Immunization_resource_list:
    immunization.insertImmunizationRecord(Immunization_resource_list)

if MedicationRequest_resource_list:
    medicationRequest.insertMedicationRequestRecord(MedicationRequest_resource_list)

if CareTeam_resource_list:
    careTeam.insertCareTeamRecord(CareTeam_resource_list)

if CarePlan_resource_list:
    carePlan.insertCarePlanRecord(CarePlan_resource_list)

if ImagingStudy_resource_list:
    imagingStudy.insertImagingStudyRecord(ImagingStudy_resource_list)

if Medication_resource_list:
    medication.insertMedicationRecord(Medication_resource_list)

if MedicationAdministration_resource_list:
    medicationAdministration.insertMedicationAdministrationRecord(MedicationAdministration_resource_list)

if Provenance_resource_list:
    provenance.insertProvenanceRecord(Provenance_resource_list)

if AllergyIntolerance_resource_list:
    allergyIntolerance.insertAllergyIntoleranceRecord(AllergyIntolerance_resource_list)

if Device_resource_list:
    device.insertDeviceRecord(Device_resource_list)

if SupplyDelivery_resource_list:
    supplyDelivery.insertSupplyDeliveryRecord(SupplyDelivery_resource_list)

if condition_resource_list:
    condition.insertConditionRecord(condition_resource_list)

if Procedure_resource_list:
    procedure.insertProcedureRecord(Procedure_resource_list)

print('End!')
print(datetime.datetime.now())
