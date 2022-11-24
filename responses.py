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
    if p_message == 'roll':
        return str(random.randint(1,6))
    if p_message == 'help':
        return '`This is a help message`'
    if p_message == 'reset draft':
        if os.path.exists('bannedchampions.txt'):
            os.remove('bannedchampions.txt')
        else:
            return '`There was no banlist`'
        return '`The banlist has been cleared`'
    if p_message == 'create draft':
        draft = draft_creator.create_draft()
        return str(f'`Blue pick: {draft[0]}\nRed pick: {draft[1]}\nSpectate: {draft[2]}`')
    if 'test' in p_message:
        print(f'{p_message} is the full message')
        return '`tested`'
    if p_message == 'commands':
        return '`!roll - rolls a number\n!help - just a default \n!test - test \n' \
               '!reset draft - clears the bannedchampions.txt that no one can actually see \n!load draft (url) - ' \
               'loads a draftlol link into bannedchampions.txt\n!create draft - creates a draft based on ' \
               'bannedchampions.txt`'
