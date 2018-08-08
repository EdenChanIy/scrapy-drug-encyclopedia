# QuotesBot
该爬虫分别在39健康网和12药房网爬取相关的中药材和中西成药的信息
修改自Scrapy文档中的Quotesbot例子

This project is only meant for educational purposes.


##爬取的数据
爬取的数据类型请参照items.py中的说明


## Spiders

This project contains two spiders and you can list them using the `list`
command:

    $ scrapy list
    toscrape-tcm
    toscrape-wm


## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl toscrape-tcm

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl toscrape-tcm -o quotes.json


## Pipeline

some pipelines are designed in pipelines.py, to turn on or turn off these pipelines, you can change the priority in settings.py, where:

    ITEM_PIPELINES = {
        'quotesbot.pipelines.QuotesbotPipeline': 300,
        'quotesbot.pipelines.ImagePipeline': 400,
        'quotesbot.pipelines.MySQLPipeline': 500,
    }


## 数据存储
当前爬虫默认将爬取数据以json的格式存放，运行爬虫后可以在项目根目录下看到data_tcm.json及data_wm.json文件


##爬取图片
本爬虫使用ImagesPipeline实现了从爬虫链接中爬取图片并保存在当前项目目录'/picture/full'当中，启动该管道需要在setting.py的ITEM_PIPELINES启动，并且要在setting.py中添加''IMAGES_STORE = './picture'''来设置存放路径，否则管道不会生效


##将数据存入到mysql中
将爬虫数据存放到mysql当中，要进行如下操作：
1. 本机安装mysql
2. 使用'pip install pymysql'命令安装pymsql依赖
3. 在mysql中根据爬取数据创建表
4. 在setting.py中设置数据库的连接参数，比如：
    ```python
    MYSQL_HOST = 'localhost'
    MYSQL_DBNAME = 'scrapy'
    MYSQL_USER = 'root'
    MYSQL_PASSWD = 'admin'
    MYSQL_PORT = 3306
    ```
5. ITEM_PIPELINES中启动对应的MySQLPipeline管道
