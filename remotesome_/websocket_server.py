import asyncio
import datetime
import websockets


async def handler(websocket, path):
    # data = await websocket.recv()
    while True:
        # dt_now = str(datetime.datetime.now())
        dt_now = datetime.datetime.now()
        str_date = dt_now.isoformat()
        await asyncio.sleep(5)
        await websocket.send(str_date)


start_server = websockets.serve(handler, "localhost", 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
