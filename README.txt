ONLINE VOTING SYSTEM - SETUP & USAGE GUIDE
===========================================

OVERVIEW
--------
A simple web-based Online Voting System built with Python Flask, featuring:
- Voter registration and login
- Secure voting with one-vote-per-person limit
- Admin dashboard for managing candidates and viewing results
- Modern Bootstrap 5 UI with responsive design
- SQLite database for data storage

SETUP INSTRUCTIONS
------------------
1. Install Flask:
   pip install flask

2. Run the application:
   python app.py

3. Open your web browser and go to:
   http://127.0.0.1:5000

DEMO CREDENTIALS
----------------
Voter Login:
- Email: student@example.com
- Password: 1234

Admin Login:
- Password: admin123

FEATURES
--------
✓ Voter Registration (Name, Email, Password)
✓ Voter Login with authentication
✓ Voting page with candidate selection
✓ One-vote-per-person enforcement
✓ Admin login with fixed password
✓ Admin dashboard showing vote counts
✓ Add new candidates from admin panel
✓ Real-time results with progress bars
✓ Bootstrap 5 responsive design
✓ SQLite database storage

TECHNICAL DETAILS
-----------------
- Backend: Python Flask
- Database: SQLite (voting.db)
- Frontend: Bootstrap 5 + HTML5
- Password Security: MD5 hashing (demo purposes)
- Session Management: Flask sessions

FILE STRUCTURE
--------------
online voting system/
├── app.py                 # Main Flask application
├── voting.db             # SQLite database (auto-created)
├── README.txt            # This file
└── templates/            # HTML templates
    ├── base.html         # Base template with Bootstrap
    ├── index.html        # Login page
    ├── register.html     # Registration form
    ├── vote.html         # Voting interface
    ├── results.html      # Results display
    └── admin.html        # Admin dashboard

DATABASE SCHEMA
---------------
- voters: Stores voter information and voting status
- candidates: Stores candidate information and vote counts
- votes: Tracks individual votes for audit purposes

USAGE WORKFLOW
--------------
1. Voters register with their details
2. Voters login and cast their vote
3. System prevents multiple voting
4. Admin can add new candidates
5. Real-time results are displayed
6. Results show vote counts and percentages

SECURITY FEATURES
-----------------
- Password hashing (MD5)
- Session-based authentication
- One-vote-per-person enforcement
- Admin access control
- SQL injection prevention

TROUBLESHOOTING
---------------
- If port 5000 is busy, change the port in app.py
- Database is auto-created on first run
- Check console for any error messages
- Ensure Flask is properly installed

DEVELOPMENT NOTES
-----------------
- This is a demo system for educational purposes
- For production use, implement stronger security measures
- Consider using more robust password hashing (bcrypt)
- Add email verification for voter registration
- Implement proper audit logging

SUPPORT
-------
For issues or questions, check the console output when running the application.
The system includes error handling and user-friendly messages.

Happy Voting! 🗳️
