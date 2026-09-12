# SCRUM-33 - Test Execution Report - SauceDemo

## Informasi Issue

| Field | Detail |
|---|---|
| Issue Key | [SCRUM-33](https://anggirahmadillah.atlassian.net/browse/SCRUM-33) |
| Issue Type | Task |
| Status | Done |
| Priority | Medium |
| Assignee | Anggi Rahmadillah |
| Reporter | Anggi Rahmadillah |

## Deskripsi

TEST EXECUTION REPORT - SAUCEDEMO

- PROJECT

Project Name:
SauceDemo Web Application
Testing Type:
Functional Testing
Testing Platform:
Web Application
Testing Tool:
Jira

- TESTING OBJECTIVE

Pengujian ini dilakukan untuk memastikan fitur-fitur utama pada aplikasi SauceDemo dapat berjalan sesuai dengan hasil yang diharapkan. Pengujian juga bertujuan untuk menemukan kesalahan atau potensi masalah pada proses penggunaan aplikasi.

- TESTING SCOPE

Fitur yang diuji meliputi:

- Login

- Product Listing

- Product Sorting

- Product Detail

- Add Product to Cart

- Remove Product from Cart

- Shopping Cart

- Checkout Information

- Checkout Validation

- Checkout Overview

- Logout

- TEST EXECUTION SUMMARY

Total Test Cases : 28
Executed Test Cases : 28
Passed : 27
Failed : 1
Not Executed : 0
Pass Rate : 96.43%

- TEST EXECUTION RESULT

Berdasarkan pengujian yang telah dilakukan, sebanyak 27 test case berhasil dijalankan sesuai dengan expected result. Sementara itu, 1 test case mengalami kegagalan pada proses validasi Postal Code ketika melakukan checkout.

- FAILED TEST CASE

Test Case ID:
TC-018
Test Case Name:
Checkout Validation with Invalid Postal Code
Test Data:
Postal Code = abc123
Expected Result:
Sistem menolak Postal Code yang mengandung karakter non-angka dan menampilkan pesan validasi kepada pengguna.
Actual Result:
Sistem menerima Postal Code "abc123" dan tetap melanjutkan ke halaman Checkout: Overview tanpa menampilkan pesan validasi.
Test Result:
FAIL

- BUG IDENTIFICATION

Ditemukan potensi masalah pada validasi Postal Code. Sistem masih menerima input yang mengandung karakter non-angka pada proses checkout.
Bug tersebut telah dicatat pada issue Jira yang berkaitan dengan TC-018.
Bug Issue Key:
SCRUM-23

- TEST EVIDENCE

Evidence 1:
Evidence 2:

Evidence 3:

Evidence 4:
Evidence 5:
Evidence 6:

- CONCLUSION

Berdasarkan hasil pengujian terhadap 28 test case pada aplikasi SauceDemo, sebanyak 27 test case berhasil dan 1 test case gagal.
Persentase keberhasilan pengujian adalah 96.43%.
Kegagalan ditemukan pada validasi Postal Code karena sistem menerima input "abc123" dan tetap melanjutkan proses checkout tanpa menampilkan pesan validasi.
Secara keseluruhan, sebagian besar fitur yang diuji dapat berjalan sesuai dengan expected result. Namun, masih terdapat potensi perbaikan pada validasi input Postal Code.

## Link Jira

[SCRUM-33 - Test Execution Report - SauceDemo](https://anggirahmadillah.atlassian.net/browse/SCRUM-33)
