from fastapi import FastAPI
import sqlite3
import random

DB_PATH = "dad_jokes_1000.db"

app = FastAPI()

def get_all_jokes():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT joke_text FROM jokes")
    jokes = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jokes

@app.get("/")
async def root():
    return {"message": "Welcome to the Dad joke API! Add /getjoke to get a random joke or /jokes to get all jokes."}

@app.get("/getjoke")
async def get_random_joke():
    jokes = get_all_jokes()
    if jokes:
        joke = random.choice(jokes)
        return {"joke": joke}
    else:
        return {"joke": "No jokes found in the database."}

@app.get("/jokes")
async def read_jokes():
    jokes = get_all_jokes()
    return {"jokes": jokes}
