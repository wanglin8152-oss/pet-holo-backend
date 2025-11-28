# main.py
# 简化版后台：先保证 Render 上能正常启动

import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI(title="Pet Holo Backend", version="0.1.0")


@app.get("/health")
async def health():
    """给 Render / 前端用的健康检查接口"""
    return {"status": "ok"}


@app.get("/")
async def root():
    return {"message": "Pet Holo backend is running"}


@app.post("/generate")
async def generate_stub(file: UploadFile = File(...)):
    """
    先占个位的生成接口：
    目前不真正做 remove.bg 和视频合成，只返回文件信息，
    目的是让接口结构先跑通。
    """
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")

    return JSONResponse(
        {
            "status": "received",
            "filename": file.filename,
            "content_type": file.content_type,
            "note": "Backend is deployed correctly. TODO: implement real generation logic.",
        }
    )
