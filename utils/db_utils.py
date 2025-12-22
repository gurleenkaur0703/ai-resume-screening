import os
import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

# -------------------- RESUME --------------------
def insert_resume(name, email, raw_text):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO resumes (name, email, raw_text)
        VALUES (%s, %s, %s)
        RETURNING id
    """, (name, email, raw_text))

    resume_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return resume_id

# -------------------- SKILLS --------------------
def insert_skills(resume_id, skills):
    conn = get_connection()
    cur = conn.cursor()

    for skill in skills:
        cur.execute("""
            INSERT INTO skills (resume_id, skill)
            VALUES (%s, %s)
        """, (resume_id, skill))

    conn.commit()
    cur.close()
    conn.close()

# -------------------- JOB --------------------
def insert_job(title, description, required_skills):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO jobs (title, description, required_skills)
        VALUES (%s, %s, %s)
        RETURNING id
    """, (title, description, ", ".join(required_skills)))

    job_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return job_id

# -------------------- MATCH SCORE --------------------
def insert_match_score(resume_id, job_id, score):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO match_scores (resume_id, job_id, score)
        VALUES (%s, %s, %s)
        ON CONFLICT (resume_id, job_id)
        DO UPDATE SET score = EXCLUDED.score
    """, (resume_id, job_id, score))

    conn.commit()
    cur.close()
    conn.close()

# -------------------- FETCH --------------------
def fetch_all_resumes_with_skills():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT r.id, r.name, r.email, ARRAY_AGG(s.skill)
        FROM resumes r
        LEFT JOIN skills s ON r.id = s.resume_id
        GROUP BY r.id;
    """)

    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows

def fetch_jobs():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, title, required_skills FROM jobs")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows

