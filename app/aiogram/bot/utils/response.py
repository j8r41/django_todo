import asyncio

import aiohttp

# from aiohttp import BasicAuth


async def is_response_ok(telegram_key: str):
    url = f"http://django:8000/api/v1/task/{telegram_key}/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            status_code = response.status
            return status_code


async def get_tasks_with_auth(telegram_key: str):
    url = f"http://django:8000/api/v1/task/{telegram_key}/"
    # auth = BasicAuth(login=username, password=password)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_data = await response.json()
            return response_data


async def main():
    result = await is_response_ok("1922b46b042a9816c3bc")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
