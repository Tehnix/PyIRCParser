import unittest

from IRCTestOutput import *
from ExpectedOutput import *
from Parser import *


class ParserTest(unittest.TestCase):
    """Test the IRC parser."""
    
    def test_parsing_gives_expected_output_on_server_codes(self):
        for key, expected in EXPECTED_SERVER_CODE_ACTIONS.items():
            self.assertEqual(parse(SERVER_CODE_ACTIONS[key]), expected)
            
    def test_parsing_gives_expected_output_on_user_actions(self):     
        for key, expected in EXPECTED_USER_ACTIONS.items():
            self.assertEqual(parse(USER_ACTIONS[key]), expected)
    
    def test_that_tokenizing_works(self):
        t = tokenize(':Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com NOTICE Innocence :hey!')
        self.assertEqual(t, ['Tehnix!Tehnix@ghost-EC31B3C1.rdns.scalabledns.com NOTICE Innocence ', 'hey!'])
    
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

