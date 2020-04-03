# encoding = utf-8
import numpy as np
import pandas as pd


def main():
    from sklearn.datasets import load_iris
    iris = load_iris()
    # 机器学习或者神经网络三个步骤：数据预处理 建模 验证

    # 预处理：将数据分为训练数据、预测数据
    from sklearn.model_selection import train_test_split
    # train 为训练集（待测数据及其对应结果） test_data为待预测数据 test_target为待预测数据的结果
    train_data, test_data, train_target, test_target = train_test_split(iris.data, iris.target, test_size=2, random_state=1)

    # 建模
    from sklearn import tree
    clf = tree.DecisionTreeClassifier(criterion='entropy')
    # 调用fit 获取模型
    clf.fit(train_data, train_target)
    # 根据模型获取预测值
    y_pred = clf.predict(test_data)

    # 验证 判断预测结果是否可行
    from sklearn import  metrics
    print(metrics.accuracy_score(y_true=test_target,y_pred=y_pred)) # 1 100%验证正确


if __name__ == '__main__':
    main()
