"""
Database Initialization Script
Run this to set up the PostgreSQL database tables
"""
import os
from flask import Flask
from database import init_db, db, Patient, Prediction, Statistics
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def initialize_database():
    """Initialize database tables"""
    app = Flask(__name__)
    
    # Initialize database
    init_db(app)
    
    print("✅ Database initialized successfully!")
    print(f"📊 Tables created:")
    print(f"   - patients")
    print(f"   - predictions")
    print(f"   - statistics")
    
    # Test connection
    with app.app_context():
        try:
            # Try to query
            patient_count = Patient.query.count()
            prediction_count = Prediction.query.count()
            print(f"\n📈 Current database status:")
            print(f"   - Patients: {patient_count}")
            print(f"   - Predictions: {prediction_count}")
        except Exception as e:
            print(f"⚠️  Error testing database: {e}")

if __name__ == '__main__':
    print("🚀 Initializing PostgreSQL database...")
    initialize_database()
