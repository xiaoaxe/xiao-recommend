#!/usr/bin/env python
# encoding: utf-8

"""
@description: 文件路径

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: pth.py
@time: 2017/1/11 15:10
"""

import os
from os.path import abspath, dirname
import logging

FILE_PATH = dirname(abspath(__file__)) + os.sep + 'file' + os.sep
LOG_PATH = dirname(abspath(__file__)) + os.sep + 'log' + os.sep

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # filename='/mnt/work/nlptrain/logs/spider.log',
                    # filemode='a'
                    )