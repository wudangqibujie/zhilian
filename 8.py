import redis
# def redis_data(redis_database_name):
#     r = redis.Redis(host="localhost",port=6379)
#     def into_data(data):
#         r.sadd(redis_database_name,data)
#     return into_data
#
# a = redis_data("changshiyixia")
# print(a)
# print(type(a))
# a("https://www.cnblogs.com/wang-yc/p/5693288.html")

r = redis.Redis(host="localhost",port=6379)
sz = r.smembers("SZ_POSE_URLS")
sh = r.smembers("SH_POSE_URLS")
bj = r.smembers("BJ_POSE_URLS")
# print(sz[:10])
# print(sh[:10])
# print(bj[:10])
for i in range(10):
    print(str(sz.pop(),encoding="utf8"))
