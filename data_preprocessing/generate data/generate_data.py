import pandas as pd
import random

data=pd.read_excel(r"C:\Users\pc\survey\dataset\STUDENT CAREERREADINESS  (Responses).xlsx")




print(data.columns)
print(len(data.columns))

## What is your department ?  

print((data["What is your department?"].value_counts()).sort_index())

## total response 117
# Computing & Data Sciences    85
# Cybersecurity                 6
# Intelligent Systems           8
# Other                        18


print("___"*50)


# for column in data.columns:
#     print(f"##! {column}")
#     print(data[column].unique())
#     print("\n" + "="*50 + "\n")



data_columns = {
    "What is your gender?": ['Female', 'Male'],
    "What is your age?": ['21–23', '18–20', '24–26'],
    "What is your current academic level?": ['Third Level', 'Fourth Level'],
    "Are you aware of your university’s career services?": [
        'Yes, but I haven’t used them', 'Yes, and I’ve used them', 'No, I’m not aware'
    ],
    "What is your department?": ['Computing & Data Sciences', 'Other', 'Intelligent Systems', 'Cybersecurity'],
    "How many internships have you completed during your studies?": [1, 2, '0 (None yet)', '3 or more'],
    "Which types of internships have you completed during your studies, and how many for each type?  [Virtual/Remote Internship]": [0, 1, 2],
    "Which types of internships have you completed during your studies, and how many for each type?  [Industry/Corporate Internship]": [0, 1, 2],
    "Which types of internships have you completed during your studies, and how many for each type?  [Government Internship]": [1, 0, 2],
    "On average, how many hours per week do you spend on self-learning (such as online courses, tutorials, or independent study)?": 
    ['7–10 hours', '4–6 hours', '11 or more', '1–3 hours'],
    "Have you attended any career-related workshops or training sessions?": 
    ['3–5 sessions', '1–2 sessions', 'More than 5 sessions'],
    "Do you have a part-time job while studying? If yes, how many hours per week do you work?": [
        'Yes, I work 1–4 hours per week', 'I don’t have a job', 'Yes, I work more than 10hours per week', 'Yes, I work 5–10 hours per week'
    ],
    "On a scale of 0 to 5, how confident are you in your ability to secure a job after graduation, considering your skills, experience, and job market conditions?": 
    [1, 3, 2, 4, 5, 0],
    "In the past 6 months, how many job applications have you submitted?": 
    ['0 (None yet)', '1–5 applications', 'More than 10 applications', '6–10 applications'],
    "How long do you expect it will take to secure a job after graduation?": 
    ['1-3 months', '4-6 months', 'More than 6 months'],
    "Have you received any job offers before graduation?": ['No', 'Yes'],
    "To what extent do you think your university’s career services have helped you prepare for the job market?": 
    ['Slightly', 'Moderately', 'Not at all', 'Very much'],
    "On a scale of 1-5, how relevant do you think your university courses are to real-world job requirements?": 
    [2, 3, 4, 1, 5],
    "How would you rate the amount of hands-on training provided by your university?": 
    ['Adequate (suitable)', 'Insufficient', 'More than enough'],
    "On a scale of 1-5, how important do you think networking is in securing a job?": 
    [4, 5, 3, 1, 2],
    "Which of the following skills do you think employers value the most in your field?": [
        "Technical skills", "Communication skills", "Leadership", "Critical thinking", "Problem-solving", "Teamwork"
    ],
    "Which of the following career paths do you prefer?": [
        "Working in a local company", "Joining a multinational corporation", "Starting my own business (Entrepreneurship)",
        "Freelancing / Self-employment"
    ],
    "How many certificates have you achieved so far?": ['3-5', '1-2', 'More than 10', '6-10', 0],
}

# Elective courses based on department
elective_courses = {
    "Computing & Data Sciences": [
        "Convex Optimization", "Non-Linear and Combinatorial Optimization", "Multivariate Statistical Analysis",
        "Bayesian Statistics", "Data Compression Techniques", "Concurrent Algorithms and Data Structures",
        "Distributed Database Systems", "Advanced Database Systems"
    ],
    "Intelligent Systems": [
        "Speech Recognition", "Natural Language Understanding", "Embedded Machine Learning", "Intelligence Technology Trends",
        "Internet of Things II", "Knowledge-Base AI", "Virtual Reality", "Game Theory"
    ],
    "Cybersecurity": [
        "AI Security Issues", "Proactive Computer Security", "Software Security Engineering",
        "Blockchain and Security of Blockchain", "Cloud Computing Security", "Social Networks Analytics",
        "Internet of Things", "Mobile Computing"
    ]
}




all_department_skill={
    "Computing & Data Sciences":[
        # Programming & Development
        "Python", "R", "SQL", "Java","C++","JavaScript", "Go", "Swift",
        
        # Data Analysis & Visualization
        "Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "Dash", 
        "Power BI", "Tableau", "Excel", "Google Sheets","Data Visualization","Data Analysis", 
        
        # Machine Learning & AI
        "Scikit-learn", "TensorFlow", "PyTorch", "XGBoost", "LightGBM",
        "Feature Engineering", "Feature Selection", "Model Tuning", "Class Imbalance Handling", 
        "Deep Learning", "NLP", "Computer Vision","Machine Learning",
        "Artificial Intelligence", "Neural Networks", "Transformers", "LLMs", "GANs", "Reinforcement Learning",

        # Big Data & Cloud Computing
        "Big Data", "AWS", "Google Cloud", "Azure", "Cloud Computing", "Spark", "Hadoop", "Kafka",

        # Databases & Management
        "MySQL", "PostgreSQL", "MongoDB", "Firebase", "SQL Server", "Oracle", 
        "Data Extraction","Data Cleaning", "Data Manipulation",
        "NoSQL","Databases"

        # Statistics & Mathematics
        "Statistical Analysis", "Statistics", 
        "Multivariate Analysis", "Stochastic Processes", "Bayesian Statistics", "Linear Algebra",

        # Other Data Science-Related Tools & Concepts
        "Recommendation Systems", "Web Scraping", "BeautifulSoup", "Selenium",
        "Data Structures","Algorithms", "Dashboards",
        "Software Development", "Critical Thinking", "Problem Solving",
    ] ,


    "Intelligent Systems":[
        # Programming & Development
        "Python", "R", "SQL", "Java","C++","JavaScript", "Go", "Swift","Scala","Koltin","Rust","CUDA",

        # Machine Learning & AI
        "Scikit-learn", "TensorFlow", "PyTorch", "XGBoost", "LightGBM","Keras"
        "Feature Engineering", "OpenCV","YOLO", "image Classification","Object Detection", "Face Recognition",
        "Deep Learning", "NLP", "Computer Vision","Machine Learning","Hugging Face Transformers","OpenAI gym","Detectron2","Autoencoders","CNNs","RNNs"
        "Artificial Intelligence", "Neural Networks", "Transformers", "LLMs", "GANs", "Reinforcement Learning","Autoencoders","Recommendation System",

        # Big Data & Cloud Computing
        "Big Data", "AWS", "Google Cloud", "Azure", "Cloud Computing", "Spark", "Hadoop", "Kafka","MLlib",

        # Databases & Management
        "MySQL", "PostgreSQL", "MongoDB", "Firebase", "SQL Server", "Oracle",
        "Data Extraction","Data Cleaning", "Data Manipulation",
        "NoSQL","Databases","Neo4j",

        # Mathematics & AI Foundations
        "Linear Algebra","Probability & Statistics","Bayesian Methods","Optimization",

        # Other Related Tools & Concepts
        "Recommendation Systems", "IoT  ", "Model Compression", "deployment",
        "AI Ethics ","Algorithms", "Edge AI",
        "AI Security", "Critical Thinking", "Problem Solving",
    ],


    "Cybersecurity" :[
        # Programming & Scripting
        "Python", "C", "C++", "Java", "JavaScript", "PowerShell", "Bash", "Go", "Rust",

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





}








def generate_random_data(department, num_records):
    data = []
    
    for _ in range(num_records):
        record = {col: random.choice(values) for col, values in data_columns.items()}
        record["What is your department?"] = department  # Set department

        # Convert lists to comma-separated strings before storing
        record["Which of the following skills do you think employers value the most in your field?"] = ", ".join(random.sample(
            data_columns["Which of the following skills do you think employers value the most in your field?"], 3
        ))

        record["Which of the following career paths do you prefer?"] = ", ".join(random.sample(
            data_columns["Which of the following career paths do you prefer?"], 2
        ))

        if department in elective_courses:
            record["Which elective course have you found most helpful for your career preparation and readiness?"] = ", ".join(random.sample(elective_courses[department], 4))
        else:
            record["Which elective course have you found most helpful for your career preparation and readiness?"] = "Not applicable"

        if department in all_department_skill:
            available_skills = all_department_skill[department]
            # Determine how many skills to select (5-10, but not more than available)
            num_skills = min(random.randint(5, 10), len(available_skills))
            # Select random unique skills
            selected_skills = random.sample(available_skills, num_skills)
            record["Reflecting on your studies, which technical skills do you feel most comfortable using or applying?"] = ", ".join(selected_skills)
        else:
            record["Reflecting on your studies, which technical skills do you feel most comfortable using or applying?"] = "Not applicable"
        data.append(record)
        
    return pd.DataFrame(data)








##! Computing & Data Sciences

cgpa_list_DataSciences = [round(random.uniform(1.50, 3.98), 2) for _ in range(100)]

extracurricular_hours_DataSciences = [random.randint(3, 33) for _ in range(100)]

expected_salary_DataSciences = [random.choice(range(1000, 10010, 250)) for _ in range(100)]


courses_DataSciences = [
    "Machine Learning – Andrew Ng (Coursera, Stanford University)",
    "Deep Learning Specialization – Andrew Ng (Coursera, DeepLearning.AI)",
    "AI for Everyone – Andrew Ng (Coursera, DeepLearning.AI)",
    "Practical Deep Learning for Coders – fast.ai",
    "TensorFlow Developer Certification – Google & TensorFlow",
    "PyTorch for Deep Learning – Udacity",
    "Reinforcement Learning Specialization – University of Alberta (Coursera)",
    "Natural Language Processing with Deep Learning – Stanford University (YouTube)",
    "Generative AI with LLMs – DeepLearning.AI (Coursera)",
    "IBM AI Engineering Professional Certificate – IBM (Coursera)",

    # Data Science & Analytics Courses
    "Data Science Specialization – Johns Hopkins University (Coursera)",
    "Python for Data Science and Machine Learning – Udemy",
    "Applied Data Science with Python – University of Michigan (Coursera)",
    "Data Science Bootcamp – DataCamp",
    "SQL for Data Science – University of California, Davis (Coursera)",
    "Data Science with R – HarvardX (edX)",
    "Practical Data Science on AWS – Amazon AWS Academy",
    "Introduction to Computational Thinking and Data Science – MIT OpenCourseWare",
    "Statistics for Data Science and Business Analysis – Udemy",
    "Big Data Analytics with Spark – University of California, Berkeley (edX)",

    # Programming & Software Engineering
    "CS50: Introduction to Computer Science – Harvard University (edX)",
    "Python for Everybody – University of Michigan (Coursera)",
    "Java Programming and Software Engineering Fundamentals – Duke University (Coursera)",
    "Data Structures and Algorithms – Udacity",
    "Object-Oriented Programming in Java – University of California, San Diego (Coursera)",
    "C++ for Programmers – Udemy",
    "Advanced Python – Pluralsight",
    "Web Scraping with Python and Selenium – Udemy",
    "Git and GitHub for Beginners – Udemy",
    "Automate the Boring Stuff with Python – Al Sweigart (Udemy)",

    # Data Visualization & Business Intelligence
    "Tableau for Data Science – Udemy",
    "Power BI for Business Analytics – Udemy",
    "Data Visualization with Python – DataCamp",
    "Data Storytelling and Visualization – Coursera",
    "Advanced Excel for Data Analysis – Udemy",
    "Business Analytics with Excel – University of Illinois (Coursera)",
    "Dashboards and Data Insights with Power BI – Pluralsight",
    "D3.js for Data Visualization – Udacity",
    "Data Journalism and Storytelling – Google News Initiative",
    "Financial Modeling and Visualization – Corporate Finance Institute (CFI)",

    # Big Data & Cloud Computing
    "Big Data and Machine Learning on AWS – Coursera",
    "Google Cloud Data Engineering – Google Cloud (Coursera)",
    "Azure AI Fundamentals – Microsoft (Udacity)",
    "Apache Spark for Big Data Processing – Udemy",
    "Data Engineering on Google Cloud – Pluralsight",
    "Data Pipelines with Apache Airflow – Udacity",
    "Kubernetes for Machine Learning – Udacity",
    "Data Warehousing with Snowflake – Coursera",
    "Cloud Computing Basics – Amazon AWS Academy",
    "Hadoop and MapReduce for Big Data – Udacity",

    # Time Series & Financial Data Analysis
    "Time Series Forecasting with Python – Udemy",
    "Quantitative Finance and Algorithmic Trading – Coursera",
    "Applied Time Series Analysis – University of Washington (Coursera)",
    "Financial Risk Analytics – Stanford University (edX)",
    "Algorithmic Trading and Quantitative Analysis – Udemy",
    "Cryptography and Blockchain Basics – University of Nicosia (Coursera)",
    "Investment Analytics and Data Science – University of Chicago (edX)",
    "Risk Modeling and Credit Scoring – DataCamp",
    "Portfolio Management and Machine Learning – Udacity",
    "Cryptocurrency and Blockchain – MIT Sloan (edX)",

    # Natural Language Processing (NLP)
    "NLP with Python – Udemy",
    "Deep Learning for NLP – Coursera",
    "Speech Recognition and Processing – Udacity",
    "Text Mining and Sentiment Analysis – DataCamp",
    "Transformers for NLP – Hugging Face (Coursera)",
    "Chatbot Development with Rasa – Udemy",
    "Question Answering with Transformers – DeepLearning.AI (Coursera)",
    "Named Entity Recognition and Text Classification – Udacity",
    "Machine Translation with Deep Learning – Google AI (YouTube)",
    "Ethical AI and Bias in NLP – IBM AI Ethics (Coursera)",

    # Reinforcement Learning & Optimization
    "Reinforcement Learning – University of Alberta (Coursera)",
    "Decision Making with Markov Models – Stanford University (edX)",
    "Game Theory and Multi-Agent Systems – Udacity",
    "AI in Robotics and Reinforcement Learning – Udacity",
    "Optimization for Machine Learning – MIT OpenCourseWare",
    "Neural Networks and Deep Reinforcement Learning – Udacity",
    "Bayesian Optimization and Probabilistic Modeling – Coursera",
    "Multi-Armed Bandits and A/B Testing – DataCamp",
    "Genetic Algorithms in AI – Udemy",
    "Learning from Demonstration in AI – DeepMind (YouTube)",

    # Ethical AI, Responsible Data Science & Soft Skills
    "AI Ethics and Fairness – IBM (Coursera)",
    "Data Privacy and GDPR Compliance – Udemy",
    "Responsible AI in Practice – Microsoft AI Ethics (Coursera)",
    "Explainable AI (XAI) and Model Interpretability – Udacity",
    "Social Implications of AI – MIT Sloan (edX)",
    "Bias and Fairness in AI Models – Google AI Ethics (YouTube)",
    "Data Science for Social Good – University of Chicago (edX)",
    "Critical Thinking for Data Science – HarvardX (edX)",
    "Communication Skills for Data Science – Udacity",
    "Leadership and Project Management for Data Science – Coursera",

    # IoT, Edge Computing & Emerging Technologies
    "IoT and Data Science – Udacity",
    "Edge AI and On-Device Machine Learning – Google AI (YouTube)",
    "Quantum Computing for Machine Learning – IBM (Coursera)",
    "Wearable Technology and AI – Stanford University (edX)",
    "5G and AI Applications – Udacity",
    "Robotics with AI – MIT OpenCourseWare",
    "AI for Medical Diagnosis – Stanford University (Coursera)",
    "AI for Self-Driving Cars – Udacity",
    "AI and Climate Change – DeepMind (YouTube)",
    "Future Trends in AI and Data Science – Oxford University (edX)"
]

missing_skills_DataSciences = [
    "Advanced SQL query optimization and performance tuning",
    "MLOps and model deployment best practices",
    "Real-world data cleaning and preprocessing techniques",
    "Deep learning productionization and scaling models",
    "Cloud computing (AWS, GCP, Azure) for data science applications",
    "End-to-end machine learning pipeline development",
    "Handling big data with distributed computing (Spark, Hadoop)",
    "Advanced feature engineering strategies",
    "Practical A/B testing and experimentation in data science",
    "Time series forecasting beyond basic models",
    "Explainable AI (XAI) and model interpretability techniques",
    "Software engineering best practices for data scientists",
    "Building recommendation systems at scale",
    "Advanced NLP techniques and transformers",
    "Financial modeling and risk analysis using machine learning",
    "Real-world reinforcement learning applications",
    "Graph data science and knowledge graphs",
    "Geospatial data analysis and GIS applications",
    "Data security, privacy, and ethical AI principles",
    "Bias mitigation techniques in machine learning models",
    "Web scraping and data collection from various sources",
    "Handling real-time data streaming with Kafka and Flink",
    "Data science in production: monitoring and debugging models",
    "Optimizing deep learning models for efficiency",
    "Deployment of AI models using Docker and Kubernetes",
    "Serverless computing for machine learning applications",
    "CI/CD pipelines for machine learning projects",
    "Quantitative finance and algorithmic trading strategies",
    "Blockchain technology and smart contracts for AI",
    "Optimization techniques and mathematical programming",
    "Computer vision applications in industry",
    "Cybersecurity applications in data science",
    "Edge AI and on-device machine learning",
    "Developing AI for robotics and automation",
    "Advanced statistical modeling beyond linear regression",
    "Monte Carlo simulations and probabilistic programming",
    "Neural architecture search and hyperparameter tuning",
    "Product management skills for data-driven decision-making",
    "Domain-specific AI applications (healthcare, finance, retail, etc.)",
    "Practical project management and teamwork in data science",
    "Communicating data science findings to non-technical stakeholders",
    "Soft skills like negotiation, leadership, and business acumen",
    "Real-world case studies and industry-relevant projects",
    "Understanding legal and compliance aspects of AI",
    "High-performance computing for AI workloads",
    "Automating workflows with Python (Airflow, Prefect)",
    "Advanced mathematical foundations for AI",
    "AI ethics and regulatory frameworks",
    "Reproducibility and documentation in machine learning",
    "Version control and collaboration with GitHub",
    "Knowledge of DevOps practices for machine learning",
    "Business intelligence and data-driven decision-making",
    "Digital marketing analytics and customer insights",
    "Synthetic data generation techniques",
    "Explainability in deep learning models (SHAP, LIME, etc.)",
    "Advanced Bayesian statistics and probabilistic inference",
    "Human-in-the-loop AI and active learning",
    "Learning how to debug and optimize ML models in production",
    "Soft computing techniques like fuzzy logic and genetic algorithms",
    "Developing serverless AI applications using cloud functions",
    "API development and integration for AI models",
    "Bias detection and fairness auditing in ML models",
    "Data storytelling and presentation skills for stakeholders",
    "AI governance, policies, and responsible AI frameworks",
    "Data annotation and labeling best practices",
    "Graph neural networks and applications",
    "Deploying ML models on edge devices and mobile applications",
    "BigQuery, Snowflake, and other modern data warehousing tools",
    "Data lakes and lakehouses: implementation and best practices",
    "Practical reinforcement learning for business applications",
    "Transfer learning and fine-tuning pre-trained models",
    "Self-supervised learning and semi-supervised techniques",
    "Bioinformatics and AI in healthcare applications",
    "Cyber threat detection using machine learning",
    "Machine learning for industrial automation and IoT",
    "Multimodal AI combining text, vision, and speech data",
    "AI for social good: climate change, poverty, and healthcare",
    "Processing and analyzing satellite and remote sensing data",
    "Data monetization and leveraging AI for business growth",
    "AI-powered search and recommendation engines",
    "Scaling machine learning models across multiple GPUs",
    "Differential privacy and privacy-preserving machine learning",
    "Zero-shot and few-shot learning techniques",
    "GANs (Generative Adversarial Networks) and deep generative models",
    "Meta-learning and learning to learn",
    "AI-based automation for customer support (chatbots, virtual assistants)",
    "Conversational AI and advanced speech processing",
    "AI-assisted software development and code generation",
    "Quantum machine learning and future AI paradigms",
    "AI applications in creative industries (art, music, design)",
    "Human-centered AI and interaction design",
    "Ethical hacking and penetration testing with AI",
    "Machine learning compilers and model optimization (TVM, TensorRT)",
    "Cloud-native AI application development",
    "Advanced reinforcement learning for game AI",
    "Neuromorphic computing and bio-inspired AI",
    "Self-supervised representation learning",
    "AI-driven knowledge management systems",
    "Distributed AI models and federated architectures",
    "Synthetic media and deepfake detection techniques"
]

career_preparation_improvements_DataSciences = [
    "More hands-on industry projects with real-world datasets",
    "Stronger partnerships with tech companies for internships",
    "Comprehensive training on technical interview preparation",
    "Workshops on AI ethics and responsible AI practices",
    "Mock technical interviews with industry professionals",
    "More opportunities for networking with data scientists",
    "Guidance on freelancing and consulting in data science",
    "Better career counseling tailored to data science roles",
    "Guest lectures from professionals in AI and ML industries",
    "Workshops on salary negotiation and contract discussions",
    "Training on problem-solving for coding interviews (LeetCode, HackerRank)",
    "Advanced SQL and database management workshops",
    "Incorporating cloud computing certifications into the curriculum",
    "More case studies on data-driven decision-making in business",
    "Regular hackathons and data science competitions",
    "Real-world datasets for class projects instead of toy datasets",
    "Training on Git, GitHub, and collaborative coding practices",
    "Internship placements in AI research labs and tech startups",
    "Practical training on data storytelling and visualization",
    "Support for students pursuing Kaggle competitions",
    "Exposure to AI governance and regulatory frameworks",
    "Introduction to entrepreneurship in AI and data science",
    "Training on writing research papers and publishing in journals",
    "Building AI-powered applications and deploying them",
    "More cross-disciplinary collaborations with business and healthcare fields",
    "Guidance on building a strong data science portfolio",
    "Connecting students with mentors in the data science field",
    "Providing access to paid courses and certifications (Coursera, Udemy, AWS, etc.)",
    "Offering flexible, self-paced learning options",
    "Organizing networking events with AI and tech leaders",
    "Hosting coding bootcamps focused on ML and AI",
    "More training in cloud computing platforms like AWS, GCP, and Azure",
    "Exposure to blockchain applications in data science",
    "Developing AI solutions for social good and sustainability",
    "Introducing courses on AI in robotics and automation",
    "More emphasis on deploying ML models into production",
    "Teaching best practices for writing clean and efficient code",
    "Providing access to AI research internships and grants",
    "Real-world case studies on AI-powered business transformation",
    "Organizing regular alumni panels to discuss career paths",
    "Partnerships with top tech firms for direct hiring pipelines",
    "Workshops on time management and productivity for data scientists",
    "Opportunities for students to work on industry-funded research projects",
    "More focus on statistical thinking and Bayesian methods",
    "Teaching students how to pitch AI-driven solutions to businesses",
    "Providing funding for students to attend AI conferences",
    "Encouraging students to contribute to open-source projects",
    "Training on scalable machine learning and MLOps",
    "More exposure to AI applications in different industries",
    "Understanding the legal and ethical aspects of AI deployment",
    "Guidance on career paths beyond traditional data science roles",
    "Support for transitioning into AI consulting and advisory roles",
    "Encouraging students to publish blog posts on AI topics",
    "Providing financial aid for cloud computing certifications",
    "More focus on AI in cybersecurity and threat detection",
    "Training in AI-driven automation and robotic process automation",
    "Helping students prepare for AI startup incubators",
    "Bringing in hiring managers to explain what they look for in candidates",
    "Developing more case studies on AI-driven business success",
    "Offering cross-training in related fields like IoT and edge AI",
    "Introducing AI applications in finance and quantitative trading",
    "Teaching students how to build end-to-end AI applications",
    "Support for international students in visa and job placement",
    "More exposure to AI-powered drug discovery and healthcare solutions",
    "Training on storytelling with data and dashboards",
    "More access to GPUs and cloud computing resources for deep learning projects",
    "Exploring AI for social good and sustainable development",
    "Incorporating data privacy and security into coursework",
    "Organizing mentorship programs with AI industry experts",
    "Providing more research assistant opportunities",
    "Teaching students about AI startup funding and investment strategies",
    "Focusing on AI in gaming and interactive media",
    "Encouraging students to build AI-driven web applications",
    "Workshops on AI-powered automation in various industries",
    "More partnerships with AI research labs and organizations",
    "Providing early exposure to AI in high school outreach programs",
    "Career coaching for students looking to transition from academia to industry",
    "More internship opportunities in AI policy and ethics",
    "Training on AI and IoT applications in smart cities",
    "Guidance on preparing strong GitHub repositories",
    "More exposure to AI-based fraud detection and cybersecurity",
    "Developing AI-powered career recommendation systems",
    "Helping students understand AI regulations and compliance laws",
    "Encouraging interdisciplinary projects in AI and humanities",
    "More training on AI in augmented reality and virtual reality",
    "Offering micro-certifications in specialized AI topics",
    "Providing hands-on experience with AI-powered chatbots",
    "Building stronger connections between academia and industry",
    "Helping students transition into AI product management roles",
    "Focusing more on AI-powered business intelligence tools",
    "Organizing company-sponsored AI challenges for students",
    "More practical exposure to AI-powered automation in finance",
    "Encouraging students to take part in AI-driven hackathons",
    "Providing access to exclusive AI job portals and career fairs",
    "Teaching students how to build AI-powered recommendation engines",
    "Helping students navigate AI-related ethical dilemmas",
    "Providing AI career roadmaps for students based on their interests",
    "Introducing AI solutions for environmental sustainability",
    "Developing personalized AI learning pathways based on skills and goals",
    "Teaching students how to scale AI applications for enterprise solutions"
]




##! Intelligent Systems


cgpa_list_IntelligentSystems = [round(random.uniform(1.50, 3.98), 2) for _ in range(100)]

extracurricular_hours_IntelligentSystems = [random.randint(3, 33) for _ in range(100)]


expected_salary_IntelligentSystems = [random.choice(range(1000, 10010, 250)) for _ in range(100)]

impactful_courses_intelligent_systems = [
    "Artificial Intelligence (CS50 AI) – Harvard University (edX)",
    "Machine Learning – Andrew Ng (Coursera, Stanford University)",
    "Deep Learning Specialization – Andrew Ng (Coursera, DeepLearning.AI)",
    "Reinforcement Learning Specialization – University of Alberta (Coursera)",
    "AI for Everyone – Andrew Ng (Coursera, DeepLearning.AI)",
    "TensorFlow Developer Certification – Google & TensorFlow",
    "PyTorch for Deep Learning – Udacity",
    "Generative AI with LLMs – DeepLearning.AI (Coursera)",
    "IBM AI Engineering Professional Certificate – IBM (Coursera)",
    "Natural Language Processing with Deep Learning – Stanford University (YouTube)",
    "Self-Driving Cars Specialization – University of Toronto (Coursera)",
    "Robotics Specialization – University of Pennsylvania (Coursera)",
    "Computer Vision and Image Processing – Udacity",
    "Edge AI and On-Device Machine Learning – Google AI (YouTube)",
    "AI in Medicine – Stanford University (Coursera)",
    "AI and Cybersecurity – University of Maryland (Coursera)",
    "AI for Healthcare – MIT OpenCourseWare",
    "AI in Finance – University of Chicago (edX)",
    "Autonomous Systems and Reinforcement Learning – Udacity",
    "AI in Smart Cities and IoT – MIT Sloan (edX)",
    "Introduction to Computational Thinking and Data Science – MIT OpenCourseWare",
    "Big Data and AI on AWS – Amazon AWS Academy",
    "Cloud AI and ML Engineering – Google Cloud (Coursera)",
    "Data Science and AI Ethics – IBM (Coursera)",
    "Explainable AI (XAI) – Udacity",
    "AI for Climate Change and Sustainability – DeepMind (YouTube)",
    "Introduction to Quantum Computing and AI – IBM (Coursera)",
    "Multi-Agent Systems and Game Theory – Udacity",
    "Neural Networks and Deep Learning – Udacity",
    "Applied AI for Business – University of London (Coursera)",
    "AI Product Management – Duke University (Coursera)",
    "AI for Decision Making – University of Washington (Coursera)",
    "Speech Recognition and Audio Processing – Udacity",
    "AI-powered Chatbot Development – Udemy",
    "Large-Scale AI Systems – Google Cloud (Coursera)",
    "AI-driven Automation and RPA – Udacity",
    "Cyber-Physical Systems and AI – University of Illinois (Coursera)",
    "Human-Robot Interaction – Stanford University (edX)",
    "Bayesian Methods for AI – Coursera",
    "Ethical AI and Bias Mitigation – Microsoft AI Ethics (Coursera)",
    "Advanced Computer Vision – Stanford University (YouTube)",
    "AI for Edge Devices – NVIDIA Deep Learning Institute",
    "Embedded AI Systems – Udacity",
    "Swarm Intelligence and Evolutionary Computing – Coursera",
    "AI in Industrial Automation – MIT OpenCourseWare",
    "AI for Space Exploration – NASA Open Learning",
    "AI-powered Drug Discovery – Harvard University (edX)",
    "Autonomous Drones and AI Navigation – Udacity",
    "AI for Smart Manufacturing – University of California, Berkeley (edX)",
    "AI for Natural Disaster Prediction – Google AI (YouTube)",
    "AI-powered Personal Assistants – DeepLearning.AI (Coursera)",
    "Biometric Recognition and AI Security – Udacity",
    "AI in Creative Arts and Music Generation – Stanford (edX)",
    "AI for Augmented Reality and VR – Udemy",
    "AI for Wearable Technology – University of California, San Diego (Coursera)",
    "AI-driven Traffic Optimization – MIT Sloan (edX)",
    "AI-powered Supply Chain Optimization – Coursera",
    "AI and Mental Health Applications – DeepMind (YouTube)",
    "Ethical Hacking and AI-driven Security – Udacity",
    "Predictive Maintenance with AI – University of Toronto (Coursera)",
    "AI for Customer Experience and Chatbots – Udemy",
    "AI and Blockchain Applications – University of Nicosia (Coursera)",
    "AI for Legal Tech and Compliance – HarvardX (edX)",
    "AI-powered Language Translation – Google AI (YouTube)",
    "Multi-Modal AI – DeepLearning.AI (Coursera)",
    "Fuzzy Logic and AI Decision Making – Stanford University (edX)",
    "AI-powered Sentiment Analysis – Udacity",
    "AI in Journalism and Automated Reporting – Google News Initiative",
    "Ethical Hacking and AI-driven Security – Udacity",
    "AI for Personalized Medicine – Johns Hopkins University (Coursera)",
    "Cognitive Computing and AI – IBM (Coursera)",
    "Quantum AI and Hybrid Intelligence – IBM (Coursera)",
    "AI-powered Fraud Detection – University of Illinois (Coursera)",
    "Neurosymbolic AI and Hybrid Approaches – MIT OpenCourseWare",
    "AI-powered Anomaly Detection – Udacity",
    "AI for Psychological Profiling – Stanford University (edX)",
    "AI in Sports Analytics – University of Chicago (edX)",
    "Meta-Learning and Few-Shot Learning – DeepLearning.AI (Coursera)",
    "AI for Predictive Analytics – Duke University (Coursera)",
    "AI-powered Recommendation Systems – Udemy",
    "AI in Agriculture and Food Security – Google AI (YouTube)",
    "AI in Marine Science and Underwater Exploration – MIT Sloan (edX)",
    "AI for Retail and E-commerce – Coursera",
    "AI for Autonomous Trading – University of Chicago (edX)",
    "AI for Personalized Learning and EdTech – Stanford University (YouTube)",
    "AI-driven HR and Talent Management – Udacity",
    "AI-powered Resume Screening and Recruitment – Coursera",
    "AI in Political Science and Public Policy – HarvardX (edX)",
    "AI for Behavioral Analysis – University of Toronto (Coursera)",
    "AI for Wildlife Conservation – DeepMind (YouTube)",
    "AI-driven Simulation and Digital Twins – Microsoft AI (Coursera)",
    "AI for Video Analytics and Surveillance – Udemy",
    "AI for Interactive Storytelling and Game AI – Udacity",
    "AI-powered Social Media Monitoring – Google AI (YouTube)",
    "AI for Smart Contracts and DeFi – University of Nicosia (Coursera)",
    "AI-powered Personalized Advertising – MIT OpenCourseWare",
    "AI for Urban Planning and Smart Cities – Coursera",
    "AI-driven Financial Portfolio Management – University of Chicago (edX)",
    "AI for Astronomy and Space Science – NASA Open Learning",
    "AI in Autonomous Robotics and Swarm Intelligence – Stanford University (edX)"
]

missing_skills_intelligent_systems = [
    "Advanced Reinforcement Learning techniques for real-world applications",
    "Edge AI and on-device machine learning deployment",
    "Explainable AI (XAI) and AI model interpretability",
    "AI ethics, fairness, and bias mitigation",
    "AI for cybersecurity and anomaly detection",
    "Multi-agent systems and game theory applications",
    "Advanced robotics and real-world robotic implementation",
    "AI for healthcare, including medical image analysis and diagnostics",
    "Generative AI and Large Language Models (LLMs)",
    "Quantum computing and AI applications",
    "AI-powered financial modeling and algorithmic trading",
    "Graph Neural Networks (GNNs) and knowledge graphs",
    "Advanced computer vision and deep learning for image analysis",
    "Autonomous vehicle navigation and real-time decision-making",
    "Neurosymbolic AI and hybrid intelligence approaches",
    "Human-AI collaboration and interactive AI systems",
    "Cognitive computing and AI-driven automation",
    "Fuzzy logic and uncertainty modeling in AI",
    "Time series forecasting and AI-driven predictive analytics",
    "Natural Language Understanding (NLU) and Conversational AI",
    "Deployment of AI models in cloud environments",
    "High-performance computing for AI workloads",
    "AI for embedded systems and microcontrollers",
    "Data privacy and compliance in AI applications",
    "AI-powered recommendation systems and personalization",
    "Real-world reinforcement learning with autonomous agents",
    "Synthetic data generation and augmentation for AI training",
    "AI in Industrial IoT and predictive maintenance",
    "Cyber-physical systems and AI-driven smart environments",
    "Deep learning model optimization and pruning techniques",
    "Self-supervised and semi-supervised learning techniques",
    "AI for mental health applications and cognitive science",
    "AI-driven optimization techniques in logistics and supply chain",
    "Energy-efficient AI and sustainable computing",
    "AI in smart agriculture and food security",
    "Automated machine learning (AutoML) and hyperparameter tuning",
    "AI-driven fraud detection and risk assessment",
    "Bayesian optimization and probabilistic reasoning",
    "Real-time AI applications and low-latency model inference",
    "Personalized AI learning systems for education technology",
    "Reinforcement learning for robotic manipulation",
    "AI-powered behavioral analysis and psychological modeling",
    "AI applications in climate change and sustainability",
    "AI for virtual and augmented reality applications",
    "AI for law enforcement and legal analytics",
    "Graph-based machine learning for social network analysis",
    "AI for bioinformatics and genetic research",
    "Interactive AI for game development and storytelling",
    "Automated reasoning and theorem proving in AI",
    "AI for real-time traffic management and smart cities",
    "Reinforcement learning with sparse rewards and exploration strategies",
    "Meta-learning and few-shot learning techniques",
    "Self-learning AI systems and continual learning strategies",
    "Differential privacy and secure AI computations",
    "AI for financial auditing and regulatory compliance",
    "Advanced time-series analysis with deep learning",
    "AI in sports analytics and athlete performance prediction",
    "Data-centric AI and best practices for model improvement",
    "AI-powered document analysis and automation",
    "Low-power AI processing and AI acceleration hardware",
    "Adversarial machine learning and model robustness",
    "AI-driven music generation and computational creativity",
    "AI-powered satellite image analysis and geospatial intelligence",
    "Behavioral economics and AI-driven decision making",
    "Hardware-aware AI model optimization",
    "Neuromorphic computing and brain-inspired AI architectures",
    "AI-driven legal technology and automated contract analysis",
    "Computational neuroscience and AI-inspired cognition models",
    "Hyperparameter tuning at scale for deep learning models",
    "Advanced AI benchmarking and performance testing",
    "Sensor fusion for AI-driven autonomous systems",
    "Few-shot and zero-shot learning approaches",
    "Transfer learning in real-world AI applications",
    "Self-evolving AI models with minimal human intervention",
    "Privacy-preserving AI and federated learning",
    "AI-powered 3D reconstruction and spatial computing",
    "AI for supply chain optimization and logistics",
    "Autonomous drone navigation with AI and computer vision",
    "Ethical considerations in autonomous AI decision-making",
    "Cross-domain AI applications and domain adaptation",
    "Bayesian deep learning for uncertainty estimation",
    "AI-driven sentiment analysis for social media monitoring",
    "AI-powered resume screening and automated hiring",
    "Medical AI applications beyond imaging, like drug discovery",
    "AI-enhanced security systems for threat detection",
    "Legal and regulatory frameworks for AI governance",
    "AI for accessibility and assistive technologies",
    "Predictive analytics for crisis management and disaster response",
    "AI for optimizing large-scale power grids and renewable energy",
    "Adaptive learning systems using AI in education",
    "Multi-modal AI-driven fake news detection",
    "AI in neuroprosthetics and rehabilitation technology",
    "Intelligent tutoring systems with adaptive learning",
    "AI-powered simulation environments for training robots",
    "AI-enhanced biometric recognition and authentication",
    "Intelligent search engines and AI-driven knowledge retrieval",
    "Advanced AI-driven cybersecurity threat detection",
    "Generative design in engineering using AI algorithms",
    "AI-powered business analytics and strategic decision-making",
    "Open-ended AI creativity models for art and media"
]

career_preparation_improvements_IntelligentSystems = [
    "More hands-on AI and machine learning projects with real-world applications.",
    "Industry partnerships for AI-focused internships and research opportunities.",
    "Workshops on deploying AI models in production environments.",
    "Guidance on securing AI research grants and funding opportunities.",
    "Regular career fairs with top AI and tech companies.",
    "AI-focused hackathons and innovation competitions.",
    "Dedicated courses on AI ethics and responsible AI development.",
    "Improved mentorship programs with industry professionals in AI and intelligent systems.",
    "Training on AI product management and startup development.",
    "Stronger emphasis on cloud computing platforms like AWS, Google Cloud, and Azure.",
    "Bootcamps on Reinforcement Learning and Deep Learning applications.",
    "Courses on edge computing and AI for IoT applications.",
    "Improved support for students to publish AI research papers.",
    "Technical interview preparation sessions focused on AI roles.",
    "AI-related soft skills training, including technical communication and teamwork.",
    "Workshops on AI-powered cybersecurity and ethical hacking.",
    "Expanded elective courses on AI-driven healthcare and bioinformatics.",
    "More opportunities for AI projects in collaboration with local businesses.",
    "Training on AI fairness, bias mitigation, and explainability techniques.",
    "AI deployment best practices using Docker and Kubernetes.",
    "Guidance on patenting AI innovations and intellectual property management.",
    "Case studies on successful AI startup journeys.",
    "Advanced training in Natural Language Processing (NLP) and Large Language Models (LLMs).",
    "Practical sessions on AI in embedded systems and robotics.",
    "AI-powered resume screening and personalized job recommendations.",
    "Training on AI model optimization and performance tuning.",
    "Mentorship programs connecting students with AI professionals.",
    "Stronger alumni network support for AI-related job placement.",
    "Courses on AI-based automation in industrial and manufacturing sectors.",
    "Specialized training on AI applications in finance and algorithmic trading.",
    "In-depth guidance on AI career paths, including research and industry roles.",
    "More networking opportunities with AI researchers and engineers.",
    "Training on AI's role in digital marketing and recommendation systems.",
    "Courses on AI for climate change and environmental sustainability.",
    "AI-driven entrepreneurship courses with startup incubation support.",
    "Better integration of AI in multidisciplinary fields like law and psychology.",
    "Exposure to government-funded AI research projects.",
    "Workshops on AI in augmented reality (AR) and virtual reality (VR).",
    "Access to high-performance computing resources for AI research.",
    "Training on federated learning and privacy-preserving AI.",
    "Better support for AI patent filing and commercialization.",
    "Hands-on experience with robotics process automation (RPA).",
    "Regular guest lectures from AI industry leaders and pioneers.",
    "Workshops on AI in humanitarian and social impact applications.",
    "Dedicated AI job placement services and recruitment drives.",
    "AI-specific leadership and project management training.",
    "AI-driven business analytics courses with real-time case studies.",
    "More exposure to AI-based smart city and urban planning solutions.",
    "AI and human-computer interaction (HCI) research integration.",
    "Career coaching for AI students tailored to different specializations.",
    "Support for AI students in participating in global AI competitions.",
    "Bootcamps on AI for edge computing and real-time processing.",
    "Collaboration opportunities with AI-focused startups.",
    "Advanced AI research fellowships and industry-sponsored projects.",
    "Training on AI-powered fraud detection in financial services.",
    "In-depth courses on graph neural networks and AI-driven knowledge graphs.",
    "Ethical AI and policy-making workshops.",
    "More industry certifications in AI-related technologies.",
    "Courses on AI and neurotechnology for brain-computer interfaces.",
    "Better integration of AI into business intelligence curricula.",
    "AI-focused consulting projects with real-world clients.",
    "Programs that teach AI-driven automation in digital transformation.",
    "Expanded AI research opportunities with faculty members.",
    "In-depth training on AI in industrial automation and robotics.",
    "AI-focused data engineering and MLOps courses.",
    "Workshops on AI-driven customer insights and behavioral analytics.",
    "More exposure to AI research centers and innovation hubs.",
    "Guidance on transitioning from academia to AI industry roles.",
    "Case studies on AI applications in government and public policy.",
    "Increased accessibility to AI computing power through cloud credits.",
    "AI-focused technical writing and documentation training.",
    "More collaboration with international AI research labs.",
    "Practical AI case studies integrated into coursework.",
    "Training on building AI-driven intelligent tutoring systems.",
    "Support for AI students in securing global research internships.",
    "Expanded career development courses specific to AI entrepreneurship.",
    "Workshops on AI bias detection and fairness testing.",
    "Mentorship for AI students looking to work in AI ethics and policy.",
    "AI-driven supply chain and logistics optimization courses.",
    "Integration of AI-powered automation into traditional engineering curricula.",
    "More university-sponsored AI projects with industry funding.",
    "Greater focus on AI-driven energy optimization and sustainability solutions.",
    "AI research networking events for graduate students.",
    "Better access to AI labs and hands-on experimentation.",
    "Opportunities to work on AI solutions for real-world social issues.",
    "Training on AI-powered scientific research methodologies.",
    "Expanded cloud-based AI coursework for scalability training.",
    "Career pathways into AI product management and AI consulting.",
    "Stronger university-industry collaborations in AI research.",
    "AI-powered financial modeling workshops for intelligent systems students.",
    "Courses on AI and creativity, including generative AI applications.",
    "AI-powered cybersecurity threat detection and response training.",
    "More exposure to AI use cases in autonomous transportation.",
    "Interdisciplinary AI programs bridging technology and social sciences.",
    "Real-world AI project showcase events for student work.",
    "Training on AI model validation and explainability best practices.",
    "AI-driven social network analysis and influence prediction workshops.",
    "AI-specific resume-building and job application guidance.",
    "More AI hackathons hosted in collaboration with major tech companies.",
    "AI career mentorship matching students with AI industry veterans."
]


##! Cybersecurity


cgpa_list_Cybersecurity = [round(random.uniform(1.50, 3.98), 2) for _ in range(100)]

extracurricular_hours_Cybersecurity = [random.randint(3, 33) for _ in range(100)]


expected_salary_Cybersecurity = [random.choice(range(1000, 10010, 250)) for _ in range(100)]

cybersecurity_courses = [
    "Certified Ethical Hacker (CEH) – EC-Council",
    "Offensive Security Certified Professional (OSCP) – Offensive Security",
    "CompTIA Security+ – CompTIA",
    "Certified Information Systems Security Professional (CISSP) – (ISC)²",
    "Certified Cloud Security Professional (CCSP) – (ISC)²",
    "Cybersecurity Fundamentals – IBM (Coursera)",
    "Practical Ethical Hacking – TCM Security (Udemy)",
    "The Complete Cyber Security Course – Nathan House (Udemy)",
    "Penetration Testing and Ethical Hacking – Cybrary",
    "Hacking Web Applications with Burp Suite – PortSwigger",
    "Digital Forensics and Cyber Investigation – University of Maryland (Coursera)",
    "Cybersecurity for Business – University of Colorado (Coursera)",
    "Cyber Threat Intelligence – Mandiant Academy",
    "Red Team Operations – Pentester Academy",
    "Blue Team Training – CyberDefenders",
    "Malware Analysis and Reverse Engineering – Udemy",
    "Cloud Security Basics – Google Cloud (Coursera)",
    "Security Engineering – University of London (Coursera)",
    "Python for Cybersecurity – Cybrary",
    "Network Security Essentials – Fortinet",
    "Security Awareness and Social Engineering – KnowBe4",
    "Ethical Hacking for Beginners – StationX",
    "CISSP Certification Training – Pluralsight",
    "Cybersecurity Law and Policy – Georgetown University (Coursera)",
    "Threat Hunting and Adversary Emulation – Black Hills InfoSec",
    "Cybersecurity Incident Management – Harvard University (edX)",
    "Advanced Web Application Penetration Testing – SANS Institute",
    "Wireless Network Security – Udemy",
    "Cloud Security Hands-On – AWS Security Training",
    "AI and Cybersecurity – Stanford University (Coursera)",
    "IoT Security Fundamentals – University of Colorado (Coursera)",
    "Dark Web and Cybercrime Investigations – Udemy",
    "CompTIA CySA+ (Cybersecurity Analyst) – CompTIA",
    "Practical Packet Analysis with Wireshark – Udemy",
    "Cryptography and Network Security – Stanford University (Coursera)",
    "Cybersecurity Leadership and Strategy – Wharton Online",
    "Digital Privacy and Anonymity – Tor Project Training",
    "Computer Hacking Forensics Investigator (CHFI) – EC-Council",
    "Cloud Penetration Testing – Offensive Security",
    "Threat Modeling and Secure Design – Microsoft Security Training",
    "Practical Malware Analysis – Pluralsight",
    "SOC Analyst Training – CyberDefenders",
    "Kali Linux for Ethical Hackers – Udemy",
    "Security Automation with Python – Cybrary",
    "Zero Trust Security Architecture – Udemy",
    "Cybersecurity Compliance and Frameworks – NIST Training",
    "Bug Bounty Hunting – HackerOne Training",
    "Mobile Application Security – NowSecure Academy",
    "Hacking and Securing APIs – APIsec University",
    "Critical Infrastructure Cybersecurity – US Department of Homeland Security (DHS)",
    "SCADA and Industrial Control System (ICS) Security – SANS Institute",
    "Darknet and OSINT Investigations – The OSINT Academy",
    "Incident Handling and Response – EC-Council",
    "Identity and Access Management (IAM) – Udemy",
    "Red Team vs Blue Team Cybersecurity – MITRE ATT&CK Training",
    "Exploit Development and Advanced Penetration Testing – Offensive Security",
    "Security Operations Center (SOC) Fundamentals – CyberWarrior Academy",
    "CISM (Certified Information Security Manager) – ISACA",
    "Data Breach Investigations – Verizon Data Breach Training",
    "Security Testing in DevOps – DevSecOps Training",
    "Cybersecurity Analytics – IBM (Coursera)",
    "Wi-Fi Hacking and Wireless Penetration Testing – Udemy",
    "Docker and Kubernetes Security – Udacity",
    "Google Cybersecurity Professional Certificate – Google (Coursera)",
    "Cyber Warfare and National Security – NATO Cyber Defence Training",
    "Digital Evidence and Cybercrime Investigation – Udemy",
    "Linux Hardening and Security – Red Hat Training",
    "Mobile and IoT Security – Georgia Tech (Coursera)",
    "AI-Based Threat Detection – MIT (edX)",
    "Cybersecurity Awareness for Executives – Harvard Business School",
    "Cloud Security Posture Management (CSPM) – Udemy",
    "Certified Kubernetes Security Specialist (CKS) – CNCF",
    "Phishing and Social Engineering Defense – KnowBe4 Training",
    "Network Intrusion Detection with Snort – Udemy",
    "Cybersecurity for Smart Cities – University of California, Berkeley (edX)",
    "GDPR and Data Privacy Compliance – Udemy",
    "Cybersecurity in Healthcare – John Hopkins University (Coursera)",
    "Honeypots and Deception Security – Pluralsight",
    "Red Teaming for Enterprise Security – MITRE Engenuity",
    "Digital Fraud Investigation – University of Toronto (Coursera)",
    "Cybersecurity for Financial Services – NYU Tandon School of Engineering",
    "Dark Web Investigations and Cyber Threats – Udemy",
    "Enterprise Security Architecture – TOGAF Training",
    "Software Security and Secure Coding – Secure Code Warrior",
    "Ethical Hacking Masterclass – The Cyber Mentor",
    "CISA (Certified Information Systems Auditor) – ISACA",
    "Public Key Infrastructure (PKI) and Digital Certificates – Udemy",
    "Ransomware Prevention and Response – SANS Institute",
    "Cybersecurity for Artificial Intelligence – IBM (Coursera)",
    "Threat Intelligence Analysis – Recorded Future Academy",
    "ICS/SCADA Cybersecurity – Udemy",
    "Metasploit for Penetration Testing – Offensive Security",
    "DevSecOps Essentials – AWS Security Training",
    "AI-Driven Cyber Threat Hunting – Carnegie Mellon University",
    "Risk Assessment and Cyber Insurance – Udemy",
    "Darknet Intelligence and Cybercrime Monitoring – Udemy",
    "Cyber Resilience and Business Continuity – MIT Sloan (edX)",
    "IoT Hacking and Security – Udemy",
    "Application Security Engineering – Udacity",
    "Cybersecurity Governance and Risk Management – Coursera"
]

missing_cybersecurity_skills = [
    "Advanced Penetration Testing and Exploit Development",
    "Real-world Incident Response and Digital Forensics",
    "Cyber Threat Intelligence and Threat Hunting",
    "Security Automation with Python and Bash Scripting",
    "Cloud Security (AWS, Azure, Google Cloud)",
    "Red Team vs. Blue Team Practical Training",
    "Zero Trust Security Architecture Implementation",
    "DevSecOps and Secure Software Development Lifecycle (SDLC)",
    "Hands-on Malware Analysis and Reverse Engineering",
    "Cyber Risk Management and Compliance Frameworks (NIST, ISO 27001, GDPR)",
    "Operational Technology (OT) and Industrial Control System (ICS) Security",
    "Advanced Web Application Security and Secure Coding Practices",
    "Mobile and IoT Security",
    "Blockchain and Smart Contract Security",
    "Dark Web Intelligence and OSINT Investigations",
    "Network Security Hardening and Intrusion Detection Systems",
    "Security in Artificial Intelligence and Machine Learning Models",
    "Cybersecurity Awareness and Social Engineering Defense",
    "Enterprise Security Governance and Policy Implementation",
    "Cybersecurity Project Management and Leadership",
    "Cloud Penetration Testing and Security Auditing",
    "Threat Modeling and Secure System Design",
    "Identity and Access Management (IAM) Implementation",
    "Wireless Network Security and Ethical Hacking",
    "Digital Privacy and Anonymity Techniques",
    "Honeypots and Deception Security Techniques",
    "Cybersecurity for Financial Services and Banking Systems",
    "Smart City and Critical Infrastructure Security",
    "Cybersecurity Risk Assessment and Quantitative Analysis",
    "Cybercrime Investigation and Digital Evidence Handling",
    "AI-Powered Cyber Threat Detection and Response",
    "Advanced Phishing Defense and Email Security",
    "Real-world Security Operations Center (SOC) Training",
    "Supply Chain Cybersecurity and Vendor Risk Management",
    "Automated Threat Intelligence Processing",
    "Incident Handling and Crisis Response Exercises",
    "Secure API Development and API Security Testing",
    "Threat Intelligence Sharing and Collaborative Cyber Defense",
    "DDoS Attack Mitigation Strategies",
    "Secure Firmware and Embedded Systems Security",
    "Digital Forensic Tools and Analysis Techniques",
    "Cyber Insurance and Legal Aspects of Cybersecurity",
    "Container Security (Docker, Kubernetes)",
    "Security Architecture for Microservices and Serverless Computing",
    "Cybersecurity for Government and Military Operations",
    "Cross-Site Scripting (XSS) and SQL Injection Prevention",
    "Cloud Security Posture Management (CSPM)",
    "Advanced Network Packet Analysis and Sniffing",
    "Zero Trust Security Architecture Implementation",
    "Security Testing in Agile and DevOps Environments",
    "Cybersecurity for AI and Deep Learning Models",
    "Mobile Application Reverse Engineering and Security Testing",
    "Automated Compliance Monitoring and Security Auditing",
    "DNS Security and Secure Network Architecture",
    "MITRE ATT&CK Framework Application",
    "Zero-Day Exploits and Advanced Persistent Threats (APTs)",
    "Cryptographic Protocols and Encryption Standards",
    "Security of Edge Computing and 5G Networks",
    "Risk-Based Authentication and Multi-Factor Authentication (MFA)",
    "IoT Device Hacking and Security Countermeasures",
    "Secure Code Review and Static Code Analysis",
    "Incident Analysis and Log Correlation Techniques",
    "Ransomware Attack Prevention and Recovery",
    "Web3 and Decentralized Security",
    "Security Metrics and Cybersecurity ROI Analysis",
    "Cybersecurity in Healthcare and Medical Device Security",
    "PCI-DSS Compliance and Payment System Security",
    "AI-Driven Security Automation and SOAR Platforms",
    "Hardware Security and Physical Penetration Testing",
    "Security Implications of Quantum Computing",
    "Bypassing Antivirus and EDR Detection Mechanisms",
    "Legal and Ethical Considerations in Ethical Hacking",
    "Cybersecurity for Autonomous Vehicles and Smart Transportation",
    "Insider Threat Detection and Prevention",
    "Advanced Social Engineering Techniques and Countermeasures",
    "GDPR, CCPA, and Global Data Privacy Regulations",
    "Cybersecurity for SaaS, PaaS, and IaaS Platforms",
    "Deepfake Detection and Synthetic Media Security",
    "Threat Actor Attribution and Cyber Espionage Analysis",
    "ICS/SCADA Cybersecurity Best Practices",
    "Darknet Research and Cybercriminal Tactics",
    "Advanced Persistent Threat (APT) Simulation and Defense",
    "Security Awareness Training for End Users",
    "Forensic Analysis of Mobile Devices and Cloud Storage",
    "Cybersecurity Investment and Budget Planning",
    "AI-Based Behavioral Analysis for Anomaly Detection",
    "Blockchain-Based Identity and Authentication Systems",
    "Cybersecurity Incident Simulation and Tabletop Exercises",
    "Disaster Recovery and Business Continuity Planning",
    "Password Cracking and Secure Authentication Mechanisms",
    "Securing SaaS Applications and Third-Party Integrations",
    "Red Teaming for Advanced Penetration Testing",
    "Cybersecurity for Robotics and Autonomous Systems",
    "Security Testing for AI-Generated Code",
    "Steganography and Covert Communication Analysis",
    "ICS/SCADA Security Incident Response Planning",
    "Using Machine Learning for Cyber Threat Analysis",
    "Threat Intelligence Platforms and Data Correlation",
    "Reverse Engineering Exploits and Vulnerability Research",
    "Digital Resilience and Cyber Warfare Strategies"
]

career_preparation_improvements_cybersecurity_ = [
    "More hands-on labs and real-world cybersecurity simulations",
    "Integration of industry-recognized certifications like CEH, CISSP, and OSCP",
    "Stronger partnerships with cybersecurity firms for internships and job placements",
    "Regular cybersecurity hackathons and Capture The Flag (CTF) competitions",
    "Industry mentorship programs with cybersecurity professionals",
    "Expanded coursework on emerging threats like AI-powered cyber attacks",
    "More practical training in penetration testing and ethical hacking",
    "A dedicated cybersecurity research center with access to real-world datasets",
    "More training in cloud security and DevSecOps methodologies",
    "Stronger focus on compliance frameworks like GDPR, NIST, and ISO 27001",
    "Enhanced job placement support with specialized cybersecurity career fairs",
    "Opportunities for students to contribute to open-source cybersecurity projects",
    "Integration of real-time threat intelligence analysis in coursework",
    "Guest lectures and workshops by ethical hackers and cybersecurity experts",
    "Development of a Security Operations Center (SOC) for student learning",
    "More networking opportunities with industry leaders and recruiters",
    "Cybersecurity bootcamps to bridge the gap between academia and industry",
    "More case studies on real-world cyberattacks and mitigation strategies",
    "Dedicated cybersecurity career coaching and resume-building workshops",
    "Practical experience with digital forensics and incident response",
    "Hands-on training with security tools like Splunk, Wireshark, and Metasploit",
    "Courses on advanced malware analysis and reverse engineering",
    "More focus on Red Team vs. Blue Team cybersecurity exercises",
    "Stronger collaboration with government cybersecurity agencies",
    "Opportunities to contribute to cybersecurity policy and ethical discussions",
    "More emphasis on soft skills like crisis management and communication",
    "Regular employer feedback to align curriculum with industry needs",
    "Cybersecurity project-based learning rather than just theoretical exams",
    "More resources for students to prepare for cybersecurity competitions",
    "Implementation of mandatory cybersecurity internships before graduation",
    "More collaboration with law enforcement on cybercrime case studies",
    "Cybersecurity startup incubation programs for students",
    "Expanded ethical hacking training with safe penetration testing environments",
    "More focus on security automation and AI-driven threat detection",
    "Creation of an alumni network for career guidance and job referrals",
    "Workshops on salary negotiation and cybersecurity career progression",
    "Practical experience in securing cloud environments (AWS, Azure, GCP)",
    "Exposure to threat intelligence platforms and risk assessment tools",
    "More coursework on secure coding and secure software development lifecycle",
    "Better funding for cybersecurity research projects and certifications",
    "Development of cybersecurity entrepreneurship programs",
    "Cross-disciplinary courses combining cybersecurity with business and law",
    "Expanded curriculum on digital privacy and online anonymity",
    "Mandatory workshops on security awareness and social engineering tactics",
    "Opportunities to work on real-world penetration testing projects",
    "Practical simulations of ransomware attacks and defense mechanisms",
    "More hands-on training with SIEM tools and threat detection systems",
    "Dedicated cybersecurity career counselors for job placement assistance",
    "Annual university-sponsored cybersecurity summits and conferences",
    "Integration of blockchain and cryptocurrency security courses",
    "More industry partnerships for cybersecurity apprenticeships",
    "Expanded training on API security and cloud-native security challenges",
    "Courses on threat modeling and secure architecture design",
    "More exposure to digital forensics case studies and investigations",
    "Ethical hacking courses with real-world penetration testing labs",
    "More cybersecurity networking events and employer engagement",
    "Live-fire cyber range environments for hands-on attack/defense scenarios",
    "Stronger collaboration between cybersecurity and software engineering programs",
    "Expanded access to cybersecurity hardware like network security appliances",
    "Focus on supply chain cybersecurity and third-party risk management",
    "Improved preparation for cybersecurity certification exams",
    "Access to real-world security incidents through case study repositories",
    "Mandatory cybersecurity ethics and legal training",
    "Courses on securing AI and machine learning models",
    "Dedicated courses on security in 5G and edge computing environments",
    "Hands-on training with exploit development and vulnerability research",
    "Opportunities to publish cybersecurity research in academic journals",
    "More real-world security project collaborations with companies",
    "Better career preparation resources for non-traditional cybersecurity roles",
    "Security consulting and advisory skill development",
    "Expanded coursework on biometric security and authentication methods",
    "More focus on automation of security testing in DevOps environments",
    "Better access to cybersecurity career transition programs for non-technical students",
    "More opportunities for cybersecurity students to present at conferences",
    "Workshops on effective incident response communication strategies",
    "Greater emphasis on cybersecurity risk assessment and business impact analysis",
    "Mandatory participation in cybersecurity internship programs",
    "Better integration of cybersecurity into software engineering courses",
    "More hands-on experience with security frameworks like MITRE ATT&CK",
    "Expanded focus on cybersecurity in fintech and banking sectors",
    "Development of a university-led cybersecurity consultancy team",
    "More funding for students to attend external cybersecurity training events",
    "More guidance on self-learning and independent cybersecurity research",
    "Expanded role-playing scenarios for real-world cyberattack simulations",
    "More coursework on OSINT and digital footprint reduction techniques",
    "Industry collaboration on real-time cybersecurity incident response drills",
    "Improved funding for cybersecurity innovation and entrepreneurship",
    "Inclusion of mobile security penetration testing in the curriculum",
    "Better exposure to cyber warfare tactics and government cybersecurity strategies",
    "Expanded focus on privacy-preserving technologies like homomorphic encryption",
    "Courses on ethical considerations in AI-driven cybersecurity",
    "More workshops on practical malware reverse engineering",
    "Advanced training on forensic analysis of encrypted data",
    "Creation of a cybersecurity student club with hands-on challenges",
    "Courses on securing software supply chains and open-source vulnerabilities",
    "Regular guest lectures from cybersecurity professionals working in top companies",
    "Introduction of cybersecurity strategy and risk management courses",
    "Integration of emerging cybersecurity trends into the curriculum",
    "Expanded use of gamification in cybersecurity training programs",
    "More networking and mentorship opportunities with industry leaders"
]





print(len(courses_DataSciences))
print(len(missing_skills_DataSciences))
print(len(career_preparation_improvements_DataSciences))

print(len(impactful_courses_intelligent_systems))
print(len(missing_skills_intelligent_systems))
print(len(career_preparation_improvements_IntelligentSystems))

print(len(cybersecurity_courses))
print(len(missing_cybersecurity_skills))
print(len(career_preparation_improvements_cybersecurity_))


##! Computing & Data Sciences
department_name = "Computing & Data Sciences"
num_samples = 100
df_datascience = generate_random_data(department_name, num_samples)

data_append_DataSciences = pd.DataFrame({
    "What is your current CGPA?": cgpa_list_DataSciences,
    "How many hours per week do you spend on extracurricular ( Non-academic / Supplementary )activities?": extracurricular_hours_DataSciences,
    "What is your expected starting salary after graduation? Please enter the amount in USD ($).": expected_salary_DataSciences,
    "Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?": courses_DataSciences,
    "Which professional or technical skills do you feel are missing from your university education?": missing_skills_DataSciences,
    "What specific improvements would you like to see in your university’s career preparation programs?": career_preparation_improvements_DataSciences
})

df_datascience =df_datascience.join(data_append_DataSciences,how='outer')


output_path = r"C:\Users\pc\survey\dataset\department\random data_Computing & Data Sciences.xlsx"
df_datascience.to_excel(output_path, index=False)

print(f"Data Computing & Data Sciences saved successfully to {output_path}")

##! Intelligent Systems
department_name = "Intelligent Systems"
num_samples = 100
df_IntelligentSystems = generate_random_data(department_name, num_samples)

data_append_IntelligentSystems = pd.DataFrame({
    "What is your current CGPA?": cgpa_list_IntelligentSystems,
    "How many hours per week do you spend on extracurricular ( Non-academic / Supplementary )activities?": extracurricular_hours_IntelligentSystems,
    "What is your expected starting salary after graduation? Please enter the amount in USD ($).": expected_salary_IntelligentSystems,
    "Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?": impactful_courses_intelligent_systems,
    "Which professional or technical skills do you feel are missing from your university education?": missing_skills_intelligent_systems,
    "What specific improvements would you like to see in your university’s career preparation programs?": career_preparation_improvements_IntelligentSystems
})

df_IntelligentSystems = df_IntelligentSystems.join(data_append_IntelligentSystems,how='outer')

output_path = r"C:\Users\pc\survey\dataset\department\random Intelligent Systems.xlsx"
df_IntelligentSystems.to_excel(output_path, index=False)

print(f"Data Intelligent Systems saved successfully to {output_path}")

##! Cybersecurity
department_name = "Cybersecurity"
num_samples = 100
df_Cybersecurity = generate_random_data(department_name, num_samples)

data_append_Cybersecurity = pd.DataFrame({
    "What is your current CGPA?": cgpa_list_Cybersecurity,
    "How many hours per week do you spend on extracurricular ( Non-academic / Supplementary )activities?": extracurricular_hours_Cybersecurity,
    "What is your expected starting salary after graduation? Please enter the amount in USD ($).": expected_salary_Cybersecurity,
    "Have you taken any courses outside of the university that you found particularly impactful that should be added to the university curriculum?": cybersecurity_courses,
    "Which professional or technical skills do you feel are missing from your university education?": missing_cybersecurity_skills,
    "What specific improvements would you like to see in your university’s career preparation programs?": career_preparation_improvements_cybersecurity_
})

df_Cybersecurity =df_Cybersecurity.join(data_append_Cybersecurity,how='outer')

output_path = r"C:\Users\pc\survey\dataset\department\random Cybersecurity.xlsx"
df_Cybersecurity.to_excel(output_path, index=False)

print(f"Data Cybersecurity saved successfully to {output_path}")


print(df_datascience.shape)
print(df_IntelligentSystems.shape)
print(df_Cybersecurity.shape)



