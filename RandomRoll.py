import discord
import random

class RandomRoll(discord.Client):

    def getRolls(self, words):
        rolls = []
        for word in words:
            roll = []
            sumOfDie = 0
            rollChar = word.split("d");
            numberOfDice = int(rollChar[0])
            sidesOfDie = int(rollChar[1])
            for i in range(numberOfDice):
                randomNumber = random.randint(1,sidesOfDie)
                roll.append(str(randomNumber))
                sumOfDie += randomNumber
            rolls.append(",".join(roll) + ";" + str(sumOfDie))
        return rolls

    async def on_message(self, messageSent):
        # Check whether this is a bot command
        if messageSent.content[0:5] == "\\roll":
            # Do the roll ...
            # Each word after command is code for a roll - number of dice of given type
            words = messageSent.content.split()
            rolls = self.getRolls(words[1:])
            for roll in rolls:
                await messageSent.channel.send(content=roll)
