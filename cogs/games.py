from logging import log
import discord
import os
import time
import datetime
from datetime import datetime
from datetime import timedelta
from discord import message
from discord import user
from discord import colour
from discord.ext import commands
import json
import random
from multiprocessing import Process
import asyncio
from discord_components import DiscordComponents, Button, ButtonStyle
import pymongo
from pymongo import MongoClient

cluster = MongoClient("")
db = cluster["UserData"]
collection = db["UserData"]

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    



    '''
    ██████╗░░█████╗░░█████╗░██╗░░██╗  ██████╗░░█████╗░██████╗░███████╗██████╗░
    ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██████╔╝██║░░██║██║░░╚═╝█████═╝░  ██████╔╝███████║██████╔╝█████╗░░██████╔╝
    ██╔══██╗██║░░██║██║░░██╗██╔═██╗░  ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
    ██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║
    ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝

    ░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗
    ██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
    ╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░
    ░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗
    ██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝
    ╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
    '''
        

    @commands.command()
    async def rps(self, ctx, user2: discord.User, rounds:int):
        for i in range(1):
            
            if user2 == ctx.author or user2.bot == True:
                error_embed = discord.Embed(description=f"<a:a_cross:860370275275505694> | Invalid Mentioned User")
                await ctx.send(embed = error_embed)
                break
                
            else:
                ynembed = discord.Embed(description=f"**User {ctx.author.mention} Wants To Start A `{rounds}` Round Duel With You.**")
                ynembed.add_field(name="Accept", value="Choose `Accept` To Start")
                ynembed.add_field(name="Reject", value="Choose `Reject` To Reject")
                await ctx.send(f"{user2.mention}")
                            
                choice_msg = await ctx.send(embed=ynembed,
                                            components = [
                                [Button(style=ButtonStyle.green, label = "Accept"),
                                    Button(style=ButtonStyle.red, label = "Reject")]
                            ])
                
                def check(res):
                    return res.user == user2
                
                res = await self.client.wait_for("button_click", check=check)
                ynoption = res.component.label
                
                if ynoption == "Accept":
                    yembed = discord.Embed(description=f"**User {ctx.author.mention} Wants To Start A `{rounds}` Round Duel With You.**")
                    yembed.add_field(name="Accept", value="Choose `Accept` To Start")
                    yembed.add_field(name="Reject", value="Choose `Reject` To Reject")
                    yembed.add_field(name="Choice", value =f"> User `{user2}` Accepted `{ctx.author}'s` Request", inline=False)
                    await choice_msg.edit(embed=yembed, components=[])
                    ynchoice = "yes"
                elif ynoption == "Reject":
                    nembed = discord.Embed(description=f"**User {ctx.author.mention} Wants To Start A `{rounds}` Round Duel With You.**")
                    nembed.add_field(name="Accept", value="Choose `Accept` To Start")
                    nembed.add_field(name="Reject", value="Choose `Reject` To Reject")
                    nembed.add_field(name="Choice", value =f"> User `{user2}` Rejected `{ctx.author}'s` Request", inline=False)
                    await choice_msg.edit(embed=nembed, components=[])
                    ynchoice = "no"
                else:
                    error_emb = discord.Embed(description=f"<a:a_cross:860370275275505694> | Error TimedOut Or Invalid Response")
                    await ctx.send(embed=error_emb)
                    
                if ynchoice == "yes":
                    user1_points = 0
                    user2_points = 0
                    i = 0
                    user1 = ctx.message.author
                    ch1 = await user1.create_dm()
                    ch2 = await user2.create_dm()
                    embed = discord.Embed(title="Welcome To The Game Of Rock Paper Scissors", color=0x33cc33)
                    await ch1.send(embed=embed)
                    await ch2.send(embed=embed)
                    
                    
                    
                    while user1_points < rounds and user2_points < rounds:
                        #stone = "<:stone:860391183082455060>"
                        #paper = "<:paper:860391300439080961>"
                        #scissor = "<:scissor:860392433577492500>"
                        
                        emoji_embed = discord.Embed(description="**Emoji Reference**", color=0x33cc33)
                        emoji_embed.add_field(name="Rock", value="Choose <:stone:860391183082455060> For Rock", inline=False)
                        emoji_embed.add_field(name="Paper", value="Choose <:paper:860391300439080961> For Paper", inline=False)
                        emoji_embed.add_field(name="Scissor", value="Choose <:scissor:860392433577492500> For Scissor", inline=False)
                        second_user_turn = discord.Embed(description="**First User's Turn**", color=0x33cc33)
                        reactions = ["<:stone:860391183082455060>", "<:paper:860391300439080961>", "<:scissor:860392433577492500>"]
                        
                        
                        ch1_msg = await ch1.send(embed=emoji_embed)
                        
                        await ch2.send(embed=second_user_turn)
                        
                        for react in reactions:
                            await ch1_msg.add_reaction(react)
                        
                        def check1(reaction, user):
                            return user == ctx.author and reaction.message.id == ch1_msg.id
                        
                        reaction1, user = await self.client.wait_for('reaction_add', check = check1)
                        
                        await ch1.send(f"You Chose {reaction1}")
                            
                            
                        ch2_msg = await ch2.send(embed=emoji_embed)
                        
                        for react in reactions:
                            await ch2_msg.add_reaction(react)
                        
                        def check2(reaction, user):
                            return user == user2 and reaction.message.id == ch2_msg.id
                        
                        reaction2, user = await self.client.wait_for('reaction_add', check=check2)
                        
                        await ch2.send(f'You Chose {reaction2}')
                            

                        r = "<:stone:860391183082455060>"
                        p = "<:paper:860391300439080961>"
                        s = "<:scissor:860392433577492500>"
                        d = "Draw"
                        
                        if str(reaction1) == "<:stone:860391183082455060>":
                            user1_choice = r
                        elif str(reaction1) == "<:paper:860391300439080961>":
                            user1_choice = p
                        elif str(reaction1) == "<:scissor:860392433577492500>":
                            user1_choice = s
                            
                        if str(reaction2) == "<:stone:860391183082455060>":
                            user2_choice = r
                        elif str(reaction2) == "<:paper:860391300439080961>":
                            user2_choice = p
                        elif str(reaction2) == "<:scissor:860392433577492500>":
                            user2_choice = s
                        
                        
                        if user1_choice == r and user2_choice == r:
                            winner = d
                        elif user1_choice == s and user2_choice == s:
                            winner = d
                        elif user1_choice == p and user2_choice == p:
                            winner = d
                        elif user1_choice == r and user2_choice == p:
                            winner = user2
                        elif user1_choice == r and user2_choice == s:
                            winner = user1
                        elif user1_choice == p and user2_choice == s:
                            winner = user2
                        elif user1_choice == p and user2_choice == r:
                            winner = user1
                        elif user1_choice == s and user2_choice == r:
                            winner = user2
                        elif user1_choice == s and user2_choice == p:
                            winner = user1
                        else:
                            pass
                        
                        if winner == user1:
                            user1_points = user1_points + 1
                            winner = winner.mention
                        elif winner == user2:
                            user2_points = user2_points + 1
                            winner = winner.mention
                        else:
                            winner = "None : Draw"
                        
                        i = i + 1
                        
                        winner_embed = discord.Embed(title=f"Round : {i}", color=0xffcc00)
                        winner_embed.add_field(name="Winner", value=f"{winner}", inline=False)
                        winner_embed.add_field(name="Moves", value=f"{user1.mention} : {reaction1} \n{user2.mention} : {reaction2}")
                        winner_embed.add_field(name="Points", value=f"{user1.mention} : {user1_points} \n{user2.mention} : {user2_points}")
                        await ctx.send(embed=winner_embed)
                        await ch1.send(embed=winner_embed)
                        await ch2.send(embed=winner_embed)
                    
                    if user1_points == rounds:
                        game_winner = user1
                    elif user2_points == rounds:
                        game_winner = user2
                    else:
                        pass
                    game_winner_embed = discord.Embed(title="Game Winner", description=game_winner.mention, color=0xff6600)
                    game_winner_embed.add_field(name="Total Scores", value=f"{user1.mention} : {user1_points} \n{user2.mention} : {user2_points}")
                    await ctx.send(embed=game_winner_embed)
                    await ch1.send(embed=game_winner_embed)
                    await ch2.send(embed=game_winner_embed)
                    
                    myquery = { "_id": game_winner.id }
                    if (collection.count_documents(myquery) == 0):
                        post = {"_id": game_winner.id, "game": {"rps" : 1, "ttt" : 0}}
                        collection.insert_one(post)
                    else:
                        query = {"_id": game_winner.id}
                        query2 = {"_id": game_winner.id}
                        queryuser = collection.find(query)
                        queryuser2 = collection.find(query2)
                        for result in queryuser:
                            score = result["game"]["rps"]
                            for result2 in queryuser2:
                                score2 = result2["game"]["ttt"]
                        score = score + 1                	    
                        collection.update_one({"_id":game_winner.id}, {"$set":{"game": {"ttt" : score2, "rps" : score}}})
                    
                elif ynchoice == "no":
                    embed = discord.Embed(description=f"{user2.mention} has rejected your request.")
                    await ctx.send(f"{ctx.author.mention}")
                    await ctx.send(embed=embed)       
        

    '''
    ████████╗██╗░█████╗░  ████████╗░█████╗░░█████╗░  ████████╗░█████╗░███████╗
    ╚══██╔══╝██║██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔════╝
    ░░░██║░░░██║██║░░╚═╝  ░░░██║░░░███████║██║░░╚═╝  ░░░██║░░░██║░░██║█████╗░░
    ░░░██║░░░██║██║░░██╗  ░░░██║░░░██╔══██║██║░░██╗  ░░░██║░░░██║░░██║██╔══╝░░
    ░░░██║░░░██║╚█████╔╝  ░░░██║░░░██║░░██║╚█████╔╝  ░░░██║░░░╚█████╔╝███████╗
    ░░░╚═╝░░░╚═╝░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░░░╚═╝░░░░╚════╝░╚══════╝
    '''

        
    @commands.command()
    async def ttt(self, ctx, user2:discord.Member):
        for i in range(1):
            if user2 == ctx.author or user2.bot == True:
                error_embed = discord.Embed(description=f"<a:a_cross:860370275275505694> | Invalid Mentioned User")
                await ctx.send(embed = error_embed)
                break
                
            else:
                cursor1 = collection.find({"_id" : ctx.author.id}, {"command" : {"$exists": True, "$ne": None }})
                if cursor1.count() > 0:
                    key1_exists = True
                    print("key1_exists")
                else:
                    key1_exists = False
                    print("key2_dont_exists")
                cursor2 = collection.find({"_id" : user2.id}, {"command" : {"$exists": True, "$ne": None }})
                if cursor2.count() > 0:
                    key2_exists = True
                    print("key2_exists")
                else:
                    key2_exists = False
                    print("key2_dont_exists")
                if key1_exists == False:
                    collection.update({"_id": ctx.author.id}, {'$set' : {"command": "none"}})
                    print("Added Command Key To User1")
                else:
                    pass
                if key2_exists == False:
                    collection.update({"_id": user2.id}, {'$set' : {"command": "none"}})
                    print("Added Command Key To User2")
                else:
                    pass    
                
                user1_status = collection.find_one({"_id": ctx.author.id})
                user2_status = collection.find_one({"_id": user2.id})
                
                if user1_status["command"] == "running" or user2_status["command"] == "running":
                    await ctx.send("You Or The Mentioned User Are Currently In A Running Game")
                    break
                else:
                    pass
                
                ynembed = discord.Embed(description=f"**User {ctx.author.mention} Wants To Start A Duel With You.**")
                ynembed.add_field(name="Accept", value="Choose `Accept` To Start")
                ynembed.add_field(name="Reject", value="Choose `Reject` To Reject")
                await ctx.send(f"{user2.mention}")
                            
                choice_msg = await ctx.send(embed=ynembed,
                                            components = [
                                [Button(style=ButtonStyle.green, label = "Accept"),
                                    Button(style=ButtonStyle.red, label = "Reject")]
                            ])
                
                def check(res):
                    return res.user == user2
                
                res = await self.client.wait_for("button_click", check=check)
                ynoption = res.component.label
                
                if ynoption == "Accept":
                    yembed = discord.Embed(description=f"**User {ctx.author.mention} Wants To Start A Duel With You.**")
                    yembed.add_field(name="Accept", value="Choose `Accept` To Start")
                    yembed.add_field(name="Reject", value="Choose `Reject` To Reject")
                    yembed.add_field(name="Choice", value =f"> User `{user2}` Accepted `{ctx.author}'s` Request", inline=False)
                    await choice_msg.edit(embed=yembed, components=[])
                    ynchoice = "yes"
                elif ynoption == "Reject":
                    nembed = discord.Embed(description=f"**User {ctx.author.mention} Wants To Start A   Duel With You.**")
                    nembed.add_field(name="Accept", value="Choose `Accept` To Start")
                    nembed.add_field(name="Reject", value="Choose `Reject` To Reject")
                    nembed.add_field(name="Choice", value =f"> User `{user2}` Rejected `{ctx.author}'s` Request", inline=False)
                    await choice_msg.edit(embed=nembed, components=[])
                    ynchoice = "no"
                else:
                    error_emb = discord.Embed(description=f"<a:a_cross:860370275275505694> | Error TimedOut Or Invalid Response")
                    await ctx.send(embed=error_emb)
                    
                if ynchoice == "yes":
                    running_game_user = [user2, ctx.author]
            
                    for game_user in running_game_user:
                        collection.update({"_id": game_user.id}, {'$set' : {"command": "running"}})
                    o = '🅾'
                    x = '❌'
                    #bl = '⬜'
                    a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = '⬜'
                    e = '⬜'
                    #blank space = "ㅤ"
                    startembed = discord.Embed(description=
                                            f'''{a1}ㅤ\t{a2}ㅤ\t{a3} \n \n{b1}ㅤ\t{b2}ㅤ\t{b3} \n \n{c1}ㅤ\t{c2}ㅤ\t{c3}''')
                    embedmsg = await ctx.send(embed=startembed)
                    
                    
                    
                    users = [ctx.author, user2]
                    firstuser = random.choice(users)
                    if firstuser == ctx.author:
                        seconduser = user2
                    else:
                        seconduser = ctx.author
                    
                    def check2(msg):
                        return msg.author == seconduser and msg.channel == ctx.channel
                    def check1(msg):
                        return msg.author == firstuser and msg.channel == ctx.channel
                            
                        
                    
                    i = 1
                    while i < 10:
                        if (i % 2) == 0: 
                        
                            option_msg = await ctx.send(f"**Choose Option {seconduser.mention}**")
                        
                            msg = await self.client.wait_for("message", check=check2)
                            
                            options = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
                                
                            if msg.content in options:
                                if msg.content == "a1":
                                    if a1 == o or a1 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        a1 = x
                                elif msg.content == "a2":
                                    if a2 == o or a2 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        a2 = x
                                elif msg.content == "a3":
                                    if a3 == o or a3 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        a3 = x
                                elif msg.content == "b1":
                                    if b1 == o or b1 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        b1 = x
                                elif msg.content == "b2":
                                    if b2 == o or b2 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        b2 = x
                                elif msg.content == "b3":
                                    if b3 == o or b3 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        b3 = x
                                elif msg.content == "c1":
                                    if c1 == o or c1 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        c1 = x
                                elif msg.content == "c2":
                                    if c2 == o or c2 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        c2 = x
                                elif msg.content == "c3":
                                    if c3 == o or c3 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        c3 = x
                                embed = discord.Embed(description="") 
                                new_embed = discord.Embed(description=f" {a1}ㅤ{a2}ㅤ{a3} \n \n{b1}ㅤ{b2}ㅤ{b3} \n \n{c1}ㅤ{c2}ㅤ{c3}")
                                await embedmsg.edit(embed=new_embed)  
                                await msg.delete()
                                await option_msg.delete()
                                line_list = [{a1, a2, a3}, {b1, b2, b3}, {c1, c2, c3}, {a1, b1, c1}, {a2, b2, c2}, {a3, b3, c3}, {a1, b2, c3}, {a3, b2, c1}]
                                if any( all(elem == x for elem in elements) or all(elem == o for elem in elements) for elements in line_list):
                                    game_winner = seconduser
                                    break
                                i = i + 1
                                
                            elif msg.content == "end":
                                break
                            
                            else:
                                await ctx.send("**Invalid Option**")
                                continue
                        else:
                            option_msg = await ctx.send(f"**Choose Option {firstuser.mention}**")
                        
                            msg = await self.client.wait_for("message", check=check1)
                            
                            options = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
                            if msg.content in options:
                                if msg.content == "a1":
                                    if a1 == o or a1 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        a1 = o
                                elif msg.content == "a2":
                                    if a2 == o or a2 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        a2 = o
                                elif msg.content == "a3":
                                    if a3 == o or a3 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        a3 = o
                                elif msg.content == "b1":
                                    if b1 == o or b1 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        b1 = o
                                elif msg.content == "b2":
                                    if b2 == o or b2 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        b2 = o
                                elif msg.content == "b3":
                                    if b3 == o or b3 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        b3 = o
                                elif msg.content == "c1":
                                    if c1 == o or c1 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        c1 = o
                                elif msg.content == "c2":
                                    if c2 == o or c2 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        c2 = o
                                elif msg.content == "c3":
                                    if c3 == o or c3 == x:
                                        await ctx.send("**Position Already Posseded**")
                                        i = i - 1
                                    else:
                                        c3 = o
                                embed = discord.Embed(description="") 
                                new_embed = discord.Embed(description=f" {a1}ㅤ{a2}ㅤ{a3} \n \n{b1}ㅤ{b2}ㅤ{b3} \n \n{c1}ㅤ{c2}ㅤ{c3}")
                                await embedmsg.edit(embed=new_embed)  
                                await msg.delete()
                                await option_msg.delete()
                                line_list = [{a1, a2, a3}, {b1, b2, b3}, {c1, c2, c3}, {a1, b1, c1}, {a2, b2, c2}, {a3, b3, c3}, {a1, b2, c3}, {a3, b2, c1}]
                                if any( all(elem == x for elem in elements) or all(elem == o for elem in elements) for elements in line_list):
                                    game_winner = firstuser
                                    break
                                i = i + 1
                            elif msg.content == "end":
                                break
                            else:
                                await ctx.send("**Invalid Option**")
                                continue
                    await ctx.send("**Game Ended!**")
                    game_winner_embed = discord.Embed(title="Game Winner", description=game_winner.mention, color=0xff6600)
                    await ctx.send(embed=game_winner_embed)
                    running_game_user2 = [ctx.author, user2] 
                    for game_user2 in running_game_user2:
                        collection.update({"_id": game_user2.id}, {'$set' : {"command": "none"}})
                    myquery = { "_id": game_winner.id }
                    if (collection.count_documents(myquery) == 0):
                        post = {"_id": game_winner.id, "game": {"rps" : 0, "ttt" : 1}}
                        collection.insert_one(post)
                    else:
                        query = {"_id": game_winner.id}
                        query2 = {"_id": game_winner.id}
                        queryuser = collection.find(query)
                        queryuser2 = collection.find(query2)
                        for result in queryuser:
                            score = result["game"]["ttt"]
                            for result2 in queryuser2:
                                score2 = result2["game"]["rps"]
                        score = score + 1                	    
                        collection.update_one({"_id":game_winner.id}, {"$set":{"game": {"ttt" : score, "rps" : score2}}})
                        await ctx.send("`Updated Score`")
                    
                    
                elif ynchoice == "no":
                    embed = discord.Embed(description=f"{user2.mention} has rejected your request.")
                    await ctx.send(f"{ctx.author.mention}")
                    await ctx.send(embed=embed)
        

    '''
    ██████╗░██████╗░░█████╗░███████╗██╗██╗░░░░░███████╗
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║██║░░░░░██╔════╝
    ██████╔╝██████╔╝██║░░██║█████╗░░██║██║░░░░░█████╗░░
    ██╔═══╝░██╔══██╗██║░░██║██╔══╝░░██║██║░░░░░██╔══╝░░
    ██║░░░░░██║░░██║╚█████╔╝██║░░░░░██║███████╗███████╗
    ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚══════╝
    '''

    @commands.command()
    async def open(self, ctx):
        user = ctx.author
        myquery = { "_id": user.id}
        if (collection.count_documents(myquery) == 0):
            post = {"_id": user.id, "game": {"ttt" : 0, "rps" : 0}, "command" : "none"}
            collection.insert_one(post)
            embed = discord.Embed(description=f"<a:a_tick:862961041788764161> Score Account Successfully Created\nUse `!profile` Or `!pr` To Check Your Score Account")
        else:
            embed = discord.Embed(description=f"<a:a_cross:860370275275505694> You Already Have A Score Account\nUse `!profile` Or `!pr` To Check Your Score Account")
        await ctx.send(embed=embed)



    @commands.command(alias = "pr")
    async def profile(self, ctx):
        user = ctx.author
        pfp = user.avatar_url
        embed = discord.Embed(title="User Profile", description=f"{user.mention} | `{user}`", color=0x33cc33)
        
        embed.set_thumbnail(url=pfp)
        
        for i in range(1):
            myquery = { "_id": user.id }
            if (collection.count_documents(myquery) == 0):
                ttt_data = "`Play And Win Some Games To Start Logging Score` Or Use `!open` To Start A New Score Account"
                rps_data = "`Play And Win Some Games To Start Logging Score` Or Use `!open` To Start A New Score Account"
            else:
                query = {"_id": user.id}
                user = collection.find(query)
                for result in user:
                    score = result["game"]["rps"]
                    score2 = result["game"]["ttt"]
                    rps_data = int(score)
                    ttt_data = int(score2)
                    
                    
            embed.add_field(name="Tic Tac Toe Wins", value=f"{ttt_data}")
            embed.add_field(name="Rock Paper Scissors Wins", value=f"{rps_data}", inline=False)
            await ctx.send(embed=embed)
        
    @commands.command()
    async def end(self, ctx):
        user = ctx.author
        collection.update({"_id": user.id}, {'$set' : {"command": "none"}})
        embed = discord.Embed(description=f"<a:a_tick:862961041788764161> Ended Any Left Over Games {user.mention}")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def invite(ctx):
        embed = discord.Embed(description="[Invite]()")
        await ctx.send(embed=embed)
      
async def setup(client):
    await client.add_cog(Games(client))
