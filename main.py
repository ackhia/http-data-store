
from fastapi import FastAPI, Request, Response

app = FastAPI()

data = {}

@app.api_route("/{path_name:path}", methods=["GET"])
async def catch_all(request: Request, path_name: str):
    print(data)
    return Response(content = data[path_name])

@app.api_route("/{path_name:path}", methods=["POST"])
async def catch_all(request: Request, path_name: str):
    data[path_name] = await request.body()
    return "ok"