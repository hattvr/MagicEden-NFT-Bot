<h1 align="center">MagicEden NFT Bot</h1>
<p align="center">
    <a href="https://github.com/hattvr/MagicEden-NFT-Bot/releases/latest">
        <img src="https://img.shields.io/github/v/release/hattvr/MagicEden-NFT-Bot?label=Latest%20Version">
    </a>
    <a href="https://github.com/hattvr/MagicEden-NFT-Bot/commit/master">
        <img src="https://img.shields.io/github/last-commit/hattvr/MagicEden-NFT-Bot?label=Last%20Update">
    </a>
    <img src="https://img.shields.io/github/languages/code-size/hattvr/MagicEden-NFT-Bot?label=Size">
    <a href="https://github.com/hattvr/MagicEden-NFT-Bot/issues">
        <img src="https://img.shields.io/github/issues/hattvr/MagicEden-NFT-Bot?label=Issues">
    </a>
</p>

---
<div align="center">
    <img src="https://i.imgur.com/0inoy40.png">
</div>

## **Getting Started**  
MagicEden NFT Bot is an advanced, easy to setup, free, and unbranded Discord bot. To being installing this bot, you're going to want to install the required python libs from the `requirements.txt` file.
```py
pip install -r requirements.txt
```

After you are done installing the required python libraries, you can setup the config file (`config.json`). You will need to grab three different pieces of information before you're able to successfully run the Discord bot.
```json
    "settings": {
        "token": "YOUR_BOT_TOKEN",
        "guild": "YOUR_GUILD_ID",
        "log-channel": "CHANNEL_ID_FOR_LOGS",
        "refreshrate": 600
    }
```
`token` - This is the token for your Discord bot, this can be accessed from your Discord account's Developer Portal!

`guild` - This is the ID of the guild/server you want the bot to send notifications in. You can get a Discord guild/server's id by right-clicking on the server icon and pressing the button named **Copy ID**

`log-channel` - This is the ID of the channel you want the bot to send notifications in. You can get a Discord channel's id by right-clicking on the channel and pressing the button named **Copy ID**

`refreshrate` - This variable is the rate at which the bot will send notifications to your server. The default setting is set to `600` seconds

## **Bot Usage**
To setup NFTs that you want to keep a watch on, you can add them straight into the `config.json` file that is given.
```json
    "nfts": [
        "NAME OF NFT",
        "NAME OF SECOND NFT",
        "NAME OF THIRD NFT"...
    ]
```

## **Any Issues?**  
If you run into any issues or problems during the process of setting up this discord bot, you can contact me using any of my socials given on my Github profile!
