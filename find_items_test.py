import source_framework
import logging

logging.basicConfig(level=1)





source_framework.init()

#scope to the useless items
useless_items = source_framework.find().useless.items

#list them
useless_items.list()








