from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import uuid

class Database:
    client = None
    db = None
    
    @staticmethod
    def initialize(uri):
        Database.client = MongoClient(uri)
        Database.db = Database.client.get_default_database()
        Database._create_indexes()
    
    @staticmethod
    def _create_indexes():
        """Create database indexes for better performance"""
        try:
            # Users collection indexes
            users_collection = Database.get_collection(User.COLLECTION)
            users_collection.create_index('firebase_uid', unique=True)
            users_collection.create_index('email')
            
            # Financial data collection indexes  
            financial_collection = Database.get_collection(FinancialData.COLLECTION)
            financial_collection.create_index('firebase_uid')
            financial_collection.create_index('created_at')
            
            # Credit scores collection indexes
            scores_collection = Database.get_collection(CreditScore.COLLECTION)
            scores_collection.create_index('firebase_uid')
            scores_collection.create_index('created_at')
            scores_collection.create_index('score_id', unique=True)
            
            # Chat history collection indexes
            chat_collection = Database.get_collection(ChatHistory.COLLECTION)
            chat_collection.create_index('firebase_uid')
            chat_collection.create_index('timestamp')
            
            print("✅ Database indexes created successfully")
        except Exception as e:
            print(f"⚠️  Error creating indexes: {str(e)}")
    
    @staticmethod
    def get_collection(name):
        return Database.db[name]

class User:
    COLLECTION = 'users'
    
    @staticmethod
    def create(user_data):
        """Create a new user record"""
        user_data['created_at'] = datetime.utcnow()
        user_data['updated_at'] = datetime.utcnow()
        result = Database.get_collection(User.COLLECTION).insert_one(user_data)
        return str(result.inserted_id)
    
    @staticmethod
    def find_by_firebase_uid(firebase_uid):
        """Find user by Firebase UID"""
        return Database.get_collection(User.COLLECTION).find_one({'firebase_uid': firebase_uid})
    
    @staticmethod
    def find_by_id(user_id):
        """Find user by MongoDB ObjectId"""
        return Database.get_collection(User.COLLECTION).find_one({'_id': ObjectId(user_id)})
    
    @staticmethod
    def update(firebase_uid, update_data):
        """Update user data"""
        update_data['updated_at'] = datetime.utcnow()
        return Database.get_collection(User.COLLECTION).update_one(
            {'firebase_uid': firebase_uid},
            {'$set': update_data}
        )

class CreditScore:
    COLLECTION = 'credit_scores'
    
    @staticmethod
    def create(score_data):
        """Create a new credit score record"""
        score_data['created_at'] = datetime.utcnow()
        score_data['score_id'] = str(uuid.uuid4())
        result = Database.get_collection(CreditScore.COLLECTION).insert_one(score_data)
        return str(result.inserted_id)
    
    @staticmethod
    def find_latest_by_user(firebase_uid):
        """Find latest credit score for user"""
        return Database.get_collection(CreditScore.COLLECTION).find_one(
            {'firebase_uid': firebase_uid},
            sort=[('created_at', -1)]
        )
    
    @staticmethod
    def find_by_user(firebase_uid):
        """Find all credit scores for user"""
        return list(Database.get_collection(CreditScore.COLLECTION).find(
            {'firebase_uid': firebase_uid}
        ).sort('created_at', -1))
    
    @staticmethod
    def update_score(firebase_uid, score_data):
        """Update or create credit score"""
        existing = CreditScore.find_latest_by_user(firebase_uid)
        
        if existing:
            score_data['updated_at'] = datetime.utcnow()
            return Database.get_collection(CreditScore.COLLECTION).update_one(
                {'_id': existing['_id']},
                {'$set': score_data}
            )
        else:
            return CreditScore.create(score_data)

class FinancialData:
    COLLECTION = 'credit_score_db'
    
    @staticmethod
    def create(financial_data):
        """Create financial data record"""
        financial_data['created_at'] = datetime.utcnow()
        financial_data['data_id'] = str(uuid.uuid4())
        result = Database.get_collection(FinancialData.COLLECTION).insert_one(financial_data)
        return str(result.inserted_id)
    
    @staticmethod
    def find_by_user(firebase_uid):
        """Find latest financial data for user"""
        return Database.get_collection(FinancialData.COLLECTION).find_one(
            {'firebase_uid': firebase_uid},
            sort=[('created_at', -1)]
        )
    
    @staticmethod
    def update_or_create(firebase_uid, financial_data):
        """Update or create financial data"""
        existing = FinancialData.find_by_user(firebase_uid)
        
        if existing:
            financial_data['updated_at'] = datetime.utcnow()
            return Database.get_collection(FinancialData.COLLECTION).update_one(
                {'firebase_uid': firebase_uid},
                {'$set': financial_data}
            )
        else:
            financial_data['firebase_uid'] = firebase_uid
            return FinancialData.create(financial_data)

class ChatHistory:
    COLLECTION = 'chat_history'
    
    @staticmethod
    def add_message(firebase_uid, message, response):
        """Add chat message and response"""
        chat_data = {
            'firebase_uid': firebase_uid,
            'message': message,
            'response': response,
            'timestamp': datetime.utcnow()
        }
        result = Database.get_collection(ChatHistory.COLLECTION).insert_one(chat_data)
        return str(result.inserted_id)
    
    @staticmethod
    def get_user_history(firebase_uid, limit=50):
        """Get chat history for user"""
        return list(Database.get_collection(ChatHistory.COLLECTION).find(
            {'firebase_uid': firebase_uid}
        ).sort('timestamp', -1).limit(limit))
