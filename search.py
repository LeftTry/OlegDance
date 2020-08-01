import webbrowser

def search(s):
        for i in range(0, len(s)):
                if s[i] == "+":
                        s = s[:len(s) - i] + "%2B" + s[i:]

        url = "https://www.google.com/search?q=" + s
        webbrowser.open(url)
