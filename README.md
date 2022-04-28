# Django whitelabel

## Features

[X] Separated settings for different environments
[X] Docker
[X] Different docker-compose for different environments
[ ] CI/CD

## Environments

- Local dev: to develop on your PC without Docker. Use `manage.py` as always.
- Docker dev: to develop on yout PC using a more production-like environment with a MySQL database. Autoreload is enabled and every change in the `app` folder is applied to `/app` in the container and vice versa. Requirements are installed at build time and migrations are applied at boot but you can do that manually.
- Staging: like production but with admin and debug enabled for testing purposes.
- Production: the deployed version.

### How to use Docker dev

1. create a file named `.env` containing the required environment variables (read the next section)
2. run `docker-compose up --build`
3. work with your local files
4. execute commands inside the container. ex `docker exec -it django-whitelabel-app_1 python manage.py makemigrations`

### Features table

|                                    | Local Dev | Docker Dev | Staging |                 Production                 |
| ---------------------------------- | :-------: | :--------: | :-----: | :----------------------------------------: |
| Auto-reload                        |    ✅     |     ✅     |   ❌    |                     ❌                     |
| Auto migrate at start              |    ✅     |     ✅     |   ✅    |                     ✅                     |
| Auto requirements install at start |    ✅     |     ✅     |   ✅    |                     ✅                     |
| Database                           |  SQLite   |  MariaDB   | MariaDB |                  MariaDB                   |
| Reverse proxy (Nginx)              |    ❌     |     ❌     |   ✅    |                     ✅                     |
| Debug                              |    ✅     |     ✅     |   ✅    |                     ❌                     |
| Admin page                         |    ✅     |     ✅     |   ✅    | ❌ (can be enabled in settings/production) |
| Serving media automatically        |    ✅     |     ✅     |   ❌    |                     ❌                     |
| CORS allow all                     |    ✅     |     ✅     |   ❌    |                     ❌                     |
| Allow all hosts                    |    ✅     |     ✅     |   ❌    |                     ❌                     |

## Configuration

### Required environment variables

- ✅ Required
- ❌ Not required
- ⚠️ Optional

|                                     | Local Dev | Docker Dev | Staging | Production |
| ----------------------------------- | :-------: | :--------: | :-----: | :--------: |
| MYSQL_PASSWORD                      |    ✅     |     ✅     |   ✅    |     ✅     |
| SECRET_KEY (default string for dev) |    ⚠️     |     ⚠️     |   ✅    |     ✅     |
| ALLOWED_HOSTS (all for dev)         |    ❌     |     ❌     |   ✅    |     ✅     |
| CORS_ALLOWED_ORIGINS (all for dev)  |    ❌     |     ❌     |   ✅    |     ✅     |
| EMAIL_HOST                          |    ⚠️     |     ⚠️     |   ⚠️    |     ⚠️     |
| EMAIL_HOST_PASSWORD                 |    ⚠️     |     ⚠️     |   ⚠️    |     ⚠️     |
| EMAIL_HOST_USER                     |    ⚠️     |     ⚠️     |   ⚠️    |     ⚠️     |
| EMAIL_PORT (default EMAIL_PORT)     |    ⚠️     |     ⚠️     |   ⚠️    |     ⚠️     |

### Example .env

```
MYSQL_PASSWORD=somerandomstring
SECRET_KEY=anotherrandomstring
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_PASSWORD=gmailpassword
EMAIL_HOST_USER=yourmail@gmail.com
EMAIL_PORT=587
ALLOWED_HOSTS=localhost,127.0.0.1,api.something.it
CORS_ALLOWED_ORIGINS=https://frontend.com,https://sub.frontend.com
```
