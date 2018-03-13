# -*- coding: utf-8 -*-

# Define your item pipelines here
#圖片下載部分（自動增量）
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
from baidu import settings
import os

#圖片下載類
class ImageDownloadPipeline(object):
    def process_item(self, item, spider):
        if 'image_urls' in item:#如何『圖片地址』在項目中
            images = []#定義圖片空集

            dir_path = '%s/%s/%s' % (settings.IMAGES_STORE, spider.name, item['image_type'][0])

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            for image_url in item['image_urls']:
                us = image_url.split('/')[3:]
                image_file_name = '_'.join(us)
                file_path = '%s/%s' % (dir_path, image_file_name)
                images.append(file_path)
                if os.path.exists(file_path):
                    continue

                with open(file_path, 'wb') as handle:
                    response = requests.get(image_url, stream=True)
                    for block in response.iter_content(1024):
                        if not block:
                            break

                        handle.write(block)

            item['images'] = images
        return item
