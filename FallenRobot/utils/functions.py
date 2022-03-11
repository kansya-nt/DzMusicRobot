from asyncio import gather<br/>from io import BytesIO<div></div>from FallenRobot import aiohttpsession as aiosession<div></div><br/>async def make_carbon(code):<br/>    url = "https://carbonara.vercel.app/api/cook"<br/>    async with aiosession.post(url, json={"code": code}) as resp:<br/>        image = BytesIO(await resp.read())<br/>    image.name = "carbon.png"<br/>    return image<br/>