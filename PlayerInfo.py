class PlayerInfo:
    
    def __init__(self):
        self.playerInfo = {}

    def storeLast(self, ctx):
        guild, author, command, message = ctx.guild(), ctx.author(), ctx.command(), ctx.message()
        if ctx.guild() not in self.playerInfo:
            self.playerInfo[guild] = {}
        if ctx.author() not in self.playerInfo[guild]:
            self.playerInfo[guild][author] = {}
        self.playerInfo[guild][author]["last"] = (command, message)