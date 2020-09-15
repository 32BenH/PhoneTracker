from pythonping import *

ip = "172.20.3.58"

def main():
    
    #This could slow someones internet down
    while True:
        output = ping(ip)
        responses = list(output._responses)
        response = responses[0].success and responses[1].success and responses[2].success and responses[3].success
        if response:
            print("Here")
        else:
            print("Not here")

if __name__ == '__main__':
    main()