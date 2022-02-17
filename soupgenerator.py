'''
Soup Generator generates content quickly for use wherever content needs to be.add()

------------------------------
-----example
soupgenerator.Text.number(4)

-----output
8432

------------------------------



'''
import csv
import random


class Text:
    '''
    Text based content generation.
    '''

    def __init__(self, length):
        self.length = int(length)


    def number(self):
        '''
        length = how many numbers to return
        '''

        val = ""

        for i in range(self.length):
            lastnum = val
            val = lastnum + str(random.randint(0,9))

        return str(val)


    def alphabet(self):
        '''
        length = how many letters to return
        '''

        val = ""
        alphabet =  self.loadlists("alphabet")

        for i in range(self.length):
            lastval = val
            val = lastval + " " + str(random.choice(alphabet))
        
        return val


    def alphanumeric(self):
        '''
        length = how many letters to return
        '''

        val = ""
        alphanumeric =  self.loadlists("alphabet")

        for i in range(10):
            alphanumeric.append(i)

        for i in range(self.length):
            if i > 0:
                lastval = val
                val = lastval + str(random.choice(alphanumeric)) 
            else:
                val = str(random.choice(alphanumeric))
            
        return val


    def word():
        return


    def adjective():
        return


    def adverb(self):
        '''
        length = how many adverbs to return
        '''

        val = ""
        adverbs =  self.loadlists("adverbs")

        for i in range(self.length):
            if i > 0:
                lastval = val
                val = lastval + " " + str(random.choice(adverbs)).lower()
            else:
                val = str(random.choice(adverbs)).upper()
            
        return val


    def noun(self):
        '''
        length = how many nouns to return
        '''

        val = ""
        nouns = self.loadlists("nouns")

        for i in range(self.length):
            if i > 0:
                lastval = val
                val = lastval + " " + str(random.choice(nouns)).lower() 
            else:
                val = str(random.choice(nouns)).upper()
            
        return val
        

    def loadlists(self, name):
        '''
        not recommended to use this diretly in your code. most other methods call this automatically.
        returns a list
        '''

        vals = []
        path = f"libs/{name}.csv"

        with open(path, "r") as f:
            r = csv.reader(f)
            for row in r:
                vals.append(row)

        return vals
        