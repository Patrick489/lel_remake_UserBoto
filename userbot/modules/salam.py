from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Semua Saya {DEFAULTUSER} Mengucapkan**")
    sleep(2)
    await typew.edit("`Assalamualaikum.....`")
    sleep(30)
    await msg.delete()
# Owner @Si_Dian + @Crypto08


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Semua Saya {DEFAULTUSER} Mengucapkan**")
    sleep(2)
    await typew.edit("`Assalamualaikum.....`")
    sleep(30)
    await msg.delete()
# Owner @Si_Dian + @Crypto08


@register(outgoing=True, pattern='^.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Astaghfirulloh Jawab Salam Dong...`")
    sleep(1)
    await typew.edit("`Waallaikumsalam......`")
    sleep(30)
    await msg.delete()
# Owner @Si_Dian + @Crypto08


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Astaghfirulloh Jawab Salam Dong...`")
    sleep(1)
    await typew.edit("`Waallaikumsalam.....`")
    sleep(30)
    await msg.delete()
# Owner @Si_Dian + @Crypto08


CMD_HELP.update({
    "salam":
    "`.p/P`\
\nUsage: Untuk Memberi salam.\
\n\n`.L/.l`\
\nUsage: Untuk Menjawab Salam."
})
