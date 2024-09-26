# Acionador lambda para criar desafio de autenticação

def lambda_handler(event, context):

    event['response']['privateChallengeParameters'] = {'secretCode': 'internal_code'}
    event['response']['publicChallengeParameters'] = {}
    
    return event