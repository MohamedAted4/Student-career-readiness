# First set of columns (from your first dataframe)
df1_columns = {
        'Timestamp', 'What is your gender?', 'What is your age?',
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
        'What specific improvements would you like to see in your university’s career preparation programs?',
        'Which elective course have you found most helpful for your career preparation and readiness?.1',
        'Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?.1',
        'Which professional or technical skills do you feel are missing from your university education?.1',
        'What specific improvements would you like to see in your university’s career preparation programs?.1',
        'Which elective course have you found most helpful for your career preparation and readiness?.2',
        'Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?.2',
        'Which professional or technical skills do you feel are missing from your university education?.2',
        'What specific improvements would you like to see in your university’s career preparation programs?.2',
        'Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?.3',
        'Which professional or technical skills do you feel are missing from your university education?.3',
        'What specific improvements would you like to see in your university’s career preparation programs?.3'
}

# Second set of columns (from your second dataframe)
df2_columns ={'What is your gender?', 'What is your age?',
        'What is your current academic level?',
        'Are you aware of your university’s career services?',
        'What is your department?',
        'How many internships have you completed during your studies?',
        'Which types of internships have you completed during your studies, and how many for each type?  [Virtual/Remote Internship]',
        'Which types of internships have you completed during your studies, and how many for each type?  [Industry/Corporate Internship]',
        'Which types of internships have you completed during your studies, and how many for each type?  [Government Internship]',
        'On average, how many hours per week do you spend on self-learning (such as online courses, tutorials, or independent study)?',
        'Have you attended any career-related workshops or training sessions?',
        'Do you have a part-time job while studying? If yes, how many hours per week do you work?',
        'On a scale of 0 to 5, how confident are you in your ability to secure a job after graduation, considering your skills, experience, and job market conditions?',
        'In the past 6 months, how many job applications have you submitted?',
        'How long do you expect it will take to secure a job after graduation?',
        'Have you received any job offers before graduation?',
        'To what extent do you think your university’s career services have helped you prepare for the job market?',
        'On a scale of 1-5, how relevant do you think your university courses are to real-world job requirements?',
        'How would you rate the amount of hands-on training provided by your university?',
        'On a scale of 1-5, how important do you think networking is in securing a job?',
        'Which of the following skills do you think employers value the most in your field?',
        'Which of the following career paths do you prefer?',
        'How many certificates have you achieved so far?',
        'Which elective course have you found most helpful for your career preparation and readiness?',
        'What is your current CGPA?',
        'How many hours per week do you spend on extracurricular ( Non-academic / Supplementary )activities?',
        'What is your expected starting salary after graduation? Please enter the amount in USD ($).',
        'Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?',
        'Which professional or technical skills do you feel are missing from your university education?',
        'What specific improvements would you like to see in your university’s career preparation programs?'}


# Find matching columns using set intersection
matching_columns = df1_columns - df2_columns

for i in matching_columns:
        print("Matching Columns:", i)




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

    # 8 - Very Important Skills
    "OpenAI Gym": 8,
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
    "Koltin": 5,
    "Rust": 5,

    # 4 - Less Common in AI
    "Swift": 4,
    "Oracle": 4,
    "Kafka": 4,
}



