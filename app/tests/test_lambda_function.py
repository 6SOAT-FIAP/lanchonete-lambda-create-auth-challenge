import unittest
from src.lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    def test_lambda_handler(self):
        event = {
            'response': {}
        }
        
        expected_response = {
            'response': {
                'privateChallengeParameters': {'secretCode': 'internal_code'},
                'publicChallengeParameters': {}
            }
        }
        
        result = lambda_handler(event, None)
        self.assertEqual(result, expected_response)

if __name__ == '__main__':
    unittest.main()