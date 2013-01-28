'''
Created on Jan 27, 2013

Main file

@author: Andrew
'''

'''
Change this import to use different bots.

dummybot is the .py filename, in the bots folder
DummyBot is the class name inside that file
ChatBot is an alias to be used in this file

'''
from bots.dummybot import DummyBot as ChatBot


def prompt_user():
    '''Get the string from the user'''
    
    user_input = raw_input('Enter text: ')
    print
    
    return user_input


def format_response(bot, response):
    '''Output the response of the bot'''
    
    print "{0}: {1}".format(bot.name, response)
    print


def main():
    '''Loop: prompt user, then get response from bot. '''
    
    #Instantiate chatbot
    bot = ChatBot()
    
    while True:
        #Get a string from the user.
        user_input = prompt_user()
        
        #Get a response from the bot given the user input
        agent_response = bot.get_response(user_input) 
        
        #Output the response
        format_response(bot, agent_response)


if __name__ == "__main__":
    main()