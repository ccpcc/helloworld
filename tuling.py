import urllib.request
import urllib.parse

def code(words):
    codes=words.encode("utf-8")
    result=[]
    for num in codes:
        b=str(hex(num)).strip("0x")
        b=b.upper()
        result.append(b)
    result="%".join(result)

def get_rpl(words):    
    url="http://www.tuling123.com/api/product_exper/chat.jhtml"
    data = {}
    data["info"]=words
    data["userid"]="e8610635-26fa-4821-b0f1-7b534dfc4b1b"
    data = urllib.parse.urlencode(data).encode('utf-8')
    head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    head["Cookie"]="SESSION=7d020fc0-c246-451c-a04f-341ca83c341b; CNZZDATA1000214860=1261911248-1499852027-null%7C1499852027; UM_distinctid=15d36672bf3262-07c1f6948142ea-572f7b6e-100200-15d36672bf539b"
    req=urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)
    htm=response.read().decode("utf-8")
    result=findword(htm)

    return result

def findword(htm):
    a=htm.find("Content")+17
    b=htm.find("/Content")-4
    return htm[a:b]

if __name__ == "__main__":
    while True:
        words=input("输入内容：")
        print(get_rpl(words))

