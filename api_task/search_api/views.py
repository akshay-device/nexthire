import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from selenium import webdriver
import pyuser_agent


@csrf_exempt
def search_amazon(request,name):
    if request.method == 'GET':
        keyword = name

        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

        # Perform the search on Amazon
        url = f'https://www.amazon.com/s?k={keyword}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the search results
        results = soup.find_all('div', {'data-component-type': 's-search-result'})
        # Process the search results
        search_results = []
        for result in results:
            title = result.find('span', {'class': 'a-size-medium'})
            url = result.find('a', {'class': 'a-link-normal'})
            if title and url:
                search_results.append({'title': title.text, 'url': url['href']})

        # Return the search results as JSON response
        print(search_results)
        return JsonResponse(search_results, safe=False)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
