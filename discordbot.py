# coding: UTF-8
import time
from discord.ext import commands
from discord.ext import tasks
from cogs import evals
from discord.utils import get
from datetime import datetime 
import os
from discord import FFmpegPCMAudio
from os import system
import random
import traceback
import discord
import time
import datetime
import requests
import psutil
import asyncio
import youtube_dl
import ffmpeg

client = discord.Client()

bot = commands.Bot(command_prefix='?')
token = os.environ['DISCORD_BOT_TOKEN']
intents = discord.Intents.all()
bot.remove_command('help')
if os.path.exists("channels.txt") == False:
    f = open("channels.txt", "w")
    f.write('')
    f.close()
f = open("channels.txt", "r")
f2 = open("channels.txt", "a")
a = f.read()
if a[len(a)-1:] != "\n":
    f2.write("\n")
f.close()
f2.close()
channelsf = a.splitlines()
channels = list()

bot.teams = [546682137240403984]

#---ログ---
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="(Python)です"))
    evals.setup(bot)
    print("logged in as " + bot.user.name)
    for channel in bot.get_all_channels():
        if channel.name == '起動メッセージ':
            await channel.send('起動完了\nコマンド等が利用できるかご確認ください。')
#---Fire System---
@bot.command()
async def firehelp(ctx):
    await ctx.send("help(使用例:$火災)\n火災警報コマンド:火災\n非火災警報コマンド:非火災\n点検モード:maintenance\n自火報を復旧コマンド:復旧)")

@bot.command(name="点検")
async def tenken(ctx):
        global channels
        for a in channels:
          await a.send("こちらは防災クリーパーです、只今より、非常放送設備の試験を行います。")

@bot.command(name="緊急事態発生(先生版)")
async def emegency(ctx):
        global channels
        for a in channels:
          await a.send("緊急事態が発生しました、先生の指示従って避難してください")

@bot.command(name="緊急事態発生(スタッフ版)")
async def emegency(ctx):
        global channels
        for a in channels:
          await a.send("緊急事態が発生しました、スタッフの指示従って避難してください")

@bot.command(name="火災")
async def kasai(ctx):
        global channels
        for a in channels:
          await a.send("火事です、火事です、火災が発生しました、落ち着いて避難してください")
          

@bot.command(name="発報")
async def happo(ctx):
    global channels
    for a in channels:
        await a.send("火災報知器が作動しました、係員が確認しておりますので、次の放送にご注意ください")
   

@bot.command(name="非火災")
async def notkasai(ctx):
    global channels
    for a in channels:
        await a.send("先ほどの火災報知器の作動は確認の結果、異常がありませんでしたご安心ください")


@bot.command()
async def maintenance(ctx):
    await ctx.send("（´・ω・｀）")


@bot.command(name="復旧")
async def recover(ctx):
    await ctx.send("復旧しました")


@bot.command()
async def join(ctx, i: int):
    global channels
    for a in channels:
        if a.id == i:
            await ctx.send("すでに入っています")
            return
    f = open("channels.txt", "a")
    f.write(str(i)+"\n")
    channels.append(bot.get_channel(i))
    f.close()
    await ctx.send("追加しました")

@bot.command()
async def leave(ctx, i: int):
    global channels
    bool1 = False
    channels2 = list()
    for ch in channels:
        if ch.id != i:
            channels2.append(ch)
        else:
            bool1 = True
    channels = channels2
    f = open("channels.txt", "w")
    for a in channels:
        f.write(str(a.id)+"\n")
    f.close()
    if bool1:
        await ctx.send("削除しました")
    else:
        await ctx.send("登録されていませんでした")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    else:
        orig_error = getattr(error, "original", error)
        error_msg = ''.join(
            traceback.TracebackException.from_exception(orig_error).format())
        await ctx.send(error_msg)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.channel.name != "creeper-fire-alarm操作盤":
        return
    await bot.process_commands(message)
#---基本機能---
@bot.event
async def on_command_error(ctx, error):
    #Bad example
    await ctx.send(error)
#---機能追加---
@bot.command()
async def junk(ctx):
    await ctx.send('ジャンクってかわいいよね。')

@bot.command()
async def fuck(ctx): 
    fuck = ["(# ﾟДﾟ)ﾀﾞﾏﾚ!!", "(´；ω；｀)", "(´・ω・｀)", "(　；∀；)", "（ノ_・。）"] #リストを作る
    await ctx.send(random.choice(fuck)) #リストの中からランダムに選んで送信する

@bot.command()
async def aisiteru(ctx): 
    if ctx.author.id == 709445238468509728:
        fuck = ["ジャンク、ｱｲｼﾃﾙ", "窓辺、ｱｲｼﾃﾙ", "くう、ｱｲｼﾃﾙ", "わーくん死ね", "（´・ω・｀）"] #リストを作る
        await ctx.send(random.choice(fuck)) #リストの中からランダムに選んで送信する
    else:
        await ctx.send('何様のつもりですか……？')

@bot.command()
async def kekkon(ctx): 
    if ctx.author.id == 709445238468509728:
        fuck = ["ジャンク、結婚しよう", "<@!704702259665043476> 窓辺、結婚しよう", "くう、結婚しよう", "わーくん、結婚しよう", "（´・ω・｀）、結婚しよう"] #リストを作る
        await ctx.send(random.choice(fuck)) #リストの中からランダムに選んで送信する
    else:
        await ctx.send('何様のつもりですか……？')

@bot.command()
async def madobe(ctx): 
    if ctx.author.id == 709445238468509728:
        await ctx.send('<@!704702259665043476> ﾏﾄﾞﾍﾞﾉｵﾁﾝﾎﾟｼﾞｭﾎﾟｼﾞｭﾎﾟｼﾀｲ')  
    else:
        await ctx.send('何様のつもりですか……？')    
#---夏海---   
@bot.command()
async def help(ctx):
    await ctx.send(embed=discord.Embed(title="ヘルプコマンドです！", description=f"junk：自分で確かめてね^^\nfuck：謎なコマンドです\nbot人数：botの数を調べます\npin：ピン留めします\nping：確認します\nping2：確認します\nui：ユーザーを調べます(使い方：ui ユーザーID)\n uuser：ユーザー調査です！(使い方：uuser ユーザーID)\nサイコロをふる：サイコロをふります！(使い方：サイコロをふる 1d6)\nチャンネル：指定したチャンネルに書き込みます！(使い方：チャンネル #(チャンネル名) てすと)\nチャンネル確認：チャンネルを確認します！\nチャンネル２：その場のチャンネルに書き込みます！(使い方：チャンネル２ てすと)\nユーザー人数：ユーザー人数を調べます！\nリンク：短縮リンクを作ります！(使い方：リンク URL)\nフォロー：アナウンスチャンネルをフォローします\n全体人数：サーバー人数を調べます！\n役職持ち確認：役職所持者を確認します！(使い方：役職持ち確認 役職名)\n時間確認：時間を確認します！\n野生：ネタコマンドです！\n鯖知りたい：サーバーの情報を知ることができます！(使い方：鯖知りたい サーバーID)\nバグ報告 (バグ報告します"))


@bot.command()
async def help2(ctx):
    if ctx.author.id == 709445238468509728:
        await ctx.send(embed=discord.Embed(title="運営用ヘルプコマンドです！", description=f"madobe：寝落ちした、窓辺を起こすコマンドです\nkekkon：知らんがな（´・ω・｀）\nmaisiteru：良くわからんコマンド\nチャンネルトピックいじります：チャンネルトピックをいじります！(使い方：チャンネルトピックいじります てすと)\nkick：対象者を蹴ります！(使い方：kick ユーザーID)\nban：対象者をBANします！(使い方：ban ユーザーID)\n役職付与系統：役職を付与します！(使い方：役職付与系統 メンバーの名前 役職名)\n脱出：サーバーから退室します！(使い方：脱出 サーバーID)\n使用率：使用率を調べます！\nvcから切断VCから強制切断します！(使い方：vcから切断 めんばあ)\nend：BOTを終了させます！\nプレイ中変更：プレイ中を変更します！(使い方：プレイ中変更 てすと)"))
    else:
        fuck = ["何様のつもりですか……？", "お前、いい加減にしろよ", "お前の権限じゃ、実行できねぇって言ってるだろ", "お前さぁ、しつこい", "しつこいと殺すぞ"] #リストを作る
        await ctx.send(random.choice(fuck)) #リストの中からランダムに選んで送信する

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(
        traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command(name="フォロー")
async def follow(ctx, channel_id:int=754149726290706483):
    syutoku = bot.get_channel(channel_id)
    # print(syutoku.id)
    tyannneru = syutoku.is_news()
    # print(tyannneru)
    if tyannneru == False:
        await ctx.send("アナウンスチャンネルじゃないよー")
    else:
        await syutoku.follow(destination=ctx.channel)
        await ctx.send("アナウンスチャンネルをフォローした。\nいらなくなったら運営に頼んで消して貰ってね。")    


@bot.event
async def on_message(message):
    try:
        if message.author.bot:
            # もし、送信者がbotなら無視する
            return
        GLOBAL_CH_NAME = "ルーミア_global"  # グローバルチャットのチャンネル名

        if message.channel.name == GLOBAL_CH_NAME:
            # hoge-globalの名前をもつチャンネルに投稿されたので、メッセージを転送する
            channels = bot.get_all_channels()
            global_channels = [
                ch for ch in channels if ch.name == GLOBAL_CH_NAME]
            # channelsはbotの取得できるチャンネルのイテレーター
            # global_channelsは hoge-global の名前を持つチャンネルのリスト

            embed = discord.Embed(title=GLOBAL_CH_NAME,
                                  description=message.content, color=0x00bfff)

            embed.set_author(name=message.author.display_name,
                             icon_url=message.author.avatar_url_as(format="png"))
            embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
                             icon_url=message.guild.icon_url_as(format="png"))
            # Embedインスタンスを生成、投稿者、投稿場所などの設定

            for channel in global_channels:
                if message.attachments:
                    file = await message.attachments[0].to_file()
                    embed.set_image(url="attachment://"+file.filename)
                # メッセージを埋め込み形式で転送
                await channel.send(embed=embed,file=(file if message.attachments else None))

            await message.delete()  # 元のメッセージは削除しておく
    except Exception as error:
        await on_command_error(message.channel, error)
    await bot.process_commands(message)


@bot.command(pass_context=True)
async def ping2(ctx):  # 処理時間を返す
    startt = time.time()
    tmp = await ctx.send("計測中……!")
    await tmp.edit(content="pong！\n結果:**" + str(round(time.time()-startt, 3))+"**秒ですฅ✧！")


@bot.command(name='野生')
async def _yasei(ctx):
    col = random.randint(0x000000, 0xffffff)
    nikkuname = ctx.author.nick
    if nikkuname == None:
        await ctx.send(embed=discord.Embed(title="あ！", description=f"野生の{ctx.author.name}が飛び出してきた！", color=col))
    else:
        await ctx.send(embed=discord.Embed(title="あ！", description=f"野生の{ctx.author.name}({nikkuname})が飛び出してきた！", color=col))


@bot.command(name='チャンネルトピックいじります')
async def channeltopic(ctx, channel: discord.TextChannel, *, topic):
    if ctx.message.author.id == 737320852617560120:
        await channel.edit(topic=topic)
        await ctx.message.delete()
    else:
        await ctx.send('何様のつもりですか……？')


@bot.command(name="チャンネル")
async def _channel(ctx, channel: discord.TextChannel, *, arg):
    await channel.send(arg)
    await ctx.message.delete()


@bot.command(name="チャンネル２")
async def _channelninini(ctx, *, arg):
    await ctx.send(arg)
    await ctx.message.delete()


@bot.command(name="kick")
async def _kick(ctx, arg, *, riyuu):
    if ctx.author.id == 709445238468509728:
        await ctx.guild.kick(discord.Object(arg))
        await ctx.send(f'実行者：{ctx.author.name}\n<@{arg}> をキックした。\n理由：{riyuu}')
    else:
        await ctx.send('何様のつもりですか……？')


@bot.command(name="ban")
async def _ban2(ctx, arg, *, riyuu):
    if ctx.author.id in 709445238468509728:
        await ctx.guild.ban(discord.Object(arg), reason=riyuu)
        await ctx.send(f'実行者：{ctx.author.name}\n<@{arg}> をえっついした。\n理由：{riyuu}')
    else:
        await ctx.send('何様のつもりですか……？')


@bot.command(name="サイコロをふる", aliases=["d"])
async def daisuno(ctx, dice: str):
    rolls, limit = map(int, dice.split('d'))
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@daisuno.error
async def daisuno_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("え？\n……お願いですが、数字d数字でお願いします。\nあと0以下はやめてください。")


@bot.command(name="役職付与系統")
async def _yakusyokunoyatu(ctx, member: discord.Member, role: discord.Role):
    if ctx.author.id == 709445238468509728:
        await member.add_roles(role)
        await ctx.send(f'{member.name}さんに{role}を付与しました。')
    else:
        await ctx.send('実行権限がありません。')


@bot.command(aliases=["ピン留め切替", "次のメッセージをピン留めして"])
async def pin(ctx, mid: int):
    msg = await ctx.message.channel.fetch_message(mid)
    if msg.pinned:
        await msg.unpin()
        await ctx.send(f"ピンを外しました。：{ctx.author.name}")
    else:
        await msg.pin()
        await ctx.send(f"ピンをしました。：{ctx.author.name}")


@bot.command(name="時間確認")
async def _zikannnnnnn(ctx):
    # t = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    color = random.randint(0x000000, 0xffffff)
    await ctx.send(embed=discord.Embed(title="時間です。よく見ておいてくださいね。", description=f"{now}", color=color))


@bot.command()
async def ui(ctx, user_id=None):
    col = random.randint(0x000000, 0xffffff)
    try:
        user = await bot.fetch_user(int(user_id))
    except:
        await ctx.send(embed=discord.Embed(description="ユーザーが見つからなかったのです……。", color=col))
    else:
        member = discord.utils.get(bot.get_all_members(), id=int(user_id))
        g_m = discord.utils.get(ctx.guild.members, id=int(user_id))
        embed = discord.Embed(title=f"{user.name}の情報", color=col)
        embed.set_thumbnail(url=f'{user.avatar_url_as(static_format="png")}')
        embed.add_field(name="名前", value=f"{user.name}", inline=False)
        embed.add_field(name="ID", value=f"{user.id}", inline=False)
        embed.add_field(name="タグ", value=f"{user.discriminator}", inline=False)
        embed.add_field(name="BOT", value=f"{user.bot}", inline=False)
        if g_m is not None:
            embed.add_field(name="サーバー上の名前",
                            value=f"{member.nick}", inline=False)
        if g_m is not None:
            # embed.add_field(name="アクティビティ", value=f"{member.activity}", inline=False)
            embed.add_field(name="権限", value=",".join(
                [row[0] for row in list(member.guild_permissions) if row[1]]), inline=False)
            if member.activity is not None:
                embed.add_field(name="アクティビティ", value=member.activity.name)
            embed.add_field(
                name="ステータス", value=f"{member.status}", inline=False)
        embed.add_field(name="アカウント作成日", value=f"{user.created_at}")
        await ctx.send(embed=embed)
        if g_m is not None:
            rui = ""
            embedni = discord.Embed(title="役職")
            for r in g_m.roles:
                rui = rui + f"{r.mention},"
                # ruiruiruiruir = ruiruiruiruir + f"{r.mention},"
            # embedni.add_field(name="役職", value=rui, inline=False)
            embedni.add_field(name="役職", value=",".join(c.mention for c in list(
                reversed(rui))[:44:]) + ("..." if len(rui) > 44 else ""), inline=False)
            # ",".join(c.mention for c in list(reversed(rui))[:44:]) + ("..." if len(rui) > 44 else "")
            await ctx.send(embed=embedni)


@bot.command(name="鯖知りたい")
async def _si(ctx, guild_id=None):
    if guild_id == None:
        guild = ctx.guild
    else:
        guild = bot.get_guild(int(guild_id))
    ch_tcount = len(guild.text_channels)
    ch_vcount = len(guild.voice_channels)
    ch_count = len(guild.channels)
    kt_count = len(guild.categories)
    guild = discord.utils.get(bot.guilds, id=int(guild_id))
    embed = discord.Embed(title=f"{guild.name}の情報", color=ctx.author.color)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name="名前", value=f"{guild.name}", inline=False)
    embed.add_field(name="ID", value=f"{guild.id}", inline=False)
    embed.add_field(name="言語", value=f"{guild.region}", inline=False)
    embed.add_field(name="作成日", value=f"{guild.created_at}", inline=False)
    embed.add_field(name="オーナー", value=f"{guild.owner.name}", inline=False)
    embed.add_field(name="テキストチャンネル数", value=f"{ch_tcount}")
    embed.add_field(name="ボイスチャンネル数", value=f"{ch_vcount}")
    embed.add_field(name="カテゴリー数", value=f"{kt_count}")
    embed.add_field(name="合計チャンネル数(カテゴリー含む)", value=f"{ch_count}")
    embed.add_field(name="サーバー承認レベル", value=f"{guild.mfa_level}")
    embed.add_field(name="サーバー検証レベル", value=f"{guild.verification_level}")
    embed.add_field(name="サーバーブーストレベル", value=f"{guild.premium_tier}")
    embed.add_field(name="サーバーをブーストしたユーザー数",
                    value=f"{guild.premium_subscription_count}")
    # embed.add_field(name="サーバーは大きい？", value=f"{guild.large}")
    await ctx.send(embed=embed)


@bot.command(name="脱出", pass_context=True)
async def huttobasu(ctx, serverid: int):
    if ctx.author.id == 737320852617560120:
        server = bot.get_guild(serverid)
        await server.leave()
        await ctx.send(f"{server.name}から退室しました。")
    else:
        await ctx.send("不可能です……。")


@bot.command(name="リンク", aliases=["短縮リンク"])
# @commands.is_owner()
async def tansyukutyannnnnnnnn(ctx, long_url):
    col = random.randint(0x000000, 0xffffff)
    url = f"https://is.gd/create.php?format=simple&url={long_url}"
    response = requests.get(url)
    print(response.text)
    await ctx.send(embed=discord.Embed(title="短縮リンク", description=response.text, color=col))
    await ctx.message.delete()


@bot.command(aliases=["ユーザー調査"])
# @commands.is_owner()
async def uuser(ctx, idi: int):
    colour = random.randint(0x000000, 0xffffff)
    guild_names = '\n'.join(
        g.name for g in bot.guilds if g.get_member(idi) in g.members)
    embed = discord.Embed(
        title="該当ユーザーが居る場所", description=guild_names[:2000] + '...' if guild_names[:2000] else '', colour=colour)
    await ctx.send(embed=embed)


@bot.command(name="使用率")
@commands.has_permissions(administrator=True)
async def naganomeeeeeee(ctx):
    mem = psutil.virtual_memory()
    allmem = str(mem.total/1000000000)[0:3]
    used = str(mem.used/1000000000)[0:3]
    ava = str(mem.available/1000000000)[0:3]
    memparcent = mem.percent
    await ctx.send(f"全てのメモリ容量:{allmem}GB\n使用量:{used}GB({memparcent}%)\n空き容量{ava}GB({100-memparcent}%)")


@bot.command(name="全体人数")
# @commands.has_permissions(administrator=True)
async def ninzuuzentai(ctx):
    guild = ctx.guild
    member_count = guild.member_count
    await ctx.send(f'メンバー数：{member_count}')


@bot.command(name="ユーザー人数")
# @commands.has_permissions(administrator=True)
async def yuzaninzuu(ctx):
    guild = ctx.guild
    user_count = sum(1 for member in guild.members if not member.bot)
    await ctx.send(f'ユーザ数：{user_count}')


@bot.command(name="bot人数")
# @commands.has_permissions(administrator=True)
async def botninzuu(ctx):
    guild = ctx.guild
    bot_count = sum(1 for member in guild.members if member.bot)
    # bot_count = sum(1 for member in guild.memers if member.bot) #間違い
    await ctx.send(f'BOT数：{bot_count}')


@bot.command(name="チャンネル確認")
async def channelchannel(ctx):
    girudo = ctx.guild.channels
    channelcount = len(girudo)
    await ctx.send(embed=discord.Embed(title=f"チャンネル数：{channelcount}", description="500になったら作れません。"))


@bot.command(name="役職持ち確認")
async def roleuserni(ctx, role: discord.Role):
    colour = random.randint(0x000000, 0xffffff)
    mario = role.id
    # guild_names = [member.name for member in ctx.guild.get_role(mario).members]
    guild_names = '\n'.join(
        member.name for member in ctx.guild.get_role(mario).members)
    guild_dayo = [member.name for member in ctx.guild.get_role(mario).members]
    rokerannni = sum(1 for member in guild_dayo)
    await ctx.send(embed=discord.Embed(title=f"{role}を持つメンバー一覧\n人数：{rokerannni}", description=guild_names[:2000] + '...' if guild_names[:2000] else '', colour=colour))


@bot.command(name="vcから切断")
async def _vckikku(ctx, member: discord.Member):
    if ctx.message.author.id == 709445238468509728:  # このidのとこは自身のIDに変更してね
        await member.move_to(None)
    else:
        await ctx.send("できません！")


@bot.command()
async def end(ctx):
    if ctx.message.author.id == 709445238468509728:  # このidのとこは自身のIDに変更してね
        color = random.randint(0x000000, 0xffffff)
        await ctx.send(embed=discord.Embed(title="シャットダウン！", description="終了します！", color=color))
        await bot.close()
    else:
        color = random.randint(0x000000, 0xffffff)
        await ctx.send(embed=discord.Embed(title="違います！", description="……。", color=color))


@bot.command(name="プレイ中変更")
# @commands.is_owner()
async def pureityuudadada(ctx, *, st):
    if ctx.message.author.id in [709445238468509728]:  # このidのとこは自身のIDに変更してね
        await bot.change_presence(activity=discord.Game(name=st))
        await ctx.send(embed=discord.Embed(title="変更しました！", description=f"{st}"))
    else:
        await ctx.send(embed=discord.Embed(title="あなたは違いますよ！？", description="何しているんですか！？"))


@bot.command(name='バグ報告')
async def bug(ctx, *, text):
    color = random.randint(0x000000, 0xffffff)
    for i in [793023244109348874]:
        ch = bot.get_channel(i)
        await ch.send(embed=discord.Embed(title="意見ありがとうございます。", description=f"報告内容：{text}\n報告者：{ctx.author.name}({ctx.author.id})\nサーバー：{ctx.guild.name}:{ctx.guild.id}", color=color))
    await ctx.send("参考にします。")
    await ctx.message.delete()


bot.run(token)

