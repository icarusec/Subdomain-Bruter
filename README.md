# Subdomain-Brute-Force 

The Subdomain Enumeration Script is a Python tool designed for the purpose of discovering subdomains associated with a given domain. Subdomains can often hide valuable information about a target's infrastructure, potentially exposing vulnerabilities or providing insights into the organization's digital footprint. This script automates the process of searching for subdomains by systematically checking a list of potential subdomain names against the target domain.

Features:

    Multi-threaded Execution: The script utilizes threading to parallelize the subdomain enumeration process, enhancing efficiency by concurrently processing multiple subdomain checks.

    Wordlist-based Enumeration: It accepts a wordlist file containing a list of potential subdomain names as input. Each word in the wordlist is appended to the target domain to form a potential subdomain for verification.

    Socket-based Domain Resolution: Utilizes Python's socket module to resolve domain names into IP addresses. If a subdomain resolves to a valid IP address, it is considered as a discovered subdomain.

    User Interaction: The script interacts with the user through the command-line interface (CLI) for inputting the target domain, wordlist filename, and the number of threads to be used for concurrent execution.

    Thread Safety: Implements thread safety using Python's threading.Lock to prevent race conditions when accessing shared resources.

Usage:

    Input Prompt: Upon execution, the script prompts the user to input the target domain, the filename of the wordlist containing potential subdomains, and the number of threads to use for enumeration.

    Enumeration Process: The script then spawns multiple threads, each responsible for checking a subset of potential subdomains against the target domain.

    Subdomain Discovery: Discovered subdomains are printed to the console in real-time as they are found during the enumeration process.

    Completion: Once all threads have finished execution, the script displays a summary of the discovered subdomains.
