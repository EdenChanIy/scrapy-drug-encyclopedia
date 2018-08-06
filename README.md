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


## 数据存储
当前爬虫默认将爬取数据以json的格式存放，运行爬虫后可以在项目根目录下看到data_tcm.json及data_wm.json文件
