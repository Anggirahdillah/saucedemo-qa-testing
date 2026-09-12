# SCRUM-17 - TC-013 - Checkout with Valid Information

## Informasi Issue

| Field | Detail |
|---|---|
| Issue Key | [SCRUM-17](https://anggirahmadillah.atlassian.net/browse/SCRUM-17) |
| Issue Type | Task |
| Status | Done |
| Priority | Medium |
| Assignee | Anggi Rahmadillah |
| Reporter | Anggi Rahmadillah |

## Deskripsi

Test Case ID: TC-013
Test Scenario:
Verify Checkout Functionality with Valid Information
Objective:
Memastikan user dapat menyelesaikan proses checkout menggunakan data yang valid.
Precondition:
User sudah berhasil login dan berada di halaman Products.
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

- Isi Postal Code dengan 40123.

- Klik tombol Continue.

- Periksa halaman Checkout: Overview.

- Klik tombol Finish.

- Amati halaman hasil checkout.

Expected Result:
User berhasil menyelesaikan proses checkout. Halaman Checkout: Complete! tampil dan menampilkan pesan "Thank you for your order!".
Actual Result:
Checkout berhasil diselesaikan. Sistem menampilkan halaman Checkout: Complete! dengan pesan "Thank you for your order!".
Status:
PASS

## Link Jira

[SCRUM-17 - TC-013 - Checkout with Valid Information](https://anggirahmadillah.atlassian.net/browse/SCRUM-17)
