import discord
from discord.ext import commands
from random import randint
import aiohttp
import random
import datetime
import os
import json

from dateutil.relativedelta import relativedelta

class Interview:
    """Open Mic related commands."""

    def __init__(self, bot):
        self.bot = bot
        self.mainsv = None
        for sv in self.bot.servers:
            if sv.id == '293782816884391936':
                self.mainsv = sv




    @commands.command(no_pm=False,pass_context=True)
    async def apply(self,ctx):
        msg1 = "Hello! Performing this command means you would like to join the DiscordList Team! If you would like to proceeed with the questions for the application, please type yes. If you are not interested, then please ignore this message."
        msg2 = "1) How old are you?"
        msg3 = "2) Which position are you applying for? (Public Relations Team, Human Resources Team, Moderation Team or Event Hosts)."
        msg4 = "3) Why would you like to join the DiscordList Team?"
        msg5 = "4) Do you have any previous experiences as a staff member? If so, what?"
        msg6 = "5) How active are you on Discord daily? (Please give an approximate figure in hours alongside your timezone)"
        msg7 = "6) What strengths do you have that you wish to offer the team?"
        msg8 = "7) What is your most favourite aspect of the server?"
        msg9 = "8) What do you think we could do to improve our server?"
        msg10 = "9) What do you think are the most important factors of working in a team?"
        msg11 = "Thank you very much for applying! You have successfully completed the application form. The Human Resources Team & Management will review your application as soon as possible. We request you to be patient until we get back to you as to whether your application was rejected or accepted. Once a decision has been made, I will send you further details through DM. Good Luck! :thumbsup:"

        #quests = ["Age", "Applying for","Reason to join the team","Previous Experiences","Usual Daily Activity","Strengths","Fav part of the svr","Thinks we can improve","Most important factors of Teamwork"]



        msgs = [msg2,msg3,msg4,msg5,msg6,msg7,msg8,msg9,msg10]
        hq_server = self.bot.get_server('294138207040176128') #server ID
        log_channel = hq_server.get_channel('294174595697737728') #log-channel ID



        await self.bot.send_message(ctx.message.author,msg1)

        
        def check(msg):
            return msg.content == "yes"

       


        def checkt(msg):
            return msg.author.id != hq_server.me.id
        message = await self.bot.wait_for_message(author=ctx.message.author, check=check)
        
        await self.bot.send_message(ctx.message.author,"Okay, i will now ask you 9 questions, please anwer them, once you send a message, that will be recorded as your answer and the next one will be asked, so please use just one message per question.")
        
        

        i = 1
        
        with open(str(ctx.message.author)+".txt",'w') as f:
            f.write(str(ctx.message.author.name)+"'s application:")
            f.write("\r\n")
            f.write("\r\n")
            while msgs != []:
                m = msgs[0]
                await self.bot.send_message(ctx.message.author,m)
                message = await self.bot.wait_for_message(author=ctx.message.author, check=checkt)
                #if quests!= []:
                    #q = quests[0]
                f.write(m)
                f.write("\r\n")
                f.write(message.content)
                f.write("\r\n")
                f.write("\r\n")
                #ad
                    #uests.remove(q)
                msgs.remove(m)


        await self.bot.send_message(ctx.message.author,msg11)

        txt = "__**Application - "+str(ctx.message.author)+"**__ \n"
        txt += "ID: " + ctx.message.author.id
        await self.bot.send_file(log_channel,fp=str(ctx.message.author)+".txt",content=txt,filename =str(ctx.message.author)+".txt")

    """Commands section"""


def setup(bot):
    bot.add_cog(Interview(bot))
