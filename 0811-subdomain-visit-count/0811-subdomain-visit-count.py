class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain_visit = {}
        for cpdomain in cpdomains:
            domain = list(cpdomain.split(" "))
            print(domain)
            
            domain_name = domain[1]
            for i in range(len(domain_name)-1, -1, -1):
                if domain_name[i] == '.':
                    if domain_name[i+1:] in subdomain_visit.keys():
                        subdomain_visit[domain_name[i+1:]] += int(domain[0])
                    else:
                        subdomain_visit[domain_name[i+1:]] = int(domain[0])
                        
                elif i == 0:
                    if domain_name[i:] in subdomain_visit.keys():
                        subdomain_visit[domain_name[i:]] += int(domain[0])
                    else:
                        subdomain_visit[domain_name[i:]] = int(domain[0])
                
        ans = []
        for domain in subdomain_visit:
            ans.append(str(subdomain_visit[domain]) + " " + str(domain))
            
        return ans
        
            
            
          
        