import wolframalpha

class Client(object):
    def __init__(self, key):
        self.key = key
        self.client = wolframalpha.Client(key)

    # Processes a user query.
    def ask(self, queryText):
        res = self.client.query("calories in " + queryText)
        try:
            numCals = next(res.results).text.split()[0]
            return numCals
        except:
            print("No calorie data.")
            return 0