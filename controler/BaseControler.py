import requests
class BaseControler(object):
    BASE_URL = "https://spoonacular.com/food-api"
    FIND_BY_INGREDIENTS_URL = "/recipes/findByIngredients/"
    def __init__(self):
        pass
        
    def testRequest(self):
        payload = {"fillIngredients" : True, "ingredients" : ["apple", "flour", "sugar"], "limitLicense" : 5}
        response = requests.get(self.BASE_URL + self.FIND_BY_INGREDIENTS_URL, params = payload)
        print(response.json())

def main():
    b = BaseControler()
    b.testRequest()

main()