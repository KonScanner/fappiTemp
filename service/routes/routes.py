import httpx
from typing import Optional
from models.models import MovieModel


async def get_movie(title_subtext: str) -> Optional[MovieModel]:
    url = f"https://movieservice.talkpython.fm/api/search/{title_subtext}"

    async with httpx.AsyncClient() as client:
        resp: httpx.Response = await client.get(url)
        resp.raise_for_status()
        data = resp.json()

    results = data["hits"]
    if not results:
        return None
    return MovieModel(**results[0])
