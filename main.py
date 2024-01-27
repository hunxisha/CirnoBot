import botpy
import os
import asyncio
import SignIn
import StoreSystem
import TextToPng
import Weather
from botpy.ext.cog_yaml import read
from botpy import logging
from botpy.message import Message

test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))
_log = logging.get_logger()


class ListFeatures(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    async def on_at_message_create(self, message: Message):
        _log.info(message.author.avatar)
        if "/签到" in message.content:
            await asyncio.sleep(1)
            _log.info(message.author.username)

            respond_to_messages = SignIn.sign_in(message.author.id, message.author.username)
            TextToPng.picture_generation(respond_to_messages, address='./img/0001.png')
            with open("./img/0001.png", "rb") as img:
                img_bytes = img.read()
            await message.reply(content=f"<@!{message.author.id}> \n", file_image=img_bytes)

        if "/商店" in message.content:
            await asyncio.sleep(1)
            _log.info(message.author.username)

            txt = StoreSystem.list_shop_items()
            TextToPng.picture_generation(txt, address='./img/0002.png')
            with open("./img/0002.png", "rb") as img:
                img_bytes = img.read()
            await message.reply(content=f"<@!{message.author.id}> \n", file_image=img_bytes)

        if "/购买道具" in message.content:
            await asyncio.sleep(1)
            _log.info(message.author.username)
            try:
                serialNumber = message.content.split(' ')[2]
            except IndexError:
                return 0
            try:
                num = message.content.split(' ')[3]
            except IndexError:
                return 0
            str1 = StoreSystem.purchase_of_goods(message.author.id, serialNumber, num)
            await message.reply(content=f"{str1}")

        if "/我的背包" in message.content:
            await asyncio.sleep(1)
            _log.info(message.author.username)

            txt = StoreSystem.backpack_inquiry(message.author.id)
            TextToPng.picture_generation(txt, address='./img/0003.png')
            with open("./img/0003.png", "rb") as img:
                img_bytes = img.read()
            await message.reply(content=f"<@!{message.author.id}> \n", file_image=img_bytes)

        if "/我的金币" in message.content:
            await asyncio.sleep(1)
            _log.info(message.author.username)
            await message.reply(content=f"{StoreSystem.gold_coin_query(message.author.id)}")

        if "/今日运势" in message.content:
            await asyncio.sleep(1)
            _log.info(message.author.username)
            await message.reply(content=f"开发中...")

        if "/塔罗牌" in message.content:
            await asyncio.sleep(1)
            _log.info(message.author.username)
            await message.reply(content=f"开发中...")

        if "/天气查询" in message.content:
            await asyncio.sleep(1)
            _log.info(message.author.username)

            city_name = message.content.split(' ')[2]
            txt = Weather.weather(city_name)
            TextToPng.picture_generation(txt, address='./img/0004.png', number_of_words_in_line=40)
            with open("./img/0004.png", "rb") as img:
                img_bytes = img.read()
            await message.reply(content=f"<@!{message.author.id}> \n", file_image=img_bytes)

        if "/幻想乡人物生成" in message.content:
            await asyncio.sleep(1)
            _log.info(message.author.username)
            await message.reply(content=f"开发中...")

        if "/对决" in message.content:
            await asyncio.sleep(1)
            _log.info(message.author.username)
            await message.reply(content=f"开发中...")

        if "/好感度查询" in message.content:
            await asyncio.sleep(1)
            _log.info(message.author.username)
            await message.reply(content=f"{SignIn.favorability_inquiry(message.author.id)}")

        if "/帮助" in message.content:
            await asyncio.sleep(1)
            _log.info(message.author.username)
            await message.reply(content=f"帮助文档\n"
                                        f"/帮助       帮助\n"
                                        f"/签到       签到\n"
                                        f"/商店       打开商店\n"
                                        f"/购买道具     /购买道具 道具序号 购买个数\n"
                                        f"/我的背包     查看背包物品\n"
                                        f"/我的金币     查看金币余额\n"
                                        f"/今日运势     开发中\n"
                                        f"/塔罗牌      开发中\n"
                                        f"/天气查询     /天气查询 城市\n"
                                        f"/幻想乡人物生成      开发中\n"
                                        f"/对决       开发中\n"
                                        f"/好感度查询        查看琪露诺对你的好感\n")


if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    # intents = botpy.Intents.none()
    # intents.public_guild_messages=True

    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_guild_messages=True)
    client = ListFeatures(intents=intents)
    client.run(appid=test_config["appid"], secret=test_config["secret"])
