from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern="^.hua$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("أ‿أ")
        await e.edit("╥﹏╥")
        await e.edit("(;﹏;)")
        await e.edit("(ToT)")
        await e.edit("(┳Д┳)")
        await e.edit("(ಥ﹏ಥ)")
        await e.edit("（；へ：）")
        await e.edit("(T＿T)")
        await e.edit("（πーπ）")
        await e.edit("(Ｔ▽Ｔ)")
        await e.edit("(⋟﹏⋞)")
        await e.edit("（ｉДｉ）")
        await e.edit("(´Д⊂ヽ")
        await e.edit("(;Д;)")
        await e.edit("（>﹏<）")
        await e.edit("(TдT)")
        await e.edit("(つ﹏⊂)")
        await e.edit("༼☯﹏☯༽")
        await e.edit("(ノ﹏ヽ)")
        await e.edit("(ノAヽ)")
        await e.edit("(╥_╥)")
        await e.edit("(T⌓T)")
        await e.edit("(༎ຶ⌑༎ຶ)")
        await e.edit("(☍﹏⁰)｡")
        await e.edit("(ಥ_ʖಥ)")
        await e.edit("(つд⊂)")
        await e.edit("(≖͞_≖̥)")
        await e.edit("(இ﹏இ`｡)")
        await e.edit("༼ಢ_ಢ༽")
        await e.edit("༼ ༎ຶ ෴ ༎ຶ༽")


@register(outgoing=True, pattern='^.huh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n />❤️ *Ini Buat Kamu`")
    sleep(3)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n/>💔  *Aku Ambil Lagi`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n💔<\\  *Terimakasih`")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "ceritacinta":

        await event.edit(input_str)

        animation_chars = [
            "`Cerita ❤️ Cinta` ",
            "  😐             😕 \n/👕\\         <👗\\ \n 👖               /|",
            "  😉          😳 \n/👕\\       /👗\\ \n  👖            /|",
            "  😚            😒 \n/👕\\         <👗> \n  👖             /|",
            "  😍         ☺️ \n/👕\\      /👗\\ \n  👖          /|",
            "  😍          😍 \n/👕\\       /👗\\ \n  👖           /|",
            "  😘   😊 \n /👕\\/👗\\ \n   👖   /|",
            " 😳  😁 \n /|\\ /👙\\ \n /     / |",
            "😈    /😰\\ \n<|\\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\\   /(👶)\\ \n  /!\\   / \\ ",
            "`TAMAT 😅`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "canda":

        await event.edit(input_str)

        animation_chars = [
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀  ⠀   ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Kamu    ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀      ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Pasti   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__|⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Belum   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀         ⡇\n  ⠙⢿⣯⠄⠀⠀(x)⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀   ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Mandi  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__ ⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀ ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Bwhaha  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__| ⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀  ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Canda   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀****⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@register(outgoing=True, pattern='^.nah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n />💖 *Ini Buat Kamu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n💖<\\  *Tapi Bo'ong`")
# Alpinnnn Gans


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 6)

    input_str = event.pattern_match.group(1)

    if input_str == "owner":

        await event.edit(input_str)

        animation_chars = [
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬜⬜⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])


@register(outgoing=True, pattern='^.hai(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Hai ,  Assalamualaikum**")
    sleep(1)
    await typew.edit("Kalian Nungguin aku gak??")
    sleep(1)
    await typew.edit("Ih ga mau🤢")
    sleep(1)
    await typew.edit("gasukaa😫")
    sleep(1)
    await typew.edit("__GELAYY__🤮")
    
   
@register(outgoing=True, pattern='^.kntl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("Tau kh kalian wahai tuan-tuan??")
    sleep(1)
    await typew.edit("se**KONT0L** **K0NTOL** nya si **K0NTOL**")
    sleep(1)
    await typew.edit("lebih **KONTOL** lagi")              
    sleep(1)
    await typew.edit("kalian **KONTOL**")


@register(outgoing=True, pattern='^.alay(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("eh kamu, iya kamu")
    sleep(1)
    await typew.edit("**ALAY** bnget sih")
    sleep(1)
    await typew.edit("spam bot mulu")
    sleep(1)
    await typew.edit("baru jadi userbot ya?? xixixi")
    sleep(1)
    await typew.edit("pantes **NORAK**")
# Alvin Imut
# Alvin Gans
# Lord
CMD_HELP.update({
    "animasi":
    "`.hua` ; `.huh`\
    \nUsage: cobain.\
    \n\n`.ceritacinta` ; `.canda`\
    \nUsage: animasi.\
    \n\n`.nah` ; `.owner`\
    \nUsage: animasi.\
    \n\n`.hai` ; `.kntl`\
    \nUsage: liat aja.\
    \n\n`.alay`\
    \nUsage: liat sendiri"
})
