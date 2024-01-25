import random
from rich.console import Console
console = Console()
from itertools import zip_longest


class Match:

    def __init__(self, teamA, teamB):

        self.teamA = teamA
        self.teamB = teamB
        self.winner = None 
        self.teamAGoals = []
        self.teamBGoals = [] 


    def playMatch(self): 

        numGoals = random.randint(0, 5)
        
        for i in range(numGoals): 

            teamScoring = random.choice([self.teamA, self.teamB]) 

            eligible_players = list(filter(lambda x: x.position != "Goalkeeper", teamScoring.playersPool))

            playerScoring = random.choices(eligible_players, [0.5,0.5,0.5,0.3,0.3,0.3,0.2,0.2,0.2,0.2])[0]

            playerScoring.totalGoalsinSeason() 

            if teamScoring == self.teamA:

                self.teamAGoals.append(playerScoring) 
                self.teamA.totalGoalsScored()
                self.teamB.totalGoalsConceded()

            elif teamScoring == self.teamB:

                self.teamBGoals.append(playerScoring)
                self.teamB.totalGoalsScored()
                self.teamA.totalGoalsConceded()

        if len(self.teamAGoals) == 0:

            for player in self.teamA.playersPool:

                if player.position == "Goalkeeper":

                    player.totalCleanSheets()

        if len(self.teamBGoals) == 0:

            for player in self.teamB.playersPool:

                if player.position == "Goalkeeper":

                    player.totalCleanSheets()

        self.setWinner()


    def setWinner(self):
        
        if len(self.teamAGoals) > len(self.teamBGoals):

            self.winner = self.teamA

            self.teamA.rankingPointsIncrementandMatchCount("Win")
            self.teamB.rankingPointsIncrementandMatchCount("Lose")

        elif len(self.teamBGoals) > len(self.teamAGoals): 

            self.winner = self.teamB

            self.teamB.rankingPointsIncrementandMatchCount("Win")
            self.teamA.rankingPointsIncrementandMatchCount("Lose")

        elif len(self.teamBGoals) == len(self.teamAGoals):

            self.teamA.rankingPointsIncrementandMatchCount("Draw")
            self.teamB.rankingPointsIncrementandMatchCount("Draw")
            
            
    def matchStats(self):

        console.print("[bold]{:>95} {:>10} - {:<10} {:<95}[/]".format(self.teamA.name, len(self.teamAGoals), len(self.teamBGoals), self.teamB.name))
        print()

        for aPlayer, bPlayer in zip_longest(self.teamAGoals, self.teamBGoals, fillvalue = ''):

            if aPlayer == '':
                withEmoji = f"{bPlayer.name} ⚽"
                print(f"{withEmoji:>127}") 
                print()

            elif bPlayer == '':
                withEmoji = f"{aPlayer.name} ⚽"
                print(f"{withEmoji:>95}")
                print()

            else:
                withEmojiA = f"{aPlayer.name} ⚽"
                withEmojiB = f"{bPlayer.name} ⚽"
                print("{:>95} {:>30}".format(withEmojiA, withEmojiB))
                print()