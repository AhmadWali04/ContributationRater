import { useState } from "react";
import { ChevronRight } from "lucide-react";

import { AppSidebar } from "@/components/app-sidebar";
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb";
import { Button } from "@/components/ui/button";
import { ResizableHandle, ResizablePanel, ResizablePanelGroup } from "@/components/ui/resizable";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";
import { SidebarProvider } from "@/components/ui/sidebar";
import { Toaster } from "@/components/ui/sonner";

import { dashboardCards, navItems, projectData, teamData, userData } from "./data";

function App() {
  // We use the collapsed state for UI adjustments when sidebar is collapsed
  const [collapsed, setCollapsed] = useState(false);

  return (
    <>
      <SidebarProvider>
        <ResizablePanelGroup direction="horizontal" className="h-screen w-full">
          <ResizablePanel
            defaultSize={20}
            minSize={15}
            maxSize={20}
            collapsible={true}
            collapsedSize={4}
            onCollapse={() => setCollapsed(true)}
            onExpand={() => setCollapsed(false)}
            className="hidden md:block"
          >
            <AppSidebar
              navMain={navItems}
              projects={projectData}
              teams={teamData}
              user={userData}
            />
          </ResizablePanel>
          <ResizableHandle withHandle />
          <ResizablePanel defaultSize={80}>
            <div className={`flex h-full flex-col ${collapsed ? "pl-0" : "pl-0 md:pl-4"}`}>
              <header className="border-b bg-background px-6 py-3">
                <div className="flex items-center justify-between">
                  <Breadcrumb>
                    <BreadcrumbList>
                      <BreadcrumbItem>
                        <BreadcrumbLink href="/">Home</BreadcrumbLink>
                      </BreadcrumbItem>
                      <BreadcrumbSeparator>
                        <ChevronRight className="h-4 w-4" />
                      </BreadcrumbSeparator>
                      <BreadcrumbItem>
                        <BreadcrumbPage>Dashboard</BreadcrumbPage>
                      </BreadcrumbItem>
                    </BreadcrumbList>
                  </Breadcrumb>
                  <div className="flex items-center gap-2">
                    <Button variant="outline" size="sm">
                      Settings
                    </Button>
                    <Button size="sm">New Project</Button>
                  </div>
                </div>
              </header>
              <main className="flex-1 overflow-auto p-6">
                <ScrollArea className="h-full">
                  <div className="space-y-6">
                    <div>
                      <h1 className="text-3xl font-bold">Dashboard</h1>
                      <p className="text-muted-foreground">
                        Overview of your project's performance and metrics.
                      </p>
                    </div>
                    <Separator />
                    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
                      {dashboardCards.map((card, index) => (
                        <div key={index} className="rounded-lg border bg-card p-4 shadow-sm">
                          <div className="flex items-center justify-between">
                            <h3 className="font-medium">{card.title}</h3>
                            <card.icon className="h-5 w-5 text-muted-foreground" />
                          </div>
                          <p className="mt-3 text-2xl font-bold">{card.value}</p>
                          <p className="text-xs text-muted-foreground">{card.description}</p>
                        </div>
                      ))}
                    </div>
                    <div className="rounded-lg border bg-card p-6 shadow-sm">
                      <h2 className="text-xl font-semibold">Recent Activity</h2>
                      <p className="text-muted-foreground">Your project's activity over time.</p>
                      <div className="mt-4 h-[300px] w-full rounded-md border bg-muted flex items-center justify-center">
                        <p className="text-muted-foreground">Chart placeholder</p>
                      </div>
                    </div>
                  </div>
                </ScrollArea>
              </main>
            </div>
          </ResizablePanel>
        </ResizablePanelGroup>
      </SidebarProvider>
      <Toaster />
    </>
  );
}

export default App;
