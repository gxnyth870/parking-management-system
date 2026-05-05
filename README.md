# Parking Web System

A modern Django web application for managing parking spaces with real-time tracking, dark mode, and responsive design.

## Features

- 🅿️ **Real-time Parking Management**: Track vehicle occupancy with live status indicators
- 👤 **Owner Information**: Store and display vehicle owner details
- ⏰ **Time Tracking**: Automatic entry/exit time recording with duration calculation
- 🌙 **Dark Mode**: Toggle between light and dark themes
- 📊 **Live Statistics**: Real-time dashboard with occupancy rates
- 🔍 **Search & Filter**: Find spaces by owner, plate, or vehicle type
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🎨 **Modern UI**: Glassmorphism effects, gradients, and smooth animations

## Local Development Setup

1. Ensure Python 3.8+ is installed
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Run the server: `python manage.py runserver`
5. Open http://127.0.0.1:8000/ in your browser

## GUI Menu

Run the graphical parking simulator: `python gui_menu.py`

## Console Menu

Run the console-based parking simulator: `python menu.py`

## Admin Panel

Access the admin at http://127.0.0.1:8000/admin/ to manage data directly.

## 🚀 Deployment to Render

### Automatic Deployment (Recommended)

1. **Push to GitHub**: Commit and push all files to a GitHub repository

2. **Connect to Render**:
   - Go to [render.com](https://render.com) and sign up/login
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository
   - Render will automatically detect the `render.yaml` configuration

3. **Environment Setup**:
   - Render will automatically create a PostgreSQL database
   - The app will be deployed with production settings

4. **Access Your App**:
   - Once deployed, you'll get a URL like `https://parking-web.onrender.com`

### Manual Deployment

If you prefer manual setup:

1. **Create Render Web Service**:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start Command: `gunicorn parking_web.wsgi:application --bind 0.0.0.0:$PORT`

2. **Add Environment Variables**:
   ```
   DEBUG=False
   SECRET_KEY=your-generated-secret-key
   ALLOWED_HOSTS=your-render-domain.onrender.com
   DATABASE_URL=postgresql://... (provided by Render)
   SECURE_SSL_REDIRECT=True
   SESSION_COOKIE_SECURE=True
   CSRF_COOKIE_SECURE=True
   ```

3. **Create PostgreSQL Database**:
   - Add a PostgreSQL database in Render
   - Connect it to your web service

## Environment Variables

For production deployment, set these environment variables:

- `DEBUG`: Set to `False` for production
- `SECRET_KEY`: Django secret key (auto-generated in render.yaml)
- `ALLOWED_HOSTS`: Comma-separated list of allowed domains
- `DATABASE_URL`: PostgreSQL connection string
- `SECURE_SSL_REDIRECT`: `True` for HTTPS
- `SESSION_COOKIE_SECURE`: `True` for HTTPS
- `CSRF_COOKIE_SECURE`: `True` for HTTPS

## Troubleshooting

- **Templates not loading**: Ensure `TEMPLATES` setting includes app directories
- **Database issues**: Check migrations with `python manage.py showmigrations`
- **Static files**: Run `python manage.py collectstatic` for production
- **Render deployment issues**: Check build logs and ensure all dependencies are in requirements.txt