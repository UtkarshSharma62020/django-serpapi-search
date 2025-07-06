import csv, os, requests
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

def search_view(request):
    if request.method == 'POST':
        queries = request.POST.getlist('query')
        api_key = os.environ.get('SERPAPI_KEY')
        session_results = []

        for query in queries:
            if not query.strip():
                messages.error(request, "One or more queries are empty.")
                continue

            params = {
                "api_key": api_key,
                "engine": "google",
                "q": query,
                "num": 5
            }

            try:
                response = requests.get("https://serpapi.com/search", params=params)
                if response.status_code != 200:
                    messages.error(request, f"API Error {response.status_code} for {query}")
                    continue

                results = response.json().get("organic_results", [])
                if not results:
                    messages.warning(request, f"No results found for: {query}")
                    continue

                for item in results:
                    session_results.append({
                        "query": query,
                        "title": item.get("title", ""),
                        "link": item.get("link", ""),
                        "snippet": item.get("snippet", "")
                    })

            except Exception as e:
                messages.error(request, f"Error fetching results for '{query}': {e}")

        request.session['latest_results'] = session_results

    return render(request, 'search.html', {'results': request.session.get('latest_results', [])})


def download_csv(request):
    results = request.session.get('latest_results', [])
    if not results:
        return HttpResponse("No results available to download.", content_type="text/plain")

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="search_results.csv"'
    writer = csv.DictWriter(response, fieldnames=["query", "title", "link", "snippet"])
    writer.writeheader()
    for row in results:
        writer.writerow(row)
    return response
