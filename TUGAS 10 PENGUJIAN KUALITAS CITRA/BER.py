import numpy as np
import cv2

def hitung_ber(citra_asli, citra_noise):
    # Mengubah citra menjadi array bit untuk perbandingan bit-demi-bit
    bit_asli = np.unpackbits(citra_asli.flatten())
    bit_noise = np.unpackbits(citra_noise.flatten())

    # Menghitung jumlah bit yang salah
    jumlah_error = np.sum(bit_asli != bit_noise)

    # Menghitung total jumlah bit
    total_bit = bit_asli.size

    # Menghitung Bit Error Rate (BER)
    ber = jumlah_error / total_bit

    return jumlah_error, total_bit, ber

def ubah_ukuran_citra(citra_asli, citra_noise):
    # Menentukan dimensi terbesar dari kedua citra
    lebar = min(citra_asli.shape[1], citra_noise.shape[1])
    tinggi = min(citra_asli.shape[0], citra_noise.shape[0])
    dimensi = (lebar, tinggi)

    citra_asli_ubah = cv2.resize(citra_asli, dimensi, interpolation=cv2.INTER_CUBIC)
    citra_noise_ubah = cv2.resize(citra_noise, dimensi, interpolation=cv2.INTER_CUBIC)

    return citra_asli_ubah, citra_noise_ubah

# Memuat citra asli dan citra dengan noise
citra_asli = cv2.imread('D:/ss/winter.jpg', cv2.IMREAD_GRAYSCALE)
citra_noise = cv2.imread('D:/ss/charlie.jpeg', cv2.IMREAD_GRAYSCALE)

# Memastikan kedua citra berhasil dimuat
if citra_asli is None or citra_noise is None:
    raise ValueError("Satu atau kedua citra tidak dapat dimuat. Periksa jalur file.")

# Mengubah ukuran citra menjadi ukuran yang sama
citra_asli_ubah, citra_noise_ubah = ubah_ukuran_citra(citra_asli, citra_noise)

# Menghitung Bit Error Rate (BER)
jumlah_error, total_bit, ber = hitung_ber(citra_asli_ubah, citra_noise_ubah)

# Menampilkan citra
cv2.imshow('Citra Asli', citra_asli_ubah)
cv2.imshow('Citra Noise', citra_noise_ubah)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Menampilkan hasil perhitungan
print(f"Jumlah bit yang salah: {jumlah_error}")
print(f"Total jumlah bit: {total_bit}")
print(f"Bit Error Rate (BER): {ber}")