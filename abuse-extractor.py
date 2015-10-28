import whois,sys,socket
host_whois = whois.whois(sys.argv[1])
if host_whois.emails != None:
        domain_emails = [host_whois.emails]
else:
        domain_emails = []
domain_ip = socket.gethostbyname(sys.argv[1])
ip_whois = whois.whois(domain_ip)
if ip_whois.emails != None:
        ip_emails = [ip_whois.emails]
else:
        ip_emails = []
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
