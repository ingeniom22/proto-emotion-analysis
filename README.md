## Panduan Menjalankan Aplikasi FastAPI

Berikut adalah panduan langkah demi langkah untuk menjalankan aplikasi FastAPI yang telah dibuat.

### Persiapan Awal

1. **Buat Virtual Environment (venv)**: Buka terminal dan masuk ke direktori proyek. Kemudian, jalankan perintah berikut untuk membuat virtual environment:

    ```bash
    python -m venv venv
    ```

2. **Aktifkan Virtual Environment**:

    - **Windows**:
      ```bash
      .\venv\Scripts\activate
      ```

    - **Unix or MacOS**:
      ```bash
      source venv/bin/activate
      ```

### Install Dependencies

3. **Instal Dependencies**: Dalam virtual environment yang diaktifkan, instal semua dependencies yang diperlukan.

    ```bash
    pip install -r requirements.txt
    ```

### Menjalankan Aplikasi

4. **Jalankan UVicorn**: Setelah instalasi selesai, jalankan UVicorn untuk menjalankan aplikasi FastAPI. Pastikan Anda berada di direktori yang berisi file `main.py`

    ```bash
    uvicorn main:app --reload
    ```


5. **Buka Aplikasi di Browser**: Buka browser dan akses [http://localhost:8000](http://localhost:8000) untuk melihat aplikasi FastAPI yang sedang berjalan.
