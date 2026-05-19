# 🗺️ Meta — Mapa Final del Ecosistema Soler

**Fecha:** 2026-05-19 03:00 (noche del 18 mayo)
**Token usado:** Long-lived (no expira, data access hasta 6-ago-2026)
**Scopes:** 10 (sin pages_messaging - requiere agregar en proximo regen)

---

## 🏢 ARQUITECTURA DE BUSINESS MANAGERS

```
3 BMs activos
├── BM "Glass Soler" (1117652308093182)
│   └── 0 ad accounts owned  ⚠️ vacío
│
├── BM "Inversiones Soler" (1106361001133983)
│   ├── act_1101364862188478 "CP Glass Soler" (USD)  ← Glass cuenta vive aqui
│   └── Catalogo Glass + Catalogo Autos
│
└── BM "Farmacologia deportiva" (1145191446124291)
    ├── act_1868510380157902 (CRC)  ← Esmeraldas cuenta
    └── Catalogo Esmeraldas  ← legacy, considerar migrar
```

**Hallazgo:** El BM "Glass Soler" está vacío. Las cuentas Glass y Autos están en "Inversiones Soler", y Esmeraldas en "Farmacologia deportiva" (legacy).

**Recomendación:** Migrar gradualmente todo a "Inversiones Soler" o crear BM "Soler Group" master.

---

## 📱 2 APPS DEVELOPER

| App | ID | Mode | Empresa | Uso recomendado |
|-----|-----|------|---------|-----------------|
| **Soler** | 25746921918314942 | ✅ Publicada | Inversiones Soler | Producción ads + mensajes |
| Soler Inversiones | 950123147611259 | 🚧 En desarrollo | Farmacologia deportiva | Sandbox/test |

**Credenciales sensibles (Soler):**
- App Secret: `a5856fc9f23679afc29864a4e5ced9af`
- Client Token: `21896fc585b9c926577ec0ac91965773`
- Dominio: `allansolis.github.io`
- Privacy: https://allansolis.github.io/soler-legal/politica-privacidad.html
- Terms: https://allansolis.github.io/soler-legal/terminos.html

---

## 📄 4 PAGES

### 🛡️ Glass Soler — 860529027138846
- **Categoría:** Cars
- **Fans/Followers:** 367 / 367
- **Contacto:** +506 6379 0438 · info@glasssoler.com
- **Web:** https://glasssoler.com/
- **Ubicación:** San José, Costa Rica
- **About:** "El polarizado de seguridad no es solo una mejora estética…"
- **IG vinculado:** @glasssoler (25 followers, **0 posts** ⚠️)
- **Bio IG:** "🚗 Protección Vehicular Premium 🔒 Película Antirobos ☀️ Bloqueo UV"
- **Webhook:** ✅ Suscrito (app Soler) con 6 fields (messages, postbacks, optins, deliveries, reads, handovers)

### 💎 Esmeraldas Soler — 797310113463115
- **Categoría:** Jewelry & Watches Company
- **Fans/Followers:** 302 / 302
- **Contacto:** +506 8798 5656
- **Web:** Instagram (no web propia)
- **About:** "Joyería de Esmeraldas 100% Naturales💍💎 Plata 925, piedras preciosas certificadas. Envíos a todo Costa Rica..."
- **IG vinculado:** @esmeraldas_soler (3,154 followers, **138 posts** ✅)
- **Bio IG:** "Joyería de Esmeraldas 100% Naturales💚 Costa Rica🇨🇷"
- **Webhook:** ✅ Suscrito (app Soler) con 6 fields

### 🚗 Autos Soler — 100123132505557
- **Categoría:** Entrepreneur
- **Fans/Followers:** 442 / 442 (el mayor en FB)
- **Contacto:** +506 6379 0438 (mismo que Glass)
- **About:** "El auto de tus sueños lo haces realidad con Autos Soler"
- **IG vinculado:** ❌ SIN IG
- **Webhook:** ❌ NO suscrito (necesita pages_messaging scope para suscribir)

### 🏘️ Inversiones Soler — 796480326889963
- **Categoría:** Real Estate
- **Fans/Followers:** 0 / 0 ⚠️
- **Contacto:** ❌ Sin teléfono ni email configurado
- **About:** ❌ Vacío
- **IG vinculado:** ❌ SIN IG (no existe @inversionessoler aun)
- **Webhook:** ❌ NO suscrito

---

## 💰 AD ACCOUNTS

| Account | Currency | Status | Balance | Spent | Spend Cap | Live |
|---------|----------|--------|---------|-------|-----------|------|
| Glass Soler `act_1101364862188478` | USD | 3 = UNSETTLED ⚠️ | $1,225 | $7,400 | $0 (∞) | ❌ |
| Esmeraldas `act_1868510380157902` | CRC | 9 = IN_GRACE_PERIOD ⚠️ | ₡6,523 | ₡100,000 | ₡100,000 | 🟡 |
| Autos Soler `act_2385776465260628` | CRC | 1 = ACTIVE ✅ | ₡0 | ₡1,497 | ₡1,500 | ✅ |

### Estados de cuenta explicados
- **1 = ACTIVE** ✅: Funciona normal
- **3 = UNSETTLED** ⚠️: Factura pendiente, anuncios NO se entregan hasta pagar
- **9 = IN_GRACE_PERIOD** ⚠️: Saldo casi 0, anuncios siguen pero corto plazo

---

## 📦 CATÁLOGOS

### 🛡️ Glass — Polarizado Paquetes (`1670886954032475`)
- BM owner: Inversiones Soler
- 4 productos in_stock:
  - Básica 8k micras → ₡299,000
  - Full 16k micras → ₡499,000
  - Premium 27k micras → ₡999,000
  - Máxima 54k micras → ₡1,500,000
- **4 product sets:** All Products, Glass Todos, Glass Esenciales (Entry), Glass Premium (Top)

### 💎 Esmeraldas — Joyería Plata 925 (`944718051249202`)
- BM owner: Farmacologia deportiva ⚠️ (legacy)
- 30 productos
- 1 product set: All Products

### 🚗 Autos — Vehículos en Venta Commerce (`955793357293894`)
- BM owner: Inversiones Soler
- 3 productos reales:
  - Hyundai Elantra 2023 → ₡9,800,000
  - Honda CR-V 2021 → ₡14,500,000
  - Toyota Hilux 2022 4x4 → ₡18,500,000
- **2 product sets:** All Products, **Últimos 3 Autos Publicados**

---

## 📢 CAMPAÑAS Y ADSETS

### 🛡️ Glass — 4 campañas / 4 adsets ACTIVE
1. **Videos de Retargeting** — Adset budget ?
2. **CR 25-55 Feed+Reels Conversaciones WA** — Adset budget $3/día
3. **Aumento de Likes Facebook** — Adset budget $2/día
4. **Conjunto de Anuncios Virales** — Adset budget ?

⚠️ Activas pero NO se entregan por UNSETTLED.

### 💎 Esmeraldas — 21 campañas / 20 adsets
- 10 publicaciones IG promocionadas activas
- 10 legacy (marketplace 2022 + Trax 2014) **considerar pausar/limpiar**

### 🚗 Autos — 2 campañas / 2 adsets
- **CR 25-65 Compradores Auto · Advantage+ Multi-canal** (PAUSED, budget ₡1,500) ← Lista para reactivar
- [Hyundai Accent GL 2017] Marketplace (ACTIVE, budget ₡500/día)

---

## 🎯 AUDIENCIAS Y PIXELS

### Glass
- **1 Custom Audience:** "PQHV Videos Iniciales" (ENGAGEMENT, ~9,100 personas)
- **1 Pixel:** Glass Soler - Pixel Seguridad (`4073809872916511`)

### Esmeraldas / Autos
- Sin custom audiences detectadas
- Sin pixels (oportunidad de crear)

---

## 📈 INSIGHTS ÚLTIMOS 30 DÍAS

| Métrica | 🛡️ Glass | 💎 Esmeraldas | 🚗 Autos |
|---------|----------|----------------|----------|
| Gasto | $74 | ₡139,762 | ₡1,497 |
| Impresiones | 35,614 | 152,318 | 2,986 |
| Reach | 26,533 | 63,189 | 1,779 |
| Clicks | 3,263 | 6,188 | 297 |
| CTR | **9.16%** ⭐ | 4.06% | 9.95% ⭐ |
| CPC | $0.022 | ₡22.59 | ₡5.04 |
| CPM | $2.08 | ₡917.57 | ₡501 |
| **Mensajes iniciados** | 34 | **330** 🔥 | 10 |
| Page engagement | 18,444 | 2,622 | 176 |

**Performer del mes:** Esmeraldas con 330 mensajes. Pero Glass tiene CTR 9.16% — cuando reactive la cuenta va a explotar.

---

## 🔔 WEBHOOK SUBSCRIPTIONS (4 pages)

| Page | App suscrita | Status |
|------|--------------|--------|
| Glass | Soler (25746921918314942) | ✅ 6 fields |
| Esmeraldas | Soler (25746921918314942) | ✅ 6 fields |
| Autos | — | ❌ Sin suscripción |
| Inversiones | — | ❌ Sin suscripción |

**Bloqueador:** Para suscribir Autos+Inversiones se requiere scope `pages_messaging` (no está en token actual). Necesita regenerar token con ese scope.

---

## 🚨 TOP 10 ACCIONES (priorizadas)

1. 💰 **Pagar factura Glass** (~$1,225) → desbloquea 4 campañas con CTR 9.16%
2. 💰 **Recargar Esmeraldas** (mínimo ₡60k) → continuar 330 mensajes/mes
3. 🔑 **Regenerar token agregando pages_messaging + instagram_basic + instagram_manage_messages** → suscribir webhooks Autos+Inversiones + ver conversaciones
4. 📱 **Crear @inversionessoler IG** + vincular a page
5. 📱 **Vincular @autossoler IG Business** a page Autos
6. 🚀 **Reactivar campaña Autos** "CR 25-65 Multi-canal Advantage+" (PAUSED, todo listo)
7. 📸 **Subir contenido a @glasssoler** (0 posts, 25 followers — necesita feed)
8. 🧹 **Pausar 11 campañas legacy Esmeraldas** (Trax 2014, marketplace 2022)
9. 🏢 **Mover catálogo Esmeraldas** de BM "Farmacologia deportiva" a "Inversiones Soler"
10. 🎯 **Crear pixel Esmeraldas y Autos** (Glass ya tiene)

---

## 🔐 CREDENCIALES GUARDADAS EN .env

```env
META_APP_ID=25746921918314942
META_APP_SECRET=a5856fc9f23679afc29864a4e5ced9af  ← NUEVO (server-side)
META_CLIENT_TOKEN=21896fc585b9c926577ec0ac91965773  ← NUEVO
META_APP_ID_INVERSIONES=950123147611259  ← Segunda app
META_APP_NAME_INVERSIONES=Soler Inversiones

META_ACCESS_TOKEN=EAFt4sGcAOb4BRQSRKNuTrLCZAJrOJzLPYxJZCZCmQ4ZAjdnnmpxa...  ← LONG-LIVED 60d+
META_ADS_TOKEN=(mismo que ACCESS)  ← Mismo token sirve para ambos

META_PAGE_ID=860529027138846  (Glass)
META_PHONE_NUMBER_ID=777414378791556  (Glass WhatsApp)
META_WABA_ID=786597210574223  (Glass WABA)
META_ESMERALDAS_PAGE_ID=797310113463115

META_ADS_ACCOUNT_GLASS=act_1101364862188478
META_ADS_ACCOUNT_ESMERALDAS=act_1868510380157902
```

---

## 📁 ARCHIVOS GENERADOS

`CRM-Soler/soler-elena-system/data/`:
- `meta-export-20260519-0256/` (30 JSONs primer extract)
- `meta-export-20260519-0305/` (30 JSONs segundo extract con long-lived token)

Doc: `META-FULL-EXTRACT-2026-05-18-NOCHE.md` + `META-MAPA-FINAL-2026-05-18.md` (este)

---

**Generado:** 2026-05-18 23:05 CR
**Token expiration:** Never (data access 6-ago-2026)
