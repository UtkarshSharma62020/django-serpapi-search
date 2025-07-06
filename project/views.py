import csv
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

latest_results = [] #For hold results


def search_view(request):
    global latest_results
    latest_results = []  

    if request.method == 'POST':
        queries = request.POST.getlist('query')  
        api_key = 'SERPAPI_KEY' 

        for query in queries:
            if query.strip() == "":
                messages.error(request, "One or more queries are empty.")
                continue

            url = "https://serpapi.com/search"
            params = {
                "api_key": api_key,
                "engine": "google",
                "q": query,
                "num": 5 
            }

            try:
                response = requests.get(url, params=params)
                data = response.json()

                results = data.get("organic_results", [])
                if not results:
                    messages.warning(request, f"No results found for: {query}")
                    continue

                for item in results:
                    latest_results.append({
                        "query": query,
                        "title": item.get("title", ""),
                        "link": item.get("link", ""),
                        "snippet": item.get("snippet", "")
                    })

            except Exception as e:
                messages.error(request, f"Error fetching results for '{query}': {e}")

    return render(request, 'search.html', {'results': latest_results})



def download_csv(request):
    global latest_results

    if not latest_results:
        return HttpResponse("No results available to download.", content_type="text/plain")

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="search_results.csv"'

    writer = csv.DictWriter(response, fieldnames=["query", "title", "link", "snippet"])
    writer.writeheader()
    for row in latest_results:
        writer.writerow(row)

    return response
