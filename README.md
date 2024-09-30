# Job Recommendation Engine - Vector search example

A recommendation engine built using spaCy and Sentence-BERT (SBERT) to provide job recommendations based on user queries. This engine utilizes advanced NLP techniques to generate embeddings for job descriptions and titles, enabling semantic similarity searches.
Built using django

## Features

- Choose between `spaCy` and `Sentence-BERT` for generating text embeddings.
- Find jobs that are semantically similar to a given query and rank.

## Requirements

- Python 3.7+
- `pandas`
- `scikit-learn`
- `sentence-transformers`
- `spacy`

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Leomv55/Job-recommendation---Django-and-Spacy.git
   cd Job-recommendation---Django-and-Spacy
   ```

2. Install the required packages:

   ```bash
    pipenv install
   ````

2. Download the spaCy model:

   ```bash
    python -m spacy download en_core_web_md
   ```

3. Optionally, download the SBERT model (if using Sentence-BERT):

   ```bash
    pipenv install sentence-transformers
   ````
4. Run the server
   ```bash
    pipenv shell
    ./manage.py runserver
   ```
5. Run the migrations
   ```bash
    pipenv shell #if not in the env
    ./manage.py migrate
   ```

6. Go to another terminal and Run the django command to populate job post
   ```bash
    pipenv shell #if not in the env
    ./manage.py create_job_posts
   ```

7. Run django command to create vector cache (dataframe dump with embeddings)
   ```bash
    pipenv shell #if not in the env
    ./manage.py create_update_vector_cache
   ``` 

# Endpoints
- List all job posts
  - `GET` `api/jobs/`
  - Request params
    - `per_page` - Count per page
    - `page` - Page no 
  - Response
```json
{
  "meta": {
    "current_page": 1,
    "has_next": true,
    "has_previous": false,
    "total": 126
  },
  "data": [
    {
      "id": 1,
      "title": "Software Engineer",
      "description": "We are looking for a skilled software engineer to join our dynamic team. You will be responsible for developing high-quality software solutions and collaborating with cross-functional teams.",
      "skills": [
        "Problem-Solving",
        "Java",
        "JavaScript",
        "Python",
        "Agile Methodologies"
      ]
    },
    {
      "id": 2,
      "title": "Data Analyst",
      "description": "Join our analytics team to provide data-driven insights. You will analyze complex datasets, generate reports, and support decision-making processes.",
      "skills": [
        "Python"
      ]
    },
    {
      "id": 3,
      "title": "Product Manager",
      "description": "Seeking a proactive product manager to lead product development from conception to launch. You will work closely with engineering, marketing, and sales teams.",
      "skills": [
        "Agile Methodologies"
      ]
    },
    {
      "id": 4,
      "title": "Graphic Designer",
      "description": "Looking for a creative graphic designer to create visually appealing designs for various media. Experience in branding and digital marketing is a plus.",
      "skills": []
    },
    {
      "id": 5,
      "title": "Marketing Specialist",
      "description": "We need a marketing specialist to develop and execute marketing strategies. You will analyze market trends and work on campaigns to enhance brand visibility.",
      "skills": [
        "Communication"
      ]
    },
    {
      "id": 6,
      "title": "Systems Administrator",
      "description": "Join our IT team as a systems administrator. You will manage and maintain our IT infrastructure, ensuring optimal performance and security.",
      "skills": []
    },
    {
      "id": 7,
      "title": "Network Engineer",
      "description": "We are looking for a network engineer to design, implement, and maintain our network infrastructure. You will ensure network security and performance.",
      "skills": []
    },
    {
      "id": 8,
      "title": "Frontend Developer",
      "description": "Join our development team as a frontend developer. You will create responsive and user-friendly web applications using modern frameworks.",
      "skills": [
        "JavaScript"
      ]
    },
    {
      "id": 9,
      "title": "Project Coordinator",
      "description": "We need a project coordinator to assist in managing project timelines and deliverables. You will work closely with project managers and teams.",
      "skills": [
        "Problem-Solving",
        "Communication"
      ]
    },
    {
      "id": 10,
      "title": "Human Resources Manager",
      "description": "Seeking an HR manager to oversee our recruitment, employee relations, and performance management processes.",
      "skills": []
    }
  ]
}
```

- Similarity search
  - `GET` `api/recommend-jobs/`
  - Request params
    - `query` - search query to get the relevant result
  - Response
```json
[
  {
    "id": 82,
    "title": "User Interface Developer",
    "description": "We are seeking a user interface developer to create user-friendly and visually appealing interfaces for our applications.",
    "skills": [
      "JavaScript",
      "CSS",
      "HTML",
      "Responsive Design"
    ],
    "similarity": 0.5281089544296265
  },
  {
    "id": 60,
    "title": "Web Developer",
    "description": "Looking for a web developer to design and maintain our websites, ensuring a great user experience.",
    "skills": [
      "JavaScript",
      "CSS",
      "HTML"
    ],
    "similarity": 0.5220771431922913
  },
  {
    "id": 85,
    "title": "Frontend UI/UX Developer",
    "description": "Join our team as a frontend UI/UX developer to design and implement engaging user interfaces.",
    "skills": [
      "JavaScript",
      "CSS",
      "HTML",
      "Prototyping",
      "User Research"
    ],
    "similarity": 0.43711382150650024
  },
  {
    "id": 8,
    "title": "Frontend Developer",
    "description": "Join our development team as a frontend developer. You will create responsive and user-friendly web applications using modern frameworks.",
    "skills": [
      "JavaScript"
    ],
    "similarity": 0.39784252643585205
  },
  {
    "id": 120,
    "title": "Mobile App Developer",
    "description": "We need a mobile app developer to design and build user-friendly mobile applications.",
    "skills": [
      "Java",
      "Swift",
      "UI/UX Design"
    ],
    "similarity": 0.36481642723083496
  },
  {
    "id": 1,
    "title": "Software Engineer",
    "description": "We are looking for a skilled software engineer to join our dynamic team. You will be responsible for developing high-quality software solutions and collaborating with cross-functional teams.",
    "skills": [
      "Problem-Solving",
      "Java",
      "JavaScript",
      "Python",
      "Agile Methodologies"
    ],
    "similarity": 0.2998475432395935
  },
  {
    "id": 55,
    "title": "User Experience Designer",
    "description": "Looking for a user experience designer to create user-centered designs that enhance product usability.",
    "skills": [
      "Prototyping",
      "Wireframing",
      "Collaboration"
    ],
    "similarity": 0.28841352462768555
  },
  {
    "id": 112,
    "title": "Graphic Designer",
    "description": "We are seeking a graphic designer to create visually appealing designs for print and digital media.",
    "skills": [
      "Attention to Detail",
      "Creativity",
      "Adobe Creative Suite",
      "Typography",
      "Collaboration"
    ],
    "similarity": 0.27945107221603394
  },
  {
    "id": 107,
    "title": "Machine Learning Engineer",
    "description": "We are seeking a machine learning engineer to design and implement machine learning models for various applications.",
    "skills": [
      "Python",
      "Machine Learning",
      "TensorFlow"
    ],
    "similarity": 0.2750617265701294
  },
  {
    "id": 49,
    "title": "Artificial Intelligence Engineer",
    "description": "We are looking for an AI engineer to develop intelligent systems and algorithms using machine learning techniques.",
    "skills": [
      "Python",
      "Data Analysis",
      "Machine Learning"
    ],
    "similarity": 0.2673020362854004
  }
]
```

# Screenshots

# settings.py

- Set the path vector cache - this will be used for searching and ranking

```
VECTOR_CACHE_PATH = "path/to/vector_cache.pkl"
```

- Set recommendation engine - available `spacy`, `bert`
```
RECOMMENDATION_MODEL = 'spacy' // Default
```
# Contributing

Contributions are welcome! If you have suggestions for improvements or want to add features, feel free to open an issue or submit a pull request.

Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.

# License

This project is licensed under the MIT License - see the LICENSE file for details.
Contact

For any inquiries, please reach out to [leomv3@gmail.com].
