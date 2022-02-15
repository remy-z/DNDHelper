class Format:  
    def __init__(self) -> None:
        pass

    #takes a list of tuples rolls, with the roll result in index 0 and a string for the roll info in index 1
    def roll(self, rolls):
        message = ""
        total = 0
        for r in rolls:
            total += r[0]
            message += f"     {str(r[0])} : {str(r[1][:-1])}"
            if r[1][-1] != 0:
                message += r[1][-1]
            message += "\n"
        message = "```" + f"Total: {total} \n" + message + "```"
        return message

    def info(self, name, info):
        body = ""
        for line in info["entries"]:
            body += line + "\n"
        return f"```{name} \n {body}```"