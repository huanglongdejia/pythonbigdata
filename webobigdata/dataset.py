# -*- coding: utf-8 -*-
"""搭建语料库，及分词"""
import os
import os.path
import codecs

filePaths = []
fileContents = []
for root, dirs, files in os.walk(
        'C:\\Users\\huanglong6\\Downloads\\Weibo Data\\Weibo Data\\weibo_train_data(new)'
):
    for name in files:
        filePath = os.path.join(root, name)
        filePaths.append(filePath)
        f = codecs.open(filePath, 'r', 'utf-8')
        fileContent = f.read()
        f.close()
        fileContents.append(fileContent)

import pandas
corpos = pandas.DataFrame({
    'filePath': filePaths,
    'fileContent': fileContents
})
