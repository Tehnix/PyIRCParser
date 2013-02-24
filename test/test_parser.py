import unittest

from test.data import *
from test.output import *
from ircparser import *


class ParserTest(unittest.TestCase):
    """Test the IRC parser."""
    
    def test_parsing_gives_expected_output_on_server_codes(self):
        for key, expected in EXPECTED_SERVER_CODE_ACTIONS.items():
            self.assertEqual(parse(SERVER_CODE_ACTIONS[key]), expected)
    
    def test_parsing_gives_expected_output_on_server_actions(self):
        for key, expected in EXPECTED_SERVER_ACTIONS.items():
            self.assertEqual(parse(SERVER_ACTIONS[key]), expected)
            
    def test_parsing_gives_expected_output_on_user_actions(self):     
        for key, expected in EXPECTED_USER_ACTIONS.items():
            self.assertEqual(parse(USER_ACTIONS[key]), expected)
    
    def test_that_tokenizing_works(self):
        t = tokenize(':Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com NOTICE Innocence :hey!')
        self.assertEqual(t, ['Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com NOTICE Innocence ', 'hey!'])
        self.assertEqual(tokenize("some text"), [])
    
    def test_all_IRC_codes_are_found(self):
        for code, text in SERVER_CODE_ACTIONS.items():
            t = tokenize(text)
            self.assertNotEqual(None, getIRCCode(t))
        for action, text in USER_ACTIONS.items():
            t = tokenize(text)
            self.assertEqual(None, getIRCCode(t))
    
    def test_that_a_nickname_is_found(self):
        t = tokenize(USER_ACTIONS['NICK'])
        self.assertEqual(getNickname(t), 'Tehnix')
    
    def test_that_server_messages_are_found(self):
        for code, text in SERVER_CODE_ACTIONS.items():
            t = tokenize(text)
            self.assertEqual(True, isServerMessage(t))
        for action, text in USER_ACTIONS.items():
            t = tokenize(text)
            self.assertEqual(False, isServerMessage(t))
    
    def test_that_irc_codes_are_found(self):
        for code, text in SERVER_CODE_ACTIONS.items():
            t = tokenize(text)
            self.assertEqual(getIRCCode(t), code)
        for action, text in USER_ACTIONS.items():
            t = tokenize(text)
            self.assertEqual(getIRCCode(t), None)
    
    def test_that_server_is_found(self):
        t = tokenize(':irc.codetalk.io 251 Innocence :There are 14 users and 12 invisible on 2 servers')
        self.assertEqual(getServer(t), 'irc.codetalk.io')
    
    def test_that_user_is_found(self):
        t = tokenize(':Prometheus!Ghost@bot.ohmagosh.com MODE #lobby +qo Tehnix Tehnix')
        self.assertEqual(getUser(t), 'Ghost')
    
    def test_that_nickname_is_found(self):
        t = tokenize(':Prometheus!Ghost@bot.ohmagosh.com MODE #lobby +qo Tehnix Tehnix')
        self.assertEqual(getNickname(t), 'Prometheus')
        
    def test_that_nickname_is_stripped(self):
        self.assertEqual(strippedNickname('@Prometheus'), 'Prometheus')
        self.assertEqual(strippedNickname('~Prometheus'), 'Prometheus')
        self.assertEqual(strippedNickname('!Prometheus'), 'Prometheus')
        self.assertEqual(strippedNickname('&Prometheus'), 'Prometheus')
    
    def test_that_hostname_is_found(self):
        t = tokenize(':Prometheus!Ghost@bot.ohmagosh.com MODE #lobby +qo Tehnix Tehnix')
        self.assertEqual(getHostname(t), 'bot.ohmagosh.com')
    
    def test_that_action_is_found(self):
        t = tokenize(':Prometheus!Ghost@bot.ohmagosh.com MODE #lobby +qo Tehnix Tehnix')
        self.assertEqual(getAction(t), 'MODE')
    
    def test_that_message_is_found(self):
        t = tokenize(':Prometheus!Ghost@bot.ohmagosh.com MODE #lobby +qo Tehnix Tehnix')
        action = getAction(t)
        self.assertEqual(action, 'MODE')
        self.assertEqual(getMsg(t, action=action), '+qo Tehnix Tehnix')
        t = tokenize(':Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com NOTICE Innocence :hey!')
        action = getAction(t)
        self.assertEqual(action, 'NOTICE')
        self.assertEqual(getMsg(t, action=action), 'hey!')
    
    def test_that_recipient_is_found(self):
        t = tokenize(':Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com NOTICE Innocence :hey!')
        self.assertEqual(getRecipient(t), 'Innocence')
        t = tokenize(':Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com NOTICE #lobby :sup?')
        self.assertEqual(getRecipient(t), '#lobby')
    
    def test_that_correct_object_is_generated_from_dict(self):
        to = {
            'server': None, # server
            'channel': '#lobby', # channel
            'recipient': None, # recipient
            'user': ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
            'type': 'PART', # type
            'msg': '#lobby' # msg
        }
        out = getOutputObject(to)
        self.assertEqual(out.server, to['server'])
        self.assertEqual(out.channel, to['channel'])
        self.assertEqual(out.recipient, to['recipient'])
        self.assertEqual(out.type, to['type'])
        self.assertEqual(out.type, to['type'])
        self.assertEqual(out.msg, to['msg'])
    
    def test_that_output_object_equality_works(self):
        data = ":Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com PART #lobby"
        recievedObject = parse(data, output='object')
        expectedObject = ParseOutput()
        expectedObject.server = None
        expectedObject.channel = '#lobby'
        expectedObject.recipient = None
        expectedObject.user = ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com')
        expectedObject.type = 'PART'
        expectedObject.msg = '#lobby'
        self.assertEqual(recievedObject, expectedObject)
    
    def test_that_correct_data_types_are_returns(self):
        data = ":Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com PART #lobby"
        expectedDict = {
            'server': None, # server
            'channel': '#lobby', # channel
            'recipient': None, # recipient
            'user': ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
            'type': 'PART', # type
            'msg': '#lobby' # msg
        }
        expectedTuple = (
            None, # server
            '#lobby', # channel
            None, # recipient
            ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
            'PART', # type
            '#lobby' # msg
        )
        expectedList = [
            None, # server
            '#lobby', # channel
            None, # recipient
            ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
            'PART', # type
            '#lobby' # msg
        ]
        self.assertEqual(parse(data, output='dict'), expectedDict)
        self.assertEqual(parse(data), expectedTuple)
        self.assertEqual(parse(data, output='list'), expectedList)
        out = parse(data, output='object')
        self.assertEqual(out.server, expectedDict['server'])
        self.assertEqual(out.channel, expectedDict['channel'])
        self.assertEqual(out.recipient, expectedDict['recipient'])
        self.assertEqual(out.type, expectedDict['type'])
        self.assertEqual(out.type, expectedDict['type'])
        self.assertEqual(out.msg, expectedDict['msg'])
        
    def test_that_correct_data_types_are_returns_on_index_error(self):
        data = "Tehnobby"
        expectedDict = {
            'server': None, # server
            'channel': None, # channel
            'recipient': None, # recipient
            'user': None, # user
            'type': None, # type
            'msg': None # msg
        }
        expectedTuple = (
            None, # server
            None, # channel
            None, # recipient
            None, # user
            None, # type
            None # msg
        )
        expectedList = [
            None, # server
            None, # channel
            None, # recipient
            None, # user
            None, # type
            None # msg
        ]
        self.assertEqual(parse(data, output='dict'), expectedDict)
        self.assertEqual(parse(data), expectedTuple)
        self.assertEqual(parse(data, output='list'), expectedList)
        out = parse(data, output='object')
        self.assertEqual(out.server, expectedDict['server'])
        self.assertEqual(out.channel, expectedDict['channel'])
        self.assertEqual(out.recipient, expectedDict['recipient'])
        self.assertEqual(out.type, expectedDict['type'])
        self.assertEqual(out.type, expectedDict['type'])
        self.assertEqual(out.msg, expectedDict['msg'])
        

