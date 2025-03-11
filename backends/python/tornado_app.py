import tornado.ioloop
import tornado.web
import json
from logic import average, compute, multiply


class AverageHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        result = average(**data)
        self.write({"status": "success", "data": result})

class ComputeHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        result = compute(**data)
        self.write({"status": "success", "data": result})

class MultiplyHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        result = multiply(**data)
        self.write({"status": "success", "data": result})


app = tornado.web.Application([

    (r"/average", AverageHandler),

    (r"/compute", ComputeHandler),

    (r"/multiply", MultiplyHandler),

])

app.listen(8000)
tornado.ioloop.IOLoop.current().start()