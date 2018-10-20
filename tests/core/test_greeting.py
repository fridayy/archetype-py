from unittest import TestCase

from archetype.core.greeting import Greeting


class GreetingTest(TestCase):

    def test_greeting(self):
        class_under_test = Greeting()
        self.assertEqual(class_under_test.hello_world(), "Hello World!")