
class Handler:
    def __init__(self, settings, all, output):
        self.settings = settings
        self.all = all
        self.output = output

    def handle(self,site, status, check):
        if self.settings.print_all:
            if self.settings.nsfw:
                self.all.append(
                    f"{site['name']}:  \t{check}(Status code: {status}{',NSFW' if site['NSFW'] == 'True' else ''})")
            if not self.settings.nsfw:
                if site['NSFW'] == "False":
                    self.all.append(f"{site['name']}:  \t{check}(Status code: {status})")
        else:
            if status == 200:
                if not self.settings.nsfw:
                    if site['NSFW'] == "False":
                        self.output.append(f"{site['name']}:  \t{check}")
                else:
                    self.output.append(f"{site['name']}:  \t{check}")