#run: python3 main.py
# sentry-cli monitors run 63261d96-2027-472a-a8bb-9895dbebd793 -- python ./main.py

from distutils.log import debug
import sentry_sdk

def before_send(event, hint):
    # print("this is event", event)
    # # print("this is hint", hint)
    if 'exc_info' in hint:
        exc_type, exc_value, tb = hint['exc_info']
        if isinstance(exc_value, NameError):
            print("before return none")
            return None
    return event
    

sentry_sdk.init(
    dsn="https://55bf09aa2ba94a0f976413998ffe8581@o1145026.ingest.sentry.io/4504889400033280",
    traces_sample_rate=1.0,

    debug=True,
    before_send=before_send,
    # ignore_errors=[],
)

# raise KeyError("invalid key")

division_by_zero = 1 / 0

# raise NameError("context test")