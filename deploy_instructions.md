# Deploy (Render) — Supabase + Cloudinary (free options)

This file documents steps to deploy the project to Render using Supabase (Postgres) for database and Cloudinary for media. Both have free tiers suitable for hobby projects.

1) Create accounts
- Supabase: create a project and get the `DATABASE_URL` (Postgres) connection string.
- Cloudinary: create account and get `CLOUDINARY_URL` (format: `cloudinary://API_KEY:API_SECRET@CLOUD_NAME`).

2) Update repository (already present)
- `requirements.txt` includes `dj-database-url`, `psycopg2-binary`, `django-cloudinary-storage` and `cloudinary`.
- `smartlibrary/settings.py` reads `DATABASE_URL` via `dj_database_url` and is configured to use Cloudinary as `DEFAULT_FILE_STORAGE`.

3) Set environment variables on Render
- `DATABASE_URL` = Supabase Postgres URL
- `CLOUDINARY_URL` = Cloudinary URL
- `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET` (optional if `CLOUDINARY_URL` set)
- `SECRET_KEY` (Django secret)
- `DEBUG` = `False`
- `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD` (optional — `createsu` command will create user on deploy)

4) Push and deploy
- git push origin main — Render will build

5) After deploy (run these in Render shell or via deploy hooks)
- Run migrations:
```
python manage.py migrate
```
- Create superuser (if not using `createsu` env vars):
```
python manage.py createsuperuser
```
- Upload local media to Cloudinary (on Render or locally pointed to remote DB):
```
python manage.py uploadmedia
```
The `uploadmedia` management command will iterate `Livro` objects and re-save local files into the configured `DEFAULT_FILE_STORAGE` (Cloudinary) so `imagem` fields point to Cloudinary-hosted images.

6) Verify
- Open the public site and confirm images are served from `res.cloudinary.com` (Cloudinary CDN) or the `CLOUDINARY` domain.

Notes
- If you prefer not to use Cloudinary, Render's Persistent Disks can be used, but ensure you configure the disk and point `MEDIA_ROOT` to it.
- For small hobby projects, Cloudinary free plan and Supabase generous free tier are usually enough.
