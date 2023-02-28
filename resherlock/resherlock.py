import json

from modules.request import normal
from modules.write_file import FileWriter
from modules.handling import Handler


class ReSherlock:
    def __init__(self, settings):
        self.settings = settings
        self.output = []
        self.all = []
        self.data = self.get_data()

    def get_data(self):
        with open("./resherlock/data/sites.json", "r") as data:
            return json.loads(data.read())

    def run(self):
        for user in self.settings.target:
            if self.output != []:
                self.output = []
            print(f"Get Data for User {user}\n")
            for site in self.data['sites']:
                link = str(site['usersite']).format(user)
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
                for file in self.settings.output:
                    FileWriter(self.settings, self.output).write_txt(file)
        return self.output
