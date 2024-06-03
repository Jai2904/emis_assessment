import mysql.connector
import pymysql


class Database:
    """DB queries operations related to
    executions and fetching
    """

    def commitRow(self, sql, args):
        """executing a sql statement to the table
        in DB
        """
        try :
            conn = pymysql.connect(host="localhost", user="root", password="password", database="patient_db")
            cursor = conn.cursor()
            cursor.executemany(sql, args)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(e, sql)

    pass


class Patient(Database):
    """DB queries related to Patient data"""

    def insertPatientRecord(self, fields):
        """inserting patient record data
        into the table in DB
        """
        sql = """
                INSERT INTO Patients 
                    (
                        id, 
                        name, 
                        gender, 
                        birthdate, 
                        marital_status, 
                        city, 
                        state, 
                        country, 
                        address_line, 
                        mrn
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class Encounter(Database):
    """DB queries related to Encounter data"""

    def insertEncounterRecord(self, fields):
        """inserting Encounter record data
        into the table in DB
        """
        sql = """
                INSERT INTO Encounter 
                    (
                        id, 
                        status, 
                        class_code, 
                        type, 
                        subject, 
                        participant, 
                        period_start, 
                        period_end, 
                        location, 
                        service_provider
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class Condition(Database):
    """DB queries related to Condition data"""

    def insertConditionRecord(self, fields):
        """inserting Condition record data
        into the table in DB
        """
        sql = """
                INSERT INTO ClinicalCondition 
                    (
                        id, 
                        clinical_status, 
                        verification_status, 
                        category, 
                        code, 
                        subject, 
                        encounter, 
                        onset_date_time, 
                        abatement_date_time, 
                        recorded_date
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class DiagnosticReport(Database):
    """DB queries related to DiagnosticReport data"""

    def insertDiagnosticReportRecord(self, fields):
        """inserting DiagnosticReport record data
        into the table in DB
        """
        sql = """
                INSERT INTO DiagnosticReport 
                    (
                        id, 
                        status, 
                        category, 
                        code, 
                        subject, 
                        encounter, 
                        effective_date_time, 
                        issued, 
                        performer, 
                        presented_form
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class DocumentReference(Database):
    """DB queries related to DocumentReference data"""

    def insertDocumentReferenceRecord(self, fields):
        """inserting DocumentReference record data
        into the table in DB
        """
        sql = """
                INSERT INTO DocumentReference 
                    (
                    id,
                    status, 
                    type, 
                    category, 
                    subject, 
                    date, 
                    author, 
                    custodian, 
                    content, 
                    context, 
                    context_period_start,
                    context_period_end
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class Claim(Database):
    """DB queries related to Claim data"""

    def insertClaimRecord(self, fields):
        """inserting Claim record data
        into the table in DB
        """
        sql = """
                INSERT INTO Claim 
                    (
                        id, 
                        status, 
                        type, 
                        claim_use, 
                        patient, 
                        billable_period_start, 
                        billable_period_end,
                        created, 
                        provider, 
                        priority,
                        facility,
                        diagnosis,
                        insurance,
                        total_value
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class ExplanationOfBenefit(Database):
    """DB queries related to ExplanationOfBenefit data"""

    def insertExplanationOfBenefitRecord(self, fields):
        """inserting ExplanationOfBenefit record data
        into the table in DB
        """
        sql = """
                INSERT INTO ExplanationOfBenefit 
                    (
                        id, status, type, eob_use, patient, billable_period_start, billable_period_end, created, insurer,
                  provider, facility, outcome, insurance, total_amount
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class Observation(Database):
    """DB queries related to Observation data"""

    def insertObservationRecord(self, fields):
        """inserting Observation record data
        into the table in DB
        """
        sql = """
                INSERT INTO Observation 
                    (
                    id, status, category, code, subject, encounter, effective_date_time, issued, value_quantity,
                    value_unit
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class Procedure(Database):
    """DB queries related to Procedure data"""

    def insertProcedureRecord(self, fields):
        """inserting Procedure record data
        into the table in DB
        """
        sql = """
                INSERT INTO Procedures 
                    (
                    id, status, code, subject, encounter, performed_period_start, performed_period_end, location
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class Immunization(Database):
    """DB queries related to Immunization data"""

    def insertImmunizationRecord(self, fields):
        """inserting Immunization record data
        into the table in DB
        """
        sql = """
                INSERT INTO Immunization 
                    (
                    id, status, vaccine, patient, encounter, occurrence_date_time, primary_source, location
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class MedicationRequest(Database):
    """DB queries related to MedicationRequest data"""

    def insertMedicationRequestRecord(self, fields):
        """inserting MedicationRequest record data
        into the table in DB
        """
        sql = """
                INSERT INTO MedicationRequest 
                    (
                    id, status, intent, medication_codeable_concept, subject, encounter, authored_on, requester
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class CareTeam(Database):
    """DB queries related to CareTeam data"""

    def insertCareTeamRecord(self, fields):
        """inserting CareTeam record data
        into the table in DB
        """
        sql = """
                INSERT INTO CareTeam 
                    (
                    id, status, subject, encounter, period_start, period_end, reason_code, managing_organization
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class CarePlan(Database):
    """DB queries related to CarePlan data"""

    def insertCarePlanRecord(self, fields):
        """inserting CarePlan record data
        into the table in DB
        """
        sql = """
                INSERT INTO CarePlan 
                    (
                    id, status, intent, category, subject, encounter, period_start, period_end
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class ImagingStudy(Database):
    """DB queries related to ImagingStudy data"""

    def insertImagingStudyRecord(self, fields):
        """inserting ImagingStudy record data
        into the table in DB
        """
        sql = """
                INSERT INTO ImagingStudy 
                    (
                    id, status, started, number_of_series, number_of_instances, procedure_code, location,
                    series_modality, series_body_site, instance_title
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class Medication(Database):
    """DB queries related to Medication data"""

    def insertMedicationRecord(self, fields):
        """inserting Medication record data
        into the table in DB
        """
        sql = """
                INSERT INTO Medication 
                    (
                    id, status, code_text
                    ) 
                    VALUES (%s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class MedicationAdministration(Database):
    """DB queries related to MedicationAdministration data"""

    def insertMedicationAdministrationRecord(self, fields):
        """inserting MedicationAdministration record data
        into the table in DB
        """
        sql = """
                INSERT INTO MedicationAdministration 
                    (
                    id, status, medication_display, subject_reference, context_reference,
                    effective_date_time, reason_reference
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class Provenance(Database):
    """DB queries related to Provenance data"""

    def insertProvenanceRecord(self, fields):
        """inserting Provenance record data
        into the table in DB
        """
        sql = """
                INSERT INTO Provenance 
                    (
                    id, recorded, agent_details
                    ) 
                    VALUES (%s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class AllergyIntolerance(Database):
    """DB queries related to AllergyIntolerance data"""

    def insertAllergyIntoleranceRecord(self, fields):
        """inserting AllergyIntolerance record data
        into the table in DB
        """
        sql = """
                INSERT INTO AllergyIntolerance 
                    (
                    id, clinical_status, verification_status, type, category, criticality,
                    code, recorded_date, reactions
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class Device(Database):
    """DB queries related to Device data"""

    def insertDeviceRecord(self, fields):
        """inserting Device record data
        into the table in DB
        """
        sql = """
                INSERT INTO Device 
                    (
                    id, status, distinct_identifier, manufacture_date, expiration_date, lot_number,
                    serial_number, device_name, device_type, type
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)


class SupplyDelivery(Database):
    """DB queries related to SupplyDelivery data"""

    def insertSupplyDeliveryRecord(self, fields):
        """inserting SupplyDelivery record data
        into the table in DB
        """
        sql = """
                INSERT INTO SupplyDelivery 
                    (
                    id, status, type, supplied_quantity, supplied_item, occurrence_datetime
                    ) 
                    VALUES (%s, %s, %s, %s, %s, %s)
        """
        args = fields

        return self.commitRow(sql, args)
