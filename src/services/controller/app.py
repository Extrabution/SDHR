from fastapi import FastAPI, Query
from datetime import datetime
import redis.asyncio as redis
from typing import Annotated
from concat_timestamp import concat_timestamp
from history_dto import History
from message_dto import Message

redis_app = redis.Redis(host="red01", port=6379)

app = FastAPI()


@app.post("/api/sens-messages/")
async def messages(message: Message) -> Message:
    await redis_app.publish('messages', str(message.dict()))
    return message


@app.get("/api/control-history/")
async def control_history(q: Annotated[str,
                                       Query(min_length=40, max_length=40,
                                             pattern=r'^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})D'
                                                     r'(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})$')]) \
        -> list[History]:

    start, end = q.split("D")
    start = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
    end = datetime.strptime(end, "%Y-%m-%dT%H:%M:%S")
    keys = await redis_app.keys("*")
    keys.sort()
    signals_history = []
    for elem in keys:
        try:
            if start.timestamp() <= float(elem.decode()) <= end.timestamp():
                signals_history.append({"timestamp": float(elem.decode()), "status": await redis_app.get(elem)})
            if float(elem.decode()) > end.timestamp():
                break
        except:
            pass
    return await concat_timestamp(signals_history)


@app.get("/")
async def index():
    return "Hello!"
