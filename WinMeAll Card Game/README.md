# Win_Me_All_Card_Game
This folder contains the "WinMeAll" game project which is developed using Python programming language.

                                                        
PROJECT  DESCRIPTION
---------------------

“WinMeAll” is a simple card game based on the famous “War” game which can be played by two players using the standard deck of cards.
Objective
The objective of this game is to win and collect all the cards. 
Gameplay:
1.	The deck of cards will be divided evenly among the players giving each one of them facing down. Hence players do not look at their cards as they remain facedown in a pile.
2.	Each player has to pick their top card from their pack of cards and flip it over– this is called a “Battle” – and the player with the higher card wins the Battle, takes all the played cards, and puts to the bottom in his/her pile.
3.	The cards are ranked with Ace being the highest and 2 being the lowest. 
4.	If all the played cards in a Battle are equal, then it is called a “War”.Both the players then place the next card of their pile face down and then another card face up. 

The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.

If a player runs out of the cards during a War, then that player immediately loses the game. 
Technical  Specifications
1.	To construct this game, the below classes are created along with the game logic:
    •	Card class: This class is required to hold the entities or attributes of a single card like its suit, rank, and value. 
    •	Deck class: This class will be constructed as an instance of the “Card” class.
    •	Player class: This class will represent a player that will be used to hold a card or to hold half a deck of cards.
2.	After the creation of the above listed classes, we will be instantiating them to perform the game logic. 
3.	In this game’s initial version, there will not be any human player instead the game will be simulated among the two computer players. In future releases, the human player    feature will be added.

