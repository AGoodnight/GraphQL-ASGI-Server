Assuing you installed python3, you need to load some dependencies. PipEnv is a great alternative to manually managing virtual environments for your app.

```bash
pip3 install --user pipx;
python3 -m pipx ensurepath;
pipx install pipenv;
pipenv install;
```

The app uses a schema first approach, not a code first approach.

The app uses a configuration YAML called `app.config.yaml`

The app uses an Ariadne ASGI to create the neccessary resolvers for our queries and mutations on the `/graphql` route/path.

The app uses SQLAlchemy to perform Postgres transactions and returns them in a schema determined by the `graphql/schema.graphql`.

It is recommended to use the playground in a browser on the `/graphql` route of your app instance to test the API.

to create the sample postgres database you can run.

```bash
psql postgres < create-server.sql
```

To use the playground run the app after installing the dependencies with pipenv.

```bash
pipenv install;
pipenv run python server.py;
```
