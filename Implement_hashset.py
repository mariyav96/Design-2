{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import math\
class MyHashSet(object):\
\
    def __init__(self):\
       \
        self.bucket = int(math.sqrt(pow(10,6)))\
        self.bucketItems = int(math.sqrt(pow(10,6)))\
        self.storage = [False]*self.bucket\
        \
    def getBucket(self,key):\
        \
        return key % self.bucket\
    \
    def getBucketItem(self,key):\
        return key//self.bucketItems\
        \
\
    def add(self, key):\
        """\
        :type key: int\
        :rtype: None\
        """\
        bucket = self.getBucket(key)\
        bucketItem = self.getBucketItem(key)\
        \
        if(self.storage[bucket] == False):\
            if(bucket == 0):\
                self.storage[bucket] = [False] *(self.bucketItems+1)\
            else:\
                self.storage[bucket] = [False] *(self.bucketItems)\
       \
        self.storage[bucket][bucketItem] = True\
            \
      \
\
    def remove(self, key):\
        """\
        :type key: int\
        :rtype: None\
        """\
        \
        bucket = self.getBucket(key)\
        bucketItem = self.getBucketItem(key)\
        \
        if(self.storage[bucket] == False):\
            return False\
        else:\
            self.storage[bucket][bucketItem] = False\
            \
            \
\
    def contains(self, key):\
        """\
        :type key: int\
        :rtype: bool\
        """\
        bucket = self.getBucket(key)\
        bucketItem = self.getBucketItem(key)\
        \
        if(self.storage[bucket] == False):\
            return \
        else:\
            return self.storage[bucket][bucketItem]\
\
\
# Your MyHashSet object will be instantiated and called as such:\
# obj = MyHashSet()\
# obj.add(key)\
# obj.remove(key)\
# param_3 = obj.contains(key)}