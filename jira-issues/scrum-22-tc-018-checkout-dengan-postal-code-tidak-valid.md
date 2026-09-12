# SCRUM-22 - TC-018 - Checkout dengan Postal Code Tidak Valid

## Informasi Issue

| Field | Detail |
|---|---|
| Issue Key | [SCRUM-22](https://anggirahmadillah.atlassian.net/browse/SCRUM-22) |
| Issue Type | Task |
| Status | Done |
| Priority | Medium |
| Assignee | Anggi Rahmadillah |
| Reporter | Anggi Rahmadillah |

## Deskripsi

Test Case ID:
TC-018
Test Scenario:
Verify Checkout Validation with Invalid Postal Code
Objective:
Memastikan sistem melakukan validasi terhadap format Postal Code yang dimasukkan pada proses checkout.
Precondition:
User sudah berhasil login dan memiliki minimal satu produk di dalam cart.
Test Steps:

- Login menggunakan username: standard_user.

- Masukkan password: secret_sauce.

- Klik tombol Login.

- Pilih produk Sauce Labs Backpack.

- Klik tombol Add to Cart.

- Buka halaman Cart.

- Klik tombol Checkout.

- Isi First Name dengan Anggi.

- Isi Last Name dengan Rahdillah.

- Isi Postal Code dengan abc123.

- Klik tombol Continue.

- Amati respons sistem.

Expected Result:
Sistem menolak Postal Code yang mengandung karakter non-angka, menampilkan pesan validasi, dan tidak melanjutkan ke halaman Checkout: Overview.
Actual Result:
Sistem menerima Postal Code "abc123" dan tetap melanjutkan ke halaman Checkout: Overview tanpa menampilkan pesan validasi.
Status:
FAIL

## Link Jira

[SCRUM-22 - TC-018 - Checkout dengan Postal Code Tidak Valid](https://anggirahmadillah.atlassian.net/browse/SCRUM-22)
