Nines on the Terminal
=====================

This project is meant to be a simple, small (less then 300 lines of python!) and text-based implementation of the some what popular trick taking game!

Rules of Nines
--------------

Nines is played with three people and a standard 52 card deck with aces high. Each player starts the game with 9 points and the goal is to get to 0 points. The entire deck is dealt in four even hands. Players then, have a chance to evaluate their hands before playing them. Starting with the dealer each player gets a chance to swap their hand with the extra fourth hand that was dealt to nobody (this is called the dummy) if they want to. Even if the dummy has been previously taken a player can decide to swap their hand. 

Once all the hands have been finalized the game then proceeds in a satisfying loop. The dealer gets to led the first card. This card can be anything in their hand. The player on the dealers left then has to play a card from the same suit as the card already on the table. The third player has to do the same. The player who played the highest card then wins that round (called a trick). The next round is started by the person who was able to take the trick. This is done by that person leading any card that they wish from their hand. The hand is finished when all the players have exhausted all their cards. If a play was able to make 4 tricks (called a book), their total score does not change, for each trick over 4 their point total is subtracted by 1 and if a player makes less then 4 then their total is added by 1 for how many tricks would be need to get them to 4. For example, if a player made 3 tricks then 1 point would be add to their total score and if a player made 8 tricks then their total score would be subtracted by 4.
