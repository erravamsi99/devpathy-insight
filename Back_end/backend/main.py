from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from devpathy import generate_report

# Define input schema for API
class ReviewRequest(BaseModel):
    code_snippet: str
    review_comments: list[str]
    style: str = "friendly"  # friendly, neutral, direct
    links: bool = True

app = FastAPI(title="Devpathy API")

# Allow frontend calls (adjust origin to your frontend URL if deployed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev; tighten for prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
def generate(request: ReviewRequest):
    markdown = generate_report(
        code_snippet=request.code_snippet,
        review_comments=request.review_comments,
        base_style=request.style,
        include_links=request.links,
    )
    return {"report": markdown}
