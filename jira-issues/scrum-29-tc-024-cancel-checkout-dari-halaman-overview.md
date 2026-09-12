# SCRUM-29 - TC-024 - Cancel Checkout dari Halaman Overview

## Informasi Issue

| Field | Detail |
|---|---|
| Issue Key | [SCRUM-29](https://anggirahmadillah.atlassian.net/browse/SCRUM-29) |
| Issue Type | Task |
| Status | Done |
| Priority | Medium |
| Assignee | Anggi Rahmadillah |
| Reporter | Anggi Rahmadillah |

## Deskripsi

Test Case ID: TC-024
Test Scenario:
Verify Cancel Checkout from Overview Page
Objective:
Memastikan tombol Cancel pada halaman Checkout: Overview mengembalikan user ke halaman Products.
Precondition:
User sudah login dan memiliki minimal satu produk di dalam cart.
Test Steps:

- Login menggunakan username: standard_user

- Masukkan password: secret_sauce

- Klik tombol Login.

- Tambahkan produk Sauce Labs Backpack ke cart.

- Buka halaman Cart.

- Klik tombol Checkout.

- Isi First Name dengan Anggi.

- Isi Last Name dengan Rahdillah.

- Isi Postal Code dengan 40123.

- Klik tombol Continue.

- Klik tombol Cancel.

- Amati halaman yang ditampilkan.

Expected Result:
User diarahkan kembali ke halaman Products.
Actual Result:
Sistem menampilkan kembali ke halaman Products.
Status:
PASS

## Link Jira

[SCRUM-29 - TC-024 - Cancel Checkout dari Halaman Overview](https://anggirahmadillah.atlassian.net/browse/SCRUM-29)
