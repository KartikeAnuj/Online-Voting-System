from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import hashlib
import os

app = Flask(__name__)
app.secret_key = 'voting_system_secret_key_2024'

# Database file path
DATABASE = 'voting.db'

def init_database():
    """Initialize the database with required tables"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create voters table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS voters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            has_voted BOOLEAN DEFAULT FALSE
        )
    ''')
    
    # Create candidates table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            votes INTEGER DEFAULT 0
        )
    ''')
    
    # Create votes table to track voting history
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            voter_id INTEGER,
            candidate_id INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (voter_id) REFERENCES voters (id),
            FOREIGN KEY (candidate_id) REFERENCES candidates (id)
        )
    ''')
    
    # Insert sample candidates if they don't exist
    cursor.execute('SELECT COUNT(*) FROM candidates')
    if cursor.fetchone()[0] == 0:
        sample_candidates = [
            ('Aakash Sharma',),
            ('Meena Kumari',),
            ('Suresh Verma',)
        ]
        cursor.executemany('INSERT INTO candidates (name) VALUES (?)', sample_candidates)
    
    # Insert demo voter if doesn't exist
    cursor.execute('SELECT COUNT(*) FROM voters WHERE email = ?', ('student@example.com',))
    if cursor.fetchone()[0] == 0:
        demo_password = hashlib.md5('1234'.encode()).hexdigest()
        cursor.execute('INSERT INTO voters (name, email, password) VALUES (?, ?, ?)',
                      ('Demo Student', 'student@example.com', demo_password))
    
    conn.commit()
    conn.close()

def hash_password(password):
    """Hash password using MD5 (simple hashing for demo purposes)"""
    return hashlib.md5(password.encode()).hexdigest()

def verify_password(password, hashed):
    """Verify password against hash"""
    return hash_password(password) == hashed

@app.route('/')
def index():
    """Home page with login forms"""
    if 'voter_id' in session:
        return redirect(url_for('vote'))
    if 'admin_logged_in' in session:
        return redirect(url_for('admin'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Voter registration"""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            
            # Check if email already exists
            cursor.execute('SELECT id FROM voters WHERE email = ?', (email,))
            if cursor.fetchone():
                flash('Email already registered! Please use a different email.', 'error')
                return render_template('register.html')
            
            # Insert new voter
            hashed_password = hash_password(password)
            cursor.execute('INSERT INTO voters (name, email, password) VALUES (?, ?, ?)',
                          (name, email, hashed_password))
            conn.commit()
            conn.close()
            
            flash('Registration successful! Please login to vote.', 'success')
            return redirect(url_for('index'))
            
        except sqlite3.Error as e:
            flash('Registration failed. Please try again.', 'error')
            return render_template('register.html')
    
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    """Voter login"""
    email = request.form['email']
    password = request.form['password']
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, name, password, has_voted FROM voters WHERE email = ?', (email,))
    voter = cursor.fetchone()
    conn.close()
    
    if voter and verify_password(password, voter[2]):
        session['voter_id'] = voter[0]
        session['voter_name'] = voter[1]
        session['has_voted'] = voter[3]
        
        if voter[3]:  # If already voted
            flash('You have already voted!', 'info')
            return redirect(url_for('results'))
        else:
            return redirect(url_for('vote'))
    else:
        flash('Invalid email or password!', 'error')
        return redirect(url_for('index'))

@app.route('/admin_login_page')
def admin_login_page():
    """Admin login page"""
    if 'admin_logged_in' in session:
        return redirect(url_for('admin'))
    return render_template('admin_login.html')

@app.route('/admin_login', methods=['POST'])
def admin_login():
    """Admin login"""
    password = request.form['admin_password']
    
    if password == 'admin123':
        session['admin_logged_in'] = True
        return redirect(url_for('admin'))
    else:
        flash('Invalid admin password!', 'error')
        return redirect(url_for('admin_login_page'))

@app.route('/vote')
def vote():
    """Voting page"""
    if 'voter_id' not in session:
        return redirect(url_for('index'))
    
    if session.get('has_voted', False):
        flash('You have already voted!', 'info')
        return redirect(url_for('results'))
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM candidates ORDER BY name')
    candidates = cursor.fetchall()
    conn.close()
    
    return render_template('vote.html', candidates=candidates)

@app.route('/submit_vote', methods=['POST'])
def submit_vote():
    """Submit vote"""
    if 'voter_id' not in session:
        return redirect(url_for('index'))
    
    voter_id = session['voter_id']
    candidate_id = request.form.get('candidate')
    
    if not candidate_id:
        flash('Please select a candidate!', 'error')
        return redirect(url_for('vote'))
    
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Check if already voted
        cursor.execute('SELECT has_voted FROM voters WHERE id = ?', (voter_id,))
        if cursor.fetchone()[0]:
            flash('You have already voted!', 'error')
            return redirect(url_for('results'))
        
        # Record the vote
        cursor.execute('INSERT INTO votes (voter_id, candidate_id) VALUES (?, ?)',
                      (voter_id, candidate_id))
        
        # Update candidate vote count
        cursor.execute('UPDATE candidates SET votes = votes + 1 WHERE id = ?', (candidate_id,))
        
        # Mark voter as voted
        cursor.execute('UPDATE voters SET has_voted = TRUE WHERE id = ?', (voter_id,))
        
        conn.commit()
        conn.close()
        
        session['has_voted'] = True
        flash('Vote submitted successfully!', 'success')
        return redirect(url_for('results'))
        
    except sqlite3.Error as e:
        flash('Vote submission failed. Please try again.', 'error')
        return redirect(url_for('vote'))

@app.route('/results')
def results():
    """Show voting results"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT name, votes FROM candidates ORDER BY votes DESC')
    results = cursor.fetchall()
    conn.close()
    
    return render_template('results.html', results=results)

@app.route('/admin')
def admin():
    """Admin dashboard"""
    if 'admin_logged_in' not in session:
        return redirect(url_for('index'))
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, votes FROM candidates ORDER BY votes DESC')
    candidates = cursor.fetchall()
    conn.close()
    
    return render_template('admin.html', candidates=candidates)

@app.route('/add_candidate', methods=['POST'])
def add_candidate():
    """Add new candidate"""
    if 'admin_logged_in' not in session:
        return redirect(url_for('index'))
    
    name = request.form['candidate_name']
    
    if name.strip():
        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO candidates (name) VALUES (?)', (name.strip(),))
            conn.commit()
            conn.close()
            flash('Candidate added successfully!', 'success')
        except sqlite3.Error:
            flash('Failed to add candidate. Please try again.', 'error')
    else:
        flash('Please enter a valid candidate name!', 'error')
    
    return redirect(url_for('admin'))

@app.route('/logout')
def logout():
    """Logout user"""
    session.clear()
    flash('Logged out successfully!', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Initialize database on first run
    init_database()
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
