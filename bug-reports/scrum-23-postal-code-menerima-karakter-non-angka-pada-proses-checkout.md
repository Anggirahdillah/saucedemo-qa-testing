# SCRUM-23 - Postal Code menerima karakter non-angka pada proses checkout

## Informasi Issue

| Field | Detail |
|---|---|
| Issue Key | [SCRUM-23](https://anggirahmadillah.atlassian.net/browse/SCRUM-23) |
| Issue Type | Bug |
| Status | Done |
| Priority | Medium |
| Assignee | Anggi Rahmadillah |
| Reporter | Anggi Rahmadillah |

## Deskripsi

Related Test Case:
TC-018 - Checkout Validation with Invalid Postal Code
Steps to Reproduce:

- Login menggunakan standard_user / secret_sauce.

- Tambahkan Sauce Labs Backpack ke cart.

- Buka Cart.

- Klik Checkout.

- Isi First Name dengan Anggi.

- Isi Last Name dengan Rahdillah.

- Isi Postal Code dengan abc123.

- Klik Continue.

Expected Result:
Sistem menolak Postal Code yang mengandung karakter non-angka dan menampilkan pesan validasi.
Actual Result:
Sistem menerima Postal Code "abc123" dan melanjutkan ke halaman Checkout: Overview.
Severity:
Low
Priority:
Medium
Status:
Open

## Link Jira

[SCRUM-23 - Postal Code menerima karakter non-angka pada proses checkout](https://anggirahmadillah.atlassian.net/browse/SCRUM-23)
