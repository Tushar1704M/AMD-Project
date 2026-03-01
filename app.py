from flask import Flask, render_template

app = Flask(__name__)

# AMD 2026 Enterprise Global Database
PORTFOLIO = {
    'ryzen9': {
        'name': 'Ryzen™ 9 9950X3D',
        'file': 'amd_ryzen_9_9950x3d_3d_model.glb',
        'price': '₹62,500',
        'node': 'TSMC 4nm (Zen 5 Optimized)',
        'summary': 'The 2026 flagship leveraging 2nd Gen 3D V-Cache. Designed for sub-30ns memory latency in extreme gaming and local LLM inferencing.',
        'specs': [['Cores', '16'], ['Threads', '32'], ['Cache', '144MB L3'], ['TDP', '120W']]
    },
    'mi350x': {
        'name': 'Instinct™ MI350X',
        'file': 'instinct_mi350.glb',
        'price': 'Enterprise Quote',
        'node': '3nm CDNA 4 Architecture',
        'summary': 'World’s most powerful AI accelerator for exascale clusters. Features 288GB HBM3e memory to run 400B+ parameter models on a single node.',
        'specs': [['Memory', '288GB HBM3e'], ['Bandwidth', '5.3 TB/s'], ['FP8 Perf', 'Exascale Ready']]
    },
    'gaming_pc': {
        'name': 'Advantage™ G1660 Extreme',
        'file': 'pc_gaming_ryzen_nvidia_1660.glb',
        'price': '₹1,45,000',
        'node': 'Unified RDNA 4 / Zen 5',
        'summary': 'A fully integrated ecosystem using Smart Access Memory 2.0. Direct Storage and AI Frame Gen 4.0 are baked into the kernel.',
        'specs': [['GPU', 'Radeon™ RX 8000 Series'], ['RAM', '32GB DDR5-8000'], ['Cooling', 'Vapor-Chamber']]
    },
    'ryzen5': {
        'name': 'Ryzen™ 5 Pro 4650G',
        'file': 'amd_cpu_am4_ryzen_5_pro_4650g_next_3.7_ghz.glb',
        'price': '₹18,500',
        'node': '7nm FinFET (PRO Optimized)',
        'summary': 'Business-critical stability with AMD Memory Guard. Integrated Radeon graphics remove the need for discrete GPUs in secure office environments.',
        'specs': [['Cores', '6'], ['GPU', '7-Core Radeon'], ['Security', 'AMD PRO']]
    }
}

# 14 Routes for Global Expansion
@app.route('/')
def index(): return render_template('index.html')

@app.route('/home')
def home(): return render_template('home.html')

@app.route('/catalog')
def catalog(): return render_template('catalog.html', products=PORTFOLIO)

@app.route('/product/<pid>')
def product(pid): return render_template('details.html', p=PORTFOLIO.get(pid), pid=pid)

@app.route('/lab/<pid>')
def lab(pid): return render_template('lab.html', p=PORTFOLIO.get(pid), pid=pid)

@app.route('/technology')
def tech(): return render_template('technology.html')

@app.route('/ai')
def ai(): return render_template('ai.html')

@app.route('/gaming')
def gaming(): return render_template('gaming.html')

@app.route('/enterprise')
def enterprise(): return render_template('enterprise.html')

@app.route('/green')
def green(): return render_template('green.html')

@app.route('/investors')
def investors(): return render_template('investors.html')

@app.route('/news')
def news(): return render_template('news.html')

@app.route('/support')
def support(): return render_template('support.html')

@app.route('/layout')
def layout(): return render_template('layout.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)