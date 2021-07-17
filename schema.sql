CREATE TABLE medication_administrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT,
    medication_id TEXT,
    bottle_opened_at TEXT
);
