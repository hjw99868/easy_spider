# tutorial
这是一个最简单傻瓜的spider，用来爬取豆瓣电影top250的信息，并没有用到数据库


！！！！！声明：这个spider真的很简单简单，高手们请自动忽略吧！！！！！


环境：python  scrapy   配置环境的方法自行百度
scrapy有官方文档，很贴心的是竟然有中文版，与scrapy相关的东西上面介绍的相当详细


命令：scrapy crawl dmoz -o 输出文件名.格式


如果大家有兴趣的话，可以尝试更改pipelines.py，把数据写入数据库。




