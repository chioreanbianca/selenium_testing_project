import unittest
from paranthesis import are_parentheses_balanced

class TestParenthesesChecker(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(are_parentheses_balanced(list("")))


    def test_only_opening_parentheses(self):
        self.assertFalse(are_parentheses_balanced(list("(((")))

    def test_only_closing_parentheses(self):
        self.assertFalse(are_parentheses_balanced(list(")))")))

    def test_balanced_parentheses(self):
        self.assertTrue(are_parentheses_balanced(list("(if (zero? x) max (/ 1 x))")))
        self.assertTrue(are_parentheses_balanced(list("I told him (that it’s not (yet) done). (But he wasn’t listening)")))
        self.assertTrue(are_parentheses_balanced(list("((x+y)***)")))

    def test_unbalanced_parentheses(self):
        self.assertFalse(are_parentheses_balanced(list("This is an (unbalanced example")))
        self.assertTrue(are_parentheses_balanced(list("(a + b) * (c + d)")))


    def test_mixed_parentheses(self):
        self.assertTrue(are_parentheses_balanced(list("[[([]){}]]")))
        self.assertFalse(are_parentheses_balanced(list("{{{[[[(()))]")))