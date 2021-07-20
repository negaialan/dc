import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random 
import json

with open('C:\\Users\\alann\\Documents\\GitHub\\dc\\setting.json','r',encoding='utf8') as jfile:
        jdata = json.load(jfile)

class miku(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'miku':