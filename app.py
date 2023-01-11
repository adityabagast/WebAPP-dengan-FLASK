from flask import Flask, render_template
app = Flask(__name__)

konten = [
    {
    'penulis': 'Aditya Bagas',
    'judul': 'Postingan Pertama',
    'sinopsis': 'Ini Adalah Sinopsis Postingan Pertama',
    'isi': 'Ini Adalah Isi dari Postingan Pertama',
    'tanggal': '11 Januari 2023',
    'jam': '14:26'
    },
    {
    'penulis': 'Aditya Bagas T',
    'judul': 'Web App Pertama Dengan FLASK',
    'sinopsis': 'Belajar buat WEB dengan FLASK',
    'isi': 'Ini Adalah Testing',
    'tanggal': '11 Januari 2023',
    'jam': '14:29'
    }
]

@app.route('/tentang/')
def tentang():
    return render_template('tentang.html', judul='Tentang')

@app.route('/')
def home():
    return render_template('home.html', konten=konten, judul='Beranda' )

if __name__ == '__main__':
    app.run(debug=True)