# checks to see if there is an internet connection

try:
    import httplib
except:
    import http.client as httplib

def have_internet():
    conn = httplib.HTTPConnection('www.google.com', timeout5)
    try:
        conn.request('Head', '/')
        conn.close()
        return True
    except:
        conn.close()
        return False

