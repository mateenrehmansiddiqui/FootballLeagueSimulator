from team import Team
from player import Player
from rich.console import Console

console = Console()



manchesterCityPlayerPool = [
          Player("Haaland", 9, "Striker", "Manchester City"),
          Player("Grealish", 10, "Striker", "Manchester City"),
          Player("Foden", 47, "Striker", "Manchester City"),
          Player("Silva", 20, "Midfielder", "Manchester City"),
          Player("De Bruyne", 17, "Midfielder", "Manchester City"),
          Player("Rodri", 16, "Midfielder", "Manchester City"),
          Player("Walker", 2, "Defender", "Manchester City"),
          Player("Dias", 3, "Defender", "Manchester City"),
          Player("Stones", 5, "Defender", "Manchester City"),
          Player("Akanji", 25, "Defender", "Manchester City"),
          Player("Ederson", 31, "Goalkeeper", "Manchester City"),

]

teamManchesterCity = Team("Manchester City", manchesterCityPlayerPool)


arsenalPlayerPool = [
          Player("Jesus", 9, "Striker", "Arsenal"),
          Player("Saka", 7, "Striker", "Arsenal"),
          Player("Martinelli", 11, "Striker", "Arsenal"),
          Player("Odegaard", 8, "Midfielder", "Arsenal"),
          Player("Havertz", 29, "Midfielder", "Arsenal"),
          Player("Rice", 41, "Midfielder", "Arsenal"),
          Player("Gabriel", 6, "Defender", "Arsenal"),
          Player("Saliba", 2, "Defender", "Arsenal"),
          Player("White", 4, "Defender", "Arsenal"),
          Player("Zinchenko", 35, "Defender", "Arsenal"),
          Player("Ramsdale", 1, "Goalkeeper", "Arsenal"),

]

teamArsenal = Team("Arsenal", arsenalPlayerPool)


manchesterUnitedPlayerPool = [
          Player("Rashford", 10, "Striker", "Manchester United"),
          Player("Garnacho", 17, "Striker", "Manchester United"),
          Player("Antony", 21, "Striker", "Manchester United"),
          Player("Fernandes", 8, "Midfielder", "Manchester United"),
          Player("Eriksen", 14, "Midfielder", "Manchester United"),
          Player("Casemiro", 18, "Midfielder", "Manchester United"),
          Player("Varane", 19, "Defender", "Manchester United"),
          Player("Wan-Bissaka", 29, "Defender", "Manchester United"),
          Player("Dalot", 20, "Defender", "Manchester United"),
          Player("Maguire", 5, "Defender", "Manchester United"),
          Player("Onana", 24, "Goalkeeper", "Manchester United"),

]

teamManchesterUnited = Team("Manchester United", manchesterUnitedPlayerPool)


liverpoolPlayerPool = [
          Player("Salah", 11, "Striker", "Liverpool"),
          Player("Nunez", 9, "Striker", "Liverpool"),
          Player("Gakpo", 18, "Striker", "Liverpool"),
          Player("Elliot", 19, "Midfielder", "Liverpool"),
          Player("Szoboszlai", 8, "Midfielder", "Liverpool"),
          Player("Mac Allister", 10, "Midfielder", "Liverpool"),
          Player("Alexander-Arnold", 66, "Defender", "Liverpool"),
          Player("Van Dijk", 4, "Defender", "Liverpool"),
          Player("Konate", 5, "Defender", "Liverpool"),
          Player("Robertson", 26, "Defender", "Liverpool"),
          Player("Alisson", 1, "Goalkeeper", "Liverpool"),

]

teamLiverpool = Team("Liverpool", liverpoolPlayerPool)


chelseaPlayerPool = [
          Player("Nkunku", 18, "Striker", "Chelsea"),
          Player("Sterling", 7, "Striker", "Chelsea"),
          Player("Palmer", 20, "Striker", "Chelsea"),
          Player("Gallagher", 23, "Midfielder", "Chelsea"),
          Player("Mudryk", 10, "Midfielder", "Chelsea"),
          Player("Fernandez", 8, "Midfielder", "Chelsea"),
          Player("Chilwell", 21, "Defender", "Chelsea"),
          Player("Fofana", 33, "Defender", "Chelsea"),
          Player("James", 24, "Defender", "Chelsea"),
          Player("Thiago Silva", 6, "Defender", "Chelsea"),
          Player("Petrovic", 28, "Goalkeeper", "Chelsea"),

]

teamChealsea = Team("Chelsea", chelseaPlayerPool)


tottenhamHotspurPlayerPool = [
          Player("Son Heung-min", 7, "Striker", "Tottenham Hotspur"),
          Player("Richarlison", 9, "Striker", "Tottenham Hotspur"),
          Player("Perisic", 14, "Striker", "Tottenham Hotspur"),
          Player("Maddison", 10, "Midfielder", "Tottenham Hotspur"),
          Player("Lo Celso", 18, "Midfielder", "Tottenham Hotspur"),
          Player("Kulusevski", 21, "Midfielder", "Tottenham Hotspur"),
          Player("Dier", 15, "Defender", "Tottenham Hotspur"),
          Player("Romero", 17, "Defender", "Tottenham Hotspur"),
          Player("Porro", 23, "Defender", "Tottenham Hotspur"),
          Player("Davies", 33, "Defender", "Tottenham Hotspur"),
          Player("Lloris", 1, "Goalkeeper", "Tottenham Hotspur"),

]

teamTottenhamHotspur = Team("Tottenham Hotspur", tottenhamHotspurPlayerPool)




allTeams = [teamManchesterCity, teamArsenal, teamManchesterUnited, teamLiverpool, teamChealsea, teamTottenhamHotspur]

fixturesList = Team.generateFixtures(allTeams)

for match in fixturesList:
     match.playMatch()

for team in allTeams:

     for player in team.playersPool:

          player.generatePlayerStats()



while True:

     print("""\nWelcome to the Football League Simulation System! Select any one of the following options: 
           
1. View Leaderboard
2. View a Match
3. View a Team's Matches
4. View a Player's Stats
5. Player vs Player Comparison
6. Exit""")
     
     option = input(("\nOption: "))

     if option == "1":

          Team.rankingsTable(allTeams) #static method
          print("\n\n\n")

     elif option == "2":

          home = input("\nHome Team: ")
          away = input("\nAway Team: ")

          for match in fixturesList:

               if match.teamA.name == home.title() and match.teamB.name == away.title():
                    
                    print()
                    match.matchStats()
                    print()
                    print()
                    break

          else:

               print("\nYou entered an incorrect team name. Please try again.")



     elif option == "3":

          team = input("\nTeam: ")
          type = input("\nEnter 'H' for Home Matches, 'A' for Away Matches, 'B' for Both: ")

          if type.title() == "H":

               for match in fixturesList:

                    if match.teamA.name == team.title():

                         print()
                         match.matchStats()
                         print()
                         print()

          elif type.title() == "A":

               for match in fixturesList:

                    if match.teamB.name == team.title():

                         print()
                         match.matchStats()
                         print()
                         print()

          elif type.title() == "B": 

               for match in fixturesList:

                    if match.teamA.name == team.title() or match.teamB.name == team.title():

                         print()
                         match.matchStats()
                         print()
                         print()

          else:
               print("\nPlease enter a valid option.")


     elif option == "4":

          type = input("\nEnter 'N' to search a player by name, 'T' to search by team, 'P' to search by position: ")

          if type.title() == "N":

               playerName = input("\nEnter the player's name: ")

               for team in allTeams:

                    for player in team.playersPool:

                         if player.name == playerName.title():

                              player.displayIndividualPlayerStats()


          elif type.title() == "T":

               teamName = input("\nEnter the team's name: ")

               capitalisedTeamName = teamName.title()

               Player.playerPanelsbyTeam(allTeams, capitalisedTeamName)        

               playerName = input("\nEnter the player's name: ")

               for team in allTeams:

                    for player in team.playersPool:

                         if player.name == playerName.title():

                              player.displayIndividualPlayerStats()


          elif type.title() == "P":
               
               positionName = input("\nEnter the player's position: ")

               capitalisedPosition = positionName.title()
       
               Player.playerPanelsbyPosition(allTeams, capitalisedPosition)

               playerName = input("\nEnter the player's name: ")

               for team in allTeams:

                    for player in team.playersPool:

                         if player.name == playerName.title():

                              player.displayIndividualPlayerStats()

          else:
               print("\nPlease enter a valid option.\n") 


     elif option == "5":

          while True:

               type = input("\nEnter 'N' to search by name, 'T' to search by team, 'P' to search by position: ")

               if type.title() == "N":

                    p1Name = input("\nEnter the first player's name: ")
                    p2Name = input("\nEnter the second player's name: ")

                    for team in allTeams:

                         for player in team.playersPool:

                              if player.name == p1Name.title():

                                   player1 = player

                              elif player.name == p2Name.title():

                                   player2 = player

                    Player.comparePlayers(player1, player2)
                    break

               elif type.title() == "T":

                    teamName = input("\nEnter the first team's name: ")

                    capitalisedTeamName = teamName.title() 

                    Player.playerPanelsbyTeam(allTeams, capitalisedTeamName)

                    playerName = input("\nEnter the first player's name: ")

                    for team in allTeams:

                         for player in team.playersPool:

                              if player.name == playerName.title():

                                   player1 = player


                    teamName = input("\nEnter the second team's name: ")

                    capitalisedTeamName = teamName.title()                     

                    Player.playerPanelsbyTeam(allTeams, capitalisedTeamName)

                    playerName = input("\nEnter the second player's name: \n")

                    for team in allTeams:

                         for player in team.playersPool:

                              if player.name == playerName.title():

                                   player2 = player

                    Player.comparePlayers(player1, player2)

                    break
               
               elif type.title() == "P":
                    
                    positionName = input("\nEnter the first player's position: ")

                    capitalisedPositionName = positionName.title()
          
                    Player.playerPanelsbyPosition(allTeams, capitalisedPositionName)

                    playerName = input("\nEnter the first player's name: ")

                    for team in allTeams:

                         for player in team.playersPool:

                              if player.name == playerName.title():

                                   player1 = player

                    positionName = input("\nEnter the second player's position: ")

                    capitalisedPositionName = positionName.title()
          
                    Player.playerPanelsbyPosition(allTeams, capitalisedPositionName)

                    playerName = input("\nEnter the second player's name: ")

                    for team in allTeams:

                         for player in team.playersPool:

                              if player.name == playerName.title():

                                   player2 = player

                    Player.comparePlayers(player1, player2)

                    break

               else:
                    print("\nPlease enter either 'N', 'T' or 'P'.") 
          

     elif option == "6":
          exit()

     else:
          print("\nPlease enter a valid option.\n")