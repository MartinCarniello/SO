'''
Created on 27/04/2013

@author: Carne
'''

class IncorrectUserOrPasswordException(Exception): pass
        
class UserAlreadyExistException(Exception): pass
        
class NotAdminException(Exception): pass
        
class UserDoesNotExistException(Exception): pass
        
class NewPasswordEqualOldPasswordException(Exception): pass
        
class IncorrectPasswordException(Exception): pass

class NoSpaceInMemory(Exception): pass

class IncorrectID(Exception): pass