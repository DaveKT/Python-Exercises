#Sean Brewer

import operator, urllib.request, urllib.error, urllib.parse
from functools import reduce

class clientlib:
    
    def __init__(self,clientname,emailaddr):
        
        self.MIN_MAX_LEN = 10000000000
        self.MIN_NUM_LEN = 1
        self.MAX_NUM_LEN = 100000
        self.MIN_COL_LEN = 1
        self.MAX_COL_LEN = 10000000000
        self.MIN_STR_LEN = 1
        self.MAX_STR_LEN = 20
        self.useragent = "client using pyRandomdotOrg: %s | email addr: %s" % (clientname,emailaddr)


    def IntegerGeneratorList(self,num,nmin,nmax,col=1,base=10,rnd="new"):
        #Perform checks
        if self.QuotaChecker() < 0:
            print("You have a negative quota. Try your request again in ten minutes.")
            return None
        if num < self.MIN_NUM_LEN or num > self.MAX_NUM_LEN:
            return None
        if nmin < -self.MIN_MAX_LEN or nmin > self.MIN_MAX_LEN:
            return None
        if nmax < -self.MIN_MAX_LEN or nmin > self.MIN_MAX_LEN:
            return None
        if nmin > nmax:
            return None
        if col < self.MIN_COL_LEN or col > self.MAX_COL_LEN:
            return None
        if reduce(operator.and_,[base != 2, base != 8, base != 10, base != 16]) == True:
            return None
        numlst = []
        url = "http://www.random.org/integers/?num=%d&min=%d&max=%d&col=%d&base=%d&format=plain&rnd=%s" \
            % (num,nmin,nmax,col,base,rnd)
        req = urllib.request.Request(url)
        req.add_header('User-Agent',self.useragent)
        opener = urllib.request.build_opener()
        u = opener.open(req)
        list(map(lambda i: [numlst.append(int(j)) for j in i.split()],u.readlines()))
        return numlst

    def IntegerGenerator(self,nmin,nmax,base=10,rnd="new"):
        if self.QuotaChecker() < 0:
            print("You have a negative quota. Try your request again in ten minutes.")
            return None
        return self.IntegerGeneratorList(1,nmin,nmax,1,base,rnd)[0]


    def SequenceGenerator(self,nmin,nmax,rnd="new"):
        if self.QuotaChecker() < 0:
            print("You have a negative quota. Try your request again in ten minutes.")
            return None
        if nmin < -self.MIN_MAX_LEN or nmin > self.MIN_MAX_LEN:
            return None
        if nmax < -self.MIN_MAX_LEN or nmin > self.MIN_MAX_LEN:
            return None
        if (nmax-nmin) + 1 > 10000:
            print("The sequence interval requested is too large.")
            return None
        url = "http://www.random.org/sequences/?min=%d&max=%d&format=plain&rnd=%s" % (nmin,nmax,rnd)
        req = urllib.request.Request(url)
        req.add_header('User-Agent',self.useragent)
        opener = urllib.request.build_opener()
        u = opener.open(req)
        return list(map(int,u.readlines()))

    def StringGenerator(self,num,len,digits=True,upperalpha=True,loweralpha=True,unique=True,rnd="new"):
        if self.QuotaChecker() < 0:
            print("You have a negative quota. Try your request again in ten minutes.")
            return None
        if num < self.MIN_NUM_LEN or num > self.MAX_NUM_LEN:
            return None
        if len < self.MIN_STR_LEN or len > self.MAX_STR_LEN:
            return None
        sdigits = "on" if digits == True else "off"
        supperalpha = "on" if upperalpha == True else "off"
        sloweralpha = "on" if loweralpha == True else "off"
        sunique = "on" if unique == True else "off"
        url = "http://www.random.org/strings/?num=%d&len=%d&digits=%s&upperalpha=%s&loweralpha=%s&unique=%s&format=plain&rnd=%s" % (num,len,sdigits,supperalpha,sloweralpha,sunique,rnd)
        req = urllib.request.Request(url)
        req.add_header('User-Agent',self.useragent)
        opener = urllib.request.build_opener()
        u = opener.open(req)
        return [i.rstrip("\n") for i in u.readlines()]

    def RandomString(self,len,digits=True,upperalpha=True,loweralpha=True,unique=True,rnd="new"):
        if self.QuotaChecker() < 0:
            print("You have a negative quota. Try your request again in ten minutes.")
            return None
        return self.StringGenerator(1,len,digits,upperalpha,loweralpha,unique,rnd)[0]

    #If you want to check the quota of another IP, you must
    #pass the desired IP address to the function as a string.
    def QuotaChecker(self,ipaddr=None):
        if ipaddr == None:
            url = "http://www.random.org/quota/?format=plain"
            req = urllib.request.Request(url)
            req.add_header('User-Agent',self.useragent)
            opener = urllib.request.build_opener()
            u = opener.open(req)
            return int(u.readlines()[0])
        else:
            url = "http://www.random.org/quota/?ip=%s&format=plain" % (ipaddr)
            req = urllib.request.Request(url)
            req.add_header('User-Agent',self.useragent)
            opener = urllib.request.build_opener()
            u = opener.open(req)
            return int(u.readlines()[0])

