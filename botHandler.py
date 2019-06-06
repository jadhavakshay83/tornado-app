from tornado.web import RequestHandler
from httpClient import HttpClientHandler
import json
import constants

class BotHandler(RequestHandler):
  async def get(self):
    httpClient = HttpClientHandler(businessTagId = "42FNCQGRPLJJ6", relativeUrl = "/user/tasks/get/"+constants.BUSINESS_TAG_ID, method = "GET")
    resp = await httpClient.processRequest()
    self.write(resp)
    self.write({'message': 'Bot handler called', 'status':'Active'})