from glob import escape
import yaml
from yaml import load
import time

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def generate_html_table(documents):
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Network Latency Report</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<nav class="dropdown">
  <button class="dropbtn">Home</button>
  <div class="dropdown-content">
    {nav}
  </div>
</nav>
    {blogpost}
</body>
</html>
"""

    nav = ""
    blogpost = ""
    for i, doc in enumerate(documents):
        i += 1
        blog = doc["blog"]
        title = blog["title"]
        para = blog["para"]
        img = blog["img"]
        nav += f"""
<a href="#blog{i}">{i} : {title}</a>
"""
        blogpost += f"""
<div class="blog" id="blog{i}">
    <div>
        <h2>{title}</h2>
        <img src="{img['path']}" alt="{img['name']}">
        <div><a href="{img['source']}">image source</a></div>
        <p>{para}</p>
    </div>
</div>
"""
    html_content = html_content.format(nav=nav, blogpost=blogpost)
    return html_content


def main():
    stream = open("pages/markdown.yaml", "r")
    documents = yaml.load_all(stream, Loader)
    html_content = generate_html_table(documents)
    with open("index.html", "w") as html_file:
        html_file.write(html_content)


if __name__ == "__main__":
    t0 = time.time()
    main()
    t1 = time.time()
    total_t = t1 - t0
    print(f"totaal tijd: {total_t}")
