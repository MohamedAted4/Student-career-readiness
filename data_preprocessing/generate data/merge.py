import pandas as pd

# Paths to your Excel files
path_data_science = r"C:\Users\pc\survey\dataset\department\random data_Computing & Data Sciences.xlsx"
path_intelligent_systems = r"C:\Users\pc\survey\dataset\department\random Intelligent Systems.xlsx"
path_cybersecurity = r"C:\Users\pc\survey\dataset\department\random Cybersecurity.xlsx"
path_surver=r"C:\Users\pc\survey\dataset\STUDENT CAREERREADINESS  (Responses).xlsx"

df_data_science = pd.read_excel(path_data_science)
df_intelligent_systems = pd.read_excel(path_intelligent_systems)
df_cybersecurity = pd.read_excel(path_cybersecurity)

df_survey=pd.read_excel(path_surver)

df_survey_total=pd.read_excel(path_surver)
df_survey_total=df_survey_total.drop(['Which elective course have you found most helpful for your career preparation and readiness?  '],axis=1)

df_survey=df_survey.drop(['Which elective course have you found most helpful for your career preparation and readiness?  '],axis=1)

# Concatenate all DataFrames vertically (row-wise)
combined_df = pd.concat(
    [df_data_science, df_intelligent_systems, df_cybersecurity],
    axis=0,           # Stack vertically
    ignore_index=True # Reset index
)


print(len(combined_df.columns))

print(len(combined_df))

mismatch_columns = []


print(df_survey.columns)
print("___"*50)
print(combined_df.columns)




# Get matching columns efficiently using set intersection
matching_columns = set(df_survey.columns)-set(combined_df.columns) 

# Convert to a sorted list (optional) and display
matching_columns = sorted(matching_columns)  # Sorting for better readability



print(len(combined_df.columns))



# Output the columns that should be dropped
for i in matching_columns:
    print("not column",i)

print("matching column",len(matching_columns))

print("__"*50)

columns_to_drop = [
    "Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?.1",
    "Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?.2",
    "Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?.3",
    "Timestamp",
    "What specific improvements would you like to see in your university’s career preparation programs?.1",
    "What specific improvements would you like to see in your university’s career preparation programs?.2",
    "What specific improvements would you like to see in your university’s career preparation programs?.3",
    "Which elective course have you found most helpful for your career preparation and readiness?.1",
    "Which elective course have you found most helpful for your career preparation and readiness?.2",
    "Which professional or technical skills do you feel are missing from your university education?.1",
    "Which professional or technical skills do you feel are missing from your university education?.2",
    "Which professional or technical skills do you feel are missing from your university education?.3"
]

# Drop the columns
df_survey = df_survey.drop(columns=columns_to_drop, errors='ignore')

# Display the updated DataFrame

print(df_survey.columns)
print("len surver",len(df_survey.columns))





desired_order = [
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
        'What specific improvements would you like to see in your university’s career preparation programs?'
]

# Reorder the dataframe while keeping only the existing columns
combined_df = combined_df[[col for col in desired_order if col in combined_df.columns]]

print("__"*50)

print(combined_df.columns)

print("combined_df",len(combined_df.columns))



##! group by datascience 

datascience_column=[
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
        'What specific improvements would you like to see in your university’s career preparation programs?'
]
df_datascience = df_survey_total[df_survey_total["What is your department?"] == "Computing & Data Sciences"][datascience_column]



print(len(df_datascience))


##! groupby intelligentsystem


intelligentsystem_column=[
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
        'Which elective course have you found most helpful for your career preparation and readiness?.1',
        'Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?.1',
        'Which professional or technical skills do you feel are missing from your university education?.1',
        'What specific improvements would you like to see in your university’s career preparation programs?.1'
]
df_intelligentsystem = df_survey_total[df_survey_total["What is your department?"] == "Intelligent Systems"][intelligentsystem_column]


df_intelligentsystem = df_intelligentsystem.rename(columns={
    'Which elective course have you found most helpful for your career preparation and readiness?.1': 'Which elective course have you found most helpful for your career preparation and readiness?',
    'Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?.1': 'Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?',
    'Which professional or technical skills do you feel are missing from your university education?.1': 'Which professional or technical skills do you feel are missing from your university education?',
    'What specific improvements would you like to see in your university’s career preparation programs?.1': 'What specific improvements would you like to see in your university’s career preparation programs?'
})


print(len(df_intelligentsystem))


##! groupby cyber


cyber_column=[
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
        'Which elective course have you found most helpful for your career preparation and readiness?.2',
        'Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?.2',
        'Which professional or technical skills do you feel are missing from your university education?.2',
        'What specific improvements would you like to see in your university’s career preparation programs?.2'
]
df_cyber = df_survey_total[df_survey_total["What is your department?"] == "Cybersecurity"][cyber_column]


df_cyber = df_cyber.rename(columns={
    'Which elective course have you found most helpful for your career preparation and readiness?.2': 'Which elective course have you found most helpful for your career preparation and readiness?',
    'Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?.2': 'Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?',
    'Which professional or technical skills do you feel are missing from your university education?.2': 'Which professional or technical skills do you feel are missing from your university education?',
    'What specific improvements would you like to see in your university’s career preparation programs?.2': 'What specific improvements would you like to see in your university’s career preparation programs?'
})

print(len(df_cyber))

##! group by other


other_column=[
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
        'Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?.3',
        'Which professional or technical skills do you feel are missing from your university education?.3',
        'What specific improvements would you like to see in your university’s career preparation programs?.3'
]
df_other = df_survey_total[df_survey_total["What is your department?"] == "Other"][other_column]


df_other = df_other.rename(columns={
    'Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?.3': 'Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?',
    'Which professional or technical skills do you feel are missing from your university education?.3': 'Which professional or technical skills do you feel are missing from your university education?',
    'What specific improvements would you like to see in your university’s career preparation programs?.3': 'What specific improvements would you like to see in your university’s career preparation programs?'
})
print(len(df_other))


##! merge all actual data 

df_merged = pd.concat(
    [df_datascience, df_intelligentsystem, df_cyber, df_other],
    axis=0,           # Stack vertically
    ignore_index=True  # Reset index
)

print(len(df_merged))

num_duplicates = df_merged.duplicated().sum()
print(f"Number of duplicate rows: {num_duplicates}")


total_missing = df_merged.isnull().sum().sum()
print(f"Total missing values: {total_missing}")

print(df_merged.isnull().sum().to_string())


##!final merge between actual and random 

all_data= pd.concat(
    [df_merged,combined_df],
    axis=0,           # Stack vertically
    ignore_index=True  # Reset index
)

print(len(all_data))


df_shuffled = all_data.sample(frac=1, random_state=42).reset_index(drop=True)


output_path = r"C:\Users\pc\survey\dataset\department\Merged_shuffle_data.xlsx"
df_shuffled.to_excel(output_path, index=False)

print(f"All departments merged successfully into: {output_path}")
print(f"Final shape: {df_shuffled.shape} (rows, columns)")



print(df_shuffled.columns)