import discord
from discord.ext import commands
import yt_dlp

# Замените 'YOUR_BOT_TOKEN' на свой токен бота
token = 'MTE0Njk1MjU4MDUyNjc3NjQ1MA.GHtVma.QsW0oiWET9JkVuhVpB6r3mckqeLKOrqaAKRAYY'

# Замените 'YOUR_YOUTUBE_API_KEY' на свой ключ API YouTube Data
youtube_api_key = 'AIzaSyCTy37jSLnN_r4btszjZucztJp5r8iR2dI'

# Инициализируем бота
intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Инициализируем YouTube Data API
youtube = yt_dlp.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'quiet': True, 'format': 'bestaudio/best', 'extractaudio': True, 'audioformat': 'mp3'})

# Функция для присоединения к голосовому каналу
async def join_channel(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

# Функция для воспроизведения музыки
async def play_music(ctx, query):
    try:
        # Выполняем поиск видео на YouTube
        ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(query, download=False)
            audio_url = info_dict['url']

        voice_client = ctx.voice_client
        if not voice_client:
            await join_channel(ctx)
            voice_client = ctx.voice_client

        if voice_client.is_playing():
            voice_client.stop()

        voice_client.play(discord.FFmpegPCMAudio(audio_url))
    except Exception as e:
        await ctx.send(f"Произошла ошибка при выполнении команды: {str(e)}")
        print(f"An error occurred while processing the audio: {str(e)}")

# Событие бота: когда бот готов
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Команда бота: присоединиться к голосовому каналу
@bot.command()
async def join(ctx):
    await join_channel(ctx)

# Команда бота: воспроизвести музыку
@bot.command()
async def play(ctx, *, query):
    await play_music(ctx, query)

# Команда бота: покинуть канал
@bot.command()
async def leave(ctx):
    voice_client = ctx.voice_client
    if voice_client:
        await voice_client.disconnect()
        print("Bot left the voice channel.")
    else:
        await ctx.send("I'm not in a voice channel.")
        print("Bot is not in a voice channel.")

# Запустите бота с вашим токеном
bot.run(token)
