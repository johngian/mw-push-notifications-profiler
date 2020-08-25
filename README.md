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

## Toxics

Toxiproxy uses toxics to manipulate the traffic in the network. Under [examples/toxics.json](/examples/toxics.json)
you can find a list of all the available toxics that we can use for resiliency testing.

A useful helper to convert the json to one line to be used in the config is:

``` sh
$ cat examples/toxics.json | jq -c
```

## Running the tests

``` sh
# Using an env file
$ docker run --env-file FILE mw-push-notifications-profiler:latest

# Using env vars
$ docker run -e VAR=VALUE mw-push-notifications-profiler:latest
```
