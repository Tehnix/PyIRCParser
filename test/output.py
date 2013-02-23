EXPECTED_SERVER_ACTIONS = {
    'PING': (
        None, # server
        None, # channel
        None, # recipient
        None, # user
        'ACTION', # type
        None, # code
        'PING', # action
        'irc.codetalk.io' # msg
    )
}

EXPECTED_SERVER_CODE_ACTIONS = {
    '001': (
        'irc.codetalk.io', # server
        None, # channel
        None, # recipient
        None, # user
        'CODE', # type
        '001', # code
        None, # action
        'Welcome to the codetalk IRC Network Innocence!Motoko@82.211.197.12' # msg
    ),
    '002': (
        'irc.codetalk.io', # server
        None, # channel
        None, # recipient
        None, # user
        'CODE', # type
        '002', # code
        None, # action
        'Your host is irc.codetalk.io, running version Unreal3.2.10' # msg
    ),
    '003': (
        'irc.codetalk.io', # server
        None, # channel
        None, # recipient
        None, # user
        'CODE', # type
        '003', # code
        None, # action
        'This server was created Sun Jan 13 2013 at 01:16:15 MSK' # msg
    ),
    '252': (
        'irc.codetalk.io', # server
        None, # channel
        None, # recipient
        None, # user
        'CODE', # type
        '252', # code
        None, # action
        'operator(s) online' # msg
    ),
    '332': (
        'irc.codetalk.io', # server
        '#lobby', # channel
        None, # recipient
        None, # user
        'CODE', # type
        '332', # code
        None, # action
        'Let\'s all have great fun! :D' # msg
    ),
    '333': (
        'irc.codetalk.io', # server
        '#lobby', # channel
        None, # recipient
        None, # user
        'CODE', # type
        '333', # code
        None, # action
        'Tehnix 1360381672' # msg
    ),
    '353': (
        'irc.codetalk.io', # server
        '#lobby', # channel
        None, # recipient
        None, # user
        'CODE', # type
        '353', # code
        None, # action
        'Innocence ~Tehnix Systemic33 Pandaen Foxboron Aurelio MrJenkins martinjlowm ljos Cam @nRage &Prometheus' # msg
    ),
    '372': (
        'irc.codetalk.io', # server
        None, # channel
        None, # recipient
        None, # user
        'CODE', # type
        '372', # code
        None, # action
        '- 13/1/2013 18:10' # msg
    )
}

EXPECTED_USER_ACTIONS = {
    'NICK': (
        None, # server
        None, # channel
        None, # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'ACTION', # type
        None, # code
        'NICK', # action
        'BlaBliBlu' # msg
    ),
    'TOPIC': (
        None, # server
        '#lobby', # channel
        None, # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'ACTION', # type
        None, # code
        'TOPIC', # action
        'Let\'s all have great fun! :D' # msg
    ),
    'PART': (
        None, # server
        '#lobby', # channel
        None, # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'ACTION', # type
        None, # code
        'PART', # action
        None # msg
    ),
    'JOIN': (
        None, # server
        None, # channel
        None, # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'ACTION', # type
        None, # code
        'JOIN', # action
        '#lobby' # msg
    ),
    'MODE': (
        None, # server
        '#lobby', # channel
        None, # recipient
        ('Prometheus', 'Ghost', 'bot.ohmagosh.com'), # user
        'ACTION', # type
        None, # code
        'MODE', # action
        '+qo Tehnix Tehnix' # msg
    ),
    'CHAN_PRIVMSG': (
        None, # server
        '#lobby', # channel
        '#lobby', # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'ACTION', # type
        None, # code
        'PRIVMSG', # action
        'there, fixed -.-' # msg
    ),
    'USER_PRIVMSG': (
        None, # server
        None, # channel
        'Innocence', # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'ACTION', # type
        None, # code
        'PRIVMSG', # action
        'hey!' # msg
    ),
    'CHAN_NOTICE': (
        None, # server
        '#lobby', # channel
        '#lobby', # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'ACTION', # type
        None, # code
        'NOTICE', # action
        'sup?' # msg
    ),
    'USER_NOTICE': (
        None, # server
        None, # channel
        'Innocence', # recipient
        ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
        'ACTION', # type
        None, # code
        'NOTICE', # action
        'hey!' # msg
    )
}
