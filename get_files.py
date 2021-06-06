import os, sys
import asyncio
import aiohttp  # pip install aiohttp
import aiofiles  # pip install aiofiles

def download_files_from_report(file_name):
    if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    REPORTS_FOLDER = "zips"
    FILES_PATH = os.path.join(REPORTS_FOLDER)
    urls = []
    with open(f'{file_name}.txt', 'r', encoding='utf-8') as links:
        for line in links:
            line = line.strip()
            urls.append(line)

    os.makedirs(FILES_PATH, exist_ok=True)
    sema = asyncio.BoundedSemaphore(5)

    async def fetch_file(url):
        fname = url.split("/")[-1]
        async with sema, aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                assert resp.status == 200
                data = await resp.read()

        async with aiofiles.open(
            os.path.join(FILES_PATH, fname), "wb"
        ) as outfile:
            await outfile.write(data)

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(fetch_file(url)) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()