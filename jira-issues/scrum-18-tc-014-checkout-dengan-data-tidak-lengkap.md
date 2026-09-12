# SCRUM-18 - TC-014 - Checkout dengan Data Tidak Lengkap

## Informasi Issue

| Field | Detail |
|---|---|
| Issue Key | [SCRUM-18](https://anggirahmadillah.atlassian.net/browse/SCRUM-18) |
| Issue Type | Task |
| Status | Done |
| Priority | Medium |
| Assignee | Anggi Rahmadillah |
| Reporter | Anggi Rahmadillah |

## Deskripsi

Test Case ID: TC-014
Test Scenario:
Verify Checkout Validation with Empty Required Fields
Objective:
Memastikan sistem menolak proses checkout apabila data wajib belum diisi.
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

- Biarkan seluruh field checkout kosong.

- Klik tombol Continue.

- Amati pesan validasi yang muncul.

Expected Result:
Sistem tidak melanjutkan ke halaman Checkout: Overview dan menampilkan pesan "Error: First Name is required".
Actual Result:
Sistem tetap dalam halaman checkout dan menampilkan pesan "Error: First Name is required".
Status:
PASS

## Link Jira

[SCRUM-18 - TC-014 - Checkout dengan Data Tidak Lengkap](https://anggirahmadillah.atlassian.net/browse/SCRUM-18)
