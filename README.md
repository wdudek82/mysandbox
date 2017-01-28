# MySandbox Project


## Built with:
- Python 3.6
- Django 1.10.5
    - Django Debug Toolbar

## Other tools:
- virtualenv
- virtualenvwrapper
- autoenv

## Relational DB:
- SQLite (in development)
- PostgreSQL (in production)


## Production Environment:
- VPS hosted by Digital Ocean
- Fedora 25
- Nginx

#### TODO:
- User profiles
- Translations (PL/EN)
- create API
- ...

#### Additional
- for some reason colorfield is searching for jscolor in media, so after collectstatic it's folder must be copied
 from static to media root,