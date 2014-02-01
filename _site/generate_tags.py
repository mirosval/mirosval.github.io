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
    if os.path.isdir(f):
        os.rmdir(os.path.join('tags', f))
    elif os.path.isfile(f):
        os.unlink(os.path.join('tags', f))

# create tag pages
for tag in tags:
    if not os.path.exists(os.path.join('tags', tag)):
        os.makedirs(os.path.join('tags', tag))
    with open(os.path.join('tags', tag, 'index.html'), 'w') as f:
        f.write("""---
layout: default
title: """ + tag.replace('-', ' ').capitalize() + """ Tag
---
<h2>{{ page.title }}</h2>

{% for post in site.tags.""" + tag + """ %}
    <article>
        <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
        <span class="published">Published {{ post.date | date: "%-d %B %Y" }}</span>
        {{ post.excerpt }}
    </article>
{% endfor %}
""")

# cleanup old categories
for f in os.listdir('categories'):
    if os.path.isdir(f):
        os.rmdir(os.path.join('categories', f))
    elif os.path.isfile(f):
        os.unlink(os.path.join('categories', f))

# create category pages
for category in categories:
    if not os.path.exists(os.path.join('categories', category)):
        os.makedirs(os.path.join('categories', category))
    with open(os.path.join('categories', category, 'index.html'), 'w') as f:
        f.write("""---
layout: default
title: """ + category.replace('-', ' ').capitalize() + """ Category
---
<h2>{{ page.title }}</h2>

{% for post in site.categories.""" + category + """ %}
    <article>
        <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
        <span class="published">Published {{ post.date | date: "%-d %B %Y" }}</span>
        {{ post.excerpt }}
    </article>
{% endfor %}
""")

