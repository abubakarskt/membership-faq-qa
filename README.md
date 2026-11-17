# Membership FAQ Q&A

A responsive single-page FAQ app built with Bootstrap 5, vanilla JavaScript, and Flask. Users can ask a question, and the page displays the matching answer with its source snippet from the sample Membership FAQ.

## What I did and why

- Created a responsive Bootstrap interface with an accessible question form, answer panel, and source block for a clear, readable experience.
- Added client-side empty-input validation so blank questions never reach the backend.
- Used `fetch('/ask', { method: 'POST', ... })` to send JSON to Flask, with friendly handling for HTTP errors and malformed JSON.
- Added a small sample FAQ backend so the end-to-end flow works locally without an external service.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open <http://localhost:5000> in your browser. Try “What are the club's membership fees?” or ask about benefits or renewal. An unsupported question shows a friendly message.

## Project files

- `app.py` — Flask page server and `/ask` JSON endpoint
- `index.html` — Bootstrap page markup
- `static/app.js` — validation, fetch, and rendering
- `static/style.css` — answer/source styling and responsive adjustments
- `requirements.txt` — Python dependencies
