import whois,sys,socket
host_whois = whois.whois(sys.argv[1])
domain_emails = [host_whois.emails]
domain_ip = socket.gethostbyname(sys.argv[1])
ip_whois = whois.whois(domain_ip)
ip_emails = [ip_whois.emails]
emails = domain_emails + ip_emails
unique = []
abuse_emails = []
other_emails = []
for email in emails:
        if email not in unique:
                unique.append(email)
                if 'abuse' in email:
                        abuse_emails.append(email)
                else:
                        other_emails.append(email)

print("Abuse emails are: " + str(abuse_emails))
print("Other emails are: " + str(other_emails))
