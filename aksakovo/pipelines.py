# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

from itemadapter import ItemAdapter


class AksakovoPipeline:
    conn = sqlite3.connect('aksakovo.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `aksakovo` (
                                            title varchar(100),
                                            description text,
                                            date text
                                            )''')
        self.conn.commit()

    def process_item(self, item, spider):
        title = item['title'][0]
        description = item['description'][0]
        date = item['date'][0]

        self.cursor.execute(f"""select * from aksakovo where title = '{title}' and date = '{date}'""")
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            self.cursor.execute(f"""insert into `aksakovo`
                                        (`title`, `description`, `date`)
                                        values (?, ?, ?)""", (title, description, date))
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
