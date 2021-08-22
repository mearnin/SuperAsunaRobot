<h1 align="center"> 
   ❤️AsunaRobot❤️ 
</h1>

<h3 align="center"> 
    Telegram Group Manager Bot Written In Python Using Pyrogram.
</h3>

<p align="center">
    <a href="https://python.org"> <img src="http://forthebadge.com/images/badges/made-with-python.svg" alt="made-with-python"></a>
    <a href="https://GitHub.com/TheHamkerCat"> <img src="http://ForTheBadge.com/images/badges/built-with-love.svg" alt="built-with-love"></a>
</p>



<p align="center">
    <img src="https://img.shields.io/badge/python-3.9-green?style=for-the-badge&logo=appveyor" alt="Python Version">
    <img src="https://img.shields.io/github/issues/mearnin/SuperAsunaRoBot?style=for-the-badge&logo=appveyor" alt="Issues">
    <img src="https://img.shields.io/github/forks/mearnin/SuperAsunaRoBot?style=for-the-badge&logo=appveyor" alt="Forks">
    <img src="https://img.shields.io/github/stars/mearnin/SuperAsunaRoBot?style=for-the-badge&logo=appveyor" alt="Stars">
</p>

<h3 align="center"> 
    Ready to use method
</h3>

<p align="center">
    A Support Group and ready-to-use running instance of this bot can be found on Telegram <br>
    <a href="https://t.me/SuperAsunaRoBot"> SuperAsunaRoBot </a> | 
    <a href="https://t.me/superasunarobotsupport"> WbbSupport </a>
</p>

<h2 align="center"> 
   ⇝ Requirements ⇜
</h2>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-390/"> Python3.9 </a> |
    <a href="https://docs.pyrogram.org/intro/setup#api-keys"> Telegram API Key </a> |
    <a href="https://t.me/botfather"> Telegram Bot Token </a> | 
    <a href="https://telegra.ph/How-To-get-Mongodb-URI-04-06"> MongoDB URI </a>
</p>

<h2 align="center"> 
   ⇝ Install Locally Or On A VPS ⇜
</h2>

```console
$ git clone https://github.com/mearnin/SuperAsunaRoBot
$ cd WilliamButcherBot
$ pip3 install -U -r requirements.txt
$ cp sample_config.py config.py
```
 
<h3 align="center"> 
    Edit <b>config.py</b> with your own values
</h3>

<h2 align="center"> 
   ⇝ Run Directly ⇜
</h2>

```console
$ python3 -m wbb
```

<h1 align="center"> 
   ⇝ Run On Heroku ⇜
</h1>

<h3 align="center"> 
   Generating Pyrogram Session For Heroku
</h3>

```console
$ git clone https://github.com/mearnin/SuperAsunaRoBot
$ cd SuperAsunaRoBot
$ pip3 install pyrogram TgCrypto
$ python3 str_gen.py
```

<p align="center">
    <a href="https://heroku.com/deploy?template=https://github.com/mearnin/SuperAsunaRoBot"> <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy"></a>
    <a href="https://railway.app/new/template?template=https://github.com/mearnin/SuperAsunaRoBot/tree/dev&envs=API_HASH,API_ID,ARQ_API_KEY,ARQ_API_URL,BOT_TOKEN,FERNET_ENCRYPTION_KEY,GBAN_LOG_GROUP_ID,LOG_GROUP_ID,LOG_MENTIONS,MESSAGE_DUMP_CHAT,MONGO_DB_URI,PM_PERMIT,RSS_DELAY,SESSION_STRING,SUDO_USERS_ID,USERBOT_PREFIX,WELCOME_DELAY_KICK_SEC"> <img src="https://railway.app/button.svg" alt="Deploy"></a>
</p>



<h3 align="center"> 
    Edit <b> config.env </b> with your own values
</h3>

```console
$ sudo docker build . -t wbb
$ sudo docker run wbb
```

<h2 align="center"> 
   ⇝ Write new modules ⇜
</h2>

```py
# Add license text here, get it from below

from wbb import app # This is bot's client
from wbb import app2 # userbot client, import it if module is related to userbot
from pyrogram import filters # pyrogram filters
...


# For /help menu
__MODULE__ = "Module Name"
__HELP__ = "Module help message"


@app.on_message(filters.command("start"))
async def some_function(_, message):
    await message.reply_text("I'm already up!!")

# Many useful functions are in, wbb/utils/, wbb, and wbb/core/
```

<h3 align="center"> 
   And put that file in wbb/modules/, restart and test your bot.
</h3>

<h2 align="center">
Special Credits ❤️
</h2>
<p>
💡 <a href="https://github.com/thehamkercat> The Hamcker Cat </a>
💡 <a href="https://github.com/DevsExpo> Friday Userbot </a>
</p>


