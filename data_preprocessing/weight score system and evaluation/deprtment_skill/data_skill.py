import pandas as pd
import re
from fuzzywuzzy import fuzz

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



##! Computing & Data Sciences
df_datascience = df[df["What is your department?"] == "Computing & Data Sciences"].copy()
df_datascience.reset_index(drop=True, inplace=True)


# Extract the relevant column and rename for easier reference
df_datascience["skill"] = df_datascience["Reflecting on your studies, which technical skills do you feel most comfortable using or applying?"]



##! Data Science Skills List
data_science_skills = [
    # Programming & Development
    "Python", "R", "SQL", "Java", "C++", "JavaScript", "Go", "Swift",
    
    # Data Analysis & Visualization
    "Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "Dash", 
    "Power BI", "Tableau", "Excel", "Google Sheets", "Data Visualization", "Data Analysis", 
    
    # Machine Learning & AI
    "Scikit-learn", "TensorFlow", "PyTorch", "XGBoost", "LightGBM",
    "Feature Engineering", "Feature Selection", "Model Tuning", "Class Imbalance Handling", 
    "Deep Learning", "NLP", "Computer Vision", "Machine Learning",
    "Artificial Intelligence", "Neural Networks", "Transformers", "LLMs", "GANs", "Reinforcement Learning",

    # Big Data & Cloud Computing
    "Big Data", "AWS", "Google Cloud", "Azure", "Cloud Computing", "Spark", "Hadoop", "Kafka",

    # Databases & Management
    "MySQL", "PostgreSQL", "MongoDB", "Firebase", "SQL Server", "Oracle", 
    "Data Extraction", "Data Cleaning", "Data Manipulation",
    "NoSQL", "Databases",

    # Statistics & Mathematics
    "Statistical Analysis", "Statistics", 
    "Multivariate Analysis", "Stochastic Processes", "Bayesian Statistics", "Linear Algebra",

    # Other Data Science-Related Tools & Concepts
    "Recommendation Systems", "Web Scraping", "BeautifulSoup", "Selenium",
    "Data Structures", "Algorithms", "Dashboards",
    "Software Development", "Critical Thinking", "Problem Solving",
]


normalization_map_datascience = {
    # Programming & Development
    "py": "Python",
    "js": "JavaScript",
    
    # Data Analysis & Visualization
    "pd": "Pandas",
    "np": "NumPy",
    
    # Machine Learning & AI
    "ml": "Machine Learning",
    "dl": "Deep Learning",
    "nlp": "Natural Language Processing",
    "ai": "Artificial Intelligence",
    "cv": "Computer Vision",
    "nn": "Neural Networks",
    "xgb": "XGBoost",


    # Statistics & Mathematics
    "stats": "Statistics",
    "mlmath": "Machine Learning Mathematics",
    "mva": "Multivariate Analysis",
}


def find_fuzzy_matches_datascience(text, terms):
    if pd.isna(text) or not text.strip():
        return set()
    
    text = text.lower()
    matches = set()
    text_words = set(re.findall(r'\w+', text))  # Get all words
    
    for term in terms:
        term_lower = term.lower()
        
        # Skip very short terms unless they're important
        if len(term_lower) < 3 and term_lower not in ['ai', 'r', 'sql']:
            continue
            
        # Check for exact match first
        if re.search(rf'\b{re.escape(term_lower)}\b', text):
            matches.add(term)
            continue
            
        # Calculate similarity scores
        similarity = max(
            fuzz.token_set_ratio(term_lower, text),  # Most reliable
            fuzz.partial_ratio(term_lower, text) * 0.8  # Less weight to partial matches
        )
        
        # Only consider matches with high similarity
        if similarity >= 90:
            matches.add(term)
            
    return matches

def process_skills_column_datascience(skill_text):
    if pd.isna(skill_text) or not skill_text.strip():
        return None
    
    skill_text = skill_text.lower()
    detected_skills = set()

    # Handle special cases and abbreviations
    special_cases = {
        'ai': 'Artificial Intelligence',
        'nlp': 'Natural Language Processing',
        'cv': 'Computer Vision',
        'db': 'Databases',
        'ml': 'Machine Learning'
    }
    
    for short, full in special_cases.items():
        if re.search(rf'\b{short}\b', skill_text):
            detected_skills.add(full)

    # Exact matching with all skills
    pattern = r'\b(' + '|'.join(re.escape(skill.lower()) for skill in data_science_skills) + r')\b'
    exact_matches = re.findall(pattern, skill_text, flags=re.IGNORECASE)
    
    # Handle single-letter skills
    if 'r' in skill_text.split():
        detected_skills.add('R')
    if re.search(r'\bgo\b', skill_text):
        detected_skills.add('Go')

    # Fuzzy matching with higher threshold
    fuzzy_matches = find_fuzzy_matches_datascience(skill_text, data_science_skills)
    
    # Combine and normalize all matches
    all_matches = detected_skills.union(
        {normalization_map_datascience.get(skill.lower(), skill.title()) 
            for skill in exact_matches + list(fuzzy_matches)}
    )
    
    return ", ".join(sorted(all_matches)) if all_matches else None

# Processing pipeline
df_datascience["cleaned_skills"] = df_datascience["skill"].apply(process_skills_column_datascience)

# Create nested list with validation
valid_skills = {s.lower(): s for s in data_science_skills}
valid_skills.update({v.lower(): v for v in normalization_map_datascience.values()})

nested_list_datascience = []
for skills in df_datascience["cleaned_skills"]:
    if pd.isna(skills):
        nested_list_datascience.append([])
    else:
        validated = [valid_skills.get(s.lower(), s) for s in skills.split(", ")]
        nested_list_datascience.append([s for s in validated if s.lower() in valid_skills])




##! evaluation skill for data science

skill_ranking_dict_datascience = {
    # 10 - Core Data Science Skills (Must-have)
    "Python": 10,
    "SQL": 10,
    "Pandas": 10,
    "NumPy": 10,
    "Machine Learning": 10,
    "Artificial Intelligence": 10,
    "Scikit-learn": 10,
    "Deep Learning": 10,
    "Data Analysis": 10,
    "Data Visualization": 10,
    "Critical Thinking": 10,
    "Problem Solving": 10,

    # 9 - Highly Important for DS Work
    "Power BI": 9,
    "Tableau": 9,
    "Feature Engineering": 9,
    "Model Tuning": 9,
    "TensorFlow": 9,
    "PyTorch": 9,
    "XGBoost": 9,
    "LightGBM": 9,
    "NLP": 9,
    "Computer Vision": 9,
    "Big Data": 9,
    "Cloud Computing": 9,
    "Google Cloud": 9,
    "AWS": 9,
    "Statistics": 9,
    "Statistical Analysis": 9,
    "Algorithms": 9,

    # 8 - Very Important Skills
    "R": 8,
    "JavaScript": 8,
    "Matplotlib": 8,
    "Seaborn": 8,
    "Transformers": 8,
    "LLMs": 8,
    "Spark": 8,
    "Hadoop": 8,
    "MySQL": 8,
    "PostgreSQL": 8,
    "Data Cleaning": 8,
    "Feature Selection": 8,
    "Neural Networks": 8,
    "Multivariate Analysis": 8,

    # 7 - Useful in Many DS Scenarios
    "Java": 7,
    "C++": 7,
    "Plotly": 7,
    "Dash": 7,
    "Excel": 7,
    "Google Sheets": 7,
    "Reinforcement Learning": 7,
    "GANs": 7,
    "Azure": 7,
    "MongoDB": 7,
    "SQL Server": 7,
    "Oracle": 7,
    "Data Extraction": 7,
    "Data Manipulation": 7,
    "NoSQL": 7,
    "Databases": 7,
    "Linear Algebra": 7,
    "Recommendation Systems": 7,
    "Web Scraping": 7,
    "BeautifulSoup": 7,
    "Selenium": 7,
    "Data Structures": 7,
    "Dashboards": 7,
    "Software Development": 7,

    # 6 - Good to Have but Not Essential
    "Kafka": 6,
    "Class Imbalance Handling": 6,
    "Bayesian Statistics": 6,
    "Stochastic Processes": 6,

    # 5 - Niche but Useful in Some DS Roles
    "Firebase": 5,

    # 4 - Less Common in DS
    "Go": 4,
    "Swift": 4,
}


##? Function to calculate the score for a student's skills

def calculate_student_score_datascience(skills_list):
    total_score = 0
    for skill in skills_list:
        skill_key = skill.strip().lower()
        standardized_skill = valid_skills.get(skill_key)
        if standardized_skill:
            total_score += skill_ranking_dict_datascience.get(standardized_skill, 0)
    return total_score

# Calculate scores for all students
student_scores_datascience = [calculate_student_score_datascience(skills) for skills in nested_list_datascience]

# Add the scores to the DataFrame
df_datascience["student_skill_score"] = student_scores_datascience

# Display the DataFrame with scores
print(df_datascience[["cleaned_skills", "student_skill_score"]])




print("\n\nSTUDENT SKILL ANALYSIS".center(120, "="))

for index, row in df_datascience[["student_skill_score", "cleaned_skills", "skill"]].iterrows():
    cleaned_skills = str(row['cleaned_skills']).replace("\n", " ")
    original_skill = str(row['skill']).replace("\n", " ")
    score = row['student_skill_score']

    print(f"\nIndex: {index}")
    print(f"Original Skill Text: {original_skill} len {len(original_skill.split(','))}")
    print(f"Detected Skills    : {cleaned_skills} len {len(cleaned_skills.split(','))}")
    print(f"data science Score              : {score}")
    print("-" * 120)






file_path = r"C:\Users\pc\survey\dataset\skill_data\datascience_skill.xlsx" 

df_datascience.to_excel(file_path, index=False)  # index=False prevents writing row numbers