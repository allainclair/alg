import asyncio


async def dead_while_loop():
    while True:
        i = 1
        # print('Sleeping fast')
        # await asyncio.sleep(0.5)


async def sleep_while_loop():
    while True:
        print('Sleeping...')
        await asyncio.sleep(1)


async def main():
    deadend = asyncio.create_task(dead_while_loop())
    print('Starting sleeping while')
    await sleep_while_loop()


if __name__ == '__main__':
    asyncio.run(main())
