import json
import aiofiles


async def read_json_file(file_path: str):
    async with aiofiles.open(file_path, "r") as file:
        data = await file.read()
        return json.loads(data)
