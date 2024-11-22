import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox

# Kết nối đến cơ sở dữ liệu
def tao_ket_noi():
    try:
        ket_noi = mysql.connector.connect(
            host="localhost",
            user="root",
            password="p123",
            database="quan_ly_sach"
        )
        if ket_noi.is_connected():
            print("Kết nối thành công đến cơ sở dữ liệu!")
        return ket_noi
    except Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi kết nối database: {e}")
        return None

ket_noi = tao_ket_noi()

# Thêm sản phẩm
def them_sach():
    ten = entry_ten_sach.get()
    tac_gia = entry_tac_gia.get()
    gia = entry_gia.get()
    nam_xb = entry_nam_xb.get()
    the_loai = entry_the_loai.get()
    tom_tat = entry_tom_tat.get("1.0", tk.END).strip()  # Lấy dữ liệu từ Text widget
    hinh_bia = entry_hinh_bia.get()

    if ten and tac_gia and gia.isdigit() and nam_xb.isdigit():
        try:
            cursor = ket_noi.cursor()
            query = """INSERT INTO sach (ten_sach, tac_gia, gia, nam_xb, the_loai, tom_tat, hinh_bia)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (ten, tac_gia, float(gia), int(nam_xb), the_loai, tom_tat, hinh_bia))
            ket_noi.commit()
            messagebox.showinfo("Thành công", "Thêm sách thành công!")
            cap_nhat_danh_sach()
        except Error as e:
            messagebox.showerror("Lỗi", f"Lỗi khi thêm sách: {e}")
    else:
        messagebox.showerror("Lỗi", "Vui lòng nhập thông tin hợp lệ!")


# Cập nhật danh sách
def cap_nhat_danh_sach():
    danh_sach_listbox.delete(0, tk.END)
    try:
        cursor = ket_noi.cursor()
        query = "SELECT ten_sach, gia, tac_gia FROM sach"
        cursor.execute(query)
        danh_sach = cursor.fetchall()
        for sach in danh_sach:
            ten, gia, tac_gia = sach
            danh_sach_listbox.insert(tk.END, f"{ten} - {gia} VND - Tác giả: {tac_gia}")
    except Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi tải danh sách: {e}")

# Giao diện Tkinter
# Tạo cửa sổ chính
window = tk.Tk()
window.title("Quản lý Sách")

# Các thành phần hiển thị danh sách sách
tk.Label(window, text="Danh sách Sách:").grid(row=0, column=0, padx=10, pady=5)
danh_sach_listbox = tk.Listbox(window, width=60, height=15)
danh_sach_listbox.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

# Các trường nhập thông tin sách
tk.Label(window, text="Tên sách:").grid(row=2, column=0, sticky="w", padx=10)
entry_ten_sach = tk.Entry(window, width=40)
entry_ten_sach.grid(row=2, column=1, padx=10)

tk.Label(window, text="Tác giả:").grid(row=3, column=0, sticky="w", padx=10)
entry_tac_gia = tk.Entry(window, width=40)
entry_tac_gia.grid(row=3, column=1, padx=10)

tk.Label(window, text="Giá (VND):").grid(row=4, column=0, sticky="w", padx=10)
entry_gia = tk.Entry(window, width=40)
entry_gia.grid(row=4, column=1, padx=10)

tk.Label(window, text="Năm xuất bản:").grid(row=5, column=0, sticky="w", padx=10)
entry_nam_xb = tk.Entry(window, width=40)
entry_nam_xb.grid(row=5, column=1, padx=10)

tk.Label(window, text="Thể loại:").grid(row=6, column=0, sticky="w", padx=10)
entry_the_loai = tk.Entry(window, width=40)
entry_the_loai.grid(row=6, column=1, padx=10)

tk.Label(window, text="Tóm tắt:").grid(row=7, column=0, sticky="nw", padx=10)
entry_tom_tat = tk.Text(window, width=30, height=5)
entry_tom_tat.grid(row=7, column=1, padx=10)

tk.Label(window, text="Hình bìa (URL):").grid(row=8, column=0, sticky="w", padx=10)
entry_hinh_bia = tk.Entry(window, width=40)
entry_hinh_bia.grid(row=8, column=1, padx=10)

# Nút thêm sách
btn_them_sach = tk.Button(window, text="Thêm Sách", command=them_sach)
btn_them_sach.grid(row=9, column=1, sticky="e", pady=10)

# Tải danh sách sách
cap_nhat_danh_sach()

# Chạy ứng dụng
window.mainloop()

