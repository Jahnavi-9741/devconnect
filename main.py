from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Database setup
DATABASE_URL = "sqlite:///./social.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    content = Column(Text)

Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    db = SessionLocal()
    posts = db.query(Post).all()
    return templates.TemplateResponse("index.html", {"request": request, "posts": posts})

@app.get("/new", response_class=HTMLResponse)
def new_post_form(request: Request):
    return templates.TemplateResponse("new_post.html", {"request": request})

@app.post("/post")
def create_post(username: str = Form(...), content: str = Form(...)):
    db = SessionLocal()
    new_post = Post(username=username, content=content)
    db.add(new_post)
    db.commit()
    return RedirectResponse(url="/", status_code=303)
