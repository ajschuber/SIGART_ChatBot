'''
Created on Jan 27, 2013

@author: Andrew
'''

from bots import ChatBot

class DummyBot(ChatBot):
    ''' Hello world chat bot '''
    
    def __init__(self):
        '''Any initialization logic would go here'''
        self.name = "Dummy"
    
    def get_response(self, user_input):
        '''Dummy response, just copy cats what the user says'''
        
        return user_input.upper().rstrip('.?') + '?'