from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.infrastructure.middlewares.logger_middleware import LoggerMiddleware
# from app.api.routes.user_route import router as user_router 
# from app.api.routes.agent_route import router as agent_router
from app.infrastructure.routers.users_router import router as user_router

app = FastAPI()

app.add_middleware(LoggerMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O los orígenes que necesites
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(user_router, prefix="/user", tags=["Agents"])

@app.get("/")
def health_check():
    return {"status": "API Gateway is running"}
