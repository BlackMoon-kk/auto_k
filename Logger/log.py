import logging.config
config = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
        # 其他的 formatter
        'stander': {
            'format':'[%(levelname)s][%(asctime)s] [%(filename)s]->[%(funcName)s] line:%(lineno)d ---> %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'stander'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logging.log',
            'level': 'DEBUG',
            'formatter': 'simple',
            'delay':True
        },
        # 其他的 handler
    },
    'loggers':{
        'StreamLogger': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'FileLogger': {
            # 既有 console Handler，还有 file Handler
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        # 其他的 Logger
    }
}

logging.config.dictConfig(config)
# StreamLogger = logging.getLogger("StreamLogger")
# FileLogger = logging.getLogger("FileLogger")
#
# logger = logging.getLogger('StreamLogger')
# logger.info("test")
# logger.warning("warning")