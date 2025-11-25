"""
Quick script to check database contents
"""
from flask import Flask
from database import init_db, db, Patient, Prediction
from db_integration import get_all_predictions, calculate_statistics

app = Flask(__name__)
init_db(app)

with app.app_context():
    print("\n" + "="*50)
    print("DATABASE STATUS CHECK")
    print("="*50)
    
    # Check patients
    patients = Patient.query.all()
    print(f"\n📊 Patients in database: {len(patients)}")
    for p in patients:
        print(f"   - {p.patient_id}: {p.name}")
    
    # Check predictions
    predictions = Prediction.query.all()
    print(f"\n📊 Predictions in database: {len(predictions)}")
    for pred in predictions:
        print(f"   - {pred.prediction_id}: {pred.disease} ({pred.confidence*100:.1f}%)")
    
    # Check statistics
    stats = calculate_statistics()
    print(f"\n📊 Statistics:")
    print(f"   - Total Predictions: {stats['total_predictions']}")
    print(f"   - Average Confidence: {stats['average_confidence']:.2f}")
    print(f"   - Disease Distribution: {stats['disease_distribution']}")
    
    print("\n" + "="*50)
    
    if len(predictions) == 0:
        print("⚠️  NO PREDICTIONS IN DATABASE!")
        print("   Make a prediction to test database save.")
    else:
        print("✅ Database has data!")
    
    print("="*50 + "\n")
