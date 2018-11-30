#import modules
from bs4 import BeautifulSoup
import pickle
import re



#Open the HTML 
f = open("html", "rb")
hypixelhtml = pickle.load(f)

#create regEx patterns for permalinks and usernames 
permalinkRegEx = re.compile(r"posts\/(\d*)\/permalink")
usernameRegEx = re.compile(r"members\/(.*)\.(\d*)\/")



#create soup object
soup = BeautifulSoup(hypixelhtml, features="html.parser")

#prints out links for testing
permalinks = soup.select(".postNumber")
print(permalinks)
for permalink in permalinks:
    print(permalink.get("data-href"))

usernames = soup.select("div > .username")
for username in usernames:
    print(username.get("href"))


#prints permalink id
for permalink in permalinks:
    print(permalinkRegEx.search(str(permalink)).group(1))

#prints member name
for username in usernames:
    print(usernameRegEx.search(str(username)).group(1))

#prints member id    
for username in usernames:
    print(usernameRegEx.search(str(username)).group(2))


#saves to array
permalinkId = []
memberName = []
memberId = []
for permalink in permalinks:
    permalinkId.append(permalinkRegEx.search(str(permalink)).group(1))
for username in usernames:
    memberName.append(usernameRegEx.search(str(username)).group(1))
for username in usernames:
    memberId.append(usernameRegEx.search(str(username)).group(2))

#print arrays for testing
print(permalinkId, memberName, memberId, sep=",")

#prints dummy quote for testing
print(f'[QUOTE="{memberName}, post: {permalinkId}, member: {memberId}"][/QUOTE]')

#prints actual quote
print(f'[QUOTE="{memberName[0]}, post: {permalinkId[0]}, member: {memberId[0]}"][/QUOTE]')

#prints all quotes
for i in range(0, len(permalinkId)):
    print(f'[QUOTE="{memberName[i]}, post: {permalinkId[i]}, member: {memberId[i]}"][/QUOTE]')


#TODO set up file saving for easier copying
ff = open("quotes.txt", "w")
for i in range(0, len(permalinkId)):
    ff.write(f'[QUOTE="{memberName[i]}, post: {permalinkId[i]}, member: {memberId[i]}"][/QUOTE]\n')