from fastapi import FastAPI
from app.routes.request import router
from app.routes.issues import router as issues_router


app = FastAPI()

app.include_router(issues_router)
app.include_router(router)