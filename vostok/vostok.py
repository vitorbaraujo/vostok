import datetime

class Vostok:
    def parse(file_path):
        print('Parse file {}'.format(file_path))

        f = open(file_path, 'r')
        content = f.read()

        return Parser(content)

class Parser:
    def __init__(self, content):
        self.content = content

    def entries(self):
        print('oi')

class TagEntry:
    def __init__(self, raw_version, raw_date=''):
        self.raw_date = raw_date
        self.date = self.get_date()
        self.unreleased = raw_version == "Unreleased"
        self.version = Version() if self.unreleased else Version(raw_version) 

    def get_date(self):
        if len(self.raw_date) == 0:
            return datetime.datetime.now()
        year, month, day = [int(i) for i in self.raw_date.split('-')]
        return datetime.datetime(year, month, day)

class Version:
    def __init__(self, raw_version='0.0.0'):
        self.raw_version = raw_version
        self.major, self.minor, self.patch = raw_version.split('.')
        

        

