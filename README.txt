Fearless Bot v0.2

The end goal of Fearless bot is to create a discord bot that can automate a session of playing fearless draft using draftlol to ban champions that have been picked/banned previously.

Fearless Draft means after a champion has been picked or banned, then it cannot be picked in future games. Due to 20 champions being used per game, there are only enough champions for about 8 consecutive games before having to start over (currently there are 162 champions in the game)

- My inital goal is to try and automate the process in creating a draft link using draftlol.dawe.gg when knowing what champions are banned 
- To expand, it should be able to take a previous draft link and scrape what champions were picked and banned by each side, then create the link for a new draft with all of those champions being banned using the advanced options setting
- The final step of this would be to create a discord bot that can store the information from consecutive links to allow 3-5 games to be played in succession and successfully store and create drafts each time until the session is over. There will be a simple reset command to clear a list of banned champion names and there could be a previous drafts command that stores the links given to look at the drafts and a banned champions command that shows what champions are currently in the ban list 
