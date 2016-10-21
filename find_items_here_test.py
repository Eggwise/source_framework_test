import source_framework
from source_framework.models.components import SourceFile
from source_framework.source_manager.source_indexer import SourceIndexer
import logging

# logging.basicConfig(level=1)


source_framework.init()

#scope to the useless items
items_here = source_framework.find().items.here # type: SourceIndexer
items_here.list()

#useless WOW


# I am here!


#useless.end



item_here = items_here.one # type: SourceFile

print('PRINT SOURCE OF ITEM HERE')
print(item_here.source)







