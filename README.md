# Peta Data Center Asia Tenggara

Peta interaktif data center di Indonesia, Asia Tenggara, India, dan negara Teluk. Isinya fasilitas yang
beroperasi, sedang dibangun, dan direncanakan, dengan filter pilihan ganda (negara, wilayah, tipe, tier,
sinyal AI) dan panel sorotan MW per tahap, termasuk porsinya terhadap total nasional.

Situsnya statis: satu `index.html` plus file data. Tidak perlu build di Vercel.

## Isi repo

| File | Fungsi |
|---|---|
| `index.html` | Halaman peta (data sudah tertanam di dalamnya) |
| `data/data-center-regional-okt2026.csv` | Master data semua negara |
| `data/data-center-indonesia-okt2026.csv` | Master data Indonesia saja |
| `data/dc_data.json` | Data yang dipakai peta |
| `src/template.html` | Template halaman (`__DATA__` diganti isi JSON) |
| `src/build.py` | Membangun ulang `index.html` dari template + JSON |
| `vercel.json` | Pengaturan Vercel (URL bersih, cache untuk folder data) |

## Deploy ke Vercel lewat GitHub (tanpa terminal)

1. **Buat repo di GitHub.** Buka https://github.com/new, beri nama (misalnya `peta-data-center-sea`),
   pilih *Private* atau *Public*, lalu klik **Create repository**.
2. **Unggah file.** Di halaman repo baru, klik **uploading an existing file**, lalu seret *isi* folder ini
   (bukan foldernya) ke browser: `index.html`, `vercel.json`, `README.md`, `.gitignore`, folder `data`, dan
   folder `src`. Klik **Commit changes**.
   - Catatan: `.gitignore` adalah file tersembunyi. Kalau tidak terlihat, boleh dilewati.
3. **Hubungkan ke Vercel.** Buka https://vercel.com/new, masuk dengan akun GitHub, pilih repo tadi, klik **Import**.
   - *Framework Preset*: **Other**. *Build Command* dan *Output Directory*: biarkan kosong.
   - Klik **Deploy**. Dalam ±1 menit situs aktif di alamat `nama-repo.vercel.app`.
4. **Domain sendiri (opsional).** Di Vercel: Project → Settings → Domains → tambahkan domainmu.

Setiap kali isi repo diubah (commit/push), Vercel otomatis men-deploy ulang.

## Memperbarui data

- Cara cepat: ganti `index.html` dan file di `data/` dengan versi baru, lalu commit.
- Kalau hanya `data/dc_data.json` yang berubah, bangun ulang halamannya:

  ```bash
  python3 src/build.py
  ```

  lalu commit `index.html` yang baru.

## Sumber data

Data Center Map (direktori fasilitas), ArusGrid (status proyek, CC BY-NC 4.0), tabel Indonesia Maps & Globe,
serta berita dan rilis DatacenterDynamics, Telkom, DCI Indonesia, ANTARA, Baxtel, dan operator terkait.
Titik lokasi adalah perkiraan. Status per 2 Oktober 2026.
