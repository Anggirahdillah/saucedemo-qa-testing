# SCRUM-26 - TC-021 - Remove Semua Produk dari Cart

## Informasi Issue

| Field | Detail |
|---|---|
| Issue Key | [SCRUM-26](https://anggirahmadillah.atlassian.net/browse/SCRUM-26) |
| Issue Type | Task |
| Status | Done |
| Priority | Medium |
| Assignee | Anggi Rahmadillah |
| Reporter | Anggi Rahmadillah |

## Deskripsi

Test Case ID: TC-021
Test Scenario:
Verify Removing All Products from Cart
Objective:
Memastikan user dapat menghapus seluruh produk dari cart hingga cart menjadi kosong.
Precondition:
User sudah berhasil login dan berada di halaman Products.
Test Steps:

- Login menggunakan username: standard_user

- Masukkan password: secret_sauce

- Klik tombol Login.

- Tambahkan produk Sauce Labs Backpack ke cart.

- Tambahkan produk Sauce Labs Bike Light ke cart.

- Buka halaman Cart.

- Klik tombol Remove pada produk Sauce Labs Backpack.

- Klik tombol Remove pada produk Sauce Labs Bike Light.

- Amati isi halaman Cart dan ikon cart.

Expected Result:
Seluruh produk berhasil dihapus dari cart. Tidak ada produk yang tersisa dan jumlah item pada cart menjadi kosong atau 0.
Actual Result:
Seluruh produk berhasil dihapus dari cart dan Tidak ada produk yang tersisa 
Status:
PASS

## Link Jira

[SCRUM-26 - TC-021 - Remove Semua Produk dari Cart](https://anggirahmadillah.atlassian.net/browse/SCRUM-26)
