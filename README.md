# Client Metric Tracker

Backend service for collecting and service client metrics.

## Local setup/development

Requires postgres, dbmate and vercel.

- `dbmate up` to create database and run migrations locally.
- `vercel dev` to run app locally.

Local dev currently relies on having a vercel project but you could
also just run the flask app locally if you wanted. I'm not doing that here
since I didn't want multiple ways to run it locally and I'm fine
with having a vercel project.

## Production

Python code deployed on vercel and database is provisioned by Supabase.

Run the following with actual config values to execute migrations in production.
```
# See migration status
DATABASE_URL="postgres://USER:PASSWORD@HOST:PORT/DATABASE?sslmode=disable" dbmate status
# Run migration
DATABASE_URL="postgres://USER:PASSWORD@HOST:PORT/DATABASE?sslmode=disable" dbmate up
```

## Release
Project is configured to release on push.
```
git push origin main

```
