from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from api import APIHandler
import logging
from tornado.log import enable_pretty_logging

# Configure logs
enable_pretty_logging()

appLogHandler = logging.FileHandler('application.log')
appLog = logging.getLogger("tornado.application")
appLog.addHandler(appLogHandler)

accessLogHandler = logging.FileHandler('access.log')
accessLog = logging.getLogger("tornado.access")
accessLog.addHandler(accessLogHandler)

class StatusHandler(RequestHandler):
  def get(self):
    self.write({'message': 'Python server is up', 'status':'Active'})

def make_app():
  url = ("/status", StatusHandler)
  urls = APIHandler.getAPIs()
  urls.append(url)
  return Application(urls, debug=True)
  
if __name__ == '__main__':
    app = make_app()
    app.listen(4000)
    IOLoop.instance().start()