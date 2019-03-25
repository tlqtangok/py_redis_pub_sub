# coding=utf-8
'''
Created on 2015-9-9
@author: Administrator
'''
import redis
pool=redis.ConnectionPool(host='localhost',port=6379,db=0)
r = redis.StrictRedis(connection_pool=pool)
while True:
    input_ = input("publish:")
    if input_ == 'over':
        print( 'no sub' )
        break;
    r.publish('channel', input_)
