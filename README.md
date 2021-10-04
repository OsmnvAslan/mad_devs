# Mad Devs test task


# Usage

create .env 
```shell
docker-compose up
```


# ENV

|env variable|Default|
|---|---|
|DEBUG|True|
|DATABASE_URL|psql://user:pass@postgres:5432/db|
|SECRET_KEY|SECRET|
|DB_HOST|postgres|
|DB_PORT|5432|
|TIME_ZONE|Asia/Almaty|
|WHERE_TO_KEEP_MEDIA|LOCAL|
|SENTRY_DSN||
|SILKY_INTERCEPT_PERCENT|100|


## Testing:

```shell
$ docker-compose exec django bash
$ $test
```

## Docs:

http://0.0.0.0:8000/docs/