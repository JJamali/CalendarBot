import discord
from discord.ext import commands


class Deadlines(commands.Cog):
    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello!')

    @commands.command(name='new')
    async def new_deadline(self, ctx, argument):
        print(argument)
        department, course_num, name, due_date = argument.split(',')
        guild_id = ctx.message.guild.id

        self.insert_deadline(guild_id, department, course_num, name, due_date)
        print('done')

    def insert_deadline(self, guild_id, department, course_num, name, due_date):
        self.cursor.execute("INSERT INTO deadlines VALUES("
                            "%s, %s, %s, %s, %s"
                            ")", (guild_id, department, course_num, name, due_date))
        self.db.commit()