# Công thức chung: request đến profile muốn follow = cookie sau đó get header vừa được set lấy msToken rồi nối như trong code ( lưu ý phải request = method post chứ get nó không nhận )

Đối với tim: thêm tt-csrf-token vào header khi gửi url tim, còn lại như nhau hết ( tt-csrf-token có thể lấy từ cookie )
Đối với comment: thêm x-secsdk-csrf-token vào header khi gửi url comment, còn lại như nhau hết ( x-secsdk-csrf-token có thể lấy lúc lấy cookie )
