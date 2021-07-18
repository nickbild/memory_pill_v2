-- SQLite3 schema for Memory Pill v2.
-- https://github.com/nickbild/memory_pill_v2

CREATE TABLE medication_administrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT,
    medication_id TEXT,
    bottle_opened_at TEXT
);

CREATE TABLE medication_schedule (
    patient_id TEXT,
    medication_id TEXT,
    `time` TEXT,
    m TEXT,
    t TEXT,
    w TEXT,
    r TEXT,
    f TEXT,
    s TEXT,
    u TEXT
);

INSERT INTO medication_schedule VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '08:00', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO medication_schedule VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '17:00', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO medication_schedule VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '08:30', '1', '1', '1', '1', '1', '0', '0');
INSERT INTO medication_schedule VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '18:30', '1', '1', '1', '1', '1', '0', '0');

CREATE TABLE medication_lookup (
    medication_id TEXT,
    medication_name TEXT
);

INSERT INTO medication_lookup VALUES ('5d91f2938cf68888e290deb643b77251', 'Amlodipine');
INSERT INTO medication_lookup VALUES ('90a450310cd0b6074c3a1885cf8e421c', 'Pantoprazole');
INSERT INTO medication_lookup VALUES ('5bc2199d9a9125748c41105f893a3a7e', 'Amoxicillin');

CREATE TABLE patients (
    patient_id TEXT,
    `name` TEXT,
    age TEXT,
    gender TEXT
);

INSERT INTO patients VALUES ('332808b0749fbbd33c631d080d52549d', 'Jane Doe', '72', 'F');
INSERT INTO patients VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', 'Greg Johnson', '55', 'M');
