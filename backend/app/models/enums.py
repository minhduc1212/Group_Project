import enum


class SystemRole(str, enum.Enum):
    USER = "USER"
    ADMIN = "ADMIN"

class EventType(str, enum.Enum):
    TRAVEL = "TRAVEL"
    DINING = "DINING"
    HANGOUT = "HANGOUT"
    ENTERTAINMENT = "ENTERTAINMENT"
    SIGHTSEEING = "SIGHTSEEING"
    CUSTOM = "CUSTOM"

class EventRole(str, enum.Enum):
    OWNER = "OWNER"
    MEMBER = "MEMBER"
    VIEWER = "VIEWER"

class PlanStatus(str, enum.Enum):
    DRAFT = "DRAFT"       
    VOTING = "VOTING"
    CONFIRMED = "CONFIRMED"
    ARCHIVED = "ARCHIVED"

class AuthProvider(str, enum.Enum):
    LOCAL = "LOCAL"
    GOOGLE = "GOOGLE"
    FACEBOOK = "FACEBOOK"

class UserStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"

class StopCategory(str, enum.Enum):
    ATTRACTION = "ATTRACTION"
    RESTAURANT = "RESTAURANT"
    CAFE = "CAFE"
    HOTEL = "HOTEL"
    ENTERTAINMENT = "ENTERTAINMENT"
    TRANSPORT = "TRANSPORT"
    SHOPPING = "SHOPPING"
    OTHER = "OTHER"

class VoteValue(str, enum.Enum):
    UP = "UP"
    DOWN = "DOWN"
    NEUTRAL = "NEUTRAL"
    
class ExpenseType(str, enum.Enum):
    ADVANCE = "ADVANCE"
    PAYMENT = "PAYMENT"
    
class SplitType(str, enum.Enum):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENTAGE = "PERCENTAGE"
    
class InvitationStatus(str, enum.Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    EXPIRED = "EXPIRED"

class ChatRole(str, enum.Enum):
    USER = "USER"
    ASSISTANT = "ASSISTANT"
    SYSTEM = "SYSTEM"