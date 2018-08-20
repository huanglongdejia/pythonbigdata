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
    def __init__(self,file_path):
        self.file_path = file_path

    def getDataset(self):
        lines = [line for line in open(self.file_path,'r',encoding='utf-8')]
        dataSet = []
        column = ['uid','mid','time','forward_count','comment_count','like_count','content']
        for line in lines:
            p = line.strip().split('\t')
            if line.strip() == '' or len(p) != 7:
                continue
            dataSet.append(p)

        return pd.DataFrame(dataSet,columns=column)

if __name__ == '__main__':
    dataSetOperator = DataSetOperator('C:\\Users\huanglong\Desktop\Weibo Data\Weibo Data\weibo_train_data(new)\weibo_train_data.txt')
    dataset = dataSetOperator.getDataset()
    print(dataset)

