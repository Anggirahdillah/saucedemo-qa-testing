# Bug Report - TC018

## Bug ID
BUG-001

## Judul
Sistem menerima postal code yang mengandung huruf

## Modul
Checkout

## Severity
Medium

## Priority
Medium

## Test Case
TC018 - Checkout dengan postal code tidak valid

## Langkah Reproduksi
1. Login ke SauceDemo.
2. Tambahkan produk ke cart.
3. Buka halaman Cart.
4. Klik Checkout.
5. Isi First Name dan Last Name.
6. Isi Postal Code dengan `abc123`.
7. Klik Continue.

## Expected Result
Sistem menolak postal code yang mengandung huruf, menampilkan pesan validasi, dan tidak melanjutkan ke halaman Checkout: Overview.

## Actual Result
Sistem menerima postal code `abc123` dan melanjutkan ke halaman Checkout: Overview.

## Status
Open

## Evidence
- Screenshot input postal code `abc123`
- Screenshot halaman Checkout: Overview
- Hasil pytest TC018