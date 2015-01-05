from __future__ import unicode_literals

import os

from mopidy import config, ext

__version__ = '1.1.1'

class MopifyExtension(ext.Extension):
    dist_name = 'Mopidy-Mopify'
    ext_name = 'mopify'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def setup(self, registry):
        registry.add('http:static', {
            'name': self.ext_name,
            'path': os.path.join(os.path.dirname(__file__), 'static'),
            'factory': mopify_app_factory,
        })   

class WebMopifySelfUpdateHandler(tornado.web.RequestHandler):

    def initialize(self, core):
        self.core = core

    def post(self):
        str("Post request")

def mopify_app_factory(config, core):
    return [
        ('/update', WebMopifySelfUpdateHandler, {'core': core}),
    ]