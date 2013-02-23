EXPECTED_SERVER_ACTIONS = {
    'PING': (
        None, # server
        None, # channel
        None, # recipient
        None, # user
        'PING', # type
        'irc.codetalk.io' # msg
    )
}

EXPECTED_SERVER_CODE_ACTIONS = {
    '001': (
        'irc.codetalk.io', # server
        None, # channel
        None, # recipient
        None, # user
        '001', # type
        'Welcome to the codetalk IRC Network Innocence!Motoko@82.211.197.12' # msg
    ),
    '002': (
        'irc.codetalk.io', # server
        None, # channel
        None, # recipient
        None, # user
        '002', # type
        'Your host is irc.codetalk.io, running version Unreal3.2.10' # msg
    ),
    '003': (
        'irc.codetalk.io', # server
        None, # channel
        None, # recipient
        None, # user
        '003', # type
        'This server was created Sun Jan 13 2013 at 01:16:15 MSK' # msg
    ),
    '252': (
        'irc.codetalk.io', # server
        None, # channel
        None, # recipient
        None, # user
        '252', # type
        'operator(s) online' # msg
    ),
    '332': (
        'irc.codetalk.io', # server
        '#lobby', # channel
        None, # recipient
        None, # user
        '332', # type
        'Let\'s all have great fun! :D' # msg
    ),
    '333': (
        'irc.codetalk.io', # server
        '#lobby', # channel
        None, # recipient
        None, # user
        '333', # type
        'Tehnix 1360381672' # msg
    ),
    '353': (
        'irc.codetalk.io', # server
        '#lobby', # channel
        None, # recipient
        None, # user
        '353', # type
        'Innocence ~Tehnix Systemic33 Pandaen Foxboron Aurelio MrJenkins martinjlowm ljos Cam @nRage &Prometheus' # msg
    ),
    '372': (
        'irc.codetalk.io', # server
        None, # channel
        None, # recipient
        None, # user
        '372', # type
        '- 13/1/2013 18:10' # msg
    )
}

EXPECTED_USER_ACTIONS = {
    'NICK': (
        None, # server
        None, # channel
        None, # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'NICK', # type
        'BlaBliBlu' # msg
    ),
    'TOPIC': (
        None, # server
        '#lobby', # channel
        None, # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'TOPIC', # type
        'Let\'s all have great fun! :D' # msg
    ),
    'PART': (
        None, # server
        '#lobby', # channel
        None, # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'PART', # type
        None # msg
    ),
    'JOIN': (
        None, # server
        None, # channel
        None, # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'JOIN', # type
        '#lobby' # msg
    ),
    'MODE': (
        None, # server
        '#lobby', # channel
        None, # recipient
        ('Prometheus', 'Ghost', 'bot.ohmagosh.com'), # user
        'MODE', # type
        '+qo Tehnix Tehnix' # msg
    ),
    'CHAN_PRIVMSG': (
        None, # server
        '#lobby', # channel
        '#lobby', # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'PRIVMSG', # type
        'there, fixed -.-' # msg
    ),
    'USER_PRIVMSG': (
        None, # server
        None, # channel
        'Innocence', # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'PRIVMSG', # type
        'hey!' # msg
    ),
    'CHAN_NOTICE': (
        None, # server
        '#lobby', # channel
        '#lobby', # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'NOTICE', # type
        'sup?' # msg
    ),
    'USER_NOTICE': (
        None, # server
        None, # channel
        'Innocence', # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'NOTICE', # type
        'hey!' # msg
    )
}
