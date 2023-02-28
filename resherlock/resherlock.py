import json

from modules.request import normal
from modules.write_file import FileWriter
from modules.handling import Handler


class ReSherlock:
    def __init__(self, settings, target):
        self.settings = settings
        self.all = []
        self.data = self.get_data()
        self.target = target
        self.output = []

    def get_data(self):
        with open("./resherlock/data/sites.json", "r") as data:
            return json.loads(data.read())

    def run(self):
        if self.output!=[]:
            self.output = []
            self.all = []
        print(f"Get Data for User {self.target}\n")
        for site in self.data['sites']:
            link = str(site['usersite']).format(self.target)
            if site['NSFW'] == "True" and not self.settings.nsfw:
                pass
            else:
                print(f"Checking {site['name']}...")
            status = normal(link)
            Handler(self.settings, self.all, self.output).handle(site, status, link)

        print("\n\n")
        if self.settings.print_all:
            self.output = sorted(list(set(self.all)))
        else:
            self.output = sorted(list(set(self.output)))

        if self.settings.output!=None:
            position = self.settings.target.index(self.target)
            FileWriter(self.settings, self.output).write_txt(self.settings.output[position])
        return self.output
