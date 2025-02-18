import threading
import requests
import time
import queue

def directory_buster(url,wordlist,queue):
    with open(wordlist,'r') as f:
        for line in f:
            full_url=url+"/"+line
            print("Trying :",full_url) 
            try:
                response=requests.get(full_url, timeout=5)
                if response.status_code == 200:
                    q.put((path, response.text))
            except requests.exceptions.RequestException:
                pass

def start_threads(url, wordlist, num_threads):
    q = queue.Queue()
    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=directory_buster, args=(url, wordlist, q))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    
    while not q.empty():
        path, content = q.get()
        print("Found Directory :", path)

if __name__ == "__main__":
    url=input("Enter the URL :")
    wordlist = input("Enter the wordlist path :")
    num_threads=int(input("Enter the number of threads :"))

    start_threads(url,wordlist,num_threads)
                    
    
    

