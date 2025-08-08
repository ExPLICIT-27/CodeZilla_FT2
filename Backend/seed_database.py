#!/usr/bin/env python3
"""
Database seeding script for CredNova
"""

import sys
import os
from datetime import datetime
from dotenv import load_dotenv

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.models.database import Database, User, FinancialData, CreditScore

def seed_database():
    """Seed the database with initial data"""
    
    # Load environment variables
    load_dotenv()
    
    # Initialize database
    mongo_uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/credit_score_dev')
    Database.initialize(mongo_uri)
    
    print("🌱 Seeding database...")
    
    # Create test users
    test_users = [
        {
            'firebase_uid': 'test-user-1',
            'email': 'john.doe@example.com',
            'name': 'John Doe',
            'profile': {
                'age': 28,
                'location': 'California',
                'occupation': 'Software Engineer'
            }
        },
        {
            'firebase_uid': 'test-user-2', 
            'email': 'jane.smith@example.com',
            'name': 'Jane Smith',
            'profile': {
                'age': 35,
                'location': 'Texas',
                'occupation': 'Marketing Manager'
            }
        }
    ]
    
    for user_data in test_users:
        existing_user = User.find_by_firebase_uid(user_data['firebase_uid'])
        if not existing_user:
            user_id = User.create(user_data)
            print(f"✅ Created user: {user_data['name']} (ID: {user_id})")
        else:
            print(f"⚠️  User {user_data['name']} already exists")
    
    # Create sample financial data
    sample_financial_data = [
        {
            'firebase_uid': 'test-user-1',
            'personal_info': {
                'age': 28,
                'state': 'CA',
                'education_level': 'bachelors'
            },
            'employment_income': {
                'employment_type': 'full_time',
                'monthly_income': 5500,
                'job_duration': '3'
            },
            'housing': {
                'monthly_cost': 2000,
                'has_mortgage': True,
                'monthly_savings': 800,
                'bank_balance': 15000
            },
            'family': {
                'dependents': 1
            },
            'credit_loans': {
                'has_student_loan': True,
                'has_car_loan': False,
                'car_loan_payment': 0,
                'stud_loan_payments': 300,
                'credit_cards': 2
            },
            'credit_behavior': {
                'recent_inquiries': 1,
                'late_payments': 0,
                'bankruptcy': False,
                'credit_history_years': 5
            }
        }
    ]
    
    for financial_data in sample_financial_data:
        result = FinancialData.update_or_create(
            financial_data['firebase_uid'], 
            financial_data
        )
        print(f"✅ Created/Updated financial data for user: {financial_data['firebase_uid']}")
    
    print("🎉 Database seeding completed!")

def clear_database():
    """Clear all data from database"""
    load_dotenv()
    mongo_uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/credit_score_dev')
    Database.initialize(mongo_uri)
    
    print("🧹 Clearing database...")
    
    # Clear all collections
    collections = ['users', 'financial_data', 'credit_scores', 'chat_history']
    for collection_name in collections:
        collection = Database.get_collection(collection_name)
        result = collection.delete_many({})
        print(f"✅ Cleared {result.deleted_count} documents from {collection_name}")
    
    print("🎉 Database cleared!")

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Database management script')
    parser.add_argument('--clear', action='store_true', help='Clear all data from database')
    parser.add_argument('--seed', action='store_true', help='Seed database with sample data')
    
    args = parser.parse_args()
    
    if args.clear:
        clear_database()
    elif args.seed:
        seed_database()
    else:
        print("Usage: python seed_database.py --seed | --clear")
