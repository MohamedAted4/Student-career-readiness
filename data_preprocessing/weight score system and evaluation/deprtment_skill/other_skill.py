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




##! Other
df_Other = df[df["What is your department?"] == "Other"].copy()
df_Other.reset_index(drop=True, inplace=True)


# Extract the relevant column and rename for easier reference
df_Other["skill"] = df_Other["Reflecting on your studies, which technical skills do you feel most comfortable using or applying?"]



##! the "Other" choice

other_department_skills = [
    # Programming Languages
    "Python", "Java", "C++","C#", "JavaScript", "TypeScript","Rust", "Swift", "Kotlin", "PHP", "Ruby",

    # Frontend Development
    "HTML", "CSS", "JavaScript", "TypeScript", "React", "Vue.js", "Angular", "Tailwind CSS", "SASS", "Bootstrap",

    # Backend Development
    "Node.js", "Express.js", "Django", "Flask", "Spring Boot", "Laravel", "ASP.NET", "Ruby on Rails",

    # Full Stack & General Development
    "REST APIs", "GraphQL", "MVC Architecture", "Microservices", "CI/CD", "Docker", "Kubernetes", "Git", "GitHub", "Bitbucket",

    # Databases
    "MySQL", "PostgreSQL", "MongoDB", "Redis", "SQLite", "Firebase", "Oracle",

    # Mobile Development
    "Android Development", "iOS Development", "Flutter", "React Native", "SwiftUI", "Jetpack Compose",

    # Software Engineering Concepts
    "Object-Oriented Programming", "Design Patterns", "Data Structures", "Algorithms", "Agile Methodologies", "Scrum", "Testing", "Unit Testing", "Integration Testing", "Version Control",

    # DevOps & Cloud
    "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes", "Terraform", "Jenkins",

    # UI/UX & Design
    "Figma", "Adobe XD", "UI Design", "UX Design", "Wireframing", "Prototyping", "Accessibility", "Responsive Design",

    # Digital Marketing
    "SEO", "SEM", "Google Analytics", "Social Media Marketing", "Email Marketing", "Content Marketing", "Google Ads", "Facebook Ads", "Affiliate Marketing",

    # Soft Skills & Others
    "Problem Solving", "Analytical Thinking", "Communication", "Teamwork", "Project Management", "Time Management", "Creativity"
]


other_department_normalization_map = {
    # Programming Languages & Scripting
    "py": "Python",
    "js": "JavaScript",
    "ts": "TypeScript",
    "cpp": "C++",
    "cs": "C#",
    "rb": "Ruby",
    "php": "PHP",
    "kt": "Kotlin",
    "swift": "Swift",
    "java": "Java",

    # Frontend Technologies
    "html": "HTML",
    "css": "CSS",
    "sass": "SASS",
    "less": "LESS",
    "vue": "Vue.js",
    "react": "React",
    "ng": "Angular",

    # Backend & Full-Stack Frameworks
    "node": "Node.js",
    "express": "Express.js",
    "dj": "Django",
    "flask": "Flask",
    "rails": "Ruby on Rails",
    "spring": "Spring Boot",
    "laravel": "Laravel",

    # Mobile App Development
    "flutter": "Flutter",
    "rn": "React Native",
    "xcode": "Xcode",
    "android": "Android Studio",

    # Databases
    "sql": "SQL",
    "mysql": "MySQL",
    "pgsql": "PostgreSQL",
    "mongo": "MongoDB",
    "firebase": "Firebase",

    # DevOps & Version Control
    "git": "Git",
    "gh": "GitHub",
    "ci": "CI/CD",
    "docker": "Docker",
    "k8s": "Kubernetes",

    # UI/UX & Design Tools
    "ux": "UX Design",
    "ui": "UI Design",
    "figma": "Figma",
    "xd": "Adobe XD",
    "ps": "Photoshop",
    "ai": "Adobe Illustrator",

    # Testing & Debugging
    "jest": "Jest",
    "mocha": "Mocha",
    "chai": "Chai",
    "cypress": "Cypress",
    "puppeteer": "Puppeteer",

    # Web Technologies & Concepts
    "seo": "SEO",
    "webp": "Web Performance Optimization",
    "pwa": "Progressive Web Apps",
    "api": "RESTful APIs",
    "graph": "GraphQL",

    # Digital Marketing
    "sem": "SEM",
    "smm": "Social Media Marketing",
    "email": "Email Marketing",
    "ga": "Google Analytics",
    "fbads": "Facebook Ads",
    "gads": "Google Ads",
    "crm": "CRM Tools",
    "cms": "CMS",
    "wordpress": "WordPress",
    "shopify": "Shopify",

    # Soft Skills
    "team": "Teamwork",
    "comm": "Communication",
    "agile": "Agile Development",
    "scrum": "Scrum",
    "pm": "Project Management",
    "design": "Design Thinking"
}




def find_fuzzy_matches_other(text, terms):
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
        
        if adjusted_score >= 85:  # High threshold for precision
            matches.add(term)
            
    return matches

def process_skills_column_other(skill_text, skills_list=other_department_skills, normalization_map=other_department_normalization_map):
    if pd.isna(skill_text) or not skill_text.strip():
        return None
    
    skill_text = skill_text.lower()
    detected_skills = set()

    # Exact matching (case-insensitive)
    pattern = r'\b(' + '|'.join(re.escape(skill.lower()) for skill in skills_list) + r')\b'
    exact_matches = re.findall(pattern, skill_text)
    
    # Handle special cases (e.g., "C", "R", "Go")
    single_char_skills = {"c", "r", "go"}  # Add others as needed
    for char in single_char_skills:
        if re.search(rf'\b{char}\b', skill_text):
            exact_matches.append(char.upper() if char == "c" else char.title())

    # Fuzzy matching
    fuzzy_matches = find_fuzzy_matches_other(skill_text, skills_list)
    
    # Normalize and combine
    all_matches = set()
    for skill in exact_matches + list(fuzzy_matches):
        normalized = normalization_map.get(skill.lower(), skill)
        all_matches.add(normalized)
    
    return ", ".join(sorted(all_matches)) if all_matches else None

# ===== PROCESSING PIPELINE =====
# Assuming df_other is your DataFrame with a "skill" column
df_Other["cleaned_skills"] = (
    df_Other["skill"]
    .apply(process_skills_column_other)
    .apply(lambda x: ", ".join(sorted(set(s.strip() for s in x.split(",")))) if pd.notna(x) else None)
)

# Output nested list (for further analysis)
nested_list_other = [
    [skill for skill in skills.split(", ")] 
    if pd.notna(skills) else [] 
    for skills in df_Other["cleaned_skills"]
]





##! evaluation skill for other department

other_department_skill_ranking = {
    # 10 - Core CS & Development Skills (Must-have)
    "Python": 10,
    "Java": 10,
    "JavaScript": 10,
    "HTML": 10,
    "CSS": 10,
    "React": 10,
    "Node.js": 10,
    "Git": 10,
    "GitHub": 10,
    "MySQL": 10,
    "REST APIs": 10,
    "Data Structures": 10,
    "Algorithms": 10,
    "Problem Solving": 10,

    # 9 - Highly Important
    "TypeScript": 9,
    "C++": 9,
    "C#": 9,
    "MongoDB": 9,
    "PostgreSQL": 9,
    "Express.js": 9,
    "Docker": 9,
    "Kubernetes": 9,
    "Firebase": 9,
    "Scrum": 9,
    "Object-Oriented Programming": 9,
    "Design Patterns": 9,
    "CI/CD": 9,
    "Agile Methodologies": 9,

    # 8 - Very Important Skills
    "Vue.js": 8,
    "Angular": 8,
    "Flask": 8,
    "Django": 8,
    "GraphQL": 8,
    "SQLite": 8,
    "Google Cloud": 8,
    "AWS": 8,
    "Azure": 8,
    "Version Control": 8,
    "Testing": 8,
    "Unit Testing": 8,
    "Integration Testing": 8,

    # 7 - Widely Useful & Valued
    "Swift": 7,
    "Kotlin": 7,
    "PHP": 7,
    "Spring Boot": 7,
    "Laravel": 7,
    "Android Development": 7,
    "iOS Development": 7,
    "React Native": 7,
    "Flutter": 7,
    "Tailwind CSS": 7,
    "Bootstrap": 7,
    "Wireframing": 7,
    "Responsive Design": 7,
    "Teamwork": 7,
    "Communication": 7,

    # 6 - Good to Have but Not Essential
    "ASP.NET": 6,
    "Ruby": 6,
    "Ruby on Rails": 6,
    "SwiftUI": 6,
    "Jetpack Compose": 6,
    "Adobe XD": 6,
    "Prototyping": 6,
    "UI Design": 6,
    "UX Design": 6,
    "Accessibility": 6,
    "Figma": 6,
    "Terraform": 6,
    "Jenkins": 6,

    # 5 - Niche but Useful in Some Roles
    "Google Analytics": 5,
    "SEO": 5,
    "SEM": 5,
    "Google Ads": 5,
    "Facebook Ads": 5,
    "Content Marketing": 5,
    "Affiliate Marketing": 5,
    "Email Marketing": 5,
    "Social Media Marketing": 5,

    # 4 - Less Common in Core CS Roles
    "Bitbucket": 4,
    "Project Management": 4,
    "Time Management": 4,
    "Creativity": 4,

    # 3 - Rarely Needed in General Dev
    "macOS": 3,
    "Oracle": 3
}


##? Function to calculate the score for a student's skills

def calculate_student_score_other(skills_list):
    if not skills_list:  # Handle empty input
        return 0
        
    total_score = 0
    
    for raw_skill in skills_list:
        if not raw_skill.strip():  # Skip empty strings
            continue
            
        # Normalize the skill name (title case, strip whitespace)
        skill = raw_skill.strip().title()
        
        # Exact match first
        if skill in other_department_skill_ranking:
            total_score += other_department_skill_ranking[skill]
            continue
            
        # Try matching with different case variations if exact match fails
        for stored_skill, score in other_department_skill_ranking.items():
            if skill.lower() == stored_skill.lower():
                total_score += score
                break
                
    return total_score



# Calculate scores for all students
student_scores_other = [calculate_student_score_other(skills) for skills in nested_list_other]

# Add the scores to the DataFrame
df_Other["student_skill_score"] = student_scores_other


print("\n\nSTUDENT SKILL ANALYSIS".center(120, "="))

# Display detailed analysis
for index, row in df_Other[["student_skill_score", "cleaned_skills", "skill"]].iterrows():
    cleaned_skills = str(row['cleaned_skills']).replace("\n", " ")
    original_skill = str(row['skill']).replace("\n", " ")
    score = row['student_skill_score']

    print(f"\nIndex: {index}")
    print(f"Original Skill Text : {original_skill} len {len(original_skill.split(','))}")
    print(f"Detected AI Skills  : {cleaned_skills} len {len(cleaned_skills.split(','))}")
    print(f"other Skill Score      : {score}")
    print("-" * 120)






file_path = r"C:\Users\pc\survey\dataset\skill_data\other_skill.xlsx" 

df_Other.to_excel(file_path, index=False)  # index=False prevents writing row numbers