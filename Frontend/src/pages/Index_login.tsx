import { LoginForm } from "@/components/LoginForm";
import { CreditStats } from "@/components/CreditStats";

const Index = () => {
  return (
    <div className="min-h-screen bg-background bg-gradient-bg flex items-center justify-center p-4">
      <div className="container max-w-6xl mx-auto">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left side - Hero content */}
          <div className="space-y-8 text-center lg:text-left">
            <div className="space-y-4">
              <h1 className="text-4xl lg:text-6xl font-bold text-foreground leading-tight">
                Fueling Business Growth Through{" "}
                <span className="bg-gradient-primary bg-clip-text text-transparent">
                  Innovative
                </span>{" "}
                and{" "}
                <span className="bg-gradient-accent bg-clip-text text-transparent">
                  Scalable Tools
                </span>{" "}
                to Scale.
              </h1>
              <p className="text-lg text-muted-foreground max-w-2xl">
                Simplifying finance with smart, scalable tools—so your business grows faster and smarter.
              </p>
            </div>
            
            <CreditStats />
          </div>

          {/* Right side - Login form */}
          <div className="flex justify-center lg:justify-end">
            <LoginForm />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Index;
