import Unirest

#    code - HTTP Response Status Code (Example 200)
#    headers- HTTP Response Headers
#    body- Parsed response body where applicable, for example JSON responses are parsed to Objects / Associative Arrays.
#    raw_body- Un-parsed response body

#    unirest.get(url, headers = {}, params = {}, auth = (), callback = None)
#    unirest.post(url, headers = {}, params = {}, auth = (), callback = None)
class BaseControler(object):
    BASE_URL = "https://spoonacular.com/food-api"
    FIND_BY_INGREDIENTS_URL = "/recipes/findByIngredients/"
    def __init__(self):
        pass
        
    def testRequest(self):
        response = unirest.get(BASE_URL + FIND_BY_INGREDIENTS_URL,
            params = {"fillIngredients" : True, "ingredients" : {"apple", "flour", "sugar"}, "limitLicense" : 5})
        print("code: " + response.code)
        print("headers" + response.headers)
        print("body-parsed" + response.body)
        print("raw-body" + response.raw_body)

def main():
    b = BaseControler()
    b.testRequest()

main()