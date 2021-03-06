import wolframalpha
import Mods.vision as vision

class Client(object):
    def __init__(self, key):
        self.key = key
        self.client = wolframalpha.Client(key)

    # Processes a user query.
    def calCount(self, queryText):
        res = self.client.query("calories in " + queryText)
        try:
            numCals = next(res.results).text.split()[0]
            return int(numCals)
        except:
            return "No calorie data."

    def cafCount(self, queryText):
        res = self.client.query("caffeine in " + queryText)
        try:
            numCaf = next(res.results).text.split()[0]
            return int(numCaf)
        except:
            return "No caffeine data."

    def wolf(self, queryText):
        res = self.client.query(queryText)
        try:
            numCaf = next(res.results).text
            return str(numCaf)
        except:
            return "No data."