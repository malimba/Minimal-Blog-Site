# Minimal Blog Site

A lightweight **Django blog** for creating, editing, and deleting posts — with AJAX-powered updates so the page never fully reloads.

![Django](https://img.shields.io/badge/Django-4.2-092E20?style=flat-square&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)

## Features

- Create posts from the home page
- **Edit** and **delete** posts inline via AJAX
- SQLite database — zero external deps for local dev
- Simple `BlogPost` model (`content`, `dateCreated`)

## Tech stack

- **Django 4.2** — MVT pattern
- **SQLite** — default Django DB
- **Vanilla JS** — `blog.min.js` for AJAX CRUD

## Quick start

```bash
cd blogsite
pip install django
python manage.py migrate
python manage.py runserver
```

Visit **http://127.0.0.1:8000**

## API-style endpoints

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | List all posts |
| `/uploadContent` | POST | Create post (AJAX) |
| `/editContent/<id>` | POST | Update post (AJAX) |
| `/delPost/<id>` | POST | Delete post (AJAX) |

## Project layout

```
blogsite/
  manage.py
  mainsite/          # models, views, templates, static JS
  blogsite/          # settings, urls, wsgi
```

School learning project — fork and extend as you like.

---

[malimba](https://github.com/malimba)
