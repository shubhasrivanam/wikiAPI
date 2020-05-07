import json
import requests

url="https://en.wikipedia.org/w/api.php?action=opensearch&search="
i = 1
while i==1:
    print("Welcome to wikipedia's fake account")
    name = input("Enter the topic you want to search for: ")
    name.replace(" ", "_")
    tempurl = url+name
    request = requests.get(tempurl)
    data = request.json()
    print()
    wikiurl = "https://en.wikipedia.org/wiki/"+name
    print("For specific searches, choose one of the following");
    for i in range(len(data[1])):
        print(i, " ", data[1][i])
    num = int(input())
    search = data[1][num]
    print()
    furl="https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles="+search
    print("Incase you want the url:",wikiurl)
    print("\nAnd here you go, have fun reading");
    request3 = requests.get(furl)
    data3 = request3.json()
    lt=[]
    for (k,v) in data3['query']['pages'].items():
        lt.append(k)
    datafin = data3['query']['pages'][lt[0]]["extract"]
    print(datafin)

    print("\nWhat to learn some more?")
    print("Enter:")
    print("1: Continue, I love learning")
    print("0: Exit, Im exausted!")
    i = int(input())
if(i==0):
    print("Hope you had fun!")
