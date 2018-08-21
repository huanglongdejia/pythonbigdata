# -*- coding: utf-8 -*-

import pandas as pd
# 数据集对象
class DataSet(object):
    def __init__(self,uid,mid,time,forward_count,comment_count,like_count,content):
        self.uid = uid
        self.mid = mid
        self.time = time
        self.forward_count = forward_count
        self.comment_count =comment_count
        self.like_count =like_count
        self.content =content

# 读取数据集
class DataSetOperator(object):
    def __init__(self,train_file_path,predict_file_path):
        self.train_file_path = train_file_path
        self.predict_file_path = predict_file_path
        self.trainSet = None
        self.prediceSet = None

    # 读取数据集
    def inital(self):
        # 数据训练的集合
        lines = [line for line in open(self.train_file_path,'r',encoding='utf-8')]
        dataSet = []
        column = ['uid','mid','time','forward_count','comment_count','like_count','content']
        for line in lines:
            p = line.strip().split('\t')
            if line.strip() == '' or len(p) != 7:
                continue
            dataSet.append(p)
        self.trainSet = pd.DataFrame(dataSet,columns=column)

        # 需要预测的数据
        lines2 = [line for line in open(self.predict_file_path,'r',encoding='utf-8')]
        dataSet2 = []
        column2 = ['uid','mid','time','content']
        for line in lines2:
            p = line.strip().split('\t')
            if line.strip() == '' or len(p) != 4:
                continue
            dataSet2.append(p)
        self.prediceSet = pd.DataFrame(dataSet2,columns=column2)

    def getDataset(self):
        lines = [line for line in open(self.train_file_path,'r',encoding='utf-8')]
        dataSet = []
        column = ['uid','mid','time','forward_count','comment_count','like_count','content']
        for line in lines:
            p = line.strip().split('\t')
            if line.strip() == '' or len(p) != 7:
                continue
            dataSet.append(p)

        return pd.DataFrame(dataSet,columns=column)

    # 获取所有训练的用户
    def getTotalUsers(self):
        users = set()
        for index,data in self.trainSet.iterrows():
            users.add(data['uid'])
        print("训练人数："+str(len(users)))
        return users

    # 获取预测的用户
    def getTrainingUsers(self):
        users = set()
        for index,data in self.prediceSet.iterrows():
            users.add(data['uid'])
        print("预测人数："+str(len(users)))
        return users



if __name__ == '__main__':
    # dataSetOperator = DataSetOperator('C:\\Users\huanglong\Desktop\Weibo Data\Weibo Data\weibo_train_data(new)\weibo_train_data.txt')
    dataSetOperator = DataSetOperator('C:\\Users\huanglong6\Downloads\Weibo Data\Weibo Data\weibo_train_data(new)\weibo_train_data.txt'
                                      ,'C:\\Users\huanglong6\Downloads\Weibo Data\Weibo Data\weibo_predict_data(new)\weibo_predict_data.txt')
    dataSetOperator.inital()
    # print(dataset)
    train_set = dataSetOperator.getTotalUsers()
    predict_set = dataSetOperator.getTrainingUsers()
    # 697个人的数据在训练集中没有
    print(len(predict_set - train_set))

