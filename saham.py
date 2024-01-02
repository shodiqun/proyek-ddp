import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import yfinance as yf

class StockTradingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Perdagangan Saham Real-Time")
        self.master.geometry("800x600")

        self.style = Style(theme="flatly")

        # Buat antarmuka pengguna
        self.create_widgets()

    def create_widgets(self):
        # Buat label untuk memasukkan simbol saham
        ttk.Label(self.master, text="Masukkan Simbol Saham:").pack(pady=10)

        # Buat entry untuk memasukkan simbol saham
        self.symbol_entry = ttk.Entry(self.master, width=10)
        self.symbol_entry.pack(pady=10)

        # Buat tombol untuk mendapatkan data saham
        get_stock_button = ttk.Button(self.master, text="Dapatkan Data Saham", command=self.get_stock_data)
        get_stock_button.pack(pady=10)

        # Buat label untuk menampilkan informasi saham
        self.stock_info_label = ttk.Label(self.master, text="")
        self.stock_info_label.pack(pady=10)

    def get_stock_data(self):
        # Ambil simbol saham dari entry
        symbol = self.symbol_entry.get().upper()

        try:
            # Dapatkan data saham menggunakan yfinance
            stock_data = yf.Ticker(symbol)
            current_price = stock_data.history(period="1d")["Close"].iloc[-1]

            # Tampilkan informasi saham pada label
            info_text = f"Informasi Saham ({symbol}):\nHarga Terakhir: ${current_price:.2f}"
            self.stock_info_label.config(text=info_text)

        except Exception as e:
            # Tampilkan pesan kesalahan jika simbol saham tidak valid
            error_text = f"Error: {str(e)}"
            self.stock_info_label.config(text=error_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = StockTradingApp(root)
    root.mainloop()
