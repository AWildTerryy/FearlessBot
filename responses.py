import random
import os
import draft_creator
import draft_puller

def handle_response(message):
    if 'load draft' in message:
        try:
            link = message[10:]
            return draft_puller.load_draft(link)
        except Exception as e:
            print(e)
            return '`Your link could not be processed`'
    # cannot use message.lower as the link is case-sensitive
    p_message = message.lower()
    if p_message == 'side':
        side = random.randint(1,2)
        if side == 1:
            return 'Blue!'
        if side == 2:
            return 'Red!'
    if p_message == 'help':
        return '`Try !commands, you can also use ?commands for to have any response be sent your DMs!`'
    if p_message == 'reset draft':
        if os.path.exists('bannedchampions.txt'):
            os.remove('bannedchampions.txt')
        else:
            return '`There was no banlist`'
        return '`The banlist has been cleared`'
    if p_message == 'create draft':
        draft = draft_creator.create_draft()
        return str(f'Blue pick: {draft[0]}\nRed pick: {draft[1]}\nSpectate: {draft[2]}')
    if p_message == 'bans':
        if os.path.exists('bannedchampions.txt'):
            banList = open('bannedchampions.txt', 'r')
            banMessage = 'The banned champions are: \n'
            for line in banList:
                banMessage += str(f'\t{line}')
            banList.close()
            return banMessage
        else:
            return '`The ban list is currently empty`'
    if 'add champion' in message:
        if os.path.exists('bannedchampions.txt'):
            banList = open('bannedchampions.txt','r+')  # using r+ to read and write in the file so file doesn't get truncated
            for line in banList:
                if line == (message[13:]+'\n'):
                    banList.close()
                    return 'Champion already in list!'
            banList.write(message[13:]+'\n')
            banList.close()
            return str(f'`{message[13:]} is added to the ban list!`')
        else:
            banList = open('bannedchampions.txt', 'w')
            banList.write(message[13:] + '\n')
            banList.close()
            return str(f'`{message[13:]} is added to the ban list!`')
    if p_message == 'commands':
        return '`All commands can be substituted with a ? to be sent to your DMs!                                  \n' \
               '!side - randomly picks a side, Red or Blue                                                         \n' \
               '!help - tells you to use !commands                                                                 \n' \
               '!bans - returns a list of champions in bannedchampions.txt                                         \n' \
               '!reset draft - clears the bannedchampions.txt                                                      \n' \
               '!load draft (url) - loads a draftlol link into bannedchampions.txt                                 \n' \
               '!create draft - creates a draft based on bannedchampions.txt                                       \n' \
               '!add champion - manually add a champion to bannedchampions.txt                                    `\n'
