CREATE TABLE IF NOT EXISTS patient_db.patients (
                    id VARCHAR(255) PRIMARY KEY,
                    name VARCHAR(255),
                    gender VARCHAR(10),
                    mrn VARCHAR(50),
                    birthdate DATE,
                    marital_status VARCHAR(50),
                    address_line VARCHAR(100),
                    city VARCHAR(100),
                    state VARCHAR(100),
                    country VARCHAR(100)
                );

CREATE TABLE IF NOT EXISTS patient_db.Encounter (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    class_code VARCHAR(255),
                    type VARCHAR(255),
                    subject VARCHAR(255),
                    participant VARCHAR(255),
                    period_start VARCHAR(255),
                    period_end VARCHAR(100),
                    location VARCHAR(255),
                    service_provider VARCHAR(255)
                );

CREATE TABLE IF NOT EXISTS patient_db.ClinicalCondition (
                    id VARCHAR(255),
                    clinical_status VARCHAR(255),
                    verification_status VARCHAR(255),
                    category VARCHAR(255),
                    code VARCHAR(255),
                    subject VARCHAR(255),
                    encounter VARCHAR(255),
                    onset_date_time VARCHAR(100),
                    abatement_date_time VARCHAR(255),
                    recorded_date VARCHAR(255)
                );

CREATE TABLE IF NOT EXISTS patient_db.DiagnosticReport (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    category VARCHAR(255),
                    code VARCHAR(255),
                    subject VARCHAR(255),
                    encounter VARCHAR(255),
                    effective_date_time VARCHAR(100),
                    issued VARCHAR(255),
                    performer VARCHAR(255),
                    presented_form LONGTEXT
                );

CREATE TABLE IF NOT EXISTS patient_db.DocumentReference (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    type VARCHAR(255),
                    category VARCHAR(255),
                    subject VARCHAR(255),
                    date VARCHAR(255),
                    author VARCHAR(255),
                    custodian VARCHAR(255),
                    content LONGTEXT,
                    context VARCHAR(255),
                    context_period_start VARCHAR(255),
                    context_period_end VARCHAR(255)
                );

CREATE TABLE IF NOT EXISTS patient_db.Claim (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    type VARCHAR(255),
                    claim_use VARCHAR(255),
                    patient VARCHAR(255),
                    billable_period_start VARCHAR(255),
                    billable_period_end VARCHAR(255),
                    created VARCHAR(255),
                    provider VARCHAR(255),
                    priority VARCHAR(255),
                    facility VARCHAR(255),
                    diagnosis VARCHAR(255),
                    insurance VARCHAR(255),
                    total_value VARCHAR(255)
                );

CREATE TABLE IF NOT EXISTS patient_db.ExplanationOfBenefit (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    type VARCHAR(255),
                    eob_use VARCHAR(255),
                    patient VARCHAR(255),
                    billable_period_start VARCHAR(255),
                    billable_period_end VARCHAR(255),
                    created VARCHAR(255),
                    insurer VARCHAR(255),
                    provider VARCHAR(255),
                    facility VARCHAR(255),
                    outcome VARCHAR(255),
                    insurance VARCHAR(255),
                    total_amount VARCHAR(255)
                );

CREATE TABLE IF NOT EXISTS patient_db.Observation (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    category VARCHAR(255),
                    code VARCHAR(255),
                    subject VARCHAR(255),
                    encounter VARCHAR(255),
                    effective_date_time VARCHAR(255),
                    issued VARCHAR(255),
                    value_quantity VARCHAR(255),
                    value_unit VARCHAR(255)
                );

CREATE TABLE IF NOT EXISTS patient_db.Procedures (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    code VARCHAR(255),
                    subject VARCHAR(255),
                    encounter VARCHAR(255),
                    performed_period_start VARCHAR(255),
                    performed_period_end VARCHAR(255),
                    location VARCHAR(255)
                );

CREATE TABLE IF NOT EXISTS patient_db.Immunization (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    vaccine VARCHAR(255),
                    patient VARCHAR(255),
                    encounter VARCHAR(255),
                    occurrence_date_time VARCHAR(255),
                    primary_source VARCHAR(255),
                    location VARCHAR(255)
                );

CREATE TABLE IF NOT EXISTS patient_db.MedicationRequest (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    intent VARCHAR(255),
                    medication_codeable_concept VARCHAR(255),
                    subject VARCHAR(255),
                    encounter VARCHAR(255),
                    authored_on VARCHAR(255),
                    requester VARCHAR(255)
                );

CREATE TABLE IF NOT EXISTS patient_db.CareTeam (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    subject VARCHAR(255),
                    encounter VARCHAR(255),
                    period_start VARCHAR(255),
                    period_end VARCHAR(255),
                    reason_code VARCHAR(255),
                    managing_organization VARCHAR(255)
                );

CREATE TABLE IF NOT EXISTS patient_db.CarePlan (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    intent VARCHAR(255),
                    category VARCHAR(255),
                    subject VARCHAR(255),
                    encounter VARCHAR(255),
                    period_start VARCHAR(255),
                    period_end VARCHAR(255)
                );

CREATE TABLE IF NOT EXISTS patient_db.ImagingStudy (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    started VARCHAR(255),
                    number_of_series VARCHAR(255),
                    number_of_instances VARCHAR(255),
                    procedure_code VARCHAR(255),
                    location VARCHAR(255),
                    series_modality VARCHAR(255),
                    series_body_site VARCHAR(255),
                    instance_title VARCHAR(255)
                );

CREATE TABLE IF NOT EXISTS patient_db.Medication (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    code_text VARCHAR(255)
                );

CREATE TABLE IF NOT EXISTS patient_db.MedicationAdministration (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    medication_display VARCHAR(255),
                    subject_reference VARCHAR(255),
                    context_reference VARCHAR(255),
                    effective_date_time VARCHAR(255),
                    reason_reference VARCHAR(255)
                );

CREATE TABLE IF NOT EXISTS patient_db.Provenance (
                    id VARCHAR(255),
                    recorded VARCHAR(255),
                    agent_details json
                );

CREATE TABLE IF NOT EXISTS patient_db.AllergyIntolerance (
                    id VARCHAR(255),
                    clinical_status VARCHAR(255),
                    verification_status VARCHAR(255),
                    type VARCHAR(255),
                    category VARCHAR(255),
                    criticality VARCHAR(255),
                    code VARCHAR(255),
                    recorded_date VARCHAR(255),
                    reactions json
                );

CREATE TABLE IF NOT EXISTS patient_db.Device (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    distinct_identifier VARCHAR(255),
                    manufacture_date VARCHAR(255),
                    expiration_date VARCHAR(255),
                    lot_number VARCHAR(255),
                    serial_number VARCHAR(255),
                    device_name VARCHAR(255),
                    device_type VARCHAR(255),
                    type VARCHAR(255)
                );

CREATE TABLE IF NOT EXISTS patient_db.SupplyDelivery (
                    id VARCHAR(255),
                    status VARCHAR(255),
                    type VARCHAR(255),
                    supplied_quantity VARCHAR(255),
                    supplied_item VARCHAR(255),
                    occurrence_datetime VARCHAR(255)
                );


truncate table patient_db.patients;

truncate table patient_db.Encounter;

truncate table patient_db.ClinicalCondition ;

truncate table patient_db.DiagnosticReport;

truncate table patient_db.DocumentReference ;

truncate table patient_db.Claim ;

truncate table patient_db.ExplanationOfBenefit;

truncate table patient_db.Observation;

truncate table patient_db.Procedures ;

truncate table patient_db.Immunization ;

truncate table patient_db.MedicationRequest ;

truncate table patient_db.CareTeam ;

truncate table patient_db.CarePlan;

truncate table patient_db.ImagingStudy ;

truncate table patient_db.Medication ;

truncate table patient_db.MedicationAdministration ;

truncate table patient_db.Provenance ;

truncate table patient_db.AllergyIntolerance;

truncate table patient_db.Device ;

truncate table patient_db.SupplyDelivery ;