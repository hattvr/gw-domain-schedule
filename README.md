<h1 align="center">Genshin Wizard's Domain Schedule Bot</h1>
<p align="center">
    <a href="https://github.com/hattvr/gw-domain-schedule/releases/latest">
        <img src="https://img.shields.io/github/v/release/hattvr/gw-domain-schedule?label=Latest%20Version">
    </a>
    <a href="https://github.com/hattvr/gw-domain-schedule/commit/master">
        <img src="https://img.shields.io/github/last-commit/hattvr/gw-domain-schedule?label=Last%20Update">
    </a>
    <img src="https://img.shields.io/github/languages/code-size/hattvr/gw-domain-schedule?label=Size">
    <a href="https://github.com/hattvr/gw-domain-schedule/issues">
        <img src="https://img.shields.io/github/issues/hattvr/gw-domain-schedule?label=Issues">
    </a>
</p>

---
<div align="center">
    <img src="https://i.imgur.com/QlM3TFR.png">
</div>

## **Getting Started**  
gw-domain-schedule is an advanced, easy to setup, free, and unbranded Discord bot. This bot allows users to send domain schedules for weapon ascension materials as well as talent materials, in the form of an image, in a desired channel. To being installing this bot, you're going to want to install the required python libs from the `requirements.txt` file.
```py
pip install -r requirements.txt
```

After you are done installing the required python libraries, you can setup the config file (`config.json`). You will need to grab three different pieces of information before you're able to successfully run the Discord bot.
```json
{
    "settings": {
        "token": "YOUR_BOT_TOKEN_HERE",
        "talent-schedule-channel": "CHANNEL_ID_FOR_TALENTS_SCHEDULE",
        "weapon-schedule-channel": "CHANNEL_ID_FOR_WEAPONS_SCHEDULE"
    }
}
```
`token` - This is the token for your Discord bot, this can be accessed from your Discord account's Developer Portal!

`guild` - This is the ID of the guild/server you want the bot to send notifications in. You can get a Discord guild/server's id by right-clicking on the server icon and pressing the button named **Copy ID**

`talent-schedule-channel` - This is the ID of the channel you want the bot to send the domain schedule for talents in. You can get a Discord channel's id by right-clicking on the channel and pressing the button named **Copy ID**

`weapon-schedule-channel` - This is the ID of the channel you want the bot to send the domain schedule for weapons in. You can get a Discord channel's id by right-clicking on the channel and pressing the button named **Copy ID**

## **Bot Usage**
All you have to do to set-up the bot is change the variables found in `config.json`. Once these are all set-up, you should be able to run the bot effortlessly.

## **Any Issues?**  
If you run into any issues or problems during the process of setting up this discord bot, you can contact me using any of my socials given on my Github profile!
