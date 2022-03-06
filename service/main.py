from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn
from models.models import MovieModel
from routes.routes import get_movie

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World", "usage": "Call /api/movie/{title} to get movie data"}


@app.get("/api/movie/{title}", response_model=MovieModel)
async def movie_search(title: str):
    movie = await get_movie(title)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie.dict()


if __name__ == "__main__":
    uvicorn.run(app)
