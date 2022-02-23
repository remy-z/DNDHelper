import json
class PlayerInfo:
    
    def __init__(self):
        self.playerInfo = {}
        userFile = open("data/user/userFile.json", "r", encoding = "utf-8")
        self.playerInfo = (json.load(userFile))

    def storeLast(self, ctx):
        guild, author, command, message = ctx.guild(), ctx.author(), ctx.command(), ctx.message()
        if ctx.guild() not in self.playerInfo:
            self.playerInfo[guild] = {}
        if ctx.author() not in self.playerInfo[guild]:
            self.playerInfo[guild][author] = {}
        self.playerInfo[guild][author]["last"] = (command, message)

    
    def setMacro(self, ctx):
        message = ""
        guild, author, command, message = ctx.guild(), ctx.author(), ctx.command(), ctx.message()
        if ctx.guild() not in self.playerInfo:
            self.playerInfo[guild] = {}
        if ctx.author() not in self.playerInfo[guild]:
            self.playerInfo[guild][author] = {}
        if "activeChar" not in self.playerInfo[guild][author]:
            return "No active character, use the '!newChar' command to create a character"
        macro = message.split(',')
        self.playerInfo[guild][author][command] = macro