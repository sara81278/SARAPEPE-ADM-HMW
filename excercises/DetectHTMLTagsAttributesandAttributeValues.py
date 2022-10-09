from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        
        for elem in attrs:
            print("->", elem[0], ">", elem[1])
     
    
parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
