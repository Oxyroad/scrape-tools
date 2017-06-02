# scrape-tools

Tools used to scrape Warsaw-related data from online API.

## Usage

1. Download appropriate archive from [this website](http://www.ztm.waw.pl/?c=628&l=1), extract it.
2. Run `./ztm_extract.py archive.txt stations.csv` (the second argument is filename of generated file).
3. Set `APIKEY` environment variable and run `python green_scraper.py`.
4. Create appropriate SQLite databases. See `./buses/create_db.py` for details.
5. Run `./buses/dump.py` and `./trams/dump.py` every minute for a month or so to gather enough data. (We used good old `watch` in background on a cheap VPS.)
