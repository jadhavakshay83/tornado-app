from tornado.web import RequestHandler
from httpClient import HttpClientHandler
import json
import constants


class FunctionHandler:
    @staticmethod
    async def get_master_entry(formID,payload=None):
        httpClient = HttpClientHandler(businessTagId = "42FNCQGRPLJJ6", relativeUrl = constants.MASTER_SEARCH.format(businessTagId="42FNCQGRPLJJ6",formID=formID), method = "POST",payload=payload)
        resp=await httpClient.processRequest()
        if json.loads(resp)["error"]==True:
            return []
        else:
            return json.dumps(json.loads(resp)["data"]["result"])

