# SCRUM-30 - TC-025 - Reset App State

## Informasi Issue

| Field | Detail |
|---|---|
| Issue Key | [SCRUM-30](https://anggirahmadillah.atlassian.net/browse/SCRUM-30) |
| Issue Type | Task |
| Status | Done |
| Priority | Medium |
| Assignee | Anggi Rahmadillah |
| Reporter | Anggi Rahmadillah |

## Deskripsi

Test Case ID: TC-025
Test Scenario:
Verify Reset App State Functionality
Objective:
Memastikan fitur Reset App State mengembalikan kondisi aplikasi ke keadaan awal.
Precondition:
User sudah berhasil login.
Test Steps:

- Login menggunakan username: standard_user

- Masukkan password: secret_sauce

- Klik tombol Login.

- Tambahkan produk Sauce Labs Backpack ke cart.

- Buka sidebar menu.

- Klik menu Reset App State.

- Amati ikon cart dan kondisi aplikasi.

Expected Result:
Produk yang ada di cart dihapus, badge jumlah cart menjadi kosong, dan kondisi aplikasi kembali seperti semula.
Actual Result:
Produk yang ada di cart terhapus, badge jumlah cart menjadi kosong, dan kondisi aplikasi kembali seperti semula.
Status:
PASS

## Link Jira

[SCRUM-30 - TC-025 - Reset App State](https://anggirahmadillah.atlassian.net/browse/SCRUM-30)
