"""
Parse IRC output.

The main function of this module is the `parse` function. It takes in some
IRC output, and generates a tuple/dict/list/object (the kwarg `output` in the `parse` function) looking like the following:

From: :irc.codetalk.io 332 Innocence #lobby :Let's all have great fun! :D
To: {
    'server': 'irc.codetalk.io',
    'channel': '#lobby',
    'recipient': None,
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
    'recipient': None,
    'user': ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'),
    'code': None,
    'action': 'NICK',
    'msg': 'BlaBliBlu'
}

Here, the user changed his nickname from 'Tehnix' to 'BlaBliBlu'.

"""

def tokenize(s):
    """Tokenize the given IRC output."""
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
    """Return the users host from a tokenized list."""
    return t[0].split('!')[1].split('@')[1].split()[0]

def getUser(t):
    """Return the user from a tokenized list."""
    return t[0].split('!')[1].split('@')[0]

def getChannel(t):
    """Return the channel from a tokenized list."""
    for item in t[0].split():
        if item.startswith('#'):
            return item
    return None

def getRecipient(t):
    """Return the recipient from a tokenized list. Only useful with NOTICE and PRIVMSG."""
    return t[0].split()[2]

def getServer(t):
    """Return the server address from a tokenized list."""
    return t[0].split()[0]

def getAction(t):
    """Return the action from a tokenized list."""
    return t[0].split()[1]

def isServerMessage(t):
    """Check if the IRC output is a server message."""
    if '!' not in t[0].split()[0]:
        return True
    return False
        
def getIRCCode(t):
    """Return the IRC code from a tokenized list."""
    c = t[0].split()[1]
    try:
        int(c)
    except ValueError:
        return None
    return c

def getMsg(t, code=None, action=None):
    """Return the message from a tokenized list."""
    if len(t) > 1:
        return ':'.join(t[1:])
    elif code == '333':
        return ' '.join(t[0].split()[4:])
    elif action == 'MODE':
        return ' '.join(t[0].split()[3:])
    return None

def getOutputObject(d):
    class ParseOutput: pass
    parseObj = ParseOutput()
    for key, val in d.items():
        setattr(parseObj, key, val)
    return parseObj

def _parse(s, output='tuple'):
    """Parse the IRC output. By default, return a tuple. Optionally return a dict, list or an object."""
    t = tokenize(s)
    if t[0].startswith('PING'):
        action = 'PING'
        msg = t[1]
        server = None
        code = None
        user = None
        recipient = None
        channel = None
    else:
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
    elif output == 'object':
        return getOutputObject({
            'server': server,
            'channel': channel,
            'recipient': recipient,
            'user': user,
            'code': code,
            'action': action,
            'msg': msg
        })
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

def parse(s, output='tuple'):
    """Wrapper for the _parse function to handle IndexError a bit neater."""
    try:
        return _parse(s, output=output)
    except IndexError:
        if output == 'dict' or output == 'dictionary':
            return {
                'server': None,
                'channel': None,
                'recipient': None,
                'user': None,
                'code': None,
                'action': None,
                'msg': None
            }
        elif output == 'object':
            return getOutputObject({
                'server': None,
                'channel': None,
                'recipient': None,
                'user': None,
                'code': None,
                'action': None,
                'msg': None
            })
        elif output == 'list':
            return [None, None, None, None, None, None, None]
        else:
            return (None, None, None, None, None, None, None)

if __name__ == '__main__':
    import sys
    print(_parse(' '.join(sys.argv[1:]), output='dict')) # read as a tuple in 2.x and uses the print function in 3.x
