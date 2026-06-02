Building a personal portfolio is a fantastic step for your resume! It gives recruiters a tangible way to see your skills.

Before we dive into the code, I need to be candid about a small technical constraint: **GitHub Pages (`yourname.github.io`) is a static hosting service.** This means it can only host static files like HTML, CSS, and JavaScript. It **cannot** run a live backend server like Python's FastAPI.

However, we can easily solve this! I will give you two things:

1. The **FastAPI code** you asked for, in case you want to build a backend (which you can deploy for free on a service like Render).
2. The **HTML/CSS template**, which you can simply upload to GitHub Pages right now to get your `.github.io` link instantly.

Here is the complete project for your portfolio.

---

### Step 1: Your Portfolio Code

You will need to create two files in the same folder.

#### 1. `index.html` (The Visual Portfolio)

This is the actual web page. It uses clean, modern CSS so you don't need any external libraries. Customize the text with your own details!

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Name | Portfolio</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            color: #333;
            line-height: 1.6;
        }
        header {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 3rem 1rem;
        }
        header h1 { margin: 0; font-size: 2.5rem; }
        header p { font-size: 1.2rem; opacity: 0.8; }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 2rem;
        }
        h2 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 0.5rem; }
        .project {
            background: #f4f4f4;
            margin-bottom: 1rem;
            padding: 1.5rem;
            border-radius: 5px;
        }
        .project h3 { margin-top: 0; color: #3498db; }
        .skills span {
            display: inline-block;
            background: #3498db;
            color: white;
            padding: 0.3rem 0.8rem;
            margin: 0.2rem;
            border-radius: 3px;
            font-size: 0.9rem;
        }
        footer {
            text-align: center;
            padding: 1rem;
            background: #ecf0f1;
            margin-top: 2rem;
        }
    </style>
</head>
<body>

    <header>
        <h1>Your Name</h1>
        <p>Software Engineer | Data Enthusiast | Problem Solver</p>
    </header>

    <div class="container">
        <section id="about">
            <h2>About Me</h2>
            <p>Hi! I'm a passionate developer looking to build impactful applications. I enjoy working with Python, data, and creating efficient backend systems. Welcome to my digital resume!</p>
        </section>

        <section id="skills">
            <h2>Skills</h2>
            <div class="skills">
                <span>Python</span>
                <span>FastAPI</span>
                <span>SQL</span>
                <span>Git & GitHub</span>
                <span>HTML/CSS</span>
            </div>
        </section>

        <section id="projects">
            <h2>Projects</h2>
            <div class="project">
                <h3>Project Title 1</h3>
                <p>A brief description of what you built, the problem it solved, and the technologies you used (e.g., Python, Pandas).</p>
                <a href="#">View Code on GitHub</a>
            </div>
            <div class="project">
                <h3>Project Title 2</h3>
                <p>Another awesome project you worked on. Highlight your specific contributions here.</p>
                <a href="#">View Code on GitHub</a>
            </div>
        </section>

        <section id="contact">
            <h2>Get In Touch</h2>
            <p>I am currently looking for new opportunities. Feel free to reach out!</p>
            <p>Email: <a href="mailto:your.email@example.com">your.email@example.com</a> | LinkedIn: <a href="#">Your Profile</a></p>
        </section>
    </div>

    <footer>
        <p>&copy; 2026 Your Name. Built with ❤️</p>
    </footer>

</body>
</html>

```

#### 2. `main.py` (The FastAPI Backend)

If you want to run this locally using FastAPI, save this code.

```python
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

# This route serves your HTML portfolio when someone visits the main URL
@app.get("/", response_class=FileResponse)
async def read_index():
    return "index.html"

if __name__ == "__main__":
    # Run this file with: python main.py
    uvicorn.run(app, host="0.0.0.0", port=8000)

```

*(To test this locally, you will need to install FastAPI and Uvicorn via your terminal: `pip install fastapi uvicorn`, then run `python main.py` and visit `http://localhost:8000` in your browser).*

---

### Step 2: How to Deploy for Free

Since a portfolio usually doesn't need a database or user logins, **Option A is highly recommended** for your resume.

#### Option A: GitHub Pages (Free `.github.io` domain) — *Recommended*

Skip the Python file entirely and just use GitHub to host the HTML. This is the industry standard for simple portfolios.

1. Create a new repository on GitHub and name it **exactly**: `yourgithubusername.github.io`
2. Upload the `index.html` file into this repository.
3. Commit the changes.
4. Wait about 2-3 minutes, then go to `https://yourgithubusername.github.io` in your browser. Your site is live!

#### Option B: Render (Free Python Hosting)

If you specifically want to prove you can deploy a live Python FastAPI application:

1. Create a GitHub repository and upload **both** `main.py` and `index.html`.
2. Create a new file called `requirements.txt` and add these two lines to it:
* `fastapi`
* `uvicorn`


3. Go to [Render.com](https://render.com) and create a free account.
4. Click "New" -> "Web Service" and connect your GitHub repository.
5. Set the Start Command to: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Render will deploy your FastAPI app for free (it will give you a domain like `your-portfolio.onrender.com`).

Which path sounds better to you: focusing entirely on the static site for GitHub Pages.
