'''
Created on 28/04/2013

@author: Carne
'''

from unittest import TestCase
from shellAndConsoleExceptions import Exceptions
from shell import Shell

class TestShell(TestCase):
    def setUp(self):
        self.shell = Shell.Shell("admin", "admin")

    def testAddUserCorrect(self):

        self.shell.addUser("u1", "123456")
        self.shell.addUser("u2", "abcdef")
        self.assertEqual(3, len(self.shell.getUsers()))
        self.assertEqual("u1", self.shell.getUsers()[1].getNickName())
        self.assertEqual("u2", self.shell.getUsers()[2].getNickName())


    def testAddUserRaiseAlreadyExists(self):
        try:
            self.shell.addUser("u1", "123456")
            self.shell.addUser("u1", "abcdef")
            self.fail("User with same name was added")
        except Exceptions.UserAlreadyExistException:
            self.assertEqual(2, len(self.shell.getUsers()))
            self.assertEqual("123456", self.shell.getUsers()[-1].getPassword())

    def testAddUserRaiseNotAdminException(self):
        try:
            self.shell.addUser("u1", "123456")
            self.shell.currentUser = self.shell.getUsers()[1]
            self.shell.addUser("u2", "abcde")
        except Exceptions.NotAdminException:
            self.assertEqual(2, len(self.shell.getUsers()))
            self.assertEqual("u1", self.shell.getUsers()[-1].getNickName())

    def testRemoveUserCorrect(self):
        self.shell.addUser("u1", "123456")
        self.shell.removeUser("u1")
        self.assertEqual(1, len(self.shell.getUsers()))

    def testRemoveUserRaiseUserDoesNotExistException(self):
        try:
            self.shell.removeUser("u1")
        except Exceptions.UserDoesNotExistException:
            self.assertEqual (1, len(self.shell.getUsers()))

    def testChangePasswordCorrect(self):
        self.shell.changePassword("admin", "abcdef")
        self.assertEqual("abcdef", self.shell.getCurrentUser().getPassword())


    def testChangePasswordRaiseNewPasswordEqualOldPasswordException(self):
        try:
            self.shell.changePassword ("admin", "admin")
        except Exceptions.NewPasswordEqualOldPasswordException:
            self.assertEqual("admin", self.shell.getCurrentUser().getPassword())


    def testLoginCorrect(self):
        self.shell.addUser("u1", "123456")
        self.shell.login("u1", "123456")
        self.assertEqual("u1", self.shell.getCurrentUser().getNickName())

    def testLoginRaiseIncorrectUserOrPasswordException(self):
        try:
            self.shell.addUser("u1", "123456")
            self.shell.login("u1", "abcdef")
        except Exceptions.IncorrectUserOrPasswordException:
            self.assertEqual("admin", self.shell.getCurrentUser().getNickName())