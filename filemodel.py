"""
File: filemodel.py
Project 16.6

Data model for a file viewer.  Supports navigation
through the lines of a file. Also supports insertions,
removals, and replacements of a line at the current position,
and saving the changes to the file.

Programmer: Shannon Kolvitz
Program 1

"""

from linkedlist import LinkedList


class FileModel(object):

    def __init__(self, filename):
        # New instance variable _canModify permits or
        # disallows removals and replacements
        # New instance variable _filename needed to save
        # modifications to the file
        file = open(filename, 'r')
        self._list = LinkedList().listIterator()
        for line in file:
            self._list.insert(line)
        file.close()
        self._canModify = False
        self._filename = filename


    def canModify(self):
        # Returns True if a line can be removed or replaced
        # or False otherwise.
        return self._canModify

    def first(self):
        # Navigate to the first line.
        # Return the next line.
        self._list.first()
        if self._list.hasNext():
            print(self._list.next())
        pass

    def last(self):
        # Navigate to the last line.
        # Return the previous line.
        self._list.last()
        if self._list.hasPrevious():
            print(self._list.previous())
        pass

    def next(self):
        # If there is a next line, set self._canModify to True
        # and return the next line. Otherwise, return None.
        if self._list.hasNext():
            self._canModify = True
            print(self._list.next())
        else:
           self._canModify = False
        pass

    def previous(self):
        # If there is a previous line, set self._canModify to True
        # and return the previous line. Otherwise, return None.
        if self._list.hasPrevious():
            self._canModify = True
            print(self._list.previous())
        else:
            self._canModify = False
        pass

    def insert(self, line):
        # Inserts line at the current position or at the
        # end of the list if the position is undefined.
        # set self._canModify to False.
        if not self._list.hasNext():
            self._list.last()
            self._list.insert(line)
            self._canModify = False
        else:
            self._list.insert(line)

        pass

    def remove(self):
        # Remove current line and set self._canModify to False.
        self._list.remove()
        self._canModify = False
        pass

    def replace(self, line):
        # Replace current line and set self._canModify to False.
        self._list.replace(line)
        self._canModify = False
        pass
