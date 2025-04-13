


import pandas as pd
import re
from fuzzywuzzy import fuzz

# Load dataset
df = pd.read_excel(r"C:\Users\pc\survey\dataset\cleaned_data.xlsx")





column_clean = [
    'gender','age','current_academic_leve','CGPA', 'aware_of_university’s_career_services', 'department',
    'num_internships_completed','types_and_num_of_internships_completed(Virtual/Remote)','types_and_num_of_internships_completed(Industry/Corporate)',
    'types_and_num_of_internships_completed(Government)','hours_per_week_spend_on_extracurricular(Non-academic/Supplementary)',
    'hours_per_week_spend_on_self-learning','attended_any_career-related',
    'part-time_job','confidence_in_finding_job_after_graduation','job_applications_submitted_last6_manths',
    'expect_scope_to_find_job_after_graduation','received_any_job_offers','expected_starting_salary',
    'university_career_services_helped_you_prepare_for_job',
    'how_relevant_university_courses_real-world_job_requirements','skills_needed_to_employers_value_most_in_your_field',
    'rate_amount_of_hands-on_training_provided_by_university','important_networking','number_of_certificates',
    'career_paths_prefer','skill','elective_course_found_helpful','courses_outside_found_particularly_impactful_should_be_added',
    'professional/technical_skills_feel_missing_in_university','specific_improvements_would_you_like_to_see_in_university']




df = df[[col for col in column_clean if col in df.columns]]



column_old=[
        'What is your gender?', 'What is your age?',
        'What is your current academic level?', 'What is your current CGPA?',
        'Are you aware of your university’s career services?',
        'What is your department?',
        'How many internships have you completed during your studies?',
        'Which types of internships have you completed during your studies, and how many for each type?  [Virtual/Remote Internship]',
        'Which types of internships have you completed during your studies, and how many for each type?  [Industry/Corporate Internship]',
        'Which types of internships have you completed during your studies, and how many for each type?  [Government Internship]',
        'How many hours per week do you spend on extracurricular ( Non-academic / Supplementary )activities?',
        'On average, how many hours per week do you spend on self-learning (such as online courses, tutorials, or independent study)?',
        'Have you attended any career-related workshops or training sessions?',
        'Do you have a part-time job while studying? If yes, how many hours per week do you work?',
        'On a scale of 0 to 5, how confident are you in your ability to secure a job after graduation, considering your skills, experience, and job market conditions?',  
        'In the past 6 months, how many job applications have you submitted?',
        'How long do you expect it will take to secure a job after graduation?',
        'Have you received any job offers before graduation?',
        'What is your expected starting salary after graduation? Please enter the amount in USD ($).',
        'To what extent do you think your university’s career services have helped you prepare for the job market?',
        'On a scale of 1-5, how relevant do you think your university courses are to real-world job requirements?',
        'Which of the following skills do you think employers value the most in your field?',
        'How would you rate the amount of hands-on training provided by your university?',
        'On a scale of 1-5, how important do you think networking is in securing a job?',
        'How many certificates have you achieved so far?',
        'Which of the following career paths do you prefer?',
        'Reflecting on your studies, which technical skills do you feel most comfortable using or applying?',
        'Which elective course have you found most helpful for your career preparation and readiness?',
        'Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?',
        'Which professional or technical skills do you feel are missing from your university education?',
        'What specific improvements would you like to see in your university’s career preparation programs?']



df = df.rename(columns=dict(zip(df.columns, column_old)))




##! Cybersecurity
df_Cybersecurity = df[df["What is your department?"] == "Cybersecurity"].copy()
df_Cybersecurity.reset_index(drop=True, inplace=True)



df_Cybersecurity["skill"] = df_Cybersecurity["Reflecting on your studies, which technical skills do you feel most comfortable using or applying?"]



##! Cyber security Skills List
cybersecurity_skills = [
    # Programming & Scripting
    "Python","C++", "Java", "JavaScript", "PowerShell", "Bash","Rust",

    # Networking & Protocols
    "Networking", "TCP/IP", "UDP", "HTTP", "HTTPS", "DNS", "SSL/TLS", "VPN", "Firewall Configuration",

    # Operating Systems & Environments
    "Linux", "Windows", "macOS", "Kali Linux", "Virtual Machines", "WSL",

    # Tools & Platforms
    "Wireshark", "Nmap", "Metasploit", "Burp Suite", "Snort", "OpenVAS", "Nikto", "Aircrack-ng",
    "Splunk", "ELK Stack", "SIEM Tools", "Tshark",

    # Security Concepts & Practices
    "Penetration Testing", "Vulnerability Assessment", "Risk Assessment", "Threat Modeling",
    "Network Security", "Web Security", "Endpoint Security", "Cloud Security",
    "Application Security", "Red Teaming", "Blue Teaming", "Purple Teaming",
    "Incident Response", "Digital Forensics", "Reverse Engineering",

    # Cryptography
    "Cryptography", "Public Key Infrastructure", "Hashing Algorithms", "Encryption Standards",
    "SSL Certificates", "Key Exchange Protocols",

    # Governance, Risk & Compliance (GRC)
    "Security Auditing", "ISO 27001", "NIST Framework", "SOC 2", "GDPR", "HIPAA", "Compliance Management",

    # Identity & Access Management
    "IAM", "Active Directory", "LDAP", "MFA", "SSO", "OAuth", "RBAC", "Access Control",

    # Cloud & DevSecOps
    "AWS Security", "Azure Security", "Google Cloud Security", "Docker Security", "Kubernetes Security",
    "CI/CD Security", "Infrastructure as Code", "Terraform Security", "Secrets Management",

    # Soft Skills & Mindset
    "Analytical Thinking", "Problem Solving", "Attention to Detail", "Communication Skills", "Ethical Hacking",
    "Security Awareness Training"
]


cybersecurity_normalization_map = {
    # Programming & Scripting
    "py": "Python",
    "ps": "PowerShell",
    "bash": "Bash",
    "js": "JavaScript",
    "cpp": "C++",

    # Networking & Protocols
    "tcp": "TCP/IP",
    "udp": "UDP",
    "dns": "DNS",
    "http": "HTTP",
    "https": "HTTPS",
    "tls": "SSL/TLS",
    "ssl": "SSL/TLS",

    # Operating Systems & Environments
    "win": "Windows",
    "linux": "Linux",
    "mac": "macOS",
    "vm": "Virtual Machines",
    "kali": "Kali Linux",

    # Tools & Platforms
    "burp": "Burp Suite",
    "nmap": "Nmap",
    "msf": "Metasploit",
    "wireshark": "Wireshark",
    "siem": "SIEM Tools",
    "elk": "ELK Stack",
    "openvas": "OpenVAS",
    "snort": "Snort",

    # Security Concepts & Practices
    "pentest": "Penetration Testing",
    "redteam": "Red Teaming",
    "blueteam": "Blue Teaming",
    "forensics": "Digital Forensics",
    "reveng": "Reverse Engineering",
    "appsec": "Application Security",
    "cloudsec": "Cloud Security",
    "netsec": "Network Security",
    "infosec": "Information Security",

    # Cryptography
    "crypto": "Cryptography",
    "pki": "Public Key Infrastructure",
    "enc": "Encryption Standards",
    "hashing": "Hashing Algorithms",

    # Identity & Access Management
    "ad": "Active Directory",
    "iam": "IAM",
    "mfa": "MFA",
    "sso": "SSO",
    "rbac": "RBAC",

    # Cloud & DevSecOps
    "awssec": "AWS Security",
    "azures": "Azure Security",
    "gcpsec": "Google Cloud Security",
    "iac": "Infrastructure as Code",
    "devsecops": "CI/CD Security",
    "terraform": "Terraform Security",

    # Governance, Risk & Compliance
    "iso": "ISO 27001",
    "nist": "NIST Framework",
    "gdpr": "GDPR",
    "soc2": "SOC 2",
    "hipaa": "HIPAA",

    # Other
    "secawareness": "Security Awareness Training",
    "attention": "Attention to Detail",
    "ethhack": "Ethical Hacking"
}


def find_fuzzy_matches_cyber(text, terms):
    matches = set()
    text = text.lower()
    text_words = set(text.split())
    
    for term in terms:
        term_lower = term.lower()
        
        # Skip clearly wrong matches for single-word terms
        if len(term_lower.split()) == 1 and len(term_lower) < len(text.split()[0]):
            continue
            
        # Require multi-word terms to share at least one full word
        if len(term_lower.split()) > 1 and not any(word in text_words for word in term_lower.split()):
            continue
            
        score = max(
            fuzz.partial_ratio(term_lower, text),
            fuzz.token_set_ratio(term_lower, text)
        )
        
        # Penalize length differences
        length_diff = abs(len(term_lower) - len(text)) / max(len(term_lower), len(text))
        adjusted_score = score * (1 - length_diff)
        
        if adjusted_score >= 90:  # High threshold for precision
            matches.add(term)
            
    return matches

def process_skills_column_cyber(skill_text, skills_list=cybersecurity_skills, normalization_map=cybersecurity_normalization_map):
    if pd.isna(skill_text) or not skill_text.strip():
        return None
    
    skill_text = skill_text.lower()
    detected_skills = set()

    # Exact matching (case-insensitive)
    pattern = r'\b(' + '|'.join(re.escape(skill.lower()) for skill in skills_list) + r')\b'
    exact_matches = re.findall(pattern, skill_text)
    
    # Handle special cases (e.g., "C", "Rust", "Go")
    single_char_skills = {"c", "go", "r"}  # Add others as needed
    for char in single_char_skills:
        if re.search(rf'\b{char}\b', skill_text):
            exact_matches.append(char.upper() if char == "c" else char.title())

    # Fuzzy matching
    fuzzy_matches = find_fuzzy_matches_cyber(skill_text, skills_list)
    
    # Normalize and combine
    all_matches = set()
    for skill in exact_matches + list(fuzzy_matches):
        normalized = normalization_map.get(skill.lower(), skill)
        all_matches.add(normalized)
    
    return ", ".join(sorted(all_matches)) if all_matches else None

# ===== PROCESSING PIPELINE =====
# cyber
df_Cybersecurity["cleaned_skills"] = (
    df_Cybersecurity["skill"]
    .apply(process_skills_column_cyber)
    .apply(lambda x: ", ".join(sorted(set(s.strip() for s in x.split(",")))) if pd.notna(x) else None)
)

# Output nested list (for further analysis)
nested_list_cyber = [
    [skill for skill in skills.split(", ")] 
    if pd.notna(skills) else [] 
    for skills in df_Cybersecurity["cleaned_skills"]
]



##! evaluation skill for cyber security

cybersecurity_skill_ranking = {
    # 10 - Core Cybersecurity Skills (Must-have)
    "Python": 10,
    "Linux": 10,
    "Networking": 10,
    "TCP/IP": 10,
    "Penetration Testing": 10,
    "Vulnerability Assessment": 10,
    "Risk Assessment": 10,
    "Incident Response": 10,
    "Cryptography": 10,
    "Wireshark": 10,
    "Firewalls": 10,
    "Security Auditing": 10,

    # 9 - Highly Important
    "Nmap": 9,
    "Metasploit": 9,
    "Threat Modeling": 9,
    "Web Security": 9,
    "Endpoint Security": 9,
    "SIEM Tools": 9,
    "Digital Forensics": 9,
    "IAM": 9,
    "Public Key Infrastructure": 9,
    "Encryption Standards": 9,
    "Red Teaming": 9,
    "Blue Teaming": 9,
    "Burp Suite": 9,
    "Cloud Security": 9,
    "Active Directory": 9,

    # 8 - Very Important Skills
    "Windows": 8,
    "Bash": 8,
    "PowerShell": 8,
    "SSL/TLS": 8,
    "Hashing Algorithms": 8,
    "OpenVAS": 8,
    "Snort": 8,
    "Reverse Engineering": 8,
    "SIEM Tools": 8,
    "OAuth": 8,
    "GDPR": 8,
    "AWS Security": 8,

    # 7 - Useful in Many Security Scenarios
    "JavaScript": 7,
    "Java": 7,
    "DNS": 7,
    "Nikto": 7,
    "Tshark": 7,
    "Application Security": 7,
    "SOC 2": 7,
    "MFA": 7,
    "Docker Security": 7,
    "CI/CD Security": 7,
    "Azure Security": 7,

    # 6 - Good to Have but Not Essential
    "Google Cloud Security": 6,
    "LDAP": 6,
    "macOS": 6,
    "Kali Linux": 6,
    "Aircrack-ng": 6,
    "HIPAA": 6,
    "Terraform Security": 6,
    "Secrets Management": 6,
    "Compliance Management": 6,

    # 5 - Niche but Useful in Some Roles
    "RBAC": 5,
    "Infrastructure as Code": 5,
    "Key Exchange Protocols": 5,
    "Security Awareness Training": 5,

    # 4 - Less Common but Still Valuable
    "ELK Stack": 4,
    "Kubernetes Security": 4,
    "Virtual Machines": 4,

    # 3 - Rarely Used in Entry-Level Roles
    "Rust": 3,
    "WSL": 3,

    # 2 - Minimal Use for Most
    "Scala": 2,
    "Koltin": 2,

    # 1 - Rare Cases Only
    "IoT": 1,
    "Ethical Hacking": 1
}



##? Function to calculate the score for a student's skills

def calculate_student_score_cyber(skills_list):
    if not skills_list:  # Handle empty input
        return 0
        
    total_score = 0
    
    for raw_skill in skills_list:
        if not raw_skill.strip():  # Skip empty strings
            continue
            
        # Normalize the skill name (title case, strip whitespace)
        skill = raw_skill.strip().title()
        
        # Exact match first
        if skill in cybersecurity_skill_ranking:
            total_score += cybersecurity_skill_ranking[skill]
            continue
            
        # Try matching with different case variations if exact match fails
        for stored_skill, score in cybersecurity_skill_ranking.items():
            if skill.lower() == stored_skill.lower():
                total_score += score
                break
                
    return total_score

# Calculate scores for all students
student_scores_cyber = [calculate_student_score_cyber(skills) for skills in nested_list_cyber]

# Add the scores to the DataFrame
df_Cybersecurity["student_skill_score"] = student_scores_cyber




print("\n\nSTUDENT SKILL ANALYSIS".center(120, "="))

# Display detailed analysis
for index, row in df_Cybersecurity[["student_skill_score", "cleaned_skills", "skill"]].iterrows():
    cleaned_skills = str(row['cleaned_skills']).replace("\n", " ")
    original_skill = str(row['skill']).replace("\n", " ")
    score = row['student_skill_score']

    print(f"\nIndex: {index}")
    print(f"Original Skill Text : {original_skill} len {len(original_skill.split(','))}")
    print(f"Detected AI Skills  : {cleaned_skills} len {len(cleaned_skills.split(','))}")
    print(f"cyber Skill Score      : {score}")
    print("-" * 120)






file_path = r"C:\Users\pc\survey\dataset\skill_data\cyber_skill.xlsx" 

df_Cybersecurity.to_excel(file_path, index=False)  # index=False prevents writing row numbers