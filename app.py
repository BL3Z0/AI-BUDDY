from flask import Flask, render_template, jsonify, redirect, url_for, send_from_directory

app = Flask(__name__)

# Complete Course Data
AI_COURSES = [
    {
        "id": 0,
        "title": "🤖 AI 101: Introduction to Artificial Intelligence",
        "duration": "2 weeks",
        "level": "Beginner",
        "image": "advanced_course.jpg",
        "emoji": "🤖",
        "color": "#FF9E00",
        "content": "Artificial Intelligence (AI) refers to the development of computer systems that can perform tasks that typically require human intelligence, such as learning, problem-solving, and decision-making. AI involves creating algorithms and models that enable machines to think and act like humans. There are several types of AI, including narrow or weak AI, general or strong AI, and superintelligence. AI has many applications in areas such as healthcare, finance, transportation, and education. It can improve efficiency, accuracy, and decision-making, and has the potential to transform many industries and aspects of our lives.",
        "lessons": [
            {
                "title": "What is AI?",
                "activities": ["Watch introductory videos", "AI terminology quiz", "Case study analysis"]
            },
            {
                "title": "Types of AI",
                "activities": ["Comparison chart creation", "Real-world examples discussion", "Future predictions exercise"]
            }
        ]
    },
    {
        "id": 1,
        "title": "🔮 Machine Learning Magic",
        "duration": "3 weeks",
        "level": "Beginner",
        "image": "neural_course.jpg",
        "emoji": "🔮",
        "color": "#00B4D8",
        "content": "Machine learning is a type of AI that enables machines to learn from data and improve their performance over time. It involves training algorithms on large datasets, allowing them to identify patterns and make predictions or decisions. Machine learning is a key aspect of many AI applications, including image recognition, natural language processing, and predictive maintenance. There are several types of machine learning, including supervised learning, unsupervised learning, and reinforcement learning. Machine learning has many applications in areas such as healthcare, finance, and marketing, and has the potential to revolutionize many industries.",
        "lessons": [
            {
                "title": "ML Fundamentals",
                "activities": ["Data collection exercise", "Simple model training", "Prediction practice"]
            }
        ]
    },
    {
        "id": 2,
        "title": "⚖️ AI Ethics: The Good, the Bad, and the Ugly",
        "duration": "2 weeks",
        "level": "Intermediate",
        "image": "detective_course.jpg",
        "emoji": "⚖️",
        "color": "#7209B7",
        "content": "AI ethics is the study of the moral implications of AI development and deployment. It involves considering the potential consequences of AI on individuals and society, including issues such as bias, privacy, and accountability. AI ethics is important because AI systems can have significant benefits or risks, and it is crucial to develop AI systems that are fair, transparent, and accountable. There are many challenges and opportunities in AI ethics, including ensuring that AI systems are designed and developed with ethics in mind, and that they are deployed in ways that benefit society.",
        "lessons": [
            {
                "title": "Ethical Dilemmas",
                "activities": ["Case study analysis", "Debate sessions", "Policy writing exercise"]
            }
        ]
    },
    {
        "id": 3,
        "title": "💬 Natural Language Processing: Talking to Machines",
        "duration": "3 weeks",
        "level": "Intermediate",
        "image": "music_course.jpg",
        "emoji": "💬",
        "color": "#F72585",
        "content": "Natural Language Processing (NLP) is a field of AI that enables machines to understand and generate human language. NLP involves developing algorithms that can process and analyze large amounts of language data, allowing machines to perform tasks such as language translation, sentiment analysis, and text summarization. NLP has many applications in areas such as customer service, language translation, and text analysis, and has the potential to revolutionize the way we interact with machines.",
        "lessons": [
            {
                "title": "Language Models",
                "activities": ["Chatbot building", "Sentiment analysis exercise", "Text generation practice"]
            }
        ]
    },
    {
        "id": 4,
        "title": "👁️ Computer Vision: Seeing is Believing",
        "duration": "3 weeks",
        "level": "Intermediate",
        "image": "game_course.jpg",
        "emoji": "👁️",
        "color": "#4361EE",
        "content": "Computer vision is a field of AI that enables machines to interpret and understand visual data from images and videos. Computer vision involves developing algorithms that can identify objects, people, and patterns, and has many applications in areas such as image recognition, surveillance, and autonomous vehicles. Computer vision is a key aspect of many AI applications, and has the potential to revolutionize many industries.",
        "lessons": [
            {
                "title": "Image Recognition",
                "activities": ["Object detection demo", "Facial recognition exercise", "Augmented reality project"]
            }
        ]
    },
    {
        "id": 5,
        "title": "🤖 Robotics and AI: Building Intelligent Machines",
        "duration": "4 weeks",
        "level": "Intermediate",
        "image": "robotics_course.jpg",
        "emoji": "🤖",
        "color": "#3A0CA3",
        "content": "Robotics and AI involve developing machines that can perform tasks autonomously, using sensors, actuators, and control systems. AI is used in robotics to enable machines to learn, make decisions, and interact with humans. Robotics and AI have many applications in areas such as manufacturing, healthcare, and transportation, and have the potential to transform many industries.",
        "lessons": [
            {
                "title": "Robot Programming",
                "activities": ["Simulator exercises", "Obstacle course challenge", "Human-robot interaction study"]
            }
        ]
    },
    {
        "id": 6,
        "title": "🛠️ AI Project Development: From Idea to Reality",
        "duration": "4 weeks",
        "level": "Advanced",
        "image": "olympiad_course.jpg",
        "emoji": "🛠️",
        "color": "#4CC9F0",
        "content": "AI project development involves several stages, including problem definition, data collection, model development, testing, and deployment. It requires a multidisciplinary approach, involving expertise in areas such as computer science, data science, and domain-specific knowledge. AI project development can be challenging, but also offers many opportunities for innovation and growth.",
        "lessons": [
            {
                "title": "Project Lifecycle",
                "activities": ["Project planning workshop", "Data collection exercise", "Model deployment demo"]
            }
        ]
    },
    {
        "id": 7,
        "title": "📊 Data Analysis with AI: Unlocking Insights",
        "duration": "3 weeks",
        "level": "Intermediate",
        "image": "space_course.jpg",
        "emoji": "📊",
        "color": "#B5179E",
        "content": "Data analysis with AI involves using machine learning and other AI techniques to extract insights from large datasets. It enables businesses and organizations to make informed decisions, and has many applications in areas such as business intelligence, healthcare, and finance. Data analysis with AI can help organizations to identify patterns, trends, and correlations, and to make predictions and recommendations.",
        "lessons": [
            {
                "title": "Data Exploration",
                "activities": ["Dataset analysis", "Visualization creation", "Pattern recognition exercise"]
            }
        ]
    },
    {
        "id": 8,
        "title": "🌍 AI in Real-World Applications: Changing the World",
        "duration": "3 weeks",
        "level": "Intermediate",
        "image": "robot_course_bg.jpg",
        "emoji": "🌍",
        "color": "#F8961E",
        "content": "AI has many real-world applications, including healthcare, finance, education, and transportation. AI can improve efficiency, accuracy, and decision-making, and has the potential to transform many industries and aspects of our lives. AI applications can range from virtual assistants and chatbots to predictive maintenance and autonomous vehicles.",
        "lessons": [
            {
                "title": "Industry Applications",
                "activities": ["Case study review", "Solution brainstorming", "Impact analysis exercise"]
            }
        ]
    },
    {
        "id": 9,
        "title": "🚀 The Future of AI: Trends and Opportunities",
        "duration": "2 weeks",
        "level": "Advanced",
        "image": "star_bg.jpg",
        "emoji": "🚀",
        "color": "#90BE6D",
        "content": "The future of AI is exciting and rapidly evolving. Emerging trends include the development of more sophisticated machine learning algorithms, increased use of AI in edge devices, and growing importance of AI ethics and governance. The future of AI holds many opportunities for innovation and growth, and it is likely to have a significant impact on many industries and aspects of our lives. As AI continues to evolve, it is crucial to consider the potential benefits and risks, and to develop AI systems that are fair, transparent, and accountable.",
        "lessons": [
            {
                "title": "Emerging Trends",
                "activities": ["Trend research project", "Future scenario planning", "Innovation workshop"]
            }
        ]
    }
]

AI_QUIZ = [
    {
        "question": "What is Artificial Intelligence (AI)?",
        "options": [
            "A type of computer hardware",
            "A type of software that can think and learn",
            "A type of programming language"
        ],
        "answer": 1,
        "category": "basics"
    },
    {
        "question": "What are the types of AI?",
        "options": [
            "Narrow AI, General AI, and Superintelligence",
            "Machine Learning, Deep Learning, and Natural Language Processing",
            "Robotics, Computer Vision, and Expert Systems"
        ],
        "answer": 0,
        "category": "basics"
    },
    {
        "question": "What is Machine Learning?",
        "options": [
            "A type of AI that enables machines to learn from data",
            "A type of programming language",
            "A type of computer hardware"
        ],
        "answer": 0,
        "category": "ml"
    },
    {
        "question": "What are the applications of Natural Language Processing (NLP)?",
        "options": [
            "Image Recognition, Object Detection, and Facial Recognition",
            "Predictive Maintenance, Quality Control, and Supply Chain Management",
            "Language Translation, Sentiment Analysis, and Text Summarization"
        ],
        "answer": 2,
        "category": "nlp"
    },
    {
        "question": "What is Computer Vision?",
        "options": [
            "A type of camera technology",
            "A field of AI that enables machines to interpret visual data",
            "A type of image editing software"
        ],
        "answer": 1,
        "category": "vision"
    },
    {
        "question": "What are the benefits of AI in healthcare?",
        "options": [
            "Reduced patient care, increased costs, and decreased outcomes",
            "No benefits",
            "Improved diagnosis accuracy, personalized medicine, and increased efficiency"
        ],
        "answer": 2,
        "category": "applications"
    },
    {
        "question": "What is the role of data in AI?",
        "options": [
            "Data is used to train and test AI models",
            "Data is used to deploy AI models",
            "Data is not necessary for AI"
        ],
        "answer": 0,
        "category": "basics"
    },
    {
        "question": "What are the types of machine learning?",
        "options": [
            "Deep Learning, Neural Networks, and Decision Trees",
            "Linear Regression, Logistic Regression, and Clustering",
            "Supervised Learning, Unsupervised Learning, and Reinforcement Learning"
        ],
        "answer": 2,
        "category": "ml"
    },
    {
        "question": "What is the difference between AI and Machine Learning?",
        "options": [
            "Machine Learning is a broader field that includes AI",
            "AI is a broader field that includes Machine Learning",
            "AI and Machine Learning are the same thing"
        ],
        "answer": 1,
        "category": "basics"
    },
    {
        "question": "What are the potential risks of AI?",
        "options": [
            "Improved efficiency, increased productivity, and enhanced customer experience",
            "No risks",
            "Bias, job displacement, and security risks"
        ],
        "answer": 2,
        "category": "ethics"
    },
    {
        "question": "What is Robotics and AI?",
        "options": [
            "Developing machines that can only follow instructions",
            "Developing machines that can perform tasks autonomously",
            "Developing machines that can only interact with humans"
        ],
        "answer": 1,
        "category": "robotics"
    },
    {
        "question": "What are the applications of AI in finance?",
        "options": [
            "Predicting stock prices, detecting fraud, and optimizing investment portfolios",
            "Managing customer accounts, processing transactions, and generating reports",
            "Developing financial models, forecasting market trends, and analyzing economic data"
        ],
        "answer": 0,
        "category": "applications"
    },
    {
        "question": "What is the importance of AI ethics?",
        "options": [
            "Ensuring that AI systems are fair, transparent, and accountable",
            "Ensuring that AI systems are efficient and effective",
            "Ensuring that AI systems are profitable and popular"
        ],
        "answer": 0,
        "category": "ethics"
    },
    {
        "question": "What are the benefits of AI in education?",
        "options": [
            "Personalized learning, improved student outcomes, and increased efficiency",
            "Standardized testing, rigid curricula, and decreased student engagement",
            "No benefits"
        ],
        "answer": 0,
        "category": "applications"
    },
    {
        "question": "What is the future of AI?",
        "options": [
            "Slow and stagnant",
            "Exciting and rapidly evolving",
            "Uncertain and unpredictable"
        ],
        "answer": 1,
        "category": "future"
    },
    {
        "question": "What are the types of AI models?",
        "options": [
            "Machine Learning models, Deep Learning models, and Neural Networks",
            "Decision Trees, Random Forests, and Support Vector Machines",
            "Linear Regression, Logistic Regression, and Clustering"
        ],
        "answer": 0,
        "category": "ml"
    },
    {
        "question": "What is the role of AI in business?",
        "options": [
            "Improving efficiency, increasing productivity, and enhancing customer experience",
            "Reducing costs, increasing profits, and improving competitiveness",
            "No role"
        ],
        "answer": 0,
        "category": "applications"
    },
    {
        "question": "What are the challenges of AI development?",
        "options": [
            "Data quality, model complexity, and interpretability",
            "Hardware limitations, software bugs, and network connectivity",
            "No challenges"
        ],
        "answer": 0,
        "category": "development"
    },
    {
        "question": "What is the relationship between AI and data science?",
        "options": [
            "AI is a key aspect of data science",
            "Data science is a key aspect of AI",
            "AI and data science are unrelated fields"
        ],
        "answer": 0,
        "category": "basics"
    },
    {
        "question": "What are the potential applications of AI in transportation?",
        "options": [
            "Self-driving cars, traffic management, and route optimization",
            "Predictive maintenance, quality control, and supply chain management",
            "No applications"
        ],
        "answer": 0,
        "category": "applications"
    }
]
@app.route('/debug-images')
def debug_images():
    images = [
        'advanced_course.jpg',
        'neural_course.jpg',
        # Add all other image filenames
    ]
    html = "<h1>Image Debugger</h1>"
    for img in images:
        path = url_for('static', filename=f'images/{img}')
        html += f'<div><img src="{path}" style="max-width:200px;"><p>{path}</p></div>'
    return html

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/courses")
def courses():
    return render_template("courses.html", courses=AI_COURSES)

@app.route('/course/<int:course_id>')
def course_detail(course_id):
    if 0 <= course_id < len(AI_COURSES):
        return render_template('course_detail.html', 
                            course=AI_COURSES[course_id],
                            AI_QUIZ=AI_QUIZ)
    return redirect(url_for('courses'))

@app.route("/quizzes")
def quizzes():
    return render_template("quizzes.html")

@app.route("/games")
def games():
    return render_template("games.html")

@app.route("/api/quiz")
def get_quiz():
    return jsonify(AI_QUIZ)

@app.route('/static/images/<filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
