import unittest

from Parser import *


RANDOM = [
    ":irc.codetalk.io NOTICE AUTH :*** Looking up your hostname...",
    ":irc.codetalk.io NOTICE AUTH :*** Couldn't resolve your hostname; using your IP address instead",
    ":irc.codetalk.io NOTICE Innocence :*** You are connected to irc.codetalk.io with TLSv1-AES256-SHA-256bits",
    ":Innocence MODE Innocence :+ixz"
]

SERVER_ACTIONS = {
    "PING": "PING :irc.codetalk.io"
}

SERVER_CODE_ACTIONS = {
    "001": ":irc.codetalk.io 001 Innocence :Welcome to the codetalk IRC Network Innocence!Motoko@82.211.197.12",
    "002": ":irc.codetalk.io 002 Innocence :Your host is irc.codetalk.io, running version Unreal3.2.10",
    "003": ":irc.codetalk.io 003 Innocence :This server was created Sun Jan 13 2013 at 01:16:15 MSK",
    "004": ":irc.codetalk.io 004 Innocence irc.codetalk.io Unreal3.2.10 iowghraAsORTVSxNCWqBzvdHtGpI lvhopsmntikrRcaqOALQbSeIKVfMCuzNTGjZ",
    "005": ":irc.codetalk.io 005 Innocence UHNAMES NAMESX SAFELIST HCN MAXCHANNELS=30 CHANLIMIT=#:30 MAXLIST=b:60,e:60,I:60 NICKLEN=30 CHANNELLEN=32 TOPICLEN=307 KICKLEN=307 AWAYLEN=307 MAXTARGETS=20 :are supported by this server\r\n:irc.codetalk.io 005 Innocence WALLCHOPS WATCH=128 WATCHOPTS=A SILENCE=15 MODES=12 CHANTYPES=# PREFIX=(qaohv)~&@%+ CHANMODES=beI,kfL,lj,psmntirRcOAQKVCuzNSMTGZ NETWORK=codetalk CASEMAPPING=ascii EXTBAN=~,qjncrRa ELIST=MNUCT STATUSMSG=~&@%+ :are supported by this server\r\n:irc.codetalk.io 005 Innocence EXCEPTS INVEX CMDS=KNOCK,MAP,DCCALLOW,USERIP,STARTTLS :are supported by this server",
    "251": ":irc.codetalk.io 251 Innocence :There are 14 users and 12 invisible on 2 servers",
    "252": ":irc.codetalk.io 252 Innocence 10 :operator(s) online",
    "254": ":irc.codetalk.io 254 Innocence 2 :channels formed",
    "255": ":irc.codetalk.io 255 Innocence :I have 11 clients and 1 servers",
    "265": ":irc.codetalk.io 265 Innocence 11 13 :Current local users 11, max 13",
    "266": ":irc.codetalk.io 266 Innocence 26 28 :Current global users 26, max 28",
    "375": ":irc.codetalk.io 375 Innocence :- irc.codetalk.io Message of the Day -",
    "372": ":irc.codetalk.io 372 Innocence :- 13/1/2013 18:10\r\n:irc.codetalk.io 372 Innocence :- Hi there\r\n:irc.codetalk.io 372 Innocence :- Goodbye again!",
    "376": ":irc.codetalk.io 376 Innocence :End of /MOTD command.",
    "332": ":irc.codetalk.io 332 Innocence #lobby :Let's all have great fun! :D", # Channel Topic
    "333": ":irc.codetalk.io 333 Innocence #lobby Tehnix 1360381672", # Who set the topic and unix timestamp on when
    "353": ":irc.codetalk.io 353 Innocence = #lobby :Innocence ~Tehnix Systemic33 Pandaen Foxboron Aurelio MrJenkins martinjlowm ljos Cam @nRage &Prometheus",
    "366": ":irc.codetalk.io 366 Innocence #lobby :End of /NAMES list."
    
}

OWN_ACTIONS = {
    "JOIN": ":Innocence!Motoko@F8A49EC3.F1F3F963.4ECC9EEA.IP JOIN :#lobby"
}

USER_ACTIONS = {
    "NICK": ":Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com NICK :BlaBliBlu",
    "TOPIC": ":Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com TOPIC #lobby :Let's all have great fun! :D",
    "PART": ":Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com PART #lobby",
    "JOIN": ":Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com JOIN :#lobby",
    "MODE": ":Prometheus!Ghost@bot.ohmagosh.com MODE #lobby +qo Tehnix Tehnix",
    "CHAN_PRIVMSG": ":Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com PRIVMSG #lobby :there, fixed -.-",
    "USER_PRIVMSG": ":Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com PRIVMSG Innocence :hey!",
    "CHAN_NOTICE": ":Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com NOTICE #lobby :sup?",
    "USER_NOTICE": ":Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com NOTICE Innocence :hey!"
}

class ParserTest(unittest.TestCase):
    """Test the IRC parser."""
    
    def test_all_IRC_codes_are_found(self):
        for code, text in SERVER_CODE_ACTIONS.items():
            t = tokenize(text)
            self.assertEqual(True, check_for_IRC_code(t))
        for action, text in USER_ACTIONS.items():
            t = tokenize(text)
            self.assertEqual(False, check_for_IRC_code(t))
    
    def test_that_a_nickname_is_found(self):
        t = tokenize(USER_ACTIONS['NICK'])
        self.assertEqual(nickname(t), 'Tehnix')
    
    def test_that_server_messages_are_found(self):
        for code, text in SERVER_CODE_ACTIONS.items():
            t = tokenize(text)
            self.assertEqual(True, is_server_message(t))
        for action, text in USER_ACTIONS.items():
            t = tokenize(text)
            self.assertEqual(False, is_server_message(t))
        
        




