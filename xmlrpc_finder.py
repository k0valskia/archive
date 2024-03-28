import requests 
from multiprocessing.dummy import Pool

class Domain:
    def __init__(self, domain):
        self.domain = domain

    def checkXMLRPC(self):
        userAgent = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0'}
        path = ["/xmlrpc.php", "/wp/xmlrpc.php", "/wordpress/xmlrpc.php"]
        for a in path:
            try:
                r = requests.get("http://"+self.domain+a)
                if "XML-RPC server accepts POST requests only." in r.text:
                    print(f"[{self.domain}] => XMLRPC OK!")
                    saveres = open("xlmrpc_ok.txt", "a")
                    saveres.write(self.domain+"\n")
                else:
                    print(f"[{self.domain}] => NO!")
                pass
            except:
                pass
        
    def process(self):
        website.checkXMLRPC()

def asuna(list):    
    global website
    website = Domain(list)
    website.process()

def main():
    print("""
Valid XMLRPC
By: Angga1337
    """)

    global selection
    try:
        urList = open(input("[List]: "), "r").read().replace("https://", "").replace("http://", "").replace("/", "").split("\n")
        thread = int(input("[Thread]: "))
        print("\n")
        pool = Pool(thread)
        pool.map(asuna, urList)
        pool.close()
        pool.join
    except:
        print("List not found!")

if __name__ == '__main__':
    main()

