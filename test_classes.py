import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Test for class AnonymousSurvey"""

    def test_something_else(self):
        """Test that a single response is stored properly"""
        
        question = "What language did you learn to speak first?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'mandarin', 'French']
        
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn('English', my_survey.responses)


if __name__ == '__main__':
    unittest.main()
