import pandas as pd 




path_data_science = r"C:\Users\pc\survey\dataset\skill_data\datascience_skill.xlsx"
path_intelligent_systems = r"C:\Users\pc\survey\dataset\skill_data\ai_skill.xlsx"
path_cybersecurity = r"C:\Users\pc\survey\dataset\skill_data\cyber_skill.xlsx"
path_other=r"C:\Users\pc\survey\dataset\skill_data\other_skill.xlsx"

df_data_science = pd.read_excel(path_data_science)
df_intelligent_systems = pd.read_excel(path_intelligent_systems)
df_cybersecurity = pd.read_excel(path_cybersecurity)
df_other = pd.read_excel(path_other)



alldata=pd.concat([df_data_science,df_intelligent_systems,df_cybersecurity,df_other],axis=0,ignore_index=True)



evaluated=alldata[[
            "What is your current academic level?",
            'What is your current CGPA?',
            'Are you aware of your university’s career services?',
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
            'Have you received any job offers before graduation?',
            'On a scale of 1-5, how important do you think networking is in securing a job?',
            'How many certificates have you achieved so far?',
            "cleaned_skills",
            'student_skill_score'
            ]].copy()



column_rename_map = {
    "What is your current academic level?": "Academic_Level",
    "What is your current CGPA?": "CGPA",
    "Are you aware of your university’s career services?": "Career_Services_Aware",
    "How many internships have you completed during your studies?": "Internships_Completed",
    "Which types of internships have you completed during your studies, and how many for each type?  [Virtual/Remote Internship]": "Virtual_Internships",
    "Which types of internships have you completed during your studies, and how many for each type?  [Industry/Corporate Internship]": "Industry_Internships",
    "Which types of internships have you completed during your studies, and how many for each type?  [Government Internship]": "Gov_Internships",
    "How many hours per week do you spend on extracurricular ( Non-academic / Supplementary )activities?": "Extracurricular_Hours",
    "On average, how many hours per week do you spend on self-learning (such as online courses, tutorials, or independent study)?": "Self_Learning_Hours",
    "Have you attended any career-related workshops or training sessions?": "Career_Workshops_Attended",
    "Do you have a part-time job while studying? If yes, how many hours per week do you work?": "PartTime_Job_Hours",
    "On a scale of 0 to 5, how confident are you in your ability to secure a job after graduation, considering your skills, experience, and job market conditions?": "Job_Confidence",
    "In the past 6 months, how many job applications have you submitted?": "Job_Applications",
    "Have you received any job offers before graduation?": "Job_Offers_Received",
    "On a scale of 1-5, how important do you think networking is in securing a job?": "Networking_Importance",
    "How many certificates have you achieved so far?": "Certificates_Achieved",
    "cleaned_skills":"Student_skill",
    "student_skill_score": "Skill_Score"
}

evaluated.rename(columns=column_rename_map, inplace=True)



# Display detailed analysis
for index, row in alldata[["student_skill_score", "cleaned_skills", "skill"]].iterrows():
    cleaned_skills = str(row['cleaned_skills']).replace("\n", " ")
    original_skill = str(row['skill']).replace("\n", " ")
    score = row['student_skill_score']

    print(f"\nIndex: {index}")
    print(f"Original Skill Text : {original_skill} len {len(original_skill.split(','))}")
    print(f"Detected AI Skills  : {cleaned_skills} len {len(cleaned_skills.split(','))}")
    print(f" Skill Score      : {score}")
    print("-" * 120)



alldata.drop(["skill"],axis=1,inplace=True)

file_path = r"C:\Users\pc\survey\dataset\student_evaluation.xlsx"
evaluated.to_excel(file_path, index=False)



file_path = r"C:\Users\pc\survey\dataset\All_data.xlsx"
alldata.to_excel(file_path, index=False)

print(alldata.shape)

for i in alldata.columns:
    print(i)

none_count=evaluated["Student_skill"].isna().sum()
print(none_count)
