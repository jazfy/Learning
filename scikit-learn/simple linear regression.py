# 预测披萨价格并可视化
'''
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[6],[8],[10],[14],[18]]).reshape(-1,1) #尺寸
y = [7,9,13,17.5,18] #价格

plt.figure()
plt.title('披萨价格和尺寸关系')
plt.xlabel('尺寸')
plt.ylabel('价格')
plt.plot(X,y,'k.')
plt.axis([0,25,0,25])
plt.grid(True)
plt.show()
'''
# 开始使用 SLR

from sklearn.linear_model import LinearRegression
import numpy as np
X = np.array([[6],[8],[10],[14],[18]]).reshape(-1,1) #尺寸
y = [7,9,13,17.5,18] #价格
model = LinearRegression() #实例化
model.fit(X,y) #给模型传入训练参数

#简单预测一下
test_pizza = np.array([[12]])
predicted_price = model.predict(test_pizza)[0]
# print(predicted_price) #看看价格为13.681034482758623

# 评估和损失函数

# print(np.var(X,ddof=1)) #方差
# print(np.cov(X.transpose(),y)[0][1]) #协方差

#带有评估措施的完整写法

import numpy as np
from sklearn.linear_model import LinearRegression

X_train = np.array([[6],[8],[10],[14],[18]]).reshape(-1,1) #尺寸,训练集
y_train = [7,9,13,17.5,18] #价格,训练集

X_test = np.array([6,8,10,14,18]).reshape(-1,1) #测试集
y_test = [11,8.5,15,18,11] #测试集

model = LinearRegression() #实例化
model.fit(X_train,y_train) #给模型传入训练集参数

r_squared = model.score(X_test,y_test) #r平方指标评估模型
# print(r_squared)




