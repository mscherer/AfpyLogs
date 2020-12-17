# encoding: utf-8

SECRET_KEY = "Choose a secret key"

JINJA_ENV = {
    "TRIM_BLOCKS": True,
    "LSTRIP_BLOCKS": True,
}

LOG_PATH = "../logs.afpy.org"

# IRSSI log pattern
DATE_FORMAT = "(\d+-\d+-\d+ )?(?P<time>\d\d:\d\d)"
LOG_PATTERN = r"^%s\s+[<*]\s*(?P<nick>[^> ]+)[> ]\s+(?P<message>.*)$" % DATE_FORMAT

# Patterns
LINK_PATTERN = r"https?://\S+"
BOLD_PATTERN = r"\*[^\*\s]+\*"

# html
LINK_HTML = '<a href="{link}">{link}</a>'
BOLD_HTML = "<b>{text}</b>"

