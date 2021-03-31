from .common import *

DEBUG = os.environ.get("DEBUG") in ["1", "t", "true", "T", "True"]

CORS_ORIGIN_WHITELIST = os.environ.get("CORS_ORIGIN_WHITELIST", "").split(",")

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
      'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
  },
  'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'logstash': {
            'level': 'WARNING',
            'class': 'logstash.TCPLogstashHandler',
            'host': '54.180.183.17',
            'port': 5959, # Default value: 5959
            'version': 1, # Version of logstash event schema. Default value: 0 (for backward compatibility of the library)
            'message_type': 'django',  # 'type' field in logstash message. Default value: 'logstash'.
            'fqdn': False, # Fully qualified domain name. Default value: false.
            'tags': ['django.request'], # list of tags. Default: None.
        },
  },
  'loggers': {
        'django.request': {
            'handlers': ['logstash'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
    }
}

ALLOWED_HOSTS += ['54.180.183.17']