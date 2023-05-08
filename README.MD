Nines on the Terminal
=====================

This project is meant to be a simple, small (less then 300 lines of python!) and text-based implementation of the some what popular trick taking game!

Rules of Nines
--------------

Nines is played with three people and a standard 52 card deck with aces high. Each player starts the game with 9 points and the goal is to get to 0 points. The entire deck is dealt in four even hands. Players then, have a chance to evaluate their hands before playing them. Starting with the dealer each player gets a chance to swap their hand with the extra fourth hand that was dealt to nobody (this is called the dummy) if they want to. Even if the dummy has been previously taken a player can decide to swap their hand. 

Once all the hands have been finalized the game then proceeds in a satisfying loop. The dealer gets to led the first card. This card can be anything in their hand. The player on the dealers left then has to play a card from the same suit as the card already on the table. The third player has to do the same. The only time a player is allowed to play are card that is not in the first card's suit is when that player does not have any of that suit left in their hand (called void). When a player is void they can either play card from any suit (sluff) or a trump card.  The player who played the highest card then wins that round (called a trick). The next round is started by the person who was able to take the trick. This is done by that person leading any card that they wish from their hand. The hand is finished when all the players have exhausted all their cards. If a play was able to make 4 tricks (called a book), their total score does not change, for each trick over 4 their point total is subtracted by 1 and if a player makes less then 4 then their total is added by 1 for how many tricks would be need to get them to 4. For example, if a player made 3 tricks then 1 point would be add to their total score and if a player made 8 tricks then their total score would be subtracted by 4.

The real spice of nines, is the strategic implications of trump cards. In nines, trump is declared at the beginning of a hand. The first hand is always clubs, the next is hearts, then diamonds, spades and finally no trump. When that cycle finishes it simply repeats, with clubs being trump again. Trump can be played if a player is void in the suit lead during that round. Trump cards are the highest in the game and can beat all other cards. If multiple players play a trump the highest trump card wins.

How it works in this version
----------------------------

At the start of a hand the player will be asked if they wish to switch to the dummy. The player then starts the game. During a round the computer will always show what (if any thing) is on the table, followed by the players hand and finally a prompt to type in a card selection. The card selection is simple, but not necessarily intuitive. The player must first declare what suit is to be played followed by what number from that suit will be played. The suit is just the first letter in lower case from the name of the suit. The number is just number printed on the card, except with numbers over 10 (because hex is cool).

### Suit Table

Spades = s

Hearts = h

Diamonds = d

Clubs = c

### Number Table
2 = 2

3 = 3

4 = 4

5 = 5

6 = 6

7 = 7

8 = 8

9 = 9

10 = a

Jack = b

Queen = d

King = e

Ace = 1

### Examples of Correct Input

Ace of Spades = s1

9 of Diamonds = d9

10 of hearts = ha

King of Clubs = ce
