import time
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.infrastructure.logger.logger_config import setup_logger

logger = setup_logger()

class LoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        start_time = time.time()

        logger.info(
            "Request received",
            method=request.method,
            path=request.url.path,
            client_ip=request.client.host,
            request_id=request_id,
        )

        try:
            response = await call_next(request)
            duration = time.time() - start_time

            logger.info(
                "Request completed",
                method=request.method,
                path=request.url.path,
                status_code=response.status_code,
                duration=f"{duration:.4f}s",
                request_id=request_id,
            )

            return response

        except Exception as e:
            logger.error(
                "Unhandled error",
                method=request.method,
                path=request.url.path,
                error=str(e),
                request_id=request_id,
            )
            raise e
