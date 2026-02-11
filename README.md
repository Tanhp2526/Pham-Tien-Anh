# LABS:
# 1. Neural Networks for Handwritten Digit Recognition.
## Problem Statement(Mô tả bài toán)
- Sử dụng một mạng lưới Noron để nhận dạng 10 chữ số viết tay, từ 0-9. 
## Dataset(Tập dữ liệu)
- Tập dữ liệu bao gồm 5000 ví dụ huấn luyện chữ số viết tay.
- Mỗi ví dụ là một bức ảnh có size: 20x20 pixel.
- Trải phẳng ra thành 1 vector chứa 400 phần tử.
- Ma trận X sẽ là: X(5000 x 400).
- Labels: y (5000 x 1), giá trị từ 0 đến 9 đại diện cho lớp số.
## Visualizing the Data(Trực quan hóa dữ liệu)
- Chọn ngẫu nhiên 64 hàng từ X, ánh xạ trở lại kích thước ban đầu 20 x 20 pixel và hiển thị bức ảnh.
- Nhãn mỗi bức ảnh hiển thị phía trên ảnh.
## Model representation(Biểu diễn mô hình)

Triển khai mô hình TensorFlow. Gồm 3 lớp layer: 
- Layer1: units = 25, kích thước W1(400, 25), b1(25,); activation = 'relu'
- Layer2: units = 15, kích thước W2(25,15) , b2(15,); activation = 'relu'
- Layer3(Output layer): units = 10, actiovation = 'softmax'

Training model: `Machine Learning/ Advanced Learning Algorithms/practice2.py`
## Predict: 
- Sau khi ta đã traing model có thể dự đoán bức ảnh đó là số nào bằng cách sử dụng use Keras predict.

# 2. Image compression with K-means
## Problem Statement(Mô tả bài toán)
- Một bức ảnh RGB được biểu diễn bởi 24-bit, mỗi pixel được biểu diễn bởi 3 số nguyên không dấu 8-bit(giá trị từ 0-255), tương ứng với 3 cường độ màu(RGB): đỏ(red), xanh lá(green), xanh dương(blue).
- Ta sẽ giảm số lượng màu xuống còn 16 màu bằng thuật toán K-means để biểu diễn ảnh sau khi nén.
- Cụ thể hơn, ta sẽ xem mỗi pixel trong ảnh gốc như một mẫu dữ liệu và sử dụng thuật toán K-means để tìm ra 16 màu có khả năng nhóm các pixel tốt nhất trong không gian RGB ba chiều.
##  Dataset(Tập dữ liệu)
Ảnh đầu vào: `bird_small.png`.

Kích thước ảnh: 128 x 128 x 3.

-128: số hàng pixel(chiều cao ảnh).
-128: số cột pixel(chiều rộng ảnh).
-3: số kênh màu (R,G,B).

Chuyển đổi dữ liệu: 

- Vì ma trận đầu vào thuật toán K-means là ma trận 2D, nên ta phải chuyển đổi ảnh gốc thành ma trận 2D.
- Ảnh gốc 3D: `original_img` có shape(128,128,3).
- Trải phẳng thành ma trận 2D có shape(m,3) trong đó m = 128 x 128.
- Mỗi hàng của `X_img` là một pixel với 3 đặc trưng(R,G,B).

## K-means Clustering(Phân cụm K-Means)
Số cụm màu: K = 16(ảnh sau khi nén chỉ còn 16 màu khác nhau).

Khởi tạo centroid(tâm cụm): chọn ngẫu nhiên K điểm từ `X_img` làm tâm cụm ban đầu bằng hàm `kMeans_init_centroids(X, K)`.

Gán cụm: gán các pixel vào các tâm cụm gần nhất bằng hàm `find_closest_centroids(X,centroids)`.

Với mỗi cụm k, lấy trung bình tất cả pixel được gán vào cụm đó để tạo centroid mới uk.

Sau khi chạy thuật toán và lặp đi lặp lại, ta quan sát được ảnh sau khi nén có ít màu hơn nhưng vẫn giữ được nội dung và cấu trúc chính của bức ảnh. `K-means lab.py`










# Python Learning 
Chủ đề em đã làm

- Basic Data Types
- Strings
- Sets
- Math
- Itertools
- Collections
- Date and Time
- Errors and Exceptions
- Python Functionals
- Regex and Parsing
- Numpy : thư viện cho máy tính khoa học , làm việc với mảng ,đại số tuyến tính, biến đổi Fourier , ma trận

# Pandas 
- Đây là 1 một thư viện mạnh về xử lý và phân tích dữ liệu 
- Thường làm việc với Series(cột) và Dataframe(bảng 2 chiều)
* Series : 
+ Là một mảng 1 chiều (giống như 1 cột trong Excel) 
+ Có chỉ số index đi kèm

* Dataframe :
+ là bảng 2 chiều gồm nhiều hàng và nhiều cột
+ có kiểu trích xuất dữ liệu như : iloc(chọn dữ liệu dựa trên chỉ số) và loc(chọn dữ liệu dựa trên header)

# API (Application Programming Interface) 
- là 1 giao diện cho các phần mềm giao tiếp với nhau thông qua input và output mà cần phải phải biết trong API đó hoạt động như thế
- Phương thức head() : hiển thị số lượng hàng đã đề cập của Dataframe
- Phương thức mean() : tính giá trị trung bình 

## REST API : 
* là cách để máy tính hoặc chương trình trao đổi dữ liệu thông qua Internet

* Thông tin được gửi và nhận thông qua HTTP, mỗi lần trao đổi gồm 2 phần:
+ Request(yêu cầu): mình sẽ gửi lên server(ví dụ : "tôi muốn dữ liệu thời tiết hôm nay)
+ Respone(phản hồi): server trả lại dữ liệu (thường là file JSON)

# HTTP(HyperText Transfer Protocol) 
- Giao thức truyền dữ liệu, bao gồm các trang web và tài nguyên - giữa máy khách(client) và máy chủ (server) trên mạng World Wide Web
- URL(Uniform Resource Locator) là cách phổ biến để tìm các tài nguyên trên web
- URL chia làm 3 phần :
  * Scheme(giao thức)
  * Địa chỉ Internet hoặc URL gốc
  * Route(đường dẫn)
- Phương thức GET: dùng để lấy thông tin
- Phương thức POST: gửi dữ liệu mới
- Phương thức PUT : cập nhật dữ liệu trên máy chủ
- Phương thức DELETE : xóa dữ liệu khỏi máy chủ

# Web Scraping
- là quá trình trích xuất dữ liệu từ các trang web để thu thập thông tin cho nhiều ứng dụng , bằng cách sử dụng các thư viện như : BeautifulSoup, Scrapy, Selenium
- Dữ liệu dạng bảng có thể được trích xuất từ các trang web bằng phương thức "read_html()"

# File Format(định dạng tệp) :
- Python hoạt động với nhiều định dạng tệp như CSV, XML, JSON, xlsx, ...
- Phần mở rộng tệp cho biết đó là loại tệp gì và cần mở bằng phần mềm nào...
