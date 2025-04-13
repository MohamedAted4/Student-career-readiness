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




##! Intelligent Systems
df_IntelligentSystems = df[df["What is your department?"] == "Intelligent Systems"].copy()
df_IntelligentSystems.reset_index(drop=True, inplace=True)




df_IntelligentSystems["skill"] = df_IntelligentSystems["Reflecting on your studies, which technical skills do you feel most comfortable using or applying?"]


##!Intelligent Systems Skills List
Intelligent_Systems_skills = [
    # Programming & Development
    "Python", "R", "SQL", "Java", "C++", "JavaScript", "Go", "Swift", "Scala", "Kotlin", "Rust", "CUDA",

    # Machine Learning & AI
    "Scikit-learn", "TensorFlow", "PyTorch", "XGBoost", "LightGBM", "Keras",
    "Feature Engineering", "OpenCV", "YOLO", "Image Classification", "Object Detection", "Face Recognition",
    "Deep Learning", "NLP", "Computer Vision", "Machine Learning", "Hugging Face Transformers", "OpenAI gym", 
    "Detectron2", "Autoencoders", "CNNs", "RNNs", "Artificial Intelligence", 
    "Neural Networks", "Transformers", "LLMs", "GANs", "Reinforcement Learning", "Recommendation Systems",

    # Big Data & Cloud Computing
    "Big Data", "AWS", "Google Cloud", "Azure", "Cloud Computing", "Spark", "Hadoop", "Kafka", "MLlib",

    # Databases & Management
    "MySQL", "PostgreSQL", "MongoDB", "Firebase", "SQL Server", "Oracle",
    "Data Extraction", "Data Cleaning", "Data Manipulation",
    "NoSQL", "Databases", "Neo4j",

    # Mathematics & AI Foundations
    "Linear Algebra", "Probability & Statistics", "Bayesian Methods", "Optimization",

    # Other Related Tools & Concepts
    "IoT", "Model Compression", "Deployment",
    "AI Ethics", "Algorithms", "Edge AI",
    "AI Security", "Critical Thinking", "Problem Solving"
]


normalization_map_Ai = {
    # Programming
    "py": "Python",
    "js": "JavaScript",

    # Libraries
    "pd": "Pandas",
    "np": "NumPy",
    "tf": "TensorFlow",
    "sklearn": "Scikit-learn",
    "torch": "PyTorch",
    "cv": "Computer Vision",
    "xgb": "XGBoost",

    # AI Concepts
    "ml": "Machine Learning",
    "dl": "Deep Learning",
    "rl": "Reinforcement Learning",
    "ai": "Artificial Intelligence",
    "nlp": "Natural Language Processing",
    "nn": "Neural Networks",
    "llm": "LLMs",
    "gan": "GANs",

    # Math
    "stats": "Statistics",
    "mva": "Multivariate Analysis",
    "bayes": "Bayesian Statistics",
    "opt": "Optimization",

    # Data Tasks
    "eda": "Data Analysis",
    "vis": "Data Visualization",
}


def find_fuzzy_matches_ai(text, terms):
    matches = set()
    text = text.lower()
    text_words = set(text.split())
    
    for term in terms:
        term_lower = term.lower()
        
        # Skip clearly wrong matches (e.g., "ja" shouldn't match "Java")
        if len(term_lower.split()) == 1 and len(term_lower) < 3:
            continue
            
        # Require multi-word terms to share at least one full word
        if len(term_lower.split()) > 1 and not any(word in text_words for word in term_lower.split()):
            continue
            
        score = max(
            fuzz.partial_ratio(term_lower, text),
            fuzz.token_set_ratio(term_lower, text)
        )
        
        # Penalize length differences more aggressively for short terms
        length_diff = abs(len(term_lower) - len(text)) / max(len(term_lower), len(text))
        adjusted_score = score * (1 - length_diff * 1.2)  # Increased penalty
        
        if adjusted_score >= 90:  # Higher threshold for precision
            matches.add(term)
            
    return matches

def process_skills_column_ai(skill_text):
    if pd.isna(skill_text) or not skill_text.strip():
        return None
    
    skill_text = skill_text.lower()
    detected_skills = set()

    # Step 1: Normalize using mapping (e.g., "prob" → "Problem Solving")
    for term, normalized in normalization_map_Ai.items():
        if re.search(rf'\b{re.escape(term)}\b', skill_text, flags=re.IGNORECASE):
            detected_skills.add(normalized.lower())  # Store lowercase for deduplication

    # Step 2: Exact matching with full skill names (case-insensitive)
    pattern = r'\b(' + '|'.join(re.escape(skill.lower()) for skill in Intelligent_Systems_skills) + r')\b'
    exact_matches = re.findall(pattern, skill_text, flags=re.IGNORECASE)
    
    # Step 3: Handle single-letter skills ("R", "Go", etc.)
    single_letter_skills = {"r", "c", "go"}
    for char in single_letter_skills:
        if re.search(rf'\b{char}\b', skill_text, flags=re.IGNORECASE):
            exact_matches.append(char.upper() if char == "r" else char.title())

    # Step 4: Fuzzy matching (adjust thresholds to avoid overmatching)
    fuzzy_matches = find_fuzzy_matches_ai(skill_text, Intelligent_Systems_skills)
    
    # Step 5: Combine all matches, normalize case, and deduplicate
    all_matches = set()
    for skill in exact_matches + list(fuzzy_matches) + list(detected_skills):
        normalized = normalization_map_Ai.get(skill.lower(), skill)
        all_matches.add(normalized.lower())  # Force lowercase for deduplication

    # Step 6: Restore original capitalization from Intelligent_Systems_skills
    final_skills = []
    for skill_lower in all_matches:
        # Find the correctly capitalized version from the original list
        original_skill = next(
            (s for s in Intelligent_Systems_skills if s.lower() == skill_lower),
            skill_lower.title()  # Fallback if not found
        )
        final_skills.append(original_skill)

    return ", ".join(sorted(set(final_skills))) if final_skills else None




# Processing pipeline (assuming df_ai is your DataFrame)
df_IntelligentSystems["cleaned_skills"] = (
    df_IntelligentSystems["skill"]
    .apply(process_skills_column_ai)
    .apply(lambda x: ", ".join(sorted(set(s.strip() for s in x.split(",")))) if pd.notna(x) else None)
)

# Generate nested list for further analysis
nested_skills_ai = [
    [skill for skill in skills.split(", ")] 
    if pd.notna(skills) else [] 
    for skills in df_IntelligentSystems["cleaned_skills"]
]








##! evaluation skill for intelligent system

AI_skill_ranking_ranking = {

    # 10 - Core AI Skills (Must-have)
    "Python": 10,
    "Deep Learning": 10,
    "Machine Learning": 10,
    "Artificial Intelligence": 10,
    "Neural Networks": 10,
    "Computer Vision": 10,
    "NLP": 10,
    "TensorFlow": 10,
    "PyTorch": 10,
    "Scikit-learn": 10,
    "Keras": 10,
    "CNNs": 10,
    "RNNs": 10,
    "Transformers": 10,
    "LLMs": 10,
    "Critical Thinking": 10,
    "Problem Solving": 10,

    # 9 - Highly Important for AI Work
    "XGBoost": 9,
    "LightGBM": 9,
    "Feature Engineering": 9,
    "YOLO": 9,
    "OpenCV": 9,
    "Image Classification": 9,
    "Object Detection": 9,
    "Hugging Face Transformers": 9,
    "Autoencoders": 9,
    "Reinforcement Learning": 9,
    "Recommendation Systems": 9,
    "SQL": 9,
    "CUDA": 9,
    "Optimization": 9,
    "AI Ethics": 9,
    "Algorithms": 9,

    "Face Recognition": 9,
    "Natural Language Processing": 10,  # For NLP


    # 8 - Very Important Skills
    "OpenAI gym": 8,
    "Detectron2": 8,
    "GANs": 8,
    "Bayesian Methods": 8,
    "Probability & Statistics": 8,
    "Spark": 8,
    "MLlib": 8,
    "Google Cloud": 8,
    "AWS": 8,
    "Cloud Computing": 8,
    "Linear Algebra": 8,
    "Data Cleaning": 8,
    "Data Manipulation": 8,

    # 7 - Useful in Many AI Scenarios
    "Java": 7,
    "C++": 7,
    "R": 7,
    "SQL Server": 7,
    "MongoDB": 7,
    "Data Extraction": 7,
    "NoSQL": 7,
    "Databases": 7,
    "Neo4j": 7,
    "Azure": 7,
    "Hadoop": 7,
    "Big Data": 7,
    "Model Compression": 7,

    # 6 - Good to Have but Not Essential
    "Firebase": 6,
    "PostgreSQL": 6,
    "JavaScript": 6,
    "Edge AI": 6,
    "AI Security": 6,
    "Deployment": 6,
    "IoT": 6,

    # 5 - Niche but Useful in Some AI Roles
    "Go": 5,
    "Scala": 5,
    "Kotlin": 5,
    "Rust": 5,

    # 4 - Less Common in AI
    "Swift": 4,
    "Oracle": 4,
    "Kafka": 4,
}



##? Function to calculate the score for a student's skills

def calculate_student_score_ai(skills_list):
    if not skills_list:  # Handle empty input
        return 0
        
    total_score = 0
    
    for raw_skill in skills_list:
        if not raw_skill.strip():  # Skip empty strings
            continue
            
        # Normalize the skill name (title case, strip whitespace)
        skill = raw_skill.strip().title()
        
        # Exact match first
        if skill in AI_skill_ranking_ranking:
            total_score += AI_skill_ranking_ranking[skill]
            continue
            
        # Try matching with different case variations if exact match fails
        for stored_skill, score in AI_skill_ranking_ranking.items():
            if skill.lower() == stored_skill.lower():
                total_score += score
                break
                
    return total_score






# Calculate scores for all students
student_scores_ai = [calculate_student_score_ai(skills) for skills in nested_skills_ai]

# Add the scores to the DataFrame
df_IntelligentSystems["student_skill_score"] = student_scores_ai

# Display the DataFrame with scores
print(df_IntelligentSystems[["cleaned_skills", "student_skill_score"]])








print("\n\nSTUDENT SKILL ANALYSIS".center(120, "="))

# Display detailed analysis
for index, row in df_IntelligentSystems[["student_skill_score", "cleaned_skills", "skill"]].iterrows():
    cleaned_skills = str(row['cleaned_skills']).replace("\n", " ")
    original_skill = str(row['skill']).replace("\n", " ")
    score = row['student_skill_score']

    print(f"\nIndex: {index}")
    print(f"Original Skill Text : {original_skill} len {len(original_skill.split(','))}")
    print(f"Detected AI Skills  : {cleaned_skills} len {len(cleaned_skills.split(','))}")
    print(f"AI Skill Score      : {score}")
    print("-" * 120)







file_path = r"C:\Users\pc\survey\dataset\skill_data\ai_skill.xlsx" 

df_IntelligentSystems.to_excel(file_path, index=False)  # index=False prevents writing row numbers