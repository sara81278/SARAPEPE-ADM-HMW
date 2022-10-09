from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for val in attrs:
                print("->",val[0],">",val[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for val in attrs:
                print("->",val[0],">",val[1])
                
parser = MyHTMLParser()
n = int(input())
if n >= 1:
    res = ''.join(input().strip() for _ in range(n))
parser.feed(res)
