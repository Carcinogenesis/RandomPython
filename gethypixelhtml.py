import sys
import requests
import pickle

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    rtxt = r.text
    f = open("html", "wb")
    pickle.dump(rtxt, f)
    f.close()
    import extractmemberlist
