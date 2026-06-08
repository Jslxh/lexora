import gradio as gr

def generate_roadmap(role):

    roadmaps = {

        "AI Engineer": """
🚀 AI Engineer
Skills:
• Python
• Machine Learning
• Deep Learning
• NLP
• LangChain
• Vector Databases
• MLOps
Projects:
• RAG Chatbot
• AI Agent
• Recommendation System
Career Path:
AI Engineer → Senior AI Engineer → AI Architect
""",

        "Machine Learning Engineer": """
🤖 Machine Learning Engineer
Skills:
• Python
• Statistics
• Scikit-Learn
• TensorFlow
• PyTorch
• Feature Engineering
Projects:
• Price Prediction
• Fraud Detection
• Churn Prediction
Career Path:
ML Engineer → Senior ML Engineer → Lead ML Engineer
""",

        "Data Scientist": """
📈 Data Scientist
Skills:
• Python
• Statistics
• SQL
• Machine Learning
• Data Visualization
Projects:
• Customer Segmentation
• Sales Forecasting
• Business Analytics
Career Path:
Data Scientist → Senior Data Scientist → Principal Data Scientist
""",

        "Data Analyst": """
📊 Data Analyst
Skills:
• Excel
• SQL
• Python
• Power BI
• Tableau
Projects:
• Sales Dashboard
• HR Analytics
• Customer Analytics
Career Path:
Data Analyst → Senior Analyst → Analytics Manager
""",

        "Business Analyst": """
💼 Business Analyst
Skills:
• Excel
• SQL
• Power BI
• Requirement Gathering
• Stakeholder Management
Projects:
• KPI Dashboard
• Business Process Analysis
Career Path:
Business Analyst → Senior BA → Product Manager
""",

        "Software Engineer": """
💻 Software Engineer
Skills:
• DSA
• OOP
• DBMS
• OS
• CN
• System Design
Projects:
• E-Commerce App
• Library Management System
• REST API
Career Path:
SDE 1 → SDE 2 → Senior Software Engineer
""",

        "Full Stack Developer": """
🌐 Full Stack Developer
Skills:
• HTML
• CSS
• JavaScript
• React
• Node.js
• MongoDB
Projects:
• Social Media App
• Job Portal
• E-Commerce Website
Career Path:
Developer → Senior Developer → Tech Lead
""",

        "MLOps Engineer": """
⚙️ MLOps Engineer
Skills:
• Docker
• Kubernetes
• MLflow
• AWS
• CI/CD
• Monitoring
Projects:
• Model Deployment Pipeline
• Automated ML Workflow
Career Path:
MLOps Engineer → Senior MLOps Engineer → Platform Architect
""",

        "Cloud Engineer": """
☁️ Cloud Engineer
Skills:
• AWS
• Azure
• Terraform
• Docker
• Kubernetes
Projects:
• Cloud Migration
• Infrastructure Automation
Career Path:
Cloud Engineer → Senior Cloud Engineer → Cloud Architect
""",

        "Cybersecurity Analyst": """
🔒 Cybersecurity Analyst
Skills:
• Networking
• Ethical Hacking
• SIEM
• Security Auditing
Projects:
• Vulnerability Assessment
• Security Monitoring
Career Path:
Security Analyst → Security Engineer → Security Architect
""",

        "DevOps Engineer": """
🚀 DevOps Engineer
Skills:
• Linux
• Docker
• Kubernetes
• Jenkins
• GitHub Actions
Projects:
• CI/CD Pipeline
• Infrastructure Automation
Career Path:
DevOps Engineer → Senior DevOps Engineer → DevOps Architect
""",

        "UI/UX Designer": """
🎨 UI/UX Designer
Skills:
• Figma
• Wireframing
• User Research
• Prototyping
Projects:
• Mobile App Design
• Website Redesign
Career Path:
Designer → Senior Designer → Design Lead
""",

        "Product Manager": """
📦 Product Manager
Skills:
• Product Strategy
• Analytics
• Agile
• Roadmapping
Projects:
• Product Launch Strategy
• Market Analysis
Career Path:
PM → Senior PM → Director of Product
"""
    }

    return roadmaps[role]


demo = gr.Interface(
    fn=generate_roadmap,
    inputs=gr.Dropdown(
        [
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist",
            "Data Analyst",
            "Business Analyst",
            "Software Engineer",
            "Full Stack Developer",
            "MLOps Engineer",
            "Cloud Engineer",
            "Cybersecurity Analyst",
            "DevOps Engineer",
            "UI/UX Designer",
            "Product Manager"
        ],
        label="Select Your Career Goal"
    ),
    outputs=gr.Textbox(lines=20, label="Your Roadmap"),
    title="LEXORA",
    description="AI-Powered Career Roadmap Generator"
)

demo.launch()
