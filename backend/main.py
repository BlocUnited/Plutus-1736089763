from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config.config import Config
from backend.middleware.middleware import Middleware
from backend.routes.route import api_router

# Load configuration
config = Config()

# Initialize FastAPI application
app = FastAPI(title='Social Platform API')

# Configure middleware
middleware = Middleware(app)

# Include CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Adjust as necessary
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Register API routes
app.include_router(api_router)

# Health check endpoint
@app.get('/health', tags=['health'])
async def health_check():
    return {'status': 'healthy'}

# Start the application
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)
