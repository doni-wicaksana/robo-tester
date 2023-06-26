
class api_request:
    method = None
    url = None
    params = None
    headers = None
    body = None
    response = None

    def reset(self):
        self.method = None
        self.url = None
        self.params = None
        self.headers = None
        self.body = None
        self.response = None

    def set_request(self,method,url):
        self.method = method
        self.url = url
    def set_parameter(self,**kwargs):
        if self.params is None and kwargs: self.params = {}
        self.params.update(**kwargs)
    def set_header(self,**kwargs):
        if self.headers is None and kwargs: self.headers = {}
        self.headers.update(**kwargs)
    def set_body(self,**kwargs):
        if self.body is None and kwargs: self.body = {}
        self.body.update(**kwargs)
    
    def send_request(self):
        browserLib = Browser()
        # browserLib = BuiltIn().get_library_instance('Browser')
        browserLib.http(self.url,self.method)
