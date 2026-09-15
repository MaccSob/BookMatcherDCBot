import requests
import time
import os
from mockdata import mock_search_response, mock_book_details
from dotenv import load_dotenv
load_dotenv()

USE_MOCK_DATA = os.getenv("USE_MOCK_DATA", "false").lower() == "true"
headers = {"User-Agent": "BookMoodBot/1.0"}

def clean_subjects(subjects_list):
    if subjects_list is None:
        return []
    cleaned = []
    for tag in subjects_list:
        slowa = tag.split()
        zawiera_cyfre = False
        for znak in tag:
            if znak.isdigit():
                zawiera_cyfre = True
        if len(slowa) <= 4 and zawiera_cyfre == False:
            cleaned.append(tag)
    return cleaned[:15]


def get_book_details(work_key):
    if USE_MOCK_DATA:
        data2 = mock_book_details(work_key)
    else:
        url2 = f"https://openlibrary.org{work_key}.json"
        response2 = requests.get(url2, headers=headers)
        data2 = response2.json()

    raw_description = data2.get('description')
    if isinstance(raw_description, dict):
        description = raw_description.get('value')
    else:
        description = raw_description
    return {
        'title': data2.get('title'),
        'subjects': data2.get('subjects'),
        'description': description
    }

def search_books(query, limit=5):
    if USE_MOCK_DATA:
        data = mock_search_response(query)
    else:
     url = f"https://openlibrary.org/search.json?q={query}"
     response = requests.get(url, headers=headers)
     data = response.json()
    all_docs = data['docs']
    top_docs = all_docs[:limit]
    results = []
    for doc in top_docs:
        work_key = doc.get('key')
        time.sleep(0.3)
        dork = get_book_details(work_key)
        dork['author'] = doc.get('author_name')
        dork['subjects'] = clean_subjects(dork['subjects'])
        results.append(dork)
    return results



