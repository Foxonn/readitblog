import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.celery import CeleryIntegration

sentry_sdk.init(
    dsn="https://8f61c97803754d458bf5788ffe154e6a@o393650.ingest.sentry.io/5243018",
    integrations=[DjangoIntegration(), CeleryIntegration(),],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
