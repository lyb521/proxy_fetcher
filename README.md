## 代理IP采集器

### 项目采用scrapy编写
    执行pip install scrapy (python版本2.7以上，具体参考scrapy官方文档)

### 代码文件结构
    ============
    proxy_fetcher
    ===========================================
    proxy_fetcher
    |-- README.md---------------------使用说明文本
    |-- config.py---------------------配置文件
    |-- proxy.py--------------------- 调用代理的测试文件
    |-- proxy.sql---------------------数据库表结构
    |-- proxy_fetcher-----------------------采集蜘蛛
    |   |-- spiders-------------------- 各网站采集蜘蛛
    |   |-- filter.py------------------ 过滤器
    |   |-- items.py------------------- 采集字段配置
    |   |-- middlewares.py------------- 中间件
    |   |-- pipelines.py -------------- 管道，采集信息入库
    |   |-- settings.py---------------- 蜘蛛各种配置
    |-- start.py--------------------- 启动scrapy蜘蛛python脚本
    |-- start.sh---------------------启动scrapy蜘蛛shell脚本
    |-- verify.py---------------------校验数据库中代理ip可用性的shell脚本（添加crontab周期性运行）

### 联系

   个人主页：[https://www.leiyongbo.com](https://www.leiyongbo.com)

   github开源: https://github.com/lyb521
    
