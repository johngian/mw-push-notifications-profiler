"""Locust load testing suite for push notification service"""

import logging
import requests

from locust import HttpUser, task, between, events

import config


@events.init.add_listener
def on_locust_init(*args, **kwargs):
    """Configure toxiproxy on load testing suite init"""
    if config.TOXIPROXY_ENABLED:
        for proxy in config.TOXIPROXY["PROXIES"]:
            logging.info("Creating toxiproxy: %s", proxy)
            requests.post(f"{config.TOXIPROXY['API_URL']}/proxies", json=proxy)

            for toxic in config.TOXIPROXY["TOXICS"]:
                logging.info("Creating toxic: %s", toxic)
                requests.post(
                    f"{config.TOXIPROXY['API_URL']}/proxies/{proxy['name']}/toxics",
                    json=toxic,
                )


@events.quitting.add_listener
def on_locust_quit(*args, **kwargs):
    """Cleanup toxiproxy config when locust quits"""
    if config.TOXIPROXY_ENABLED:
        for proxy in config.TOXIPROXY["PROXIES"]:
            logging.info("Deleting toxiproxy: %s", proxy)
            requests.delete(f"{config.TOXIPROXY['API_URL']}/proxies", json=proxy)


class PushNotifications(HttpUser):
    """Load test push notifications service"""

    wait_time = between(5, 9)
    host = config.SVC_BASE_URL

    @task
    def apns_send_message(self):
        """Send an APNS message"""
        url = "/v1/message/apns"
        payload = {
            "messageType": config.MESSAGE_TYPE,
            "deviceTokens": config.APNS["TOKENS"],
            "dryRun": config.APNS["DRY_RUN"],
        }
        self.client.post(url, json=payload)

    @task
    def fcm_send_message(self):
        """Send FCM message"""
        url = "/v1/message/fcm"
        payload = {
            "messageType": config.MESSAGE_TYPE,
            "deviceTokens": config.FCM["TOKENS"],
            "dryRun": config.FCM["DRY_RUN"],
        }
        self.client.post(url, json=payload)

    @task
    def apns_send_bogus_tokens(self):
        """Send an APNS message with bogus tokens"""
        url = "/v1/message/apns"
        payload = {
            "messageType": config.MESSAGE_TYPE,
            "deviceTokens": [
                f"apnstoken{i}" for i in range(config.BOGUS_TOKENS_MAX_SIZE)
            ],
            "dryRun": config.APNS["DRY_RUN"],
        }
        self.client.post(url, json=payload)

    @task
    def fcm_send_bogus_tokens(self):
        """Send FCM message with bogus tokens"""
        url = "/v1/message/fcm"
        payload = {
            "messageType": config.MESSAGE_TYPE,
            "deviceTokens": [
                f"fcmtoken{i}" for i in range(config.BOGUS_TOKENS_MAX_SIZE)
            ],
            "dryRun": config.FCM["DRY_RUN"],
        }
        self.client.post(url, json=payload)
