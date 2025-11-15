# Python Learning 
Chủ đề em đã làm :

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

# Pandas : 
- Đây là 1 một thư viện mạnh về xử lý và phân tích dữ liệu 
- Thường làm việc với Series(cột) và Dataframe(bảng 2 chiều)
* Series : 
+ Là một mảng 1 chiều (giống như 1 cột trong Excel) 
+ Có chỉ số index đi kèm

* Dataframe :
+ là bảng 2 chiều gồm nhiều hàng và nhiều cột
+ có kiểu trích xuất dữ liệu như : iloc(chọn dữ liệu dựa trên chỉ số) và loc(chọn dữ liệu dựa trên header)

# API (Application Programming Interface) :
- là 1 giao diện cho các phần mềm giao tiếp với nhau thông qua input và output mà cần phải phải biết trong API đó hoạt động như thế
- Phương thức head() : hiển thị số lượng hàng đã đề cập của Dataframe
- Phương thức mean() : tính giá trị trung bình 

- REST API : 
* là cách để máy tính hoặc chương trình trao đổi dữ liệu thông qua Internet

* Thông tin được gửi và nhận thông qua HTTP, mỗi lần trao đổi gồm 2 phần:
+ Request(yêu cầu): mình sẽ gửi lên server(ví dụ : "tôi muốn dữ liệu thời tiết hôm nay)
+ Respone(phản hồi): server trả lại dữ liệu (thường là file JSON)

# HTTP(HyperText Transfer Protocol) :
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

# Web Scraping:
- là quá trình trích xuất dữ liệu từ các trang web để thu thập thông tin cho nhiều ứng dụng , bằng cách sử dụng các thư viện như : BeautifulSoup, Scrapy, Selenium
- Dữ liệu dạng bảng có thể được trích xuất từ các trang web bằng phương thức "read_html()"

# File Format(định dạng tệp) :
- Python hoạt động với nhiều định dạng tệp như CSV, XML, JSON, xlsx, ...
- Phần mở rộng tệp cho biết đó là loại tệp gì và cần mở bằng phần mềm nào...
