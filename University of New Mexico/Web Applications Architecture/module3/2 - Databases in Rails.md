# Database in Rails

How Rails interact with the applications and how he connects to the database.

## Database Migrations
- When we ran the scaffold generator, Rails created a **database migrations**
  file and placed it in the `db/migrate` folder.
- Rails uses the rake command <code>$ rake db:migrate</code> to run there
  migrations.
- Migrations can also be used to undo the work of previous migrations.

## Rails Environments
Rails automatically sets up applications to run in one of three prebuilt
environments.

1. Development
2. Test
3. Production

By default, when we run <code>$ rails server</code> rails runs in the development
environment.
To force rails to run in a different environment, use <code> $ rails server -e
-production</code> for example.

## Production Mode
- In the production mode, if we make a change in the source code, will
not reflect to the running application immediately.
- Rails optimizes the delivery of assets.

## Development and Production Databases

- The developer are the only one accessing the database.
- Automatically sets up to use **SQLite**,a simple easy-to-use file-based that
  runs in memory and is **not** a production grade database.
- The databases for different environments are specified in `db/database.yml` file.
- Popular production databases are **PostgreSQL** and **MySQL**.
