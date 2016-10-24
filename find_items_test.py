import source_framework
from source_framework.models.components import SourceFile
from source_framework.source_manager.source_indexer import SourceIndexer
import logging

# logging.basicConfig(level=1)


source_framework.init()

#scope to the useless items
useless_items = source_framework.find().useless.items # type: SourceIndexer

cool_useless_item = useless_items.cool.one # type: SourceFile



# cool_useless_item =  source_framework.find().cool.useless.items.one
# cool_useless_item =  source_framework.find().useless.cool.one



#list them
useless_items.list()








