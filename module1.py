import urllib2
import json
import sys
import time
import multiprocessing
from cookielib import CookieJar
from urllib import urlencode

### Other 3rd party functions
def decrypt_caesar(text, shift):
    plain = ''
    for ch in text:
        if ch.isalpha():
            chint = ord(ch) + shift
            if chint > ord('z'):
                chint -= 26
            chd = chr(chint)
        else:
            chd = ch
        plain += chd
    return plain


def text2int(textnum, numwords={}):
    textnum = textnum.replace(',','').replace('-',' ')
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
              "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current



class HackerRank(multiprocessing.Process):
    def __init__(self, username, password, queue1, queue2):
        multiprocessing.Process.__init__(self)
        self.username = username
        self.password = password
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CookieJar()))
        self.base_url = 'https://www.hackerrank.com/{URI}.json'
        self.queue1 = queue1
        self.queue2 = queue2


    def _send(self, uri, data=None, method='POST'):
        if data == None:
            data = {}
        data['remote'] = 'true'
        url = self.base_url.replace('{URI}', uri)
        if method is not 'GET':
            request = urllib2.Request(url, data=urlencode(data))
            request.add_header('Content-Type', 'application/x-www-form-urlencoded')
            request.get_method = lambda: method
        else:
            request = url
        good = False
        while not good:
            try:
                response = self.opener.open(request)
                good = True
            except:
                pass
        data = json.loads(response.read())
        #print data
        return data


    def login(self):
        uri = 'users/sign_in'
        data = {
            'commit': 'Sign in',
            'user[login]': self.username,
            'user[password]': self.password,
            'user[remember_me]': 1
        }
        self._send(uri, data)


    def challenge1(self, start):
        '''Will automatically play the first challenge'''
        uri = 'splash/challenge'
        current = start
        data = self._send(uri, {'n': current})
        if 'current' in data:
            while current != 0:
                pick = current % 6
                if pick not in [1,2,3,4,5]:
                    pick = 1
                data = self._send(uri, {'move': pick}, 'PUT')
                current = int(data['game']['current'])
            if 'solved' in data['game']:
                print 'PID(%s) Job(C1,%s) done' % (self.pid, start)
        else:
            print 'PID(%s) Job(C1,%s) FAILED: %s' % (self.pid, start, data['message'])


    def challenge2(self, start):
        uri = 'game'
        num = -5
        while num == -5:
            data = self._send(uri, {'n': start})
            for shift in range(26):
                try:
                    text = decrypt_caesar(data['game']['cph_number'], shift)
                    num = text2int(text)
                    break
                except:
                    pass
        print 'PID(%s) Job(C2,%s) done' % (self.pid, start)
        resp = self._send(uri, {'answer': num, 'id': data['game']['id']}, 'PUT')        


    def userstats(self):
        uri = 'splash/userstats'
        return self._send(uri, method='GET')


    def run(self):
        self.login()
        for challenge, queue, name in [
            (self.challenge1, self.queue1, 'C1'), 
            (self.challenge2, self.queue2, 'C2'),
                ]:
            print 'PID(%s) %s' % (self.pid, name)
            stop = False
            fails = 0
            while not stop:
                try:
                    if not queue.empty():
                        job = queue.get_nowait()
                        challenge(job)
                    else:
                        stop = True
                except Exception, err:
                    fails +=1
                    print 'PID(%s) FAILED %s Times: %s' % (self.pid, fails, err)
                    if fails > 10:
                        stop = True
            print 'PID(%s) Terminated' % self.pid
        


if __name__ == '__main__':
    username = raw_input('Enter Username : ')
    password = raw_input('Enter Password : ')
    num_childs = int(raw_input('Enter Number of Children to Spawn : '))
    #num_childs = 10
    ch1 = raw_input('Do Challenge 1 (y/N): ')
    ch2 = raw_input('Do Challenge 2 (y/N): ')

    runstart = time.time()
    queue1 = multiprocessing.Queue()
    queue2 = multiprocessing.Queue()
    if ch1.lower() == 'y':
        for job in range(6,2561):
            queue1.put(job)
    if ch2.lower() == 'y':
        for job in range(10000):
            queue2.put(job)

    children = [HackerRank(username, password, queue1, queue2) for i in range(num_childs)]
    for child in children:
        child.start()
    for child in children:
        child.join()