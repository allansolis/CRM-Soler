/**
 * Helper para leer business actual desde cookie en server components.
 *
 * Usage:
 *   import { getBusinessFromCookies } from "@/lib/getBusinessFromCookies";
 *   const business = await getBusinessFromCookies(); // "glass_soler" etc
 */
import { cookies } from "next/headers";

export type BusinessId =
  | "glass_soler"
  | "esmeraldas_soler"
  | "autos_soler"
  | "inversiones_soler";

const VALID_BUSINESSES: BusinessId[] = [
  "glass_soler",
  "esmeraldas_soler",
  "autos_soler",
  "inversiones_soler",
];

export async function getBusinessFromCookies(): Promise<BusinessId> {
  try {
    const cookieStore = await cookies();
    const v = cookieStore.get("business")?.value;
    if (v && VALID_BUSINESSES.includes(v as BusinessId)) {
      return v as BusinessId;
    }
  } catch {
    // ignore
  }
  return "glass_soler"; // default
}

export const BUSINESS_LABELS: Record<BusinessId, { name: string; emoji: string; color: string }> = {
  glass_soler: { name: "Glass Soler", emoji: "🛡️", color: "#0EA5E9" },
  esmeraldas_soler: { name: "Esmeraldas Soler", emoji: "💎", color: "#10B981" },
  autos_soler: { name: "Autos Soler", emoji: "🚗", color: "#F59E0B" },
  inversiones_soler: { name: "Inversiones Soler", emoji: "🏘️", color: "#8B5CF6" },
};
