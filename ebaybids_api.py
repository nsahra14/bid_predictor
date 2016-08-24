"""API implemented using Google Cloud Endpoints.

Contains declarations of endpoint, endpoint methods,
as well as the ProtoRPC message class and container required
for endpoint method definition.
"""
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote


# If the request contains path or querystring arguments,
# you cannot use a simple Message class.
# Instead, you must use a ResourceContainer class
REQUEST_CONTAINER = endpoints.ResourceContainer(
    message_types.VoidMessage,
    average=messages.IntegerField(1),
    std=messages.IntegerField(2),
    opening=messages.IntegerField(3)
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
      path = "calculateClosing", http_method='GET', name = "calculateClosing")
    def calculuate_Closing(self, request):
      #calculate delta from linear model
      closing = "{}".format(request.opening)
      return Query(msg=closing)



APPLICATION = endpoints.api_server([EbayBidsApi])
