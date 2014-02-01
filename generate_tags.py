import os
import re

tags = set()
categories = set()

# gather tags and categories from post files
for post in os.listdir('_posts'):
    with open(os.path.join('_posts', post), 'r') as f:
        for line in f:
            if line.startswith('categories:'):
                line = re.sub('categories: ?\[', '', line)
                line = re.sub('\]\n', '', line)
                categories = categories | set(re.split(', ?', line))

            if line.startswith('tags:'):
                line = re.sub('tags: ?\[', '', line)
                line = re.sub('\]\n', '', line)
                tags = tags | set(re.split(', ?', line))

tags = [tag for tag in list(tags) if tag != '']
categories = [cat for cat in list(categories) if cat != '']

# cleanup old tags
for f in os.listdir('tags'):
    path = os.path.join('tags', f)
    if os.path.isdir(path):
        import shutil
        shutil.rmtree(path)
    elif os.path.isfile(path):
        os.unlink(path)

# create tag pages
for tag in tags:
    path = os.path.join('tags', tag.lower())
    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join('tags', tag.lower(), 'index.html'), 'w') as f:
        f.write("""---
layout: default
title: """ + tag.replace('-', ' ').capitalize() + """ Tag
---
<h2>{{ page.title }}</h2>

{% for post in site.tags.""" + tag.lower() + """ %}
    <article>
        <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
        <span class="published">Published {{ post.date | date: "%-d %B %Y" }}</span>
        {{ post.excerpt }}
    </article>
{% endfor %}
""")

# cleanup old categories
for f in os.listdir('categories'):
    path = os.path.join('categories', f)
    if os.path.isdir(path):
        import shutil
        shutil.rmtree(path)
    elif os.path.isfile(path):
        os.unlink(path)

# create category pages
for category in categories:
    path = os.path.join('categories', category.lower())
    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join('categories', category.lower(), 'index.html'), 'w') as f:
        f.write("""---
layout: default
title: """ + category.replace('-', ' ').capitalize() + """ Category
---
<h2>{{ page.title }}</h2>

{% for post in site.categories.""" + category.lower() + """ %}
    <article>
        <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
        <span class="published">Published {{ post.date | date: "%-d %B %Y" }}</span>
        {{ post.excerpt }}
    </article>
{% endfor %}
""")

