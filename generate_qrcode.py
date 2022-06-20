import qrcode

client = {
    "cli1": "https://www.youtube.com",
    "cli2": "https://www.youtube.com",
    "cli3": "https://www.youtube.com",
    "cli4": "https://www.youtube.com",
    "cli5": "https://www.youtube.com",
    "cli6": "https://www.youtube.com",
    }

for list in client:
    links = client[list]
    image = qrcode.make(links) #menssage
    image.save(f"img/qrcode_{list}.jpg") # png or etc