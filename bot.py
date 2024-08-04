import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command('info')
async def cmd_info(ctx: commands.Context):
    name = ctx.author.global_name
    text = f'Привет, {name}! Я бот, который помогает в борьбе с экологическими проблемами.😎'
    await ctx.send(text)


@bot.command('memo')
async def cmd_memo(ctx: commands.Context):
    embed = discord.Embed(
        title = 'Как спасти нашу планету? 🤨 ',
        description='Проблема экологии сейчас очень актуальна, мы должны постараться сохранить нашу планету 🤓',
        color=discord.Colour.from_rgb(244, 11, 33)
    )

    embed.add_field(
        name = '1 правило',
        value='Сортируйте мусорные отходы. Это поможет уменьшить загрязнение водоёмов и других природных зон.🏞️'
    )

    embed.add_field(
        name = '2 правило',
        value='Меньше пользуйтесь машинами. Ходите пешком или используйте экологичный транспорт. 🚗'
    )

    embed.add_field(
        name = '3 правило',
        value='Защищайте животных. 🦝'
    )


    await ctx.send(embed=embed)




@bot.command('test')
async def cmd_test(ctx: commands.Context):
    text = "Бла **бла бла** Бла __бла бла__ Бла --бла бла-- бла ~~бла бла~~ "
    await ctx.send(text)


bot.run('')
