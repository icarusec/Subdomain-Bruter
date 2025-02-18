import dns
import time
import threading

#####################################
#Author :Icarusec
#Program : Subdomain Brute Force Tool
#Function : Brute forces and tests for subdomains using a pre-set wordlist
#####################################
def subdomain_enum(domain,wordlist,dns_timeout=1):

    def subdomain_resolve(subdomain_full):
        try:
            answers=dns.resolver.Resolver.query(subdomain_full, 'A')
            for answer in answers:
                printf("[+]Subdomain Found at : ",answer.address)
        except dns.resolver.NoAnswer:
            printf("Subdomain not found: ",subdomain_full)
        except dns.resolver.NXDOMAIN:
            printf("Subdomain not Found",subdomain_full)
        except dns.resolver.timeout:
            printf("DNS resolver timed out")

    threads=[]
    for word in wordlist:
        subdomain_full=word+"."+domain
        thread=threading.Thread(target=subdomain_resolve, args=(subdomain_full,))
        threads.append(thread)
        thread.start()
        time.sleep(dns_timeout)

def main():
    domain = input("Enter domain :")
    wordlistpath = input("Enter wordlist path :")
    with open(wordlistpath, "r") as f:
        wordlist=f.read().splitlines()
    dns_timeout = input("Enter DNS Timeout(default 1) :")
    subdomain_enum(domain,wordlist,dns_timeout)

if __name__ =="__main__":
    main()