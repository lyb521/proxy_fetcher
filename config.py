# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/3/8
# @Time: 16:45
# @Description: 配置文件


configs = {
    # mysql配置
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': 'root',
        'database': 'proxy',
        'table_prefix' : 'xb_',
        'charset':'utf8mb4'

    },
    'session': {
        'secret': 'AwEsOmE'
    }
}
