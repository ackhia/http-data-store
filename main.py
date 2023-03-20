
from fastapi import FastAPI, Request, Response

app = FastAPI()

data = {}

@app.api_route("/{path_name:path}", methods=["GET"])
async def catch_all(request: Request, path_name: str):
    if path_name in data:
        return Response(content = data[path_name])
    else:
        return Response(status_code=404)

@app.api_route("/{path_name:path}", methods=["POST"])
async def catch_all(request: Request, path_name: str):
    data[path_name] = await request.body()
    return "ok"