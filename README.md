##  Django SerpAPI Search Project

This is a beginner-friendly Django project that uses the **SerpAPI** to fetch and display Google search results. It supports multiple keyword queries and allows users to download results as a CSV file.

---

##  Features

-  Google search using [SerpAPI](https://serpapi.com/)
-  Search multiple keywords at once
-  Display search result titles, links, and snippets
-  Download results as a CSV file
-  Responsive layout using HTML & CSS
-  Templates and static files properly configured
-  Ready for deployment on Render or similar platforms

---

##  How to Run This Project Locally

Follow these steps to get the project running on your system:

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/UtkarshSharma62020/django-serpapi-search.git
cd django-serpapi-search
```

---

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

- **Windows**:  
  `venv\Scripts\activate`

- **macOS/Linux**:  
  `source venv/bin/activate`

---

### 3️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure SerpAPI Key (Important 🔐)

This project uses **SerpAPI** to fetch Google results. You must set your API key.

#### ✅ Steps:

- Go to: https://serpapi.com/manage-api-key ,if already signed in, if not just do it.
- Copy your API key
- And then in file path named, django-serpapi-search\project\settings.py, replace the SERPAPI_KEY in quotation marks("SERPAPI_KEY") to actual api key under quotation mark.
---

### 5️⃣ Set Up the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

Visit:  
👉 To your Port

---
