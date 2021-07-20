import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random 
import json

with open('C:\\Users\\alann\\Documents\\GitHub\\dc\\setting.json','r',encoding='utf8') as jfile:
        jdata = json.load(jfile)

class Pic(Cog_Extension):
    @commands.command()
    async def sampic(self, ctx):
        random_pic = random.choice(jdata['miku'])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)