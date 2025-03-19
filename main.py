from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

app = FastAPI()

# Cấu hình thư mục template
templates = Jinja2Templates(directory="templates")

# Mount thư mục static (nếu cần thêm CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Danh sách các string được định nghĩa trước
string_list = ["Hello", "FastAPI", "Python", "Web App", "Interactive"]

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "strings": string_list})

@app.get("/interact/{string}")
def interact_string(string: str):
    return JSONResponse(content={"message": f"Bạn đã tương tác với: {string}"})
