import json
import os

with open("./resherlock/data/sites.json", "r") as data_file:
    data = json.loads(data_file.read())

# Read the data.json file
def sort_json():

    with open("./resherlock/data/sites.json", "w") as data_file:
        data['sites'] = sorted(data['sites'], key=lambda x: x['name'], reverse=False)
        sorted_data = json.dumps(data, indent=4)
        data_file.write(sorted_data)
        data_file.write("\n")
    return "List sorted successfully"

def supported():
    all = ""
    all+=(f"-----Supported Sites ({len(data['sites'])})-----\n\n")
    for i in data['sites']:
        all+=f"{i['name']}  \t  |\t{i['mainsite']}\n"

    return all

def genmd():
    open("supported.md", "w").write("")
    with open("supported.md", "a+") as supported_file:
        supported_file.write("## Supported Websites:\n\n")
        for site in data['sites']:
            print(f"Write hyperlink for {site['name']} into file")
            string = f"+ [{site['name']}]({site['mainsite']}) "
            if site["NSFW"]=="True":
                string+= "(NSFW)"
            string+="\n"
            supported_file.write(string)
    return "List generated"
