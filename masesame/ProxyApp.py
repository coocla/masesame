#coding:utf-8
import os
import sys
from masesame.model.context import Context
from masesame.common.FileUtil import FileUtil
from masesame.AMQPProxy import AMQPProxyService
from sesame.common.logger import LoggerFactory
logger = LoggerFactory.getLogger(__name__)

class ProxyServer(object):
    def __init__(self, proxy_json):
        self.proxy_json = proxy_json

    def start(self):
        logger.info("Start AMQPProxy Service!")
        if not os.path.exists(self.proxy_json):
            logger.error("%s no such file or directory" % self.proxy_json)
            sys.exit(6)
        context = Context.fromJSON(FileUtil.readContent(self.proxy_json))
        proxyService = AMQPProxyService(context)
        proxyService.run()

if __name__ == '__main__':
    proxy = ProxyServer('/data/masesame/etc/proxy.json')
    proxy.start()
