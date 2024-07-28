import unittest
from src.my_token import Token


class TestMyToken(unittest.TestCase):
    def test_token(self):
        token = Token(Token.Kind.LBRACE, "{")
        self.assertEqual(token.get_kind(), Token.Kind.LBRACE)
        self.assertEqual(token.get_lexeme(), "{")
