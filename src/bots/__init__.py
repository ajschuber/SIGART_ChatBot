'''
Created on Jan 27, 2013

@author: Andrew
'''


class ChatBot(object):
    '''Main interface for an chat bot'''
    
    def __init__(self):
        self.name = "ChatBot"
        
    def get_response(self, user_input):
        return ''