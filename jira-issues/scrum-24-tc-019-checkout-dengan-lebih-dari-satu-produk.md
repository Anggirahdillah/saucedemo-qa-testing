# SCRUM-24 - TC-019 - Checkout dengan Lebih dari Satu Produk

## Informasi Issue

| Field | Detail |
|---|---|
| Issue Key | [SCRUM-24](https://anggirahmadillah.atlassian.net/browse/SCRUM-24) |
| Issue Type | Task |
| Status | Done |
| Priority | Medium |
| Assignee | Anggi Rahmadillah |
| Reporter | Anggi Rahmadillah |

## Deskripsi

Test Case ID: TC-019
Test Scenario:
Verify Checkout with Multiple Products
Objective:
Memastikan sistem dapat memproses checkout ketika user membeli lebih dari satu produk.
Precondition:
User sudah berhasil login dan berada di halaman Products.
Test Steps:

- Login menggunakan username: standard_user

- Masukkan password: secret_sauce

- Klik tombol Login.

- Tambahkan produk Sauce Labs Backpack ke cart.

- Kembali ke halaman Products.

- Tambahkan produk Sauce Labs Bike Light ke cart.

- Buka halaman Cart.

- Periksa daftar produk yang tampil.

- Klik tombol Checkout.

- Isi First Name dengan Anggi.

- Isi Last Name dengan Rahdillah.

- Isi Postal Code dengan 40123.

- Klik tombol Continue.

- Periksa halaman Checkout: Overview.

Expected Result:
Cart dan halaman Checkout: Overview menampilkan kedua produk yang dipilih. Jumlah item dan total harga sesuai dengan produk yang dibeli, dan user dapat melanjutkan proses checkout.
Actual Result:
Cart dan halaman Checkout: Overview menampilkan kedua produk yang dipilih. Jumlah item dan total harga sesuai dengan produk yang dibeli, dan dapat melanjutkan proses checkout
Status:
PASS

## Link Jira

[SCRUM-24 - TC-019 - Checkout dengan Lebih dari Satu Produk](https://anggirahmadillah.atlassian.net/browse/SCRUM-24)
