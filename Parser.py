def parse(s, output='list'):
    t = tokenize(s)
    print t
    print check_for_IRC_code(t)

def tokenize(s):
    s = s.split(':')
    if len(s) > 1:
        return s[1:]
    else:
        return []

def nickname(t):
    """Take in a token list, and return the nickname."""
    return t[0].split('!')[0]

def stripped_nickname(s):
    """Take a nickname and strip it from excessive information."""
    if len(s) > 1 and s[0:1] in ['@', '!', '&', '~']:
        return s[1:]
    else:
        return s

def is_server_message(t):
    if '!' not in t[0].split()[0]:
        return True
    return False
        
def check_for_IRC_code(t):
    c = t[0].split()[1]
    try:
        int(c)
    except ValueError:
        return False
    return True

def handle_IRC_code(i, t):
    pass

def nicks_from_names_list(t):
    pass
