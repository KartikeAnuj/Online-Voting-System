# 🗳️ Online Voting System

A modern, secure web-based voting system built with Python Flask and Bootstrap 5. This system allows voters to register, login, and cast votes while providing administrators with tools to manage candidates and view real-time results.

![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Flask](https://img.shields.io/badge/flask-v3.1.2-green.svg)
![Bootstrap](https://img.shields.io/badge/bootstrap-v5.3.0-purple.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- 🔐 **Secure Voter Registration & Login**
- 🗳️ **One-Vote-Per-Person Enforcement**
- 👨‍💼 **Admin Dashboard** for candidate management
- 📊 **Real-time Results** with progress bars
- 📱 **Responsive Design** with Bootstrap 5
- 🎨 **Modern UI** with gradient backgrounds
- 🗄️ **SQLite Database** for data storage
- 🚀 **Easy Deployment** with GitHub Actions

## 🚀 Live Demo

**[View Live Application](https://online-voting-system-app.herokuapp.com/)**

## 📸 Screenshots

### Home Page
![Home Page](https://via.placeholder.com/800x400/667eea/ffffff?text=Online+Voting+System+Home)

### Voting Interface
![Voting Page](https://via.placeholder.com/800x400/764ba2/ffffff?text=Voting+Interface)

### Admin Dashboard
![Admin Panel](https://via.placeholder.com/800x400/28a745/ffffff?text=Admin+Dashboard)

## 🛠️ Installation

### Prerequisites
- Python 3.11+
- pip (Python package installer)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/KartikeAnuj/Online-Voting-System.git
   cd Online-Voting-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://127.0.0.1:5000`

## 🔑 Demo Credentials

### Voter Login
- **Email:** `student@example.com`
- **Password:** `1234`

### Admin Login
- **Password:** `admin123`

## 📁 Project Structure

```
Online-Voting-System/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment config
├── runtime.txt           # Python version specification
├── test_app.py           # Unit tests
├── .github/
│   └── workflows/
│       └── deploy.yml    # GitHub Actions workflow
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── register.html     # Registration form
│   ├── vote.html         # Voting interface
│   ├── results.html      # Results display
│   ├── admin.html        # Admin dashboard
│   └── admin_login.html  # Admin login page
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables
- `PORT`: Server port (default: 5000)
- `FLASK_ENV`: Environment mode (development/production)

### Database
The application uses SQLite database (`voting.db`) which is automatically created on first run with sample data:
- **Sample Candidates:** Aakash Sharma, Meena Kumari, Suresh Verma
- **Demo Voter:** student@example.com / 1234

## 🚀 Deployment

### GitHub Actions + Heroku

This project includes automated deployment using GitHub Actions:

1. **Set up Heroku Account**
   - Create account at [heroku.com](https://heroku.com)
   - Create a new app named `online-voting-system-app`

2. **Configure GitHub Secrets**
   - Go to repository Settings → Secrets and variables → Actions
   - Add `HEROKU_API_KEY` with your Heroku API key

3. **Deploy**
   - Push to `main` branch triggers automatic deployment
   - Check Actions tab for deployment status

### Manual Heroku Deployment

```bash
# Install Heroku CLI
npm install -g heroku

# Login to Heroku
heroku login

# Create Heroku app
heroku create online-voting-system-app

# Deploy
git push heroku main
```

## 🧪 Testing

Run the test suite:
```bash
python test_app.py
```

## 🛡️ Security Features

- Password hashing (MD5 for demo purposes)
- Session-based authentication
- One-vote-per-person enforcement
- SQL injection prevention
- Admin access control

## 🔄 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page with login forms |
| GET | `/register` | Voter registration page |
| POST | `/register` | Process voter registration |
| POST | `/login` | Voter login |
| GET | `/admin_login_page` | Admin login page |
| POST | `/admin_login` | Admin authentication |
| GET | `/vote` | Voting interface |
| POST | `/submit_vote` | Submit vote |
| GET | `/results` | View results |
| GET | `/admin` | Admin dashboard |
| POST | `/add_candidate` | Add new candidate |
| GET | `/logout` | User logout |

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Kartike Anuj**
- GitHub: [@KartikeAnuj](https://github.com/KartikeAnuj)

## 🙏 Acknowledgments

- Flask framework
- Bootstrap 5 for UI components
- Bootstrap Icons for icons
- Heroku for hosting platform
- GitHub Actions for CI/CD

## 📞 Support

If you have any questions or need help, please open an issue on GitHub.

---

⭐ **Star this repository if you found it helpful!**