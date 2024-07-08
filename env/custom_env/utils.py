CONFIGS_SIMPLE = [
    "1tls_2x2",
    "1tls_3x3",
    "1tls_4x4"
    # "1tls_5x5"
]

CONFIGS_MULTI = [
    "2tls_3x3x2",
    "3tls_2x2x3",
    "3tls_3x3x3",
    "4tls_3x3x2x2",
    "9tls_3x3x3x3"
]

SUMO_PARAMS = {
    "config": CONFIGS_SIMPLE[1],

    "steps": 3600,
    "delay": 0,
    "gui": True,
    "log": False,
    "rnd": (True, True),
    "seed": False,

    "v_type_def": "def",
    "v_type_con": "con",
    "v_length": 5,
    "v_min_gap": 2.5,
    "v_max_speed": 16.67,

    "veh_p_hour": [200, 800, 800, 200],

    "con_penetration_rate": 1.,
    "con_range": 160,

    "cell_length": 8
}

# 1. con_penetration_rate
# Ý nghĩa:

# Đây là tỷ lệ thâm nhập của các phương tiện kết nối (connected vehicles) trong tổng số phương tiện trên đường.
# Giá trị này dao động từ 0 đến 1, trong đó:
# 0: Không có phương tiện nào được kết nối.
# 1: Tất cả các phương tiện đều được kết nối.
# Ví dụ:

# con_penetration_rate = 1.0: Tất cả các phương tiện trên đường đều là phương tiện kết nối.
# con_penetration_rate = 0.5: 50% số phương tiện trên đường là phương tiện kết nối.
# 2. con_range
# Ý nghĩa:

# Đây là khoảng cách (tính bằng mét) mà một phương tiện kết nối có thể truyền và nhận thông tin từ các phương tiện hoặc hạ tầng xung quanh.
# Phạm vi này quy định khả năng giao tiếp của phương tiện kết nối, từ đó ảnh hưởng đến khả năng thu thập thông tin và phản hồi lại tình trạng giao thông xung quanh.
# Ví dụ:

# con_range = 160: Phương tiện kết nối có thể truyền và nhận thông tin trong phạm vi 160 mét.
# 3. cell_length
# Ý nghĩa:

# Đây là độ dài của một ô (cell) trong mô phỏng lưới giao thông.
# Tham số này thường được sử dụng trong các mô hình phân chia lưới giao thông thành các ô nhỏ để dễ dàng quản lý và mô phỏng chuyển động của các phương tiện trong mỗi ô.
# Ví dụ:

# cell_length = 8: Mỗi ô trong mô phỏng lưới giao thông có chiều dài là 8 mét.
# Tóm tắt:
# con_penetration_rate: Tỷ lệ phần trăm các phương tiện kết nối trong tổng số phương tiện.
# con_range: Phạm vi (tính bằng mét) mà một phương tiện kết nối có thể giao tiếp với các phương tiện khác hoặc hạ tầng.
# cell_length: Độ dài của một ô trong mô phỏng lưới giao thông (tính bằng mét).
