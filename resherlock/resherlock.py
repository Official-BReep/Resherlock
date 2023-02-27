import json
import os

import httpx
import more_termcolor


class ReSherlock:
    def __init__(self, settings):
        self.settings = settings
        self.output = []
        self.all = []
        self.data = self.get_data()

    def get_data(self):
        with open("./resherlock/data/sites.json", "r") as data:
            return json.loads(data.read())

    def test(self, url):
        try:
            response = httpx.get(url)
            if "codechef" in url:
                if "The username specified does not exist in our database" in str(response.content):
                    return False
            return response.status_code  # To print http response code
        except:
            return False


    def run(self):
        for user in self.settings.target:
            for site in self.data['sites']:
                print(f"Checking {site['name']}...")
                check = str(site['usersite']).format(user)
                status = self.test(check)
                if self.settings.print_all:
                    if self.settings.nsfw:
                        self.all.append(f"{site['name']}:  \t{check}(Status code: {status}{',NSFW' if site['NSFW']=='True' else ''})")
                    if not self.settings.nsfw:
                        if site['NSFW'] == "False":
                            self.all.append(f"{site['name']}:  \t{check}(Status code: {status})")
                else:
                    if status==200:
                        if not self.settings.nsfw:
                            if site['NSFW'] == "False":
                                self.output.append(f"{site['name']}:  \t{check}")
                        else:
                            self.output.append(f"{site['name']}:  \t{check}")

        print("\n\n")
        if self.settings.print_all:
            self.output = sorted(list(set(self.all)))
        else:
            self.output = sorted(list(set(self.output)))

        if self.settings.output!=None:
            self.write_output()
        return self.output

    def write_output(self,):
        file = self.settings.output
        if os.path.exists(file):
            os.remove(file)
        with open(file, "a+") as output_file:
            for line in self.output:
                output_file.write(line+"\n")
