import pandas as pd
import numpy as np

evaluated=pd.read_excel(r"C:\Users\pc\survey\dataset\student_evaluation.xlsx")


alldata=pd.read_excel(r"C:\Users\pc\survey\dataset\All_data.xlsx")




print(evaluated.columns)

evaluated.drop("Student_skill",inplace=True,axis=1) #run one time 

print(evaluated.info())

##! Career_Services_Aware
print(evaluated["Career_Services_Aware"].unique())

# Define the mapping
career_services_mapping = {
    "No, I’m not aware": 0,
    "Yes, but I haven’t used them": 0,
    "Yes, and I’ve used them": 1.0
}

# Apply the mapping to the column
evaluated["Career_Services_Aware"] = evaluated["Career_Services_Aware"].map(career_services_mapping)

# Display the updated DataFrame
print(evaluated[["Career_Services_Aware"]].head())


##! Academic_Level
Academic_Level_mapping={
    "Third Level":.85,
    "Fourth Level":1.0
}
evaluated["Academic_Level"] = evaluated["Academic_Level"].map(Academic_Level_mapping)

##! Internships_Completed 
print(evaluated["Internships_Completed"].unique())
Internships_Completed_mapping={
    '0 (None yet)':0,
    1:.85,
    2:.95,
    '3 or more':1.0
}

evaluated["Internships_Completed"] = evaluated["Internships_Completed"].map(Internships_Completed_mapping)

##! Extracurricular_Hours
evaluated["Extracurricular_Hours"] = pd.to_numeric(evaluated["Extracurricular_Hours"], errors='coerce').fillna(0).astype(int)


##! Self_Learning_Hours
print(evaluated["Self_Learning_Hours"].unique())

Self_Learning_Hours_mapping={
    '1–3 hours':.75,
    '4–6 hours':.85,
    '7–10 hours':.95,
    '11 or more' :1.0
}

evaluated["Self_Learning_Hours"] = evaluated["Self_Learning_Hours"].map(Self_Learning_Hours_mapping)


##! Career_Workshops_Attended
print(evaluated["Career_Workshops_Attended"].unique())

# evaluated["Career_Workshops_Attended"].fillna("empty",inplace=True)
Career_Workshops_Attended_mapping={
    0:0,
    '1–2 sessions':.85,
    '3–5 sessions':.95,
    'More than 5 sessions':1.0
}

evaluated["Career_Workshops_Attended"] = evaluated["Career_Workshops_Attended"].map(Career_Workshops_Attended_mapping)


##! PartTime_Job_Hours
print(evaluated["PartTime_Job_Hours"].unique())

PartTime_Job_Hours_mapping={
    'I don’t have a job':0,
    'Yes, I work 1–4 hours per week':.75, 
    'Yes, I work 5–10 hours per week':.95,
    'Yes, I work more than 10hours per week':1.0
}

evaluated["PartTime_Job_Hours"]=evaluated["PartTime_Job_Hours"].map(PartTime_Job_Hours_mapping)



##! Job_Confidence
print(evaluated["Job_Confidence"].unique())
Job_Confidence_mapping={
    0:0,
    1:.75, 
    2:.80,
    3:.85,
    4:.95,
    5: 1.0
}
evaluated["Job_Confidence"]=evaluated["Job_Confidence"].map(Job_Confidence_mapping)

##! Job_Applications
print(evaluated["Job_Applications"].unique())
Job_Applications_mapping={
    '0 (None yet)':0,
    '1–5 applications':.85, 
    '6–10 applications':.95,
    'More than 10 applications':1.0
}

evaluated["Job_Applications"]=evaluated["Job_Applications"].map(Job_Applications_mapping)

##! Job_Offers_Received
print(evaluated["Job_Offers_Received"].unique())
Job_Offers_Received_mapping={
    'No':0,
    'Yes':1.0
}
evaluated["Job_Offers_Received"]=evaluated["Job_Offers_Received"].map(Job_Offers_Received_mapping)

##! Networking_Importance
print(evaluated["Networking_Importance"].unique())
Networking_Importance_mapping={
    1:.65,
    2:.75,
    3:.85,
    4:.95,
    5:1.0
}
evaluated["Networking_Importance"]=evaluated["Networking_Importance"].map(Networking_Importance_mapping)


##! Certificates_Achieved
print(evaluated["Certificates_Achieved"].unique())

Certificates_Achieved_mapping={
    0:0,
    '1-2':.75,
    '3-5':.85, 
    '6-10':.95,
    'More than 10':1.0 
}
evaluated["Certificates_Achieved"]=evaluated["Certificates_Achieved"].map(Certificates_Achieved_mapping)


##! Virtual_Internships" "Industry_Internships" "Gov_Internships"
# evaluated[["Virtual_Internships", "Industry_Internships", "Gov_Internships"]] = evaluated[["Virtual_Internships", "Industry_Internships", "Gov_Internships"]].fillna(0).astype(int)


evaluated['Virtual_Internships'] = np.ceil(evaluated['Virtual_Internships']).astype(int)
evaluated['Industry_Internships'] = np.ceil(evaluated['Industry_Internships']).astype(int)
evaluated['Gov_Internships'] = np.ceil(evaluated['Gov_Internships']).astype(int)


##! match after cell up


alldata['Which types of internships have you completed during your studies, and how many for each type?  [Virtual/Remote Internship]'] = np.ceil(alldata['Which types of internships have you completed during your studies, and how many for each type?  [Virtual/Remote Internship]']).astype(int)
alldata['Which types of internships have you completed during your studies, and how many for each type?  [Industry/Corporate Internship]'] = np.ceil(alldata['Which types of internships have you completed during your studies, and how many for each type?  [Industry/Corporate Internship]']).astype(int)
alldata['Which types of internships have you completed during your studies, and how many for each type?  [Government Internship]'] = np.ceil(alldata['Which types of internships have you completed during your studies, and how many for each type?  [Government Internship]']).astype(int)




print(evaluated.info())
print(evaluated[["Virtual_Internships", "Industry_Internships", "Gov_Internships"]].head(30))

Internships_mapping={
    0:0,
    1:.95,
    2:1.0,
}
evaluated["Virtual_Internships"]=evaluated["Virtual_Internships"].map(Internships_mapping)
evaluated["Industry_Internships"]=evaluated["Industry_Internships"].map(Internships_mapping)
evaluated["Gov_Internships"]=evaluated["Gov_Internships"].map(Internships_mapping)


print(evaluated.columns)

# evaluated["Extracurricular_Hours"] = evaluated["Extracurricular_Hours"].fillna(0).astype(int)



# evaluated['Extracurricular_Hours'] = evaluated['Extracurricular_Hours'].clip(lower=0)
print("min Extracurricular_Hours")
print(evaluated["Extracurricular_Hours"].min())


from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

columns_to_scale = ["Skill_Score", "CGPA", "Extracurricular_Hours"]

# Apply Min-Max Scaling (transform to range 0-1)
evaluated[columns_to_scale] = scaler.fit_transform(evaluated[columns_to_scale])

print(evaluated[columns_to_scale].head())

print(evaluated.describe())

for column in evaluated.columns:
    max_value = evaluated[column].max()
    print(f"Max value in '{column}': {max_value}")


##! weights score system

weights = {
    'Academic_Level': 0.05,
    'CGPA': 0.08,
    'Career_Services_Aware': 0.05,
    'Internships_Completed': 0.03,
    'Virtual_Internships': 0.06,
    'Industry_Internships':0.10 ,
    'Gov_Internships': 0.04,
    'Extracurricular_Hours': 0.05,
    'Self_Learning_Hours': 0.07,
    'Career_Workshops_Attended': 0.05,
    'PartTime_Job_Hours': 0.04,
    'Job_Confidence': 0.07,
    'Job_Applications': 0.05,
    'Job_Offers_Received': 0.06,
    'Networking_Importance': 0.05,
    'Certificates_Achieved': 0.05,
    'Skill_Score': 0.10
}

total_weight = 0
for key, value in weights.items():
    total_weight += value

# Print the total weight sum
print("Total Weight Sum:", total_weight)

# Calculate weighted score for each student
evaluated["Weighted_Score"] = evaluated[list(weights.keys())].mul(weights).sum(axis=1)

print(evaluated[["Weighted_Score"]].head(50))

print(evaluated["Weighted_Score"].describe())

##! store the percentage of Weighted_Score

evaluated["Career_Readiness_Percentage"]=evaluated["Weighted_Score"].apply(lambda x: int(round(x * 100)))

import numpy as np

evaluated["Readiness_Status"] = np.where(evaluated["Career_Readiness_Percentage"] > 50, "Ready", "Not Ready")

print(evaluated)


file_path = r"C:\Users\pc\survey\dataset\Career_Readiness.xlsx"
evaluated.to_excel(file_path, index=False)



readness_column=evaluated[["Career_Readiness_Percentage", "Readiness_Status"]]

final_merged_data = pd.concat([alldata, readness_column],axis=1)


print(evaluated["Readiness_Status"].value_counts())


print(final_merged_data.shape)



df_shuffled = final_merged_data.sample(frac=1, random_state=42).reset_index(drop=True)


df_shuffled["cleaned_skills"].fillna("No Good Skill",inplace=True)


file_path= r"C:\Users\pc\survey\dataset\All_Merge_Shuffle_data.xlsx"
df_shuffled.to_excel(file_path, index=False)





# Display detailed analysis
for index, row in df_shuffled[["student_skill_score", "cleaned_skills", "Reflecting on your studies, which technical skills do you feel most comfortable using or applying?"]].iterrows():
    cleaned_skills = str(row['cleaned_skills']).replace("\n", " ")
    original_skill = str(row['Reflecting on your studies, which technical skills do you feel most comfortable using or applying?']).replace("\n", " ")
    score = row['student_skill_score']

    print(f"\nIndex: {index}")
    print(f"Original Skill Text : {original_skill} len {len(original_skill.split(','))}")
    print(f"Detected AI Skills  : {cleaned_skills} len {len(cleaned_skills.split(','))}")
    print(f" Skill Score      : {score}")
    print("-" * 120)



print(df_shuffled.shape)