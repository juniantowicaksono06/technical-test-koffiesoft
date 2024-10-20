from fastapi import HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from utils import verify_jwt

class IsAuthenticated(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        path = str(request.url.path)
        if path.startswith("/api"):
            if not path.startswith("/api/auth"):
                print("TES")
                token = request.headers.get("Authorization")
                token = str(token).replace("Bearer ", "")
                verify = verify_jwt(token)
                if verify == 2 or verify == 3:
                    return JSONResponse(status_code=401, content={"message": "Unauthorized"})

        response = await call_next(request)
        return response