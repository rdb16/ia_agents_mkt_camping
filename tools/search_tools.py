import os
import json
from langchain.tools import tool
import requests


class SearchTools:
    @tool("Search the internet")
    def search_internet(query):
        """
        Utile pour rechercher un topic sur internet et
         ramener un résultat pertinent
         """
        top_results_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {'X-API-KEY': os.environ['SERPER_API_KEY'],
                   'Content-Type': 'application/json'
                   }
        response = requests.request("POST", url, headers=headers, data=payload)
        if 'organic' not in response.json():
            return "Sorry, I could not find anything about that, ..."
        else:
            results = response.json()['organic']
            string = []
            for result in results[:top_results_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}", f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}", "\n-------------"
                    ]))
                except KeyError:
                    next

            return '\n'.join(string)
