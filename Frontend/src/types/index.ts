export interface User {
  id: string;
  email: string;
  name?: string;
}

export interface PersonalInfo {
  age: number;
  state: string;
  education_level: string;
}

export interface EmploymentIncome {
  employment_type: string;
  monthly_income: number;
  job_duration: string;
}

export interface Housing {
  monthly_cost: number;
  has_mortgage: boolean;
  monthly_savings: number;
  bank_balance: number;
}

export interface Family {
  dependents: number;
}

export interface CreditLoans {
  has_student_loan: boolean;
  has_car_loan: boolean;
  car_loan_payment: number;
  stud_loan_payments: number;
  credit_cards: number;
}

export interface CreditBehavior {
  recent_inquiries: number;
  late_payments: number;
  bankruptcy: boolean;
  credit_history_years: number;
}

export interface FinancialData {
  personal_info: PersonalInfo;
  employment_income: EmploymentIncome;
  housing: Housing;
  family: Family;
  credit_loans: CreditLoans;
  credit_behavior: CreditBehavior;
}

export interface DashboardData {
  creditScore: number;
  scoreRange: string;
  bestAchievableScore: number;
  loanApproved: boolean;
  lastUpdatedDate: string;
  hasData: boolean;
}

export interface ChatMessage {
  message: string;
  response: string;
  timestamp: string;
}

export interface Insight {
  category: string;
  impact: "positive" | "negative" | "neutral";
  description: string;
  recommendation: string;
}

export interface APIResponse<T = unknown> {
  success: boolean;
  data: T;
  message?: string;
  error?: string;
}

export interface AuthResponse {
  token: string;
  user: User;
}

export interface ChatResponse {
  response: string;
  timestamp: string;
}

export interface InsightsResponse {
  insights: Insight[];
}
