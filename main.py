from fastapi import FastAPI # type: ignore
from sckrebt import check_security  # استيراد الوظيفة من ملفك اللي سويناه

app = FastAPI()

@app.get("/scan")
def scan_site(url: str):
    return check_security(url)
from fastapi import FastAPI # type: ignore
from fastapi.responses import FileResponse # type: ignore
from sckrebt import check_security

app = FastAPI()

# لفتح الصفحة الرئيسية
@app.get("/")
def read_root():
    return FileResponse("index.html")

# لعملية الفحص
@app.get("/scan")
def scan_site(url: str):
    return check_security(url)