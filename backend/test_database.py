"""
Quick test to verify database connection and app imports
"""
print("🧪 Testing database and app imports...")

try:
    print("\n1️⃣ Testing database imports...")
    from database import db, Patient, Prediction, Statistics
    print("   ✅ Database models imported successfully")
    
    print("\n2️⃣ Testing database integration...")
    from db_integration import calculate_statistics, get_all_patients
    print("   ✅ Database integration imported successfully")
    
    print("\n3️⃣ Testing AI recommendations...")
    from ai_recommendations import generate_ai_recommendations
    print("   ✅ AI recommendations imported successfully")
    
    print("\n4️⃣ Testing Flask app...")
    from flask import Flask
    from database import init_db
    
    app = Flask(__name__)
    init_db(app)
    print("   ✅ Flask app initialized with database")
    
    print("\n5️⃣ Testing database connection...")
    with app.app_context():
        patient_count = Patient.query.count()
        prediction_count = Prediction.query.count()
        print(f"   ✅ Database connected!")
        print(f"   📊 Patients: {patient_count}")
        print(f"   📊 Predictions: {prediction_count}")
    
    print("\n✅ All tests passed! Your app is ready to run.")
    print("\n🚀 Start the app with: python app.py")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
    print("\n💡 Try running: pip install -r requirements.txt")
