import tkinter as tk
from tkinter import messagebox

# Danh sách sản phẩm
products = [
    {"id": 1, "name": "Sách: Dune  ", "price": 10000},
    {"id": 2, "name": "Sách: Dune 2", "price": 20000},
]

# Hàm đăng nhập
def login():
    username = entry_username.get()
    password = entry_password.get()
    # thông tin đăng nhập cố định 
    if username == "admin" and password == "123":
        messagebox.showinfo("Đăng nhập thành công", "Chào mừng!")
        show_product_interface()
    else:
        messagebox.showerror("Lỗi", "Sai thông tin đăng nhập")

# Hàm hiển thị giao diện sản phẩm
def show_product_interface():
    login_frame.pack_forget()  # Ẩn frame đăng nhập
    product_frame.pack()  # Hiển thị frame sản phẩm
    update_product_list()

# Cập nhật danh sách 
def update_product_list():
    product_listbox.delete(0, tk.END)
    for product in products:
        product_listbox.insert(tk.END, f"ID: {product['id']} - Tên: {product['name']} - Giá: {product['price']} VND")

# Hàm thêm 
def add_product():
    name = entry_name.get()
    price = entry_price.get()

    # Kiểm tra xem giá có phải là số hay không
    if name and price:
        try:
            price = int(price)  # Chuyển giá trị sang số nguyên
            new_id = len(products) + 1
            products.append({"id": new_id, "name": name, "price": price})
            update_product_list()
        except ValueError:
            messagebox.showerror("Lỗi", "Giá phải là một số hợp lệ")
    else:
        messagebox.showerror("Lỗi", "Xin hãy điền đầy đủ thông tin")

# Hàm xóa 
def delete_product():
    selected = product_listbox.curselection()
    if selected:
        del products[selected[0]]
        update_product_list()
    else:
        messagebox.showerror("Lỗi", "Vui lòng chọn sản phẩm để xóa")

# Hàm sửa 
def edit_product():
    selected = product_listbox.curselection()
    if selected:
        new_name = entry_name.get()
        new_price = entry_price.get()

        # Kiểm tra xem giá mới có phải là số hay không
        if new_name and new_price:
            try:
                new_price = int(new_price)  # Chuyển giá trị sang số nguyên
                products[selected[0]]["name"] = new_name
                products[selected[0]]["price"] = new_price
                update_product_list()
            except ValueError:
                messagebox.showerror("Lỗi", "Giá phải là một số hợp lệ")
        else:
            messagebox.showerror("Lỗi", "Xin hãy điền đầy đủ thông tin")
    else:
        messagebox.showerror("Lỗi", "Chọn sản phẩm để sửa")

# Tạo cửa sổ 
window = tk.Tk()
window.title("Quản lý sản phẩm")

# Giao diện đăng nhập
login_frame = tk.Frame(window)
tk.Label(login_frame, text="Username:").pack(pady=5)
entry_username = tk.Entry(login_frame)
entry_username.pack(pady=5)

tk.Label(login_frame, text="Password:").pack(pady=5)
entry_password = tk.Entry(login_frame, show="*")
entry_password.pack(pady=5)

btn_login = tk.Button(login_frame, text="Đăng nhập", command=login)
btn_login.pack(pady=10)

login_frame.pack()

# Giao diện 
product_frame = tk.Frame(window)

# Danh sách 
product_listbox = tk.Listbox(product_frame, width=50)
product_listbox.pack(pady=10)

# Thêm 
tk.Label(product_frame, text="Tên sản phẩm:").pack(pady=5)
entry_name = tk.Entry(product_frame)
entry_name.pack(pady=5)

tk.Label(product_frame, text="Giá sản phẩm:").pack(pady=5)
entry_price = tk.Entry(product_frame)
entry_price.pack(pady=5)

btn_add = tk.Button(product_frame, text="Thêm sản phẩm", command=add_product)
btn_add.pack(pady=5)

btn_delete = tk.Button(product_frame, text="Xóa sản phẩm", command=delete_product)
btn_delete.pack(pady=5)

btn_edit = tk.Button(product_frame, text="Sửa sản phẩm", command=edit_product)
btn_edit.pack(pady=5)

window.mainloop()
