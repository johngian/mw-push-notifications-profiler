# MW push notifications service profiles
## Install

``` sh
$ docker build . -t mw-push-profiler:latest
$ docker run mw-push-profiler:latest
```

## Configuration

Configuration is handled using environment variables or a dot-env file.
Parameters:

| Key                                | Value                                     | Default         | Required |
|:-----------------------------------|:------------------------------------------|:----------------|----------|
| SVC_BASE_URL                       | Push notification service base url        | None            | True     |
| MW_SVC_PROF_APNS_TOKENS            | Comma seperated list of APNS tokens       | "APNSTESTTOKEN" | False    |
| MW_SVC_PROF_APNS_DRYRUN            | APNS dry run flag                         | True            | False    |
| MW_SVC_PROF_FCM_TOKENS             | Comma seperated list of APNS tokens       | "FCMTESTTOKEN"  | False    |
| MW_SVC_PROF_FCM_DRYRUN             | FCM dry run flag                          | True            | False    |
| MW_SVC_PROF_PUSH_TOXIPROXY_URL     | Toxiproxy API URL                         | ""              | False    |
| MW_SVC_PROF_PUSH_TOXIPROXY_PROXIES | List of toxiproxy proxies required (JSON) | []              | False    |
| MW_SVC_PROF_PUSH_TOXIPROXY_TOXICS  | List of toxics required (JSON)            | []              | False    |
