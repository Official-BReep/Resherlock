import httpx

r = httpx.get("https://de.wikipedia.org/wiki/Benutzer:GregorBungensheim")
print(r)