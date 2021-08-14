-- SQLite3 schema for Memory Pill v2.
-- https://github.com/nickbild/memory_pill_v2

CREATE TABLE medication_administrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT,
    medication_id TEXT,
    bottle_opened_at TEXT
);

INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-01 08:04:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-01 17:10:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-02 08:09:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-02 14:21:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-02 17:11:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-03 08:04:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-03 17:13:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-04 08:05:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-04 17:17:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-05 08:01:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-05 17:12:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-06 08:04:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-06 17:12:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-07 08:08:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-07 17:15:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-08 08:06:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-08 17:15:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-09 08:09:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-09 17:19:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-10 17:17:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-11 08:06:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-11 17:17:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-12 08:03:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-12 17:14:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-13 08:01:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-13 17:18:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-14 08:05:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-14 17:16:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-15 08:05:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-15 17:13:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-16 08:02:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-16 17:14:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-17 08:01:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-17 17:11:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-18 08:02:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-18 17:14:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-19 08:25:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-19 17:16:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '2021-08-20 08:54:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '2021-08-20 17:33:00.000000');

INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-01 08:04:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-02 08:09:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-02 08:11:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-03 08:13:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-04 17:17:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-05 08:12:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-06 08:12:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-07 08:15:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-08 08:15:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-09 08:19:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-11 08:06:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-12 08:03:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-13 08:01:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-14 08:05:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-15 08:05:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-16 08:02:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-17 08:01:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-18 08:02:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-19 08:25:00.000000');
INSERT INTO medication_administrations ('patient_id', 'medication_id', 'bottle_opened_at') VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '2021-08-20 08:54:00.000000');

CREATE TABLE medication_schedule (
    patient_id TEXT,
    medication_id TEXT,
    `time` TEXT
);

INSERT INTO medication_schedule VALUES ('332808b0749fbbd33c631d080d52549d', '5d91f2938cf68888e290deb643b77251', '08:00');
INSERT INTO medication_schedule VALUES ('332808b0749fbbd33c631d080d52549d', '90a450310cd0b6074c3a1885cf8e421c', '17:00');
INSERT INTO medication_schedule VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', '5bc2199d9a9125748c41105f893a3a7e', '08:30');

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

ALTER TABLE patients ADD img TEXT;

INSERT INTO patients VALUES ('332808b0749fbbd33c631d080d52549d', 'Jane Doe', '72', 'F');
INSERT INTO patients VALUES ('7ddf32e17a6ac5ce04a8ecbf782ca509', 'Greg Johnson', '55', 'M');
