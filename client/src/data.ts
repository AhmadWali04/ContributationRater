import {
  BarChart3,
  BookOpen,
  Home,
  LayoutDashboard,
  LineChart,
  PieChart,
  Settings,
  Users,
} from "lucide-react";
import { type LucideIcon } from "lucide-react";

// Navigation items for the sidebar
export const navItems = [
  {
    title: "Dashboard",
    url: "/",
    icon: LayoutDashboard,
    isActive: true,
  },
  {
    title: "Analytics",
    url: "/analytics",
    icon: BarChart3,
    items: [
      {
        title: "Overview",
        url: "/analytics/overview",
      },
      {
        title: "Reports",
        url: "/analytics/reports",
      },
      {
        title: "Metrics",
        url: "/analytics/metrics",
      },
    ],
  },
  {
    title: "Users",
    url: "/users",
    icon: Users,
    items: [
      {
        title: "All Users",
        url: "/users/all",
      },
      {
        title: "Active Users",
        url: "/users/active",
      },
      {
        title: "User Details",
        url: "/users/details",
      },
    ],
  },
  {
    title: "Documentation",
    url: "/docs",
    icon: BookOpen,
  },
  {
    title: "Settings",
    url: "/settings",
    icon: Settings,
  },
];

// User data for the sidebar
export const userData = {
  name: "John Doe",
  email: "john@example.com",
  avatar: "/avatars/user.jpg",
};

// Team data for the sidebar
export const teamData = [
  {
    name: "My Team",
    logo: Home,
    plan: "Pro",
  },
];

// Project data for the sidebar
export const projectData = [
  {
    name: "Main Project",
    url: "/projects/main",
    icon: LineChart,
  },
  {
    name: "Analytics Project",
    url: "/projects/analytics",
    icon: PieChart,
  },
];

// Dashboard card data
export interface DashboardCard {
  title: string;
  value: string;
  description: string;
  icon: LucideIcon;
}

export const dashboardCards: DashboardCard[] = [
  {
    title: "Total Users",
    value: "2,543",
    description: "+12.5% from last month",
    icon: Users,
  },
  {
    title: "Active Sessions",
    value: "187",
    description: "+4.3% from yesterday",
    icon: BarChart3,
  },
  {
    title: "Engagement Rate",
    value: "24.8%",
    description: "+2.1% from last week",
    icon: LineChart,
  },
  {
    title: "Avg. Session Duration",
    value: "3m 42s",
    description: "-0.5% from last week",
    icon: PieChart,
  },
];
