import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import matplotlib.pyplot as plt


RANDOM_STATE = 55 ## We will pass it to every sklearn call so we ensure reproducibility

"""Context:
* Bệnh tim mạch(CVDs) là một trong những nguyên nhângây tử vong trên toàn cầu, cướp đi ước tính 17.9 triệu sinh mạng mỗi năm, chiếm 31% tổng số ca tử vong trên toàn thế giới.
* Bống trong 5 ca tử vong do CVD là nhồi máu cơ tim, đột quỵ, một phần 3 trong số ca tử vong này xảy ra sớm ở những người dưới 70 tuổi....
* Tập dữ liệu này chứa 11 đặc trưng có thể dự đoán khả năng mắc bệnh tim
* Chúng ta huấn luyên mô hình MK nhằm hỗ trợ chuẩn đoán căn bệnh này

===> Bài toán chuẩn đoán căn bệnh tim"""

"""Thông tin thuộc tính:
* Age: tuổi bệnh nhân
* Sex: giới tính bệnh nhân
* ChestPainType: loại đau ngực 
   * TA(Typical Angina): đau thắt ngực điển hình
   * ATA(Atypical Angina): thắt ngực không điển hình
   * NAP(Non- Anginal Pain): đau ngực không do tim
   * ASY(Asymptomatic): Không có triệu chứng
* RestingBP: Huyết áp lúc nghỉ mmHg
* Cholesterol: Cholesterol huyết thanh mm/dl
* FastingBS: Đường huyết lúc đói
   * 1: nếu FastingBS > 12 mg/dl
   * 0: ngược lại
* RestingECG: kết quả điện tâm đồ lúc nghỉ
   * Normal: bình thường
   * ST: Có bất thường ST-T (Đảo sóng T và hoặc ST chênh lên hoặc chênh xuống > 0.05mV)
   * LVH: có khả năng hoặc xác định phì đại thất trái theo chuẩn Estes
* MaxHR
* ExerciseAngina
* Oldpeak
* St_Slope
* HeartDisease"""

"""Vì các biến sex, chespainType, restingecg, exerciseAngina,St_slope là các biến phân loại
==> ta dùng one-hot mã hóa chúng"""

#load dataset bằng pandass
df = pd.read_csv("./Machine Learning/Advanced Learning Algorithms/heart.csv")
print(df.head())

#sử dụng pandas để mã hóa 5 đặc trưng phân loại
cat_variables = ['Sex','ChestPainType','RestingECG','ExerciseAngina','ST_Slope']
"""prefix: giúp gán nhãn cho các cột mới để mỗi giá trị được mã hóa đều sẽ biết nó thuộc biến nào"""

df = pd.get_dummies(data = df, prefix = cat_variables, columns= cat_variables)
print(df.head())

#lựa chọn các biến làm đặc trưng đầu vào X và tách biến mục tiêu y
features = [x for x in df.columns if x not in 'HeartDisease']

print(len(features)) #số đặc trưng đầu vào

#Splitting the dataset(chia tập dữ liệu huấn luyện và kiểm tra)

#help(train_test_split)
X_train, X_val, y_train, y_val = train_test_split(df[features], df['HeartDisease'],train_size=0.8, random_state= RANDOM_STATE)
print(f"train sample: {len(X_train)}")
print(f"validation sample: {len(X_val)}")
print(f"target proportion: {sum(y_train)/len(y_train):.4f}")

#xây dựng mô hình 
"""1. Decision Tree, sử dụng sklearn
min_samples_split_list = [2,10,30,50,100,200,300,700] # danh sách các giá trị min_samples_split để thử nghiệm
max_depth_list = [1,2,3,4,8,16,32,64, None] # danh sách các giá trị max_depth để thử nghiệm

accuracy_list_train = [] # chứa độ chính xác trên tập huấn luyện
accuracy_list_val = [] # chứa độ chính xác trên tập kiểm tra

for min_samples_split in min_samples_split_list: 

    model = DecisionTreeClassifier(min_samples_split=min_samples_split, random_state=RANDOM_STATE)# khởi tạo mô hình Decision Tree với tham số min_samples_split và random_state
    model.fit(X_train, y_train) # huấn luyện mô hình trên tập huấn luyện

    predictions_train = model.predict(X_train)#dự đoán giá trị trên tập huấn luyện
    predictions_val = model.predict(X_val) # dự đoán giá trị trên tập kiểm tra
    accuracy_train = accuracy_score(predictions_train, y_train) # tính độ chính xác trên tập huấn luyện
    accuracy_val = accuracy_score(predictions_val, y_val) # tính độ chính xác trên tập kiểm tra
    accuracy_list_train.append(accuracy_train)# thêm độ chính xác vào danh sách
    accuracy_list_val.append(accuracy_val) # thêm độ chính xác vào danh sách

plt.title("Train x Validation metrics")
plt.xlabel("min_samples_split")
plt.ylabel("accuracy")
plt.xticks(ticks = range(len(min_samples_split_list )), labels=min_samples_split_list)
plt.plot(accuracy_list_train)
plt.plot(accuracy_list_val)
plt.legend( ['train', 'validation'])
#plt.show()

for max_depth in max_depth_list:
    model = DecisionTreeClassifier(max_depth=max_depth, random_state=RANDOM_STATE).fit(X_train, y_train)

    predictions_train = model.predict(X_train)
    predictions_val = model.predict(X_val)
    accuracy_train = accuracy_score(predictions_train, y_train) # số dự đoán đúng chia cho tổng số mẫu
    accuracy_val = accuracy_score(predictions_val, y_val)
    accuracy_list_train.append(accuracy_train)
    accuracy_list_val.append(accuracy_val)

plt.title("Train x Validation metrics")
plt.xlabel("max_depth")
plt.ylabel("accuracy")
plt.xticks(
    ticks = range(len(max_depth_list)),
    labels=max_depth_list
)
plt.plot(accuracy_list_train)
plt.plot(accuracy_list_val)
plt.legend( ['train', 'validation'])
#plt.show()

Dựa vào ta thấy:
* ở đồ thị thứ nhất khi min_samples_split > 50 thì tập kiểm tra và huấn luyện đều giảm đây là hiện tượng underfit, < 50 ta thầy val giảm còn train tăng đây là hiện tượng overfiting
* ở đồ thị thứ 2 khi max_depth > 4 thì val giảm còn train thì tăng đây là hiện tượng overfit, ngc lại < 4 thì val giảm, train giảm đấy là underfit
vì vậy chọn giá trị tốt nhất : max_depth = 4, min_samples_split = 50

decision_tree_model = DecisionTreeClassifier(min_samples_split = 50,
                                             max_depth = 4,
                                             random_state = RANDOM_STATE).fit(X_train,y_train)
print(f"Metrics train:\n\tAccuracy score: {accuracy_score(decision_tree_model.predict(X_train),y_train):.4f}")
print(f"Metrics validation:\n\tAccuracy score: {accuracy_score(decision_tree_model.predict(X_val),y_val):.4f}")
"""



"""2.Random Forest"""
min_samples_split_list = [2,10,30,50,100,200,300,700] # danh sách các giá trị min_samples_split để thử nghiệm
max_depth_list = [1,2,3,4,8,16,32,64, None] # danh sách các giá trị max_depth để thử nghiệm
n_estimators_list = [10,50,100,500]

accuracy_list_train = []
accuracy_list_val = []

for min_samples_split in min_samples_split_list:

    model = RandomForestClassifier(min_samples_split=min_samples_split, random_state=RANDOM_STATE).fit(X_train,y_train)

    predictions_train = model.predict(X_train)
    predictions_val = model.predict(X_val)
    accuracy_train = accuracy_score(predictions_train, y_train)
    accuracy_val = accuracy_score(predictions_val, y_val)
    accuracy_list_train.append(accuracy_train)
    accuracy_list_val.append(accuracy_val)

plt.title("Train x Validation metrics")
plt.xlabel("min_samples_split")
plt.ylabel("accuracy")
plt.xticks(
    ticks = range(len(min_samples_split_list)),
    labels = min_samples_split_list
)
plt.plot(accuracy_list_train)
plt.plot(accuracy_list_val)
plt.legend(['Train', 'Validation'])
#plt.show()

accuracy_list_train = []
accuracy_list_val = []
for max_depth in max_depth_list:
    # You can fit the model at the same time you define it, because the fit function returns the fitted estimator.
    model = RandomForestClassifier(max_depth = max_depth,
                                   random_state = RANDOM_STATE).fit(X_train,y_train) 
    predictions_train = model.predict(X_train) ## The predicted values for the train dataset
    predictions_val = model.predict(X_val) ## The predicted values for the test dataset
    accuracy_train = accuracy_score(predictions_train,y_train)
    accuracy_val = accuracy_score(predictions_val,y_val)
    accuracy_list_train.append(accuracy_train)
    accuracy_list_val.append(accuracy_val)

plt.title('Train x Validation metrics')
plt.xlabel('max_depth')
plt.ylabel('accuracy')
plt.xticks(ticks = range(len(max_depth_list )),labels=max_depth_list)
plt.plot(accuracy_list_train)
plt.plot(accuracy_list_val)
plt.legend(['Train','Validation'])

accuracy_list_train = []
accuracy_list_val = []
for n_estimators in n_estimators_list:
    # You can fit the model at the same time you define it, because the fit function returns the fitted estimator.
    model = RandomForestClassifier(n_estimators = n_estimators,
                                   random_state = RANDOM_STATE).fit(X_train,y_train) 
    predictions_train = model.predict(X_train) ## The predicted values for the train dataset
    predictions_val = model.predict(X_val) ## The predicted values for the test dataset
    accuracy_train = accuracy_score(predictions_train,y_train)
    accuracy_val = accuracy_score(predictions_val,y_val)
    accuracy_list_train.append(accuracy_train)
    accuracy_list_val.append(accuracy_val)

plt.title('Train x Validation metrics')
plt.xlabel('n_estimators')
plt.ylabel('accuracy')
plt.xticks(ticks = range(len(n_estimators_list )),labels=n_estimators_list)
plt.plot(accuracy_list_train)
plt.plot(accuracy_list_val)
plt.legend(['Train','Validation'])

"""Giá trị tốt nhất
   max_depth: 16
   min_samples_split: 10
   n_estimators: 100"""

random_forest_model = RandomForestClassifier(n_estimators = 100,
                                             max_depth = 16, 
                                             min_samples_split = 10).fit(X_train,y_train)
print(f"Metrics train:\n\tAccuracy score: {accuracy_score(random_forest_model.predict(X_train),y_train):.4f}\nMetrics test:\n\tAccuracy score: {accuracy_score(random_forest_model.predict(X_val),y_val):.4f}")

