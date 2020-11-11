from cleo import Command
from parser import parse

class ConvCommand(Command):
    """
    Generate new file from donor file

    gen
        {name? : Which file do we start from?}
        {destination? : And where should the new file be placed?}
        {--p|poetry : If set, a pyproject.toml will be created}
        {--i|pipfile : If set, a pipfile will be created}
        {--r|requirements : If set, a requirements.txt will be created}
    """

    def handle(self):
        opt = 0
        file_name = self.argument('name')

        if file_name:
            text = 'Hello {}'.format(file_name)
        else:
            text = 'Hello'

        if self.option('poetry'):
            opt = 1

        elif self.option('pipfile'):
            opt = 2

        elif self.option('requirements'):
            opt = 3

        if(opt):
            parse(file_name,opt)
        else:
            self.line("A destination file option has to be provided! Check help for more details")
