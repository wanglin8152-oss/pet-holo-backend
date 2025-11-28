# main.py
# 这是你完整可运行的后端 FastAPI 程序

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI(title="Pet Holo Backend", version="0.1.0")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/")
async def root():
    return {"message": "Pet Holo backend is running"}


@app.post("/generate")
async def generate_stub(file: UploadFile = File(...)):
    """
    生成全息投影图（Stub）
    当前为示例：仅返回文件信息
    """
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")

    return JSONResponse(
        {
            "status": "received",
            "filename": file.filename,
            "content_type": file.content_type,
            "note": "Backend working. TODO: implement real generation logic."
        }
    )
