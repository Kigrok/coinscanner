# Telegram Bot _[VCoinScannerBot](https://t.me/VCoinScannerBot)_

![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![\[Telegram\] aiogram live](https://img.shields.io/badge/telegram-aiogram-blue.svg?style=flat-square)

![First Page in Bot](https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gPey7enyxwP18z5Im0ABV-KSI5LPVtz79DTqwZM5uhvCZUXwCroBdU5wfeiw0WyBVDhABOzcRyJmd7I0x00iByd0F6kAg=w1366-h663)

### _The [bot](https://t.me/VCoinScannerBot)  converts and compares all ads on [Binance](https://www.binance.info/ru/activity/referral-entry/CPA?fromActivityPage=true&ref=CPA_00P2G3TCHK) and [Huobi](https://www.huobi.com/ru-ru/v/register/double-invite/?invite_code=48vd5223&inviter_id=11345710) and returns the ad with the best price._

---

## Process

- Exchange Choice ([Binance](https://www.binance.info/ru/activity/referral-entry/CPA?fromActivityPage=true&ref=CPA_00P2G3TCHK) or [Huobi](https://www.huobi.com/ru-ru/v/register/double-invite/?invite_code=48vd5223&inviter_id=11345710)).
- Choice of action (BUY or SELL).
- Bank selection.
- Select amount.
- Getting the best result.

---

## Bot subscription check

![Subscribe Page in Bot](https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gOJU19zA0qSHwxK85dBT2dTgTEGlFJaatcpX0v2CqF3izP1jV3BRbWFW3pa4Z3XYKiToPWt1kdGZ99a3feR5CvYgixzHA=w1366-h663)

---

## Choice of action 
### (Checker or Help message)

![Action Page in Bot](https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gOxgx_uOitrXERTAmzZU_oTCO5fETp0C4B2iVNNHCfjwNbPZKifP9upjg2s_TrRU0g9EGGr47JfSAqPDR-9b4Sbmi0v=w1366-h663)

---

## Help Message

![Help Page in Bot](https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gPl0nvr86MmXKCoXvhx2Bkb3K78fmT9mVLMmIy6yetAuyUxlX08vNC_0sCgxpB_XrwxKiw8HfoGshCwH2qwKVtporkh=w1366-h663)

---

## Exchange Choice 
### ([Binance](https://www.binance.info/ru/activity/referral-entry/CPA?fromActivityPage=true&ref=CPA_00P2G3TCHK) or [Huobi](https://www.huobi.com/ru-ru/v/register/double-invite/?invite_code=48vd5223&inviter_id=11345710))

![Exchange Page in Bot](https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gPY1z33yHw3iiuLu7J39BrksDOTHh0u5DGg4StgrcD2RMmh-tHiWg-wSEgtiDlm06L2kCLWaxM8FGzspF40ZygvzbAc=w1366-h663)

---

## Choice of action 
### (BUY or SELL)

![Action Page in Bot](https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gPr6S9dSJoa8CYMCfFX4ux2kOqHAlFg0i6BhHIiLkKM7-YcWkp2JEy0E-WNe1PgyEyP-cirA0p5W5ssN4FNXmW2P7bkTw=w1366-h663)

---

## Bank selection

![Banks Page in Bot](https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gPChVydkv8ItEaMUSysraPdfQ-a7MZfPY1vwOqjjBL1OpVXeIwKALqrbz2HeWFA_NSOJoa8Uznnx0s_RPxNvbwr6p3L=w1366-h663)

---

## Select amount

![Amont Page in Bot](https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gOAL_SS-eFUwcg_RCcsT0V1eIsj9rSx5A8hIYNSryjN3sKpI4_Om4x_wZzzMsPwti0wmTmzU3k5i9dBiwtoy8rwGKG-=w1366-h663)

---

## Getting the best result

![Result Page in Bot](https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gNPWcPbD8GcEIHL3AqPpFhdXVCEp2IDXrLKNeA3NHJQNZHlSWHZjskJZONGhtH9iUOTI7rBt-1rek0Vw8BO9Sj2FdqrQw=w1366-h663)

---

## Administrator Features

-  Command ```/sendall [text message] ```
    >Send a message to all subscribers of the bot.
- Command ```/static```
    >Return bot statistics:
        1. Number of users added to the bot.
        2. Number of users subscribed to the bot.

---

## Install 

Cloning a repository
```sh
git clone https://github.com/Kigrok/coinscanner.git
cd coinscanner
```

Installing the virtual environment and packages

```sh
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

Adding a bot token and owner id (optional)

```sh
export TOKEN='your bot token'
export ADMIN='your id in Telegram'
export CHANNEL='your channel name(format: @channel)'
```

----

# DataBase 
![SQLITE](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
Create DataBase
```sh
python3 cdb.py
```
---

# Start

```sh
python3 main.py
```
