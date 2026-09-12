# SCRUM-20 - TC-016 - Checkout dengan Postal Code Kosong

## Informasi Issue

| Field | Detail |
|---|---|
| Issue Key | [SCRUM-20](https://anggirahmadillah.atlassian.net/browse/SCRUM-20) |
| Issue Type | Task |
| Status | Done |
| Priority | Medium |
| Assignee | Anggi Rahmadillah |
| Reporter | Anggi Rahmadillah |

## Deskripsi

Test Case ID: TC-016
Test Scenario:
Verify Checkout Validation with Empty Postal Code
Objective:
Memastikan sistem menolak proses checkout apabila field Postal Code belum diisi.
Precondition:
User sudah berhasil login dan memiliki minimal satu produk di dalam cart.
Test Steps:

- Login menggunakan username: standard_user

- Masukkan password: secret_sauce

- Klik tombol Login.

- Pilih produk Sauce Labs Backpack.

- Klik tombol Add to Cart.

- Buka halaman Cart.

- Klik tombol Checkout.

- Isi First Name dengan Anggi.

- Isi Last Name dengan Rahdillah.

- Biarkan field Postal Code kosong.

- Klik tombol Continue.

- Amati pesan validasi yang muncul.

Expected Result:
Sistem tidak melanjutkan ke halaman Checkout: Overview dan menampilkan pesan "Error: Postal Code is required".
Actual Result:
Sistem tetap pada halaman Checkout: Your Information dan menampilkan pesan "Error: Postal Code is required". 
Status:
PASS

## Link Jira

[SCRUM-20 - TC-016 - Checkout dengan Postal Code Kosong](https://anggirahmadillah.atlassian.net/browse/SCRUM-20)
