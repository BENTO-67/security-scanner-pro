import fastapi # pyright: ignore[reportMissingImports]
import fastapi.middleware.cors # type: ignore
import fastapi.responses # pyright: ignore[reportMissingImports]
import sckrebt

app = fastapi.FastAPI()

app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return fastapi.responses.FileResponse("index.html")

@app.get("/scan")
def scan_site(url: str):
    return sckrebt.check_security(url)