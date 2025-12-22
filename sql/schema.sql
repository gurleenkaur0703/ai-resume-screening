-- Stores basic resume info
CREATE TABLE IF NOT EXISTS resumes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    raw_text TEXT
);

-- Stores extracted skills (normalized)
CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resume_id INTEGER,
    skill TEXT,
    FOREIGN KEY (resume_id) REFERENCES resumes(id)
);

-- Job descriptions uploaded by recruiter
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    required_skills TEXT
);

-- Final matching score
CREATE TABLE IF NOT EXISTS match_scores (
    resume_id INTEGER,
    job_id INTEGER,
    score REAL,
    PRIMARY KEY (resume_id, job_id)
);
