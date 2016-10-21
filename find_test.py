import source_framework
import logging

# logging.basicConfig(level=1)

source_framework.init()
useless_files = source_framework.find().some.useless.files

useless_files.list()

useless_files.ok.do.write_to(name=lambda manager: manager.file.name + '.usefull.file')

