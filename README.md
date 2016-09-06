# bid_predictor
This project is a web application meant to predict the closing price of an eBay auction, given certain information about the auction/bids.

- Application is hosted on Google App Engine
- Can be accessed at bidpredictor.appspot.com
- GAE does not support the `pandas` library, so the parameters calculated using 'pandas' in `ebaydataframe.ipynb` 
have been temporarily hardcoded into `ebaybids_api.py` 
