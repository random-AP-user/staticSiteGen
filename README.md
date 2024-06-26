# staticSiteGen
# Guide: Building a Simple Static Site Generator in Python

## 1. Understanding Static Site Generators (SSGs)
- Research what SSGs are and their significance in web development.
- Explore examples of popular SSGs like Eleventy, Hugo, Gatsby, and Jekyll.

## 2. Markdown Basics and YAML Front Matter
- Learn how to write Markdown for content.
- Understand YAML front matter and its role in defining metadata for Markdown files.
- Familiarize yourself with Python libraries for parsing Markdown and YAML front matter.

## 3. Setting Up Your Project
- Create a directory structure for your project, including folders for pages and templates.
- Populate the pages folder with static pages written in Markdown and YAML front matter.
- Establish the templates folder containing HTML files to be mixed with Markdown content.

## 4. Introduction to Jinja Templating Engine
- Explore Jinja and its function as a templating engine.
- Understand how to integrate Jinja into Python code for templating purposes.
- Learn how Jinja combines templates with text (Markdown) and data (YAML).

## 5. Generating the Static Site
- Write a Python script to iterate through files in the pages directory.
- Utilize Jinja to merge templates with Markdown content and YAML data.
- Ensure the generated site is stored in a directory named "docs".

## 6. Implementing Site Navigation
- Design and incorporate automatic navigation elements for each generated page.
- Enable users to navigate seamlessly between different pages of the site.

## 7. Version Control with Git and GitHub Pages
- Set up version control using Git for your project.
- Explore GitHub Pages for hosting your static site.
- Configure automatic deployment to update the live site with each push to the Git repository.

## 8. Best Practices in Development
- Develop your project using modular, organized functions.
- Utilize virtual environments for a clean development environment.
- Prioritize writing clean, readable, and maintainable code throughout the project.

### Bonus Challenge:
- **Implementing Blog Functionality**
  - Extend your SSG to include blog post functionality.
  - Introduce tags for blog posts and create a tag archive page within the site.

Following this guide will provide you with the necessary steps to build a simple static site generator in Python. By integrating Markdown content, YAML front matter, Jinja templating, site navigation, version control, and deployment automation, you can create a robust and efficient tool for generating static websites.
