# SCRUM-21 - TC-017 - Checkout dengan First Name Kosong

## Informasi Issue

| Field | Detail |
|---|---|
| Issue Key | [SCRUM-21](https://anggirahmadillah.atlassian.net/browse/SCRUM-21) |
| Issue Type | Task |
| Status | Done |
| Priority | Medium |
| Assignee | Anggi Rahmadillah |
| Reporter | Anggi Rahmadillah |

## Deskripsi

Test Case ID: TC-017
Test Scenario:
Verify Checkout Validation with Empty First Name
Objective:
Memastikan sistem menolak proses checkout apabila field First Name belum diisi.
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

- Biarkan field First Name kosong.

- Isi Last Name dengan Rahdillah.

- Isi Postal Code dengan 40123.

- Klik tombol Continue.

- Amati pesan validasi yang muncul.

Expected Result:
Sistem tidak melanjutkan ke halaman Checkout: Overview dan menampilkan pesan "Error: First Name is required".
Actual Result:
Sistem tetap pada halaman Checkout: Your Information dan menampilkan pesan "Error: First Name is required".
Status:
PASS

## Link Jira

[SCRUM-21 - TC-017 - Checkout dengan First Name Kosong](https://anggirahmadillah.atlassian.net/browse/SCRUM-21)
