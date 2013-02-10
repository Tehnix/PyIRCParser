import unittest

from IRCTestOutput import *
from Parser import *


class ParserTest(unittest.TestCase):
    """Test the IRC parser."""
    
    def test_parsing_gives_expected_output(self):
        expected1 = (
            None, # server
            None, # channel
            ('Tehnix', 'Tehnix', 'ghost-EC31B3C1.rdns.scalabledns.com'), # user
            None, # code
            'NICK', # action
            'BlaBliBlu' # msg
        )
        expected2 = (
            'irc.codetalk.io', # server
            '#lobby', # channel
            None, # user
            '332', # code
            None, # action
            'Let\'s all have great fun! :D' # msg
        )
        self.assertEqual(parse(SERVER_CODE_ACTIONS['332']), expected2)
        self.assertEqual(parse(USER_ACTIONS['NICK']), expected1)
    
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
        
        




