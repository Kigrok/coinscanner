from functions.sorted import checker
from data import buttons as btn


# Post with ad 
async def check(bot, exchange, chat_id, action, volume, bank):
    ''' Message weth best ad'''
    item=await checker(exchange=exchange, action=action, volume=volume, bank=bank)
    card=(f"""
<b>{item["Exchange"]} | {item["Action"]} {item["Coin"]}</b>\n\
{item["Merchant"]} {item["User"]} | ({item["UserOrders"]} Orders; {item["UserReating"]}% Completion)
Price: {item["Price"]} ₽
Price on USDT: {item["USDT"]} ₽
Limit: ₽ {item["MinLimit"]} - {item["MaxLimit"]}
Bank: {", ".join(map(str, item["Bank"]))}""")
    await bot.send_message(
        chat_id=chat_id,
        text=card, 
        disable_web_page_preview=True,
        reply_markup=btn.mainMenu)