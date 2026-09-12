# SCRUM-31 - TC-026 - Akses Halaman Products Setelah Logout

## Informasi Issue

| Field | Detail |
|---|---|
| Issue Key | [SCRUM-31](https://anggirahmadillah.atlassian.net/browse/SCRUM-31) |
| Issue Type | Task |
| Status | Done |
| Priority | Medium |
| Assignee | Anggi Rahmadillah |
| Reporter | Anggi Rahmadillah |

## Deskripsi

Test Case ID: TC-026
Test Scenario:
Verify Access to Products Page After Logout
Objective:
Memastikan user yang sudah logout tidak dapat mengakses halaman Products melalui navigasi browser sebelumnya.
Precondition:
User sudah berhasil login dan berada di halaman Products.
Test Steps:

- Login menggunakan username: standard_user

- Masukkan password: secret_sauce

- Klik tombol Login.

- Catat URL halaman Products.

- Klik sidebar menu.

- Klik Logout.

- Gunakan tombol Back pada browser.

- Amati halaman yang ditampilkan.

Expected Result:
User tidak dapat menggunakan halaman Products dalam kondisi login dan sistem mengarahkan user ke halaman login atau menampilkan halaman login.
Actual Result:
User tidak dapat menggunakan halaman Products dan sistem tetap pada halaman login 
Status:
PASS

## Link Jira

[SCRUM-31 - TC-026 - Akses Halaman Products Setelah Logout](https://anggirahmadillah.atlassian.net/browse/SCRUM-31)
