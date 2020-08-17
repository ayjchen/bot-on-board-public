import discord
import random
import asyncio
import time
from discord.ext import commands
from datetime import datetime, timedelta
import json

client = commands.Bot(command_prefix = '.')

d2_options = ['images/d2_i.png', 'images/d2_p.png']
d2_special = ['images/d2_is.png', 'images/d2_is2.png']

d3_options = ['images/d3_rock.png',
              'images/d3_scissors.png',
              'images/d3_paper.png']

d4_options = ['images/d4_1.png',
              'images/d4_2.png',
              'images/d4_3.png',
              'images/d4_4.png']

bzz_options = ['images/bzz_black.png',
               'images/bzz_blue.png',
               'images/bzz_green.png',
               'images/bzz_red.png']

bobei_options = ['images/bobei_1.png',
                 'images/bobei_2.png',
                 'images/bobei_3.png',
                 'images/bobei_4.png']

d6_options = ['images/d6_1.png',
              'images/d6_2.png',
              'images/d6_3.png',
              'images/d6_4.png',
              'images/d6_5.png',
              'images/d6_6.png']

dice2_options = ['images/dice2_1.png',
                 'images/dice2_2.png',
                 'images/dice2_3.png',
                 'images/dice2_4.png',
                 'images/dice2_5.png',
                 'images/dice2_6.png']

draw_options = ['images/draw_1.png',
                'images/draw_2.png',
                'images/draw_3.png',
                'images/draw_4.png',
                'images/draw_5.png',
                'images/draw_6.png',
                'images/draw_7.png']

d8_options = ['images/d8_1.png',
              'images/d8_2.png',
              'images/d8_3.png',
              'images/d8_4.png',
              'images/d8_5.png',
              'images/d8_6.png',
              'images/d8_7.png',
              'images/d8_8.png']

d10_options = ['images/d10_1.png',
               'images/d10_2.png',
               'images/d10_3.png',
               'images/d10_4.png',
               'images/d10_5.png',
               'images/d10_6.png',
               'images/d10_7.png',
               'images/d10_8.png',
               'images/d10_9.png',
               'images/d10_10.png']

digit_options = ['images/digit_1.png',
                 'images/digit_2.png',
                 'images/digit_3.png',
                 'images/digit_4.png',
                 'images/digit_5.png',
                 'images/digit_6.png',
                 'images/digit_7.png',
                 'images/digit_8.png',
                 'images/digit_9.png',
                 'images/digit_0.png']

panties_options = ['images/panties_1.png',
                   'images/panties_2.png',
                   'images/panties_3.png',
                   'images/panties_4.png',
                   'images/panties_5.png',
                   'images/panties_6.png',
                   'images/panties_7.png',
                   'images/panties_8.png',
                   'images/panties_9.png',
                   'images/panties_10.png']

d12_options = ['images/d12_1.png',
               'images/d12_2.png',
               'images/d12_3.png',
               'images/d12_4.png',
               'images/d12_5.png',
               'images/d12_6.png',
               'images/d12_7.png',
               'images/d12_8.png',
               'images/d12_9.png',
               'images/d12_10.png',
               'images/d12_11.png',
               'images/d12_12.png']

d20_options = ['images/d20_1.png',
               'images/d20_2.png',
               'images/d20_3.png',
               'images/d20_4.png',
               'images/d20_5.png',
               'images/d20_6.png',
               'images/d20_7.png',
               'images/d20_8.png',
               'images/d20_9.png',
               'images/d20_10.png',
               'images/d20_11.png',
               'images/d20_12.png',
               'images/d20_13.png',
               'images/d20_14.png',
               'images/d20_15.png',
               'images/d20_16.png',
               'images/d20_17.png',
               'images/d20_18.png',
               'images/d20_19.png',
               'images/d20_20.png']

congrats = ":confetti_ball: 求婚成功 :confetti_ball: 恭喜 :confetti_ball: 百年好合 :confetti_ball: \n :tada: :tada: :tada: :tada:  媽:ring:爸  :tada: :tada: :tada: :tada: \n :tada: :tada: :tada: :tada:  爸:ring:媽  :tada: :tada: :tada: :tada: \n :clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap:"

# list of emotes to randomize
emotes = ["<:A15:700714739793264641>",
          "<:A11:700714739730481259>",
          "<:A23:700714740002979900>",
          "<:A25:700714740011499570>",
          "<:A52:718028464829104148>"]

# list of advice to randomize
advices = [REDACTED]

# for config.json
config = {}

# for greetings.json
greetings = []

@client.event
async def on_ready():
    global config
    global greetings
    with open('config.json') as f:
        config = json.load(f)
    with open("greetings.json", "r", encoding="utf-8") as f:
        greetings = json.load(f)
    await client.change_presence(activity=discord.Game('v1.4.5 抽特殊骰大賽現在開始'))
    print('We have logged in as {0.user}'.format(client))
    print(discord.__version__)


alarm_time = '18:00' # 暫時沒用到

target_date = '07/15'
df = '%m/%d'
tf = '%H:%M'

notif_cooldown = 0
notif = True

servers = {}
class Cooldown:
    def __init__(self):
        self.in_cooldown = False
        self.cd_seconds = 0

@client.event
async def on_message(message):
    global config
    global notif
    global notif_cooldown
    if message.author == client.user:
        return
    elif message.author.id == 700546709943484427: # for chick1988, chick1988 ID: 700546709943484427
        if not config['surprised']:
            global congrats
            global greetings

            this_greeting_index = next((i for i, item in enumerate(greetings) if item["sent"] == False), -1)

            config['surprised'] = True


            if (this_greeting_index != -1):
                await message.channel.send(congrats + "\n\n今日投稿的問候：\n" + greetings[this_greeting_index]["content"])
                greetings[this_greeting_index]["sent"] = True
                with open("greetings.json", "w", encoding="utf-8") as json_file:
                    json.dump(greetings, json_file)
            else:
                await message.channel.send(congrats + "\n\n" + random.choice(greetings)["content"]) # greetings 都用過就隨機

            with open('config.json', 'w') as json_file:
                json.dump(config, json_file)

        checkmybf = ["我男友", "我的男友", "我男朋友", "我的男朋友", "幫主男朋友", "幫主男友", "幫主的男朋友", "幫主的男友"]
        if any(s in message.content for s in checkmybf):
            await message.channel.send("男友？ 自己去罰寫十遍老公")
        elif ("男友" in message.content or "男朋友" in message.content):
            await message.channel.send("...哦，別人的男友？好吧。")

        # notif
        if notif:
            notif_ch = client.get_channel(718853266657640468) # fill in w/ channel id 早安媽組通知區 ID: 718853266657640468
            msg_ch = message.channel.name
            await notif_ch.send(f'<@&718851402390175804> 各位！你媽上線了囉！\n||噓，他在{msg_ch}||<:A41:701096183426449449>') # fill in w/ role id 早安媽組 ID: 718851402390175804
            notif_cooldown = 600 # reset cooldown to 600s (10 min)
            notif = False
        else:
            notif_cooldown = 600 # reset cooldown to 600s (10 min)

    # elif message.author.id == 206273796951244810: # for testing only (mochi3202 ID: 206273796951244810)
        checkKeyword = ["嗷", "汪", "咕", "嚕", "昂", "ㄤ"]
        if ("咕嚕" in message.content):
            await message.channel.send(random.choice(["你484肚子餓", "484你肚子在叫"]) + "<:A34:701064350986928209>")
        elif ("ㄠ" in message.content) and len(message.content) < 5:
            await message.channel.send("講人話好嗎？<:A24:700714740002979910>")
        elif any(s in message.content for s in checkKeyword):
        # elif ("嗷" in message.content) or ("汪" in message.content) or ("咕" in message.content) or ("嚕" in message.content) or ("昂" in message.content):
            count = message.content.count("嗷")
            countw = message.content.count("汪")
            countg = message.content.count("咕")
            countl = message.content.count("嚕")
            countu = message.content.count("昂")
            countu2 = message.content.count("ㄤ")
            if countu == 3 or countu2 == 3:
                await message.channel.send(":microphone: 頭特摸大死去～多啦 A 夢嗯～ :microphone:")
            elif countg == 2:
                await message.channel.send("過兒乖～")
            elif count > 5 and random.randint(0, 100) < 70:
                await message.channel.send("別再嗷了，我要壞ㄌ <:A7:700714739621429248>")
            elif countw > 5 and random.randint(0, 100) < 50:
                await message.channel.send("好會汪 <:A18:700714739835076648>")
            elif countw > 5 and random.randint(0, 100) < 50:
                await message.channel.send("嗷嗚嗷ㄨ～咳咳咳（嗆到")
            else:
                final_str = "嗷" * count
                final_w_str = "嗷嗚" * countw
                final_g_str = "嚕" * countg
                final_l_str = "咕"*(1 if countl > 0 else 0) + "嗚" * countl
                final_u_str = "嗯"*(1 if countu > 0 else 0) + "昂" * countu
                final_u2_str = "ㄤ" * countu2
                final_b_str = ""
                opt_emote = ""
                punct = "！"
                if random.randint(0, 100) < 20:
                    punct = random.choice(["？", "。"])
                if random.randint(0, 100) < 60:
                    opt_emote = random.choice(emotes)
                if ("嗷嗚" in message.content):
                    count_double = message.content.count("嗷嗚")
                    final_str = "汪" * count_double
                elif ("掰補" in message.content):
                    final_b_str = "掰比"
                    punct = "～"
                elif count == 1 and message.content.find("嗷") != 0 and random.randint(0, 100) < 90:
                    position = message.content.find("嗷")
                    final_str = message.content[position - 1:position + 1]
                elif countu == 1 and message.content.find("昂") != 0 and random.randint(0, 100) < 90:
                    position = message.content.find("昂")
                    final_u_str = message.content[position - 1:position + 1]
                elif countu2 == 1 and message.content.find("ㄤ") != 0 and random.randint(0, 100) < 90:
                    position = message.content.find("ㄤ")
                    final_u2_str = message.content[position - 1:position + 1]
                await message.channel.send(final_str + final_w_str + final_g_str + final_l_str + final_u_str + final_u2_str + final_b_str + punct + opt_emote)
        elif ("嗚" in message.content):
            count5 = message.content.count("嗚")
            if (count5 > 1):
                await message.channel.send(random.choice(["鼻要哭 <:A35:701064350995185694>", "給你抱抱 <:A52:718028464829104148> <:A52:718028464829104148> <:A52:718028464829104148>"]))
        elif ("嘔" in message.content):
            await message.channel.send("阿加西嘔嘔嘔嘔嘔嘔嘔")

    today = datetime.strftime(datetime.now(), df)

    global servers
    if message.guild.id not in servers:
        servers[message.guild.id] = Cooldown()

    this_server = servers[message.guild.id]

    if not this_server.in_cooldown and (('媽呢' in message.content) or ('想媽了' in message.content)):
        date_diff = round((datetime.strptime(target_date, df) - datetime.strptime(today, df)).total_seconds() // 86400)
        if (date_diff > 0):
            await message.channel.send(f'你媽已經回國啦！距離咪咪貓貓只剩 {date_diff} 天囉！(到期日 {target_date})')
        else:
            await message.channel.send(f'你媽已回國解除隔離咪咪貓貓啦 <:A37:701064351188123738> <:A37:701064351188123738> <:A37:701064351188123738> ')

        this_server.in_cooldown = True
        await asyncio.sleep(int(this_server.cd_seconds)) # wait for cooldown {this_server.cd_seconds}
        this_server.in_cooldown = False

    await client.process_commands(message) # important: https://discordpy.readthedocs.io/en/rewrite/faq.html#why-does-on-message-make-my-commands-stop-working

@client.command(aliases = ['ad'])
async def advice(ctx):
    await ctx.message.delete()
    await ctx.send(f"{ctx.message.author.display_name}：\n{random.choice(advices)}")

@client.command()
async def testMention(ctx):
    notif_ch = client.get_channel(718853266657640468) # fill in w/ channel id 早安媽組通知區 ID: 718853266657640468
    await notif_ch.send('<@&718851402390175804> 測試一下各位有沒有被 tag 到喔！') # fill in w/ role id 早安媽組 ID: 718851402390175804

@client.command()
async def limit(ctx, seconds):
    global servers
    await ctx.message.delete()
    if ctx.guild.id in servers:
        servers[ctx.guild.id].cd_seconds = seconds
    else:
        servers[ctx.guild.id] = Cooldown()
        servers[ctx.guild.id].cd_seconds = seconds
    await ctx.send(f'Cooldown set to {seconds} second(s)')

@client.command()
async def resetSurprise(ctx):
    global config
    await ctx.message.delete()
    config['surprised'] = False
    await ctx.send(':clown: :ok_hand_tone1:')
    with open('config.json', 'w') as json_file:
        json.dump(config, json_file)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases = ['coin'])
async def d2(ctx, *args):
    await ctx.message.delete()
    if (random.randint(0, 1000) <= 1):
        await ctx.send(f"{ctx.message.author.display_name}：\n {' '.join(args)}", file=discord.File(random.choice(d2_special)))
    else:
        await ctx.send(f"{ctx.message.author.display_name}：\n {' '.join(args)}", file=discord.File(random.choice(d2_options)))

@client.command(aliases = ['rps'])
async def d3(ctx, *args):
    await ctx.message.delete()
    await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File(random.choice(d3_options)))

@client.command()
async def d4(ctx, *args):
    await ctx.message.delete()
    await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File(random.choice(d4_options)))

@client.command()
async def bzz(ctx, *args):
    await ctx.message.delete()
    await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File(random.choice(bzz_options)))

@client.command(aliases = ['bb'])
async def bobei(ctx, *args):
    await ctx.message.delete()
    if (random.randint(0, 1000) <= 1):
        await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File('images/bobei_s.png'))
    else:
        await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File(random.choice(bobei_options)))

@client.command(aliases = ['dice'])
async def d6(ctx, *args):
    await ctx.message.delete()
    await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File(random.choice(d6_options)))

@client.command()
async def dice2(ctx, *args):
    await ctx.message.delete()
    if (random.randint(0, 1000) <= 1):
        await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File('images/dice2_s.png'))
    else:
        await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File(random.choice(dice2_options)))

@client.command(aliases = ['lots', 'lot'])
async def draw(ctx, *args):
    await ctx.message.delete()
    await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File(random.choice(draw_options)))

@client.command()
async def d8(ctx, *args):
    await ctx.message.delete()
    await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File(random.choice(d8_options)))

@client.command()
async def d10(ctx, *args):
    await ctx.message.delete()
    await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File(random.choice(d10_options)))

@client.command()
async def digit(ctx, *args):
    await ctx.message.delete()
    await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File(random.choice(digit_options)))

@client.command(aliases = ['pa'])
async def panties(ctx, *args):
    await ctx.message.delete()
    if (random.randint(0, 1000) <= 1):
        await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File('images/panties_s.png'))
    else:
        await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File(random.choice(panties_options)))

@client.command()
async def d12(ctx, *args):
    await ctx.message.delete()
    await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File(random.choice(d12_options)))

@client.command()
async def d20(ctx, *args):
    await ctx.message.delete()
    await ctx.send(f"{ctx.message.author.display_name}：\n{' '.join(args)}", file=discord.File(random.choice(d20_options)))

burger = False
med1 = False
med2 = False
liquid = False

# background task
async def my_background_task():
    await client.wait_until_ready()

    global burger
    global notif_cooldown
    global notif
    global med1
    global med2
    global liquid
    record_day = datetime.now().day
    channel1 = client.get_channel(700867103414157322) # 語音用聊天 ID: 700867103414157322
    channel2 = client.get_channel(700545165160349747) # 聊天室 ID: 700545165160349747
    while not client.is_closed():
        if (record_day != datetime.now().day):
            record_day = datetime.now().day

            today = datetime.strftime(datetime.now(), df)
            date_diff = round((datetime.strptime(target_date, df) - datetime.strptime(today, df)).total_seconds() // 86400)

            if (date_diff > 0):
                await channel1.send(f'<:A11:700714739730481259> 整點報倒數：距離你媽解除隔離享樂只剩 {date_diff} 天囉！(到期日 {target_date})')
                await channel2.send(f'<:A11:700714739730481259> 整點報倒數：距離你媽解除隔離享樂只剩 {date_diff} 天囉！(到期日 {target_date})')
            elif date_diff == 0:
                await channel1.send(f'<:A11:700714739730481259> 整點報倒數：94 今天啦！要咪咪貓貓啦 <:A37:701064351188123738> <:A37:701064351188123738> <:A37:701064351188123738> (到期日 {target_date})')
                await channel2.send(f'<:A11:700714739730481259> 整點報倒數：94 今天啦！要咪咪貓貓啦 <:A37:701064351188123738> <:A37:701064351188123738> <:A37:701064351188123738> (到期日 {target_date})')

            burger = False
            med1 = False
            med2 = False
            liquid = False

            # 隔日 reset config
            config['surprised'] = False
            with open('config.json', 'w') as json_file:
                json.dump(config, json_file)

        if not burger and (datetime.strftime(datetime.now(), tf) == '03:00'):
            vc1 = len(client.get_channel(700589041372102666).members)
            vc2 = len(client.get_channel(700589156417667094).members)
            vc3 = len(client.get_channel(700589178991411351).members)
            vc4 = len(client.get_channel(700589195181424731).members)
            vc_total = vc1 + vc2 + vc3 + vc4
            await channel1.send(f'今日蟹堡人數：{vc_total}人 :hamburger:')
            burger = True

        if not liquid and (datetime.strftime(datetime.now(), tf) == '06:00'):
            await channel1.send(REDACTED)
            liquid = True

        if not med1 and (datetime.strftime(datetime.now(), tf) == '12:00'):
            await channel2.send(REDACTED)
            med1 = True

        if not med2 and (datetime.strftime(datetime.now(), tf) == '18:00'):
            await channel2.send(REDACTED)
            med2 = True

        if notif_cooldown > 0:
            notif_cooldown -= 5 # subtract 5s on every task run from total 600s (10 min) cooldown
        elif notif_cooldown <= 0:
            notif = True

        await asyncio.sleep(5) # task runs every 5 seconds

client.loop.create_task(my_background_task())

client.run(REDACTED)
