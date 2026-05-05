#!/bin/bash
# Render Deployment Script for Parking Management System

echo "🚀 Preparing for Render deployment..."

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo "✅ Deployment preparation complete!"
echo "🎉 Your Django app is ready for Render deployment!"
echo ""
echo "Next steps:"
echo "1. Push this code to GitHub"
echo "2. Connect your GitHub repo to Render"
echo "3. Render will automatically detect the render.yaml file"
echo "4. Your app will be deployed with PostgreSQL database"