import source_framework
import logging

# logging.basicConfig(level=1)


source_framework.init()

#scope to the useless items
useless_items = source_framework.find().useless.items

cool_useless_item = useless_items.cool.one
# cool_useless_item =  source_framework.find().cool.useless.items.one
# cool_useless_item =  source_framework.find().useless.cool.one


#list them
useless_items.list()








