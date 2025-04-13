import pandas as pd
import numpy as np

evaluated=pd.read_excel(r"C:\Users\pc\survey\dataset\student_evaluation.xlsx")


alldata=pd.read_excel(r"C:\Users\pc\survey\dataset\cleaned_data.xlsx")




alldata = alldata.reset_index(drop=True)
evaluated = evaluated.reset_index(drop=True)

evaluated_column = evaluated[["Student_skill", "Skill_Score"]].reset_index(drop=True)



for idx in range(10):
    print(alldata.iloc[idx]["skill"])
    print(evaluated_column.iloc[idx]["Reflecting on your studies, which technical skills do you feel most comfortable using or applying?"])

