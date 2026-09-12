# SCRUM-19 - TC-015 - Checkout dengan Last Name Kosong

## Informasi Issue

| Field | Detail |
|---|---|
| Issue Key | [SCRUM-19](https://anggirahmadillah.atlassian.net/browse/SCRUM-19) |
| Issue Type | Task |
| Status | Done |
| Priority | Medium |
| Assignee | Anggi Rahmadillah |
| Reporter | Anggi Rahmadillah |

## Deskripsi

Test Case ID: TC-015
Test Scenario:
Verify Checkout Validation with Empty Last Name
Objective:
Memastikan sistem menolak proses checkout apabila field Last Name belum diisi.
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

- Biarkan field Last Name kosong.

- Isi Postal Code dengan 40123.

- Klik tombol Continue.

- Amati pesan validasi yang muncul.

Expected Result:
Sistem tidak melanjutkan ke halaman Checkout: Overview dan menampilkan pesan "Error: Last Name is required".
Actual Result:
Sistem hanya pada halaman chexkout : your information dengan pesan "Error: Last Name is required".
Status:
PASS

## Link Jira

[SCRUM-19 - TC-015 - Checkout dengan Last Name Kosong](https://anggirahmadillah.atlassian.net/browse/SCRUM-19)
