from .. import loader
import logging, random

logger = logging.getLogger(__name__)

def register(cb):
    cb(InsultMod())


class InsultMod(loader.Module):
    """Shouts at people"""
    def __init__(self):
        self.commands = {'insult':self.insultcmd}
        self.config = {}
        self.name = "Insulter"

    async def insultcmd(self, message):
        adjectives_start = ["salty", "fat", "fucking", "shitty", "stupid", "retarded"]
        adjectives_mid = ["little", ""]
        nouns = ["cunt", "pig", "pedophile", "alpha male", "retard", "ass licker"]
        starts = ["You're a", "You"]
        ends = ["!!!!", "!", ""]
        start = random.choice(starts)
        adjective_start = random.choice(adjectives_start)
        adjective_mid = random.choice(adjectives_mid)
        noun = random.choice(nouns)
        end = random.choice(ends)
        insult = start + " " + adjective_start + " " + adjective_mid + (" " if adjective_mid else "") + noun + end
        logger.debug(insult)
        await message.edit(insult)
