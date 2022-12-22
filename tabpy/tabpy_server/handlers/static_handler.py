import base64
import binascii
import concurrent
import json
import logging
import tornado.web
import uuid




class BaseStaticHandler(tornado.web.StaticFileHandler):
    def set_extra_headers(self, path):        
        self.set_header("Strict-Transport-Security", "preload; max-age=2592000")
        
