"use client";

import { useState, useEffect, useRef } from "react";
import { useBusiness, BusinessId } from "@/context/BusinessContext";
import { ChevronDown, Check } from "lucide-react";

export function BusinessSwitcher() {
  const { business, businessConfig, setBusiness, allBusinesses } = useBusiness();
  const [open, setOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  // Persistir en localStorage
  useEffect(() => {
    const saved = typeof window !== "undefined" ? localStorage.getItem("business") : null;
    if (saved && allBusinesses.find((b) => b.id === saved)) {
      setBusiness(saved as BusinessId);
    }
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => {
    if (typeof window !== "undefined") {
      localStorage.setItem("business", business);
    }
  }, [business]);

  // Click outside to close
  useEffect(() => {
    function onClickOutside(e: MouseEvent) {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target as Node)) {
        setOpen(false);
      }
    }
    document.addEventListener("mousedown", onClickOutside);
    return () => document.removeEventListener("mousedown", onClickOutside);
  }, []);

  return (
    <div className="relative" ref={dropdownRef}>
      <button
        onClick={() => setOpen(!open)}
        className="flex items-center gap-2 px-3 py-1.5 rounded-md hover:bg-muted/60 transition-colors text-sm border border-transparent hover:border-border"
        style={{ borderLeftColor: businessConfig.color, borderLeftWidth: 3 }}
      >
        <span className="text-base">{businessConfig.emoji}</span>
        <span className="font-medium hidden md:inline">{businessConfig.name}</span>
        <ChevronDown
          className={`h-3.5 w-3.5 text-muted-foreground transition-transform ${
            open ? "rotate-180" : ""
          }`}
        />
      </button>

      {open && (
        <div className="absolute top-full right-0 mt-1 w-64 rounded-md border bg-card shadow-lg z-50 overflow-hidden">
          <div className="px-3 py-2 text-xs text-muted-foreground border-b">
            Cambiar negocio
          </div>
          <div className="py-1">
            {allBusinesses.map((b) => {
              const isActive = b.id === business;
              return (
                <button
                  key={b.id}
                  onClick={() => {
                    setBusiness(b.id);
                    setOpen(false);
                  }}
                  className={`w-full text-left flex items-center gap-3 px-3 py-2 hover:bg-muted/60 transition-colors ${
                    isActive ? "bg-muted/40" : ""
                  }`}
                  style={
                    isActive
                      ? { borderLeftColor: b.color, borderLeftWidth: 3 }
                      : {}
                  }
                >
                  <span className="text-xl">{b.emoji}</span>
                  <div className="flex-1 min-w-0">
                    <div className="text-sm font-medium">{b.name}</div>
                    <div className="text-xs text-muted-foreground truncate">
                      {b.description}
                    </div>
                  </div>
                  {isActive && <Check className="h-4 w-4 text-primary" />}
                </button>
              );
            })}
          </div>
          <div className="px-3 py-2 text-xs text-muted-foreground border-t bg-muted/30">
            Cambia la vista a través de toda la app
          </div>
        </div>
      )}
    </div>
  );
}
