

def mock_search_response(query):
    return {
        "docs": [
            {"key": "/works/OL1M", "author_name": ["Ann Patchett"]},
            {"key": "/works/OL2M", "author_name": ["Gail Honeyman"]},
            {"key": "/works/OL3M", "author_name": ["Fredrik Backman"]},
        ]
    }


def mock_book_details(work_key):
    fake_books = {
        "/works/OL1M": {
            "title": "Bel Canto",
            "subjects": ["Fiction", "Hostages", "Opera"],
            "description": "A birthday party is disrupted by a hostage situation, and unlikely bonds form between captors and captives.",
        },
        "/works/OL2M": {
            "title": "Eleanor Oliphant Is Completely Fine",
            "subjects": ["Fiction", "Loneliness", "Humor"],
            "description": "A socially awkward woman's carefully ordered life starts to unravel after a chance encounter.",
        },
        "/works/OL3M": {
            "title": "A Man Called Ove",
            "subjects": ["Fiction", "Grief", "Neighbors"],
            "description": "A grumpy widower's rigid routine is upended by a lively family moving in next door.",
        },
    }
    return fake_books.get(work_key, {
        "title": "Unknown Title",
        "subjects": [],
        "description": None,
    })