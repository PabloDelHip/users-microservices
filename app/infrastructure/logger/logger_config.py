import logging
import sys
import structlog
from pythonjsonlogger import jsonlogger

def setup_logger():
    # Configuración del logger estándar
    handler = logging.StreamHandler(sys.stdout)
    formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(message)s')

    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(handler)

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.stdlib.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    return structlog.get_logger("api-gateway")
