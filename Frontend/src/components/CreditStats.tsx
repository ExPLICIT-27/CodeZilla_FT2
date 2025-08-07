import { GlassCard } from "@/components/ui/glass-card";
import { TrendingUp, Users, Shield, Calculator } from "lucide-react";

export const CreditStats = () => {
  const stats = [
    {
      icon: Shield,
      value: "100k+",
      label: "Money Protected",
      gradient: "from-blue-500 to-purple-600"
    },
    {
      icon: Users,
      value: "30k+",
      label: "Active Users",
      gradient: "from-purple-600 to-pink-600"
    },
    {
      icon: Calculator,
      value: "99.9%",
      label: "Accuracy Rate",
      gradient: "from-orange-500 to-red-600"
    },
    {
      icon: TrendingUp,
      value: "24/7",
      label: "Support Available",
      gradient: "from-green-500 to-blue-600"
    }
  ];

  return (
    <div className="grid grid-cols-2 gap-4 w-full max-w-md">
      {stats.map((stat, index) => (
        <GlassCard key={index} className="p-4 text-center space-y-2">
          <div className={`mx-auto w-8 h-8 rounded-full bg-gradient-to-r ${stat.gradient} flex items-center justify-center`}>
            <stat.icon className="h-4 w-4 text-white" />
          </div>
          <div className="text-xl font-bold text-foreground">{stat.value}</div>
          <div className="text-xs text-muted-foreground">{stat.label}</div>
        </GlassCard>
      ))}
    </div>
  );
};
