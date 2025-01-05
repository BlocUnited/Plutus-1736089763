from fastapi import Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Middleware:
    def __init__(self, app):
        self.app = app
        self.setup_cors()
        self.app.middleware('http')(self.auth_middleware)

    def setup_cors(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],  # Adjust as necessary
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )

    async def auth_middleware(self, request: Request, call_next):
        token = request.headers.get('Authorization')
        if not token:
            raise HTTPException(status_code=401, detail='Authorization token is missing')
        # Here you would add your token validation logic
        logger.info('Authorization token provided')
        response = await call_next(request)
        return response

    @staticmethod
    async def error_handling_middleware(request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            logger.error(f'Error occurred: {str(e)}')
            return JSONResponse(status_code=500, content={'detail': 'Internal Server Error'})
