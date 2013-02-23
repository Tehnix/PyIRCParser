## IRC Parser ##

Parses IRC output and returns a structured tuple/dict/list that's easier to use.

The main function of this module is the `parse` function. It takes in some
IRC output, and generates a tuple/dict/list/object (the kwarg `output` in the `parse` function) looking like the following:

From: `:irc.codetalk.io 332 Innocence #lobby :Let's all have great fun! :D`
To: 
<pre>{
    'server': 'irc.codetalk.io',
    'channel': '#lobby',
    'recipient': None,
    'user': None,
    'type': 'CODE',
    'code': 332,
    'action': None,
    'msg': 'Let us all have great fun! :D'
}</pre>

This will indicate that a topic has been found for a channel. An example of 
a user action would be:

From: `:Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com NICK :BlaBliBlu`
To: 
<pre>{
    'server': None,
    'channel': None,
    'recipient': None,
    'user': ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'),
    'type': 'ACTION',
    'code': None,
    'action': 'NICK',
    'msg': 'BlaBliBlu'
}</pre>

Here, the user changed his nickname from 'Tehnix' to 'BlaBliBlu'.

From `PING :D2FB5C1B`
To: 
<pre>{
    'server': None,
    'channel': None,
    'recipient': None,
    'user': None,
    'type': 'ACTION',
    'code': None,
    'action': 'PING',
    'msg': 'D2FB5C1B'
}</pre>

This would be a PING from the server.

## Tests ##
Approximately 100% (or close to) of the code is covered with tests. It's tested using nosetests, but that shouldn't do much difference.

A tip, using fswatch to continuesly run the tests during development is quite handy, `fswatch . 'clear && clear && nosetests'`.