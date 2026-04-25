from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 🔥 penyimpanan sementara (RAM)
users = []

# ======================
# HALAMAN
# ======================

@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/register')
def register_page():
    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# ======================
# PROSES LOGIN
# ======================

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    for user in users:
        if user['email'] == email and user['password'] == password:
            return redirect('/dashboard')

    return render_template('error.html')


# ======================
# PROSES REGISTER
# ======================

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']

    users.append({
        'email': email,
        'password': password
    })

    return redirect('/')


# ======================
# LOGOUT
# ======================

@app.route('/logout')
def logout():
    return redirect('/')


# ======================
# RUN
# ======================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 10000)
