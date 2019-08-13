from tornado.web import RequestHandler
from httpClient import HttpClientHandler
import json
import constants
from FunctionHandler import FunctionHandler


class BotHandler(RequestHandler):
  async def get(self):
    # httpClient = HttpClientHandler(businessTagId = "42FNCQGRPLJJ6", relativeUrl = "/user/tasks/get/"+constants.BUSINESS_TAG_ID, method = "GET")
    # resp = await httpClient.processRequest()
    payload=[
        {
            "FieldLabel": "OYO ID",
            "Value": "FAR040"}]
    resp=await FunctionHandler.get_master_entry(formID="5",payload=payload)
    self.write(resp)
    self.write({'message': 'Bot handler called', 'status':'Active'})

