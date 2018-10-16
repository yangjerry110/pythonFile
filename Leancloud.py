import leancloud
import logging
import pdb

appId = 'B9VuTB35pPfu9kCUKfA6zqQ7-gzGzoHsz'
appkey = 'Qu9ymPXvosXgXpsuCrsqRgUh'
thisTable = 'player'
leancloud.init(appId,appkey)

#插入数据
def insertData(data):
    theObject = leancloud.Object.extend(thisTable)
    insertObject = theObject()
    thisNameCount = searchData(data['name'])
    if thisNameCount == 0:
        for i in data:
            insertObject.set(i,data[i])
        insertObject.save()
    return True

#查找数据
def searchData(name):
    thisObject = leancloud.Object.extend(thisTable)
    query = thisObject.query
    query.equal_to('name',name)
    count = query.count()
    return count
