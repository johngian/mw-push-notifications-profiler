import requests

from locust import HttpUser, task, between

from mw_push_profiler import config


HTTP_HEADERS = {"content-type": "application/json"}


class PushNotifications(HttpUser):
    wait_time = between(5, 9)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """

    @task
    def apnsSendMessage(self):
        url = f"{config.SVC_BASE_URL}/v1/message/apns"
        payload = {
            "messageType": config.MESSAGE_TYPE,
            "deviceTokens": config.APNS["TOKENS"],
            "dryRun": config.APNS["DRY_RUN"],
        }
        self.client.post(
            url, data=payload, headers=HTTP_HEADERS,
        )

    @task
    def fcmSendMessage(self):
        url = f"{config.SVC_BASE_URL}/v1/message/fcm"
        payload = {
            "messageType": config.MESSAGE_TYPE,
            "deviceTokens": config.APNS["FCM_TOKENS"],
            "dryRun": config.FCM["DRY_RUN"],
        }
        headers = {"content-type": "application/json"}
        self.client.post(
            url, data=payload, headers=HTTP_HEADERS,
        )
