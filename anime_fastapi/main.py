# Config imports | 5439 "
import os
import uvicorn
from dotenv import load_dotenv
#Tortoise imports


# FastAPI imports
from fastapi import FastAPI


load_dotenv(f"{os.path.dirname(os.path.abspath(__file__))}/.env")


app = FastAPI()


async def init():
    """
        Инициализцаия базы данных для Tortoise
    """
    await Tortoise.init(
        db_url=os.getenv("DB_URL"),
        modules={"models": ["app.models", "aerich.models"]},
        default_connection = "default"
    )
    await Tortoise.generate_schemas()



def main():
    init()
    uvicorn.run("anime_fastapi.main:app", host=os.getenv("HOST"), port=int(os.getenv("PORT")), reload=True)

if __name__ == "__main__":
    main()