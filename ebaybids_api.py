"""Hello World API implemented using Google Cloud Endpoints.

Contains declarations of endpoint, endpoint methods,
as well as the ProtoRPC message class and container required
for endpoint method definition.
"""
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

import os
import urllib
import pandas as pd
import random
from statsmodels.robust import scale
from sklearn import preprocessing
from sklearn.linear_model import SGDClassifier
from sklearn.cross_validation import StratifiedKFold, train_test_split
from sklearn.metrics import roc_auc_score, roc_curve

df = pd.read_csv('/Users/naina/Documents/Personal/Coding/ebay_auctions.csv')

df

def difference(x, y):
    return abs(x - y)

df['delta'] = difference(df['price'], df['openbid'])

byid = df.groupby('auctionid')

stats = {
    'bid': {
        'std_dev_bids': 'std',
        'average_bids': 'mean',
        'total_bids': 'count'
        },
    'delta': {
        'delta': 'mean'
    }
}

new_df = byid.agg(stats)
new_df.columns = new_df.columns.droplevel(level=0)
new_df

train, test = train_test_split(new_df, test_size = 0.4)
test

import statsmodels.formula.api as sm
result = sm.ols(formula="delta ~ average_bids + std_dev_bids", data=test).fit()
return result.params

# If the request contains path or querystring arguments,
# you cannot use a simple Message class.
# Instead, you must use a ResourceContainer class
REQUEST_CONTAINER = endpoints.ResourceContainer(
    message_types.VoidMessage,
    bidcount=messages.IntegerField(1),
    openbid=messages.IntegerField(2),
    lastbid=messages.IntegerField(3)
)

# package = 'Hello'


class Query(messages.Message):
    """string stores output message."""
    msg = messages.StringField(1)


@endpoints.api(name='ebaybidsendpoints', version='v1')
class EbayBidsApi(remote.Service):
    """EbayBidsApi API v1."""

    @endpoints.method(message_types.VoidMessage, Query,
      path = "noInput", http_method='GET', name = "noInput")
    def noInput(self, request):
      return Query(msg="No User Input Yet")

    @endpoints.method(REQUEST_CONTAINER, Query,
      path = "repeatInput", http_method='GET', name = "repeatInput")
    def repeat_input(self, request):
      summary = "The opening price was set at {}. There have been {} bids so far, the last of which was {}.".format(request.openbid, request.bidcount, request.lastbid)
      return Query(msg=summary)



APPLICATION = endpoints.api_server([EbayBidsApi])
