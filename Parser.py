"""
Parse IRC output.

The main function of this module is the `parse` function. It takes in some
IRC output, and generates a tuple/dict/list looking like the following:

From: :irc.codetalk.io 332 Innocence #lobby :Let's all have great fun! :D
To: {
    'server': 'irc.codetalk.io',
    'channel': '#lobby',
    'user': None,
    'code': 332,
    'action': None,
    'msg': 'Let us all have great fun! :D'
}
    
This will indicate that a topic has been found for a channel. An example of 
a user action would be:

From: :Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com NICK :BlaBliBlu
To: {
    'server': None,
    'channel': None,
    'user': ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'),
    'code': None,
    'action': 'NICK',
    'msg': 'BlaBliBlu'
}

Here, the user changed his nickname from 'Tehnix' to 'BlaBliBlu'.

"""

def tokenize(s):
    s = s.split(':')
    if len(s) > 1:
        return s[1:]
    else:
        return []

def getNickname(t):
    """Take in a token list, and return the nickname."""
    return t[0].split('!')[0]

def strippedNickname(s):
    """Take a nickname and strip it from excessive information."""
    if len(s) > 1 and s[0:1] in ['@', '!', '&', '~']:
        return s[1:]
    else:
        return s

def getHostname(t):
    return t[0].split('!')[1].split('@')[1].split()[0]

def getUser(t):
    return t[0].split('!')[1].split('@')[0]

def getChannel(t):
    for item in t[0].split():
        if item.startswith('#'):
            return item
    return None

def getRecipient(t):
    return t[0].split()[2]

def getServer(t):
    return t[0].split()[0]

def getAction(t):
    return t[0].split()[1]

def isServerMessage(t):
    if '!' not in t[0].split()[0]:
        return True
    return False
        
def getIRCCode(t):
    c = t[0].split()[1]
    try:
        int(c)
    except ValueError:
        return None
    return c

def getMsg(t, code=None, action=None):
    if len(t) > 1:
        return ':'.join(t[1:])
    elif code == '333':
        return ' '.join(t[0].split()[4:])
    elif action == 'MODE':
        return ' '.join(t[0].split()[3:])
    return None

def parse(s, output='tuple'):
    """Parse the IRC output. By default, return a tuple. Optionally return a dict or a list."""
    t = tokenize(s)
    code = getIRCCode(t)
    channel = getChannel(t)
    if isServerMessage(t):
        server = getServer(t)
        user = None
        action = None
    else:
        server = None
        user = (strippedNickname(getNickname(t)), getUser(t), getHostname(t))
        action = getAction(t)
    if not isServerMessage(t) and action in ['NOTICE', 'PRIVMSG']:
        recipient = getRecipient(t)
    else:
        recipient = None
    msg = getMsg(t, code=code, action=action)
    if output == 'dict' or output == 'dictionary':
        return {
            'server': server,
            'channel': channel,
            'recipient': recipient,
            'user': user,
            'code': code,
            'action': action,
            'msg': msg
        }
    elif output == 'list':
        return [
            server,
            channel,
            recipient,
            user,
            code,
            action,
            msg
        ]
    else:
        return (
            server,
            channel,
            recipient,
            user,
            code,
            action,
            msg
        )
