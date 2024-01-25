from rich.table import Table
from match import Match
from rich.console import Console
console = Console()


class Team:

    def __init__(self, name, playersPool):

        self.name = name
        self.playersPool = playersPool
        self.rankingPoints = 0
        self.matchesWon = 0
        self.matchesDrawn = 0
        self.matchesLost = 0
        self.totalScored = 0
        self.totalConceded = 0


    def rankingPointsIncrementandMatchCount(self, result): 

        if result == "Draw":

            self.rankingPoints += 1
            self.matchesDrawn += 1

        elif result == "Win":

            self.rankingPoints += 3
            self.matchesWon += 1

        elif result == "Lose":

            self.matchesLost += 1


    def rankingPointsGetter(self):

        return self.rankingPoints
    

    def totalGoalsScored(self):
         
        self.totalScored += 1


    def totalGoalsConceded(self):
         
        self.totalConceded += 1


    @staticmethod
    def generateFixtures(allTeams): 

        allFixtures = []

        for roundNum in range(2):
        
            for i in range(len(allTeams)):

                for j in range(i + 1, len(allTeams)):
                        
                        match = Match(allTeams[i], allTeams[j])

                        if roundNum == 1:
                                match = Match(allTeams[j], allTeams[i])

                        allFixtures.append(match)

        return allFixtures
    

    @staticmethod
    def rankingsTable(allTeams):
                  
            table = Table(title="ENGLISH PREMIER LEAGUE", caption="SEASON 2023/24", expand=True, show_lines=True)

            table.add_column("Pos", justify="center", style="grey50")
            table.add_column("Club", justify="center", style="blue")
            table.add_column("W", justify="center", style="cyan2")
            table.add_column("D", justify="center", style="cyan2")
            table.add_column("L", justify="center", style="cyan2")
            table.add_column("Goals", justify="center", style="cyan2")
            table.add_column("GD", justify="center", style="cyan2")
            table.add_column("Pts", justify="center", style="cyan2")

            sortedTeams = sorted(allTeams, key=lambda x: (x.rankingPoints, x.totalScored - x.totalConceded), reverse=True)

            for index, team in enumerate(sortedTeams, start=1):

                goals = f"{team.totalScored}:{team.totalConceded}"
                goalDifference = f"{team.totalScored - team.totalConceded}"
                
                table.add_row(str(index), team.name, str(team.matchesWon), str(team.matchesDrawn), str(team.matchesLost), goals, goalDifference, str(team.rankingPointsGetter()))

            console.print(table)