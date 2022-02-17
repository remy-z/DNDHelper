class Format:  
    def __init__(self) -> None:
        pass

    #takes a list of tuples rolls, in the format (roll total, list with all individual rolls and modifer as last argument, intial argument)
    def roll(self, rolls):
        message = ""
        total = 0
        for r in rolls:
            total += r[0]
            message += f"     {r[2]} : {str(r[1][:-1])}"
            if r[1][-1] != 0:
                message += r[1][-1]
            message +=  f" = **{r[0]}**"
            message += "\n"
        message = f">>> Total: **{total}** \n" + message
        return message

    def info(self, name, info):
        body = ""
        for line in info["entries"]:
            body += line + "\n"
        return f">>> {name} \n {body}"