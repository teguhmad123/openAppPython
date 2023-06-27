import pygetwindow
# untuk mbuka tutup windows

# print(pygetwindow.getActiveWindowTitle())
win =pygetwindow.getWindowsWithTitle('Aplikasi Registrasi Sidik Jari')[0]
# win = pygetwindow.getWindowsWithTitle('Python331')
# print(win)
win.activate()
# win.minimize()