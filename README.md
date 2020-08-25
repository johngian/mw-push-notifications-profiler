# MW push notifications service profiler
## Install

``` sh
$ docker build . -t mw-push-notifications-profiler:latest
```

## Configuration

Configuration is handled using environment variables or a dot-env file.
Parameters:

| Key                                  | Value                                     | Default           | Required |
|:-------------------------------------|:------------------------------------------|:------------------|----------|
| `MW_SVC_PROF_PUSH_BASE_URL`          | Push notification service base url        | `None`            | `True`   |
| `MW_SVC_PROF_APNS_TOKENS`            | Comma seperated list of APNS tokens       | `"APNSTESTTOKEN"` | `False`  |
| `MW_SVC_PROF_APNS_DRYRUN`            | APNS dry run flag                         | `True`            | `False`  |
| `MW_SVC_PROF_FCM_TOKENS`             | Comma seperated list of FCM tokens        | `"FCMTESTTOKEN"`  | `False`  |
| `MW_SVC_PROF_FCM_DRYRUN`             | FCM dry run flag                          | `True`            | `False`  |
| `MW_SVC_PROF_PUSH_TOXIPROXY_URL`     | Toxiproxy API URL                         | `""`              | `False`  |
| `MW_SVC_PROF_PUSH_TOXIPROXY_PROXIES` | List of toxiproxy proxies required (JSON) | `[]`              | `False`  |
| `MW_SVC_PROF_PUSH_TOXIPROXY_TOXICS`  | List of toxics required (JSON)            | `[]`              | `False`  |

## Running the tests

``` sh
# Using an env file
$ docker run --env-file FILE mw-push-notifications-profiler:latest

# Using env vars
$ docker run -e VAR=VALUE mw-push-notifications-profiler:latest
```
