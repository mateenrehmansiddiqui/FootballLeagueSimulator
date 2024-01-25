import random
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns 
console = Console() 


class Player:

    def __init__(self, name, jerseyNumber, position, team):

        self.name = name
        self.jerseyNumber = jerseyNumber
        self.position = position
        self.team = team
        self.totalGoals = 0   
        self.cleanSheets = 0
        self.shotAccuracy = 0
        self.passAccuracy = 0
        self.successfulBlocks = 0
        self.totalSaves = 0
        self.yellowCards = 0
        self.redCards = 0


    def totalGoalsinSeason(self):

        self.totalGoals += 1


    def totalCleanSheets(self):

        self.cleanSheets += 1


    def shotAccuracySetter(self):

        if self.position == "Striker":

            self.shotAccuracy = round(random.uniform(63, 95), 1)
        
        elif self.position == "Defender":

            self.shotAccuracy = round(random.uniform(49, 75), 1)

        elif self.position == "Midfielder":

            self.shotAccuracy = round(random.uniform(65, 97), 1)


    def passAccuracySetter(self):

        if self.position == "Striker":

            self.passAccuracy = round(random.uniform(77, 95), 1)
        
        elif self.position == "Defender":

            self.passAccuracy = round(random.uniform(60, 70), 1)

        elif self.position == "Midfielder":

            self.passAccuracy = round(random.uniform(80, 97), 1)

        elif self.position == "Goalkeeper":

            self.passAccuracy = round(random.uniform(58, 73), 1)


    def successfulBlocksSetter(self):

        if self.position == "Striker":

            self.successfulBlocks = random.randint(4, 7)
        
        elif self.position == "Defender":

            self.successfulBlocks = random.randint(12, 18)

        elif self.position == "Midfielder":

            self.successfulBlocks = random.randint(1, 4)


    def totalSavesSetter(self):

        if self.position == "Goalkeeper":

            self.totalSaves = random.randint(13, 23)
    

    def yellowCardsSetter(self):

        self.yellowCards = random.randint(0, 2)


    def redCardsSetter(self):

        self.redCards = random.randint(0, 1)  


    def generatePlayerStats(self):
        
        self.shotAccuracySetter()
        self.passAccuracySetter()
        self.successfulBlocksSetter()
        self.totalSavesSetter()
        self.yellowCardsSetter()
        self.redCardsSetter()
  

    def displayIndividualPlayerStats(self):

        console.print(f"\n[bold][italic]{self.name}[/] | [italic][cyan2]{self.jerseyNumber}[/][/] | [italic]{self.position}[/] | [italic][blue]{self.team}[/][/][/]\n\n")
        console.print(f"[grey50][bold]Total Goals:[/][/][turquoise2]{self.totalGoals:>13}[/]\n")
        console.print(f"[grey50][bold]Shot Accuracy:[/][/][turquoise2]{self.shotAccuracy:>11}%[/]\n") 
        console.print(f"[grey50][bold]Pass Accuracy:[/][/][turquoise2]{self.passAccuracy:>14}%[/]\n")
        console.print(f"[grey50][bold]Successful Blocks:[/][turquoise2]{self.successfulBlocks:>7}[/]\n")
        console.print(f"[grey50][bold]Clean Sheets:[/][/][turquoise2]{self.cleanSheets:>12}[/]\n")
        console.print(f"[grey50][bold]Total Saves:[/][/][turquoise2]{self.totalSaves:>14}[/]\n")
        console.print(f"[grey50][bold]Yellow Cards:[/][/][turquoise2]{self.yellowCards:>12}[/]\n")
        console.print(f"[grey50][bold]Red Cards:[/][/][turquoise2]{self.redCards:>15}[/]\n")


    @staticmethod
    def comparePlayers(player1, player2):
       
        table = Table(expand=True, show_lines=True)

        table.add_column(f"[italic]{player1.name.upper()}[/] | [italic][cyan2]{player1.jerseyNumber}[/][/] | [italic]{player1.position.upper()}[/] | [italic][blue]{player1.team.upper()}[/][/]", justify="center", style="turquoise2")

        table.add_column("[italic][bold]PLAYER COMPARISON[/][/] | [bold][italic]SEASON 2023/24[/][/]", justify="center", style="grey50") 
        table.add_column(f"[italic]{player2.name.upper()}[/] | [italic][cyan2]{player2.jerseyNumber}[/][/] | [italic]{player2.position.upper()}[/] | [italic][blue]{player2.team.upper()}[/][/]", justify="center", style="turquoise2")

        table.add_row(str(player1.totalGoals), "Goals", str(player2.totalGoals))
        table.add_row(f"{str(player1.shotAccuracy)}%", "Shot Accuracy", f"{str(player2.shotAccuracy)}%")
        table.add_row(f"{str(player1.passAccuracy)}%", "Pass Accuracy", f"{str(player2.passAccuracy)}%")
        table.add_row(str(player1.successfulBlocks), "Successful Blocks", str(player2.successfulBlocks))
        table.add_row(str(player1.cleanSheets), "Clean Sheets", str(player2.cleanSheets))
        table.add_row(str(player1.totalSaves), "Total Saves", str(player2.totalSaves))
        table.add_row(str(player1.yellowCards), "[bright_yellow]Yellow Cards[/]", str(player2.yellowCards))
        table.add_row(str(player1.redCards), "[bright_red]Red Cards[/]", str(player2.redCards))

        console.print(table)

        
    @staticmethod
    def playerPanelsbyTeam(allTeams, teamName):

        allPanels = []

        for team in allTeams:

            if teamName.title() == team.name:

                for player in team.playersPool:

                    allPanels.append(Panel(f"{player.name} | {player.jerseyNumber}\n{player.position}"))

                console.print(Columns(allPanels, expand=True)) 


    @staticmethod
    def playerPanelsbyPosition(allTeams, positionName):

        allPanels = []

        for team in allTeams:

            for player in team.playersPool:

                if positionName.title() == player.position:

                    allPanels.append(Panel(f"{player.name} | {player.jerseyNumber}\n{player.team}"))
               
        console.print(Columns(allPanels, expand=True))