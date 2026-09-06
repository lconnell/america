# Sofia’s American Adventure

A responsive first-time USA itinerary for September 9–23, 2026: Los Angeles, Las Vegas and New York City.

Live site: https://lconnell.github.io/america/

## Edit and preview

The site is dependency-free static HTML, CSS and JavaScript. Python 3.12+ is used to generate the HTML from the itinerary in `scripts/build.py`.

- `npm run build` regenerates `index.html`.
- `npm run check` verifies dates, links, local assets and trip constraints.
- `npm run dev` serves the folder on http://127.0.0.1:4173/.

`npm` is optional: the scripts can also be run directly with Python. Deployment runs via GitHub Actions on pushes to `main`.

## Planning assumptions

- September 23 is the departure day; hotel and flight details are not yet supplied.
- Three LA nights, three Las Vegas nights and eight NYC nights.
- The helicopter experience is in NYC only: September 18 primary, September 19 the only backup. No Grand Canyon excursion.
- All schedule windows and budgets are estimates, not reservations or live quotes.
- Primary travel sources and Unsplash photographer credits are linked on the page.

## Implementation

All 15 days are present in static HTML and can be expanded without JavaScript. JavaScript adds expand/collapse-all and a print action that opens every day and restores the previous view afterward. Photos are stored locally; Google Fonts is optional, with system and serif fallbacks. No tracking or user data collection.
