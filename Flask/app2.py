from flask import Flask, render_template, request, redirect, url_for
import math

app = Flask(__name__)

calculations = []

@app.route('/')
def index():
    "Halaman utama"
    return render_template('index.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    """Halaman pengeksekusian perhitungan"""
    if request.method == 'POST':
        shape = request.form['shape']
        var1 = float(request.form['var1'])
        var2 = float(request.form.get('var2', 0))
        var3 = float(request.form.get('var3', 0))
        
        # Menghitung volume berdasarkan bangun ruang
        if shape == 'cube':
            volume = var1 ** 3
            shape_name = 'Kubus'
            var1_name = 'Sisi'
            var2_name = '-'
        elif shape == 'block':
            var2 = float(request.form['var2'])
            volume = var1 * var2 * float(request.form['var3'])
            shape_name = 'Balok'
            var1_name = 'Panjang'
            var2_name = 'Lebar'
        elif shape == 'sphere':
            volume = (4/3) * math.pi * (var1 ** 3)
            shape_name = 'Bola'
            var1_name = 'Jari-jari'
            var2_name = '-'
        elif shape == 'cylinder':
            var2 = float(request.form['var2'])
            volume = math.pi * (var1 ** 2) * var2
            shape_name = 'Tabung'
            var1_name = 'Jari-jari'
            var2_name = 'Tinggi'
        elif shape == 'cone':
            var2 = float(request.form['var2'])
            volume = (1/3) * math.pi * (var1 ** 2) * var2
            shape_name = 'Kerucut'
            var1_name = 'Jari-jari'
            var2_name = 'Tinggi'
        else:
            volume = 0
            shape_name = 'Unknown'
            var1_name = 'Variabel 1'
            var2_name = 'Variabel 2'
        
        # Menyimpan hasil perhitungan
        calculation_data = {
            'shape': shape_name,
            'var1': var1,
            'var2': var2,
            'var1_name': var1_name,
            'var2_name': var2_name,
            'volume': round(volume, 2)
        }
        calculations.append(calculation_data)
        
        return redirect(url_for('results'))
    
    return render_template('calculate.html')

@app.route('/results')
def results():
    """Halaman untuk menampilkan daftar data yang diinput dan hasilnya"""
    return render_template('results.html', calculations=calculations)

if __name__ == '__main__':
    app.run(debug=True)