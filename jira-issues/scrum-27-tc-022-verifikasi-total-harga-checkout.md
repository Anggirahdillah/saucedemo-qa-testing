# SCRUM-27 - TC-022 - Verifikasi Total Harga Checkout

## Informasi Issue

| Field | Detail |
|---|---|
| Issue Key | [SCRUM-27](https://anggirahmadillah.atlassian.net/browse/SCRUM-27) |
| Issue Type | Task |
| Status | Done |
| Priority | Medium |
| Assignee | Anggi Rahmadillah |
| Reporter | Anggi Rahmadillah |

## Deskripsi

Test Case ID: TC-022
Test Scenario:
Verify Checkout Total Price Calculation
Objective:
Memastikan total harga pada halaman Checkout: Overview sesuai dengan harga produk dan perhitungan pajak.
Precondition:
User sudah berhasil login dan berada di halaman Products.
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

- Amati Item total, Tax, dan Total pada halaman Checkout: Overview.

Expected Result:
Item total sesuai dengan harga produk. Tax dihitung oleh sistem dan Total merupakan hasil penjumlahan Item total dan Tax.
Actual Result:
Item total sesuai dengan harga produk. Tax dihitung oleh sistem dan Total merupakan hasil penjumlahan Item total dan Tax.
Status:
PASS

## Link Jira

[SCRUM-27 - TC-022 - Verifikasi Total Harga Checkout](https://anggirahmadillah.atlassian.net/browse/SCRUM-27)
