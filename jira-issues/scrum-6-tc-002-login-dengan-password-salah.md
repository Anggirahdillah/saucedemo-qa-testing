# SCRUM-6 - TC-002 - Login dengan Password Salah

## Informasi Issue

| Field | Detail |
|---|---|
| Issue Key | [SCRUM-6](https://anggirahmadillah.atlassian.net/browse/SCRUM-6) |
| Issue Type | Task |
| Status | Done |
| Priority | Medium |
| Assignee | Anggi Rahmadillah |
| Reporter | Anggi Rahmadillah |

## Deskripsi

Test Case ID: TC-002
Test Scenario:
Verify Login Functionality
Objective:
Memastikan sistem menolak login ketika password yang dimasukkan salah.
Precondition:
User berada pada halaman login SauceDemo.
Test Steps:

- Buka halaman  

- Masukkan username: standard_user

- Masukkan password yang salah, misalnya: wrong_password

- Klik tombol Login.

Expected Result:
Sistem menolak proses login dan menampilkan pesan error:
Epic sadface: Username and password do not match any user in this service
Actual Result:
Sistem menolak proses login dan menampilkan pesan error:
Epic sad face: Username and password do not match any user in this service
Status:
PASS

## Link Jira

[SCRUM-6 - TC-002 - Login dengan Password Salah](https://anggirahmadillah.atlassian.net/browse/SCRUM-6)
