from telethon import TelegramClient, events
import re


api_id = 27272508
api_hash = "fd910ebdfc761b86e5e2f143d71f45c0"
phone = "380507478894"

client = TelegramClient(phone, api_id, api_hash, system_version='4.16.30-vxCUSTOM')
client.parse_mode = 'html'

main_channel = -1001998091404

channels_for_grab = [-1001606401919,-1001949005395,-1001295005098,-1001660722954,-1001857132617,-1001322813943,-1001604013421,-1001350832778,-1001657132982,-1001581519471,-1001177079955,-1001277862355,-1001325190160,-1001181579326,-1001543510066,-1001791271427,-1001389837789,-1001896345357,-1001233154810,-1001318459173,-1001983684965,-1001517199518,-1001786005753,-1001685123337,-1001529532603,-1001393712717,-1001674186593,-1001576305880,-1001751525601,-1001811247070,-1001371916046,-1002028354470, -1001525543664,-1001290983142,-1001579208217,-1001673787979,-1001553038207,-1001244592602,-1001833426987,-1001904339991,-1001318459173,-1001967244124,-1001603058549,-1001995528971,-1001718809245,-1001961266885,-1001380511806,-1002087504613,-1001450269392,-1001995902277,-1001583799495]



async def check_links(text):
    words = ['t.me/']
    chk_pat = '(?:{})'.format('|'.join(words))
    return bool(re.search(chk_pat, text, flags=re.I))


@client.on(events.NewMessage(chats=channels_for_grab))
async def my_event_handler(event):
    text = str(event.message.text)
    check_linkss = await check_links(text)
    if check_linkss:
        if event.message:
            try:
                # await client.send_file(main_channel, file=event.message, caption=text)
                await client.forward_messages(main_channel, messages=event.message)
            except TypeError:
                try:
                    await client.send_file(main_channel, file=event.message, caption=text)
                except:
                    try:
                        await client.send_message(main_channel, text)
                    except:
                        pass
    else:
        return

client.start()
client.run_until_disconnected()
