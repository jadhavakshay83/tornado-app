import json
import hashlib
import constants
from utils.utilityFuntions import UtilityFuntions
from utils.cacheFunctions import CacheHandler
from tornado import gen
from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPError


class HttpClientHandler(RequestHandler):
    
    def __init__(self, businessTagId, relativeUrl, method, payload = None):
        self.businessTagId = businessTagId
        self.relativeUrl = relativeUrl
        self.method = method
        self.payload = payload

    def getConfig(self):
        with open('config/config.json', 'r') as f:
            config = json.load(f)
            return config
    
    def getUrl(self):
        if(UtilityFuntions.checkSubsStr(self.relativeUrl,constants.BUSINESS_TAG_ID)):
            self.relativeUrl = self.relativeUrl.replace(constants.BUSINESS_TAG_ID,self.businessTagId)
        config = self.getConfig()
        return config['API_PROTO'] + config['API_BASE_URL'] + '/' + config['API_VERSION'] + self.relativeUrl

    async def getHeaders(self):
        headers = {}
        loginToken = await self.getLoginToken()
        headers['Content-Type'] = 'application/json'
        headers['businessTagId'] = self.businessTagId
        headers['device'] = 'python'
        headers['jwt'] = loginToken
        return headers

    async def getLoginToken(self):
        loginToken = CacheHandler.getValue(self.businessTagId)
        if(loginToken == False):
            resp = await self.login()
            obj = json.loads(resp)
            loginToken = obj['loginToken']
            CacheHandler.setValue(self.businessTagId,loginToken)
        return loginToken
        
    async def login(self):
        config = self.getConfig()
        url = config['API_PROTO'] + config['API_BASE_URL'] + '/' + config['API_VERSION'] + constants.LOGIN_URL
        email = config['API_EMAIL']
        password = hashlib.sha512(config['API_PASS'].encode()).hexdigest() 
        http_client = AsyncHTTPClient()
        request = HTTPRequest(
            url = url,
            method = 'POST',
            user_agent = 'Python-Tornado',
            headers = {
                'Content-Type': 'application/json',
                'jwt':'true',
                'businessTagId': self.businessTagId
            },
            body = json.dumps({"email":email,"password":password})
        )
        try:
            response = await http_client.fetch(request)
        except Exception as e:
            print("Error: %s" % e)
        else:
            return response.body

    async def processRequest(self):
        headers = await self.getHeaders()
        url = self.getUrl()
        payload = json.dumps(self.payload)
        http_client = AsyncHTTPClient()
        if(self.method == 'POST'):
            request = HTTPRequest(
                url = url,
                method = self.method,
                user_agent = 'Python-Tornado',
                headers = headers,
                body = payload
            )
        else:
            request = HTTPRequest(
                url = url,
                method = self.method,
                user_agent = 'Python-Tornado',
                headers = headers
            )
        try:
            response = await http_client.fetch(request)
        except Exception as e:
            print("Error: %s" % e)
        else:
            return response.body
    