"""API implemented using Google Cloud Endpoints.

Contains declarations of endpoint, endpoint methods,
as well as the ProtoRPC message class and container required
for endpoint method definition.
"""
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
#import ebaydata 

# If the request contains path or querystring arguments,
# you cannot use a simple Message class.
# Instead, you must use a ResourceContainer class
REQUEST_CONTAINER = endpoints.ResourceContainer(
    message_types.VoidMessage,
    average=messages.FloatField(1),
    std=messages.FloatField(2),
    opening=messages.FloatField(3)
)

package = 'Bid'


class Bid(messages.Message):
    """string stores output message."""
    msg = messages.StringField(1)
    opening = messages.FloatField(2)
    delta = messages.FloatField(3)
    closing = messages.FloatField(4)




@endpoints.api(name='ebaybidsendpoints', version='v1')
class EbayBidsApi(remote.Service):
    """EbayBidsApi API v1."""

    #@endpoints.method(message_types.VoidMessage, Bid,
    #  path = "noInput", http_method='GET', name = "noInput")
    #def noInput(self, request):
    #  return Bid(msg="No User Input Yet")

    @endpoints.method(REQUEST_CONTAINER, Bid,
      path = "calculateClosing", http_method='GET', name = "calculateClosing")
    def calculuate_Closing(self, request):
      #calculate delta from ols model
      o = float(request.opening)
      d = (-0.224271) + (0.066683*request.average) + (3.070601*request.std)
      c = o + d
      retval = Bid(msg = "success", 
        opening = o, 
        delta = d, 
        closing = c)

      return retval



APPLICATION = endpoints.api_server([EbayBidsApi])
