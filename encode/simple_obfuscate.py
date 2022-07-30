import marshal, os
from py_compile import compile as com_pyc

data = []

# 'pendragon.py' adalah nama file atau file yang akan kita encode.
# 'pendragon_hasil.py' adalah nama output filw atau file hasil.
files = 'pendragon.py'
output_file = 'pendragon_hasil.py'

# Membaca file.
read_file = open(files).read()

# Convert program ke file sementara dengan bentuk tipe data list.
for i in read_file:
    data.append(ord(i))
    temp = open('temp.py', 'w')
    temp.write('exec(\'\'.join(chr(_) for _ in %s))' % data)
    temp.close()

# Membaca file temporary dan melakukan encode program ke hash Marshal.
temp_read = open('temp.py').read()
com = marshal.dumps(compile(temp_read, '<Ryuuou>', 'exec'))

# Menulis executer program untuk menjalankan hash marshal dan menulisnya di file pendragon_hasil.py.
f_ = open(output_file, 'w')
f_.write(f'exec(__import__(\'marshal\').loads({com}))')
f_.close()

# Convert/Compile program yang telah di enkripsi ke bentuk file biner.
com_pyc(output_file, output_file)

# Menghapus file temporary.
os.remove('temp.py')