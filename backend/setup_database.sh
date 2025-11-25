#!/bin/bash

echo "🚀 Setting up PostgreSQL Database Integration"
echo "=============================================="
echo ""

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "❌ ERROR: .env file not found!"
    echo "Please create a .env file with your credentials."
    echo "See .env.example for template."
    exit 1
fi

echo ""
echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "🗄️  Initializing database tables..."
python init_database.py

echo ""
echo "✅ Database setup complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Update your app.py to use database functions"
echo "   2. Run your Flask application"
echo "   3. Test the API endpoints"
echo ""
echo "📚 See DATABASE_INTEGRATION.md for detailed instructions"
