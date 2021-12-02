book={ }
book['tom'] = {
    'name':'tom',
    'address':'1 road , np',
    'phone': 56465464
}
book['bob']={
    'name': 'bob',
    'address': '2 raod,ny',
    'phone': 456454544
}
import json
s = json.dumps(book)
with open("F:\Python\working with json\data exchange.txt","w") as f:
    f.write(s)