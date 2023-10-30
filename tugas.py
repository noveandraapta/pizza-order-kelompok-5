#Nama Toko
print('=' * 30)
print('          Pizza Hut        ')
print('=' * 30)
#Daftar Menu 
print("Pizza Menu :")
print("1. Frankfurter BBQ        :120000")
print("2. Meat Monsta            :145000")
print("3. Super Supreme          :141000")
print("4. Super Supreme Chicken  :125000")
#Input 
pesan_pizza = input("Pilih jenis pizza : ").lower()
print("Crust Pizza :")
print("1. Original                    : Free")
print("2. Pan                         : 4000")
print("3. Cheesy Bite Crust           : 8000")
print("4. Chilli Cheesy Stuffed Crust : 10000")
print("5. Stuffed Crust               : 12000")
crust_pizza = input("Tambahkan topping : ").lower()
print("Ukuran Pizza :")
print("1. Small  : 10000")
print("2. Medium : 12000")
print("3. Large  : 14000")
ukuran_pizza = input("Pilih ukuran pizza : ").lower()
nambah_keju = (input("Tambah 13000 untuk Extra Keju (ya/tidak): ")).lower() == "y"
# Harga pizza
if pesan_pizza == "frankfurter bbq":
    harga_pizza = 120000
elif pesan_pizza == "meat monsta":
    harga_pizza = 145000
elif pesan_pizza == "super supreme":
    harga_pizza = 141000
elif pesan_pizza == "super supreme chicken":
    harga_pizza = 125000
else:
    print("Jenis pizza tidak valid.")
    exit()
# Biaya topping
if crust_pizza == "original":
    harga_crust = 0
elif crust_pizza == "pan":
    harga_crust = 4000
elif crust_pizza == "cheesy bite crust":
    harga_crust = 8000
elif crust_pizza == "chilli cheesy stuffed crust":
    harga_crust = 10000
elif crust_pizza == "stuffed crust":
    harga_crust = 12000
else:
    print("Jenis Crust tidak valid.")
    exit()

# Biaya ukuran
if ukuran_pizza == "small":
    ukuran_price = 10000
elif ukuran_pizza == "medium":
    ukuran_price = 12000
elif ukuran_pizza == "large":
    ukuran_price = 14000
else:
    print("Ukuran pizza tidak valid.")
    exit()
# Biaya tambahan keju
harga_keju = 13000 if nambah_keju else 0
# Total biaya
total_cost = harga_pizza + harga_crust + ukuran_price + harga_keju
# Menampilkan pesanan dan total biaya
print("Thank you for choosing Pizza Hut Delivery!")
print("Your final bill will be: Rp",total_cost)