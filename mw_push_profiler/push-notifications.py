import logging
import requests

from locust import HttpUser, task, between

from mw_push_profiler import config


class PushNotifications(HttpUser):
    wait_time = between(5, 9)
    host = config.SVC_BASE_URL

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        if config.TOXIPROXY_ENABLED:
            for proxy in config.TOXIPROXY["PROXIES"]:
                logging.info(f"Creating toxiproxy: {proxy}")
                requests.post(f"{config.TOXIPROXY_BASE_URL}/proxies", json=proxy)

                for toxic in config.TOXIPROXY["TOXICS"]:
                    logging.info(f"Creating toxic: {toxic}")
                    requests.post(
                        f"{config.TOXIPROXY_BASE_URL}/proxies/{proxy['name']}/toxics",
                        json=toxic,
                    )

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        if config.TOXIPROXY_ENABLED:
            for proxy in config.TOXIPROXY.PROXIES:
                logging.info(f"Deleting toxiproxy: {proxy}")
                requests.delete(f"{config.TOXIPROXY_BASE_URL}/proxies", json=proxy)

    @task
    def apnsSendMessage(self):
        url = "/v1/message/apns"
        payload = {
            "messageType": config.MESSAGE_TYPE,
            "deviceTokens": config.APNS["TOKENS"],
            "dryRun": config.APNS["DRY_RUN"],
        }
        self.client.post(url, json=payload)

    @task
    def fcmSendMessage(self):
        url = "/v1/message/fcm"
        payload = {
            "messageType": config.MESSAGE_TYPE,
            "deviceTokens": config.FCM["TOKENS"],
            "dryRun": config.FCM["DRY_RUN"],
        }
        self.client.post(url, json=payload)
