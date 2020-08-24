"""Locust load testing suite for push notification service"""

import logging
import requests

from locust import HttpUser, task, between

from mw_push_profiler import config


class PushNotifications(HttpUser):
    """Load test push notifactions service"""

    wait_time = between(5, 9)
    host = config.SVC_BASE_URL

    def on_start(self):
        """Prepare resiliency testing setup"""
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

    def on_stop(self):
        """Cleanup resiliency testing setup """
        if config.TOXIPROXY_ENABLED:
            for proxy in config.TOXIPROXY["PROXIES"]:
                logging.info("Deleting toxiproxy: %s", proxy)
                requests.delete(f"{config.TOXIPROXY['API_URL']}/proxies", json=proxy)

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
