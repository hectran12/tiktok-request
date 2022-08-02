# Công thức chung: request đến profile or video muốn follow, tim, comment = cookie sau đó get header vừa được set lấy msToken rồi nối như trong code ( lưu ý phải request = method post chứ get nó không nhận )

Đối với tim: thêm tt-csrf-token vào header khi gửi url tim, còn lại như nhau hết ( tt-csrf-token có thể lấy từ cookie ) <br>
Đối với comment: thêm x-secsdk-csrf-token vào header khi gửi url comment, còn lại như nhau hết ( x-secsdk-csrf-token có thể lấy lúc lấy cookie ) <br>

# NÀY CHỈ ÁP DỤNG KHI BẠN MUỐN CONVERT SANG NGÔN NGỮ KHÁC, CHỨ NGOÀI RA CODE TRÊN CHỈ CẦN COOKIE TIKTOK LÀ ĐỦ
# XIN 1 SAO NẾU BẠN THẤY HỮU ÍCH :)))
