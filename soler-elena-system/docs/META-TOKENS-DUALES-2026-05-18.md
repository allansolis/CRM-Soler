# 🔑 Meta Tokens DUALES — Estrategia 2 apps

**Fecha:** 2026-05-18 23:30 CR
**Estrategia:** Usar 2 apps Meta complementarias para acceso completo

---

## 📱 Las 2 Apps de Meta Soler

| App | ID | Modo | BMs accesibles | Caso de uso |
|-----|-----|------|----------------|-------------|
| **Soler** | 25746921918314942 | ✅ Publicada | Inversiones Soler, Glass Soler | **MARKETING_API_ADS_MANAGEMENT** — crear/gestionar campañas, catálogos Glass+Autos |
| **Soler Inversiones** | 950123147611259 | 🚧 Sandbox | Farmacologia deportiva | **MARKETING_API_ADS_ANALYTICS** — leer insights Esmeraldas + leadgen forms |

---

## 🔑 Tokens activos en .env

### `META_ACCESS_TOKEN` (long-lived, never expires)
- **App:** Soler (25746921918314942)
- **Tipo:** Long-lived via App Secret
- **Expira:** never (data access hasta 6-ago-2026)
- **Scopes (10):**
  - catalog_management, threads_business_basic, pages_show_list
  - **ads_management, ads_read, business_management**
  - pages_read_engagement, pages_manage_metadata, pages_manage_ads
  - public_profile

### `META_ADS_TOKEN_INVERSIONES`
- **App:** Soler Inversiones (950123147611259)
- **Tipo:** Short-lived (regenerar cada 60 dias)
- **Expira:** 2026-07-17 21:27 (60 dias)
- **Scopes (10):**
  - catalog_management, pages_show_list, ads_management, ads_read
  - business_management, **leads_retrieval** ✨ (extra)
  - pages_read_engagement, pages_manage_metadata, pages_manage_ads
  - public_profile

---

## 🏢 4 Ad Accounts detectadas

| ID | Currency | Status | BM Owner | Uso |
|----|----------|--------|----------|-----|
| `act_1101364862188478` | USD | 3=UNSETTLED ⚠️ | Inversiones Soler | **Glass Soler** — pagar factura |
| `act_1868510380157902` | CRC | 9=GRACE | Farmacologia deportiva | **Esmeraldas** — recargar |
| `act_2385776465260628` | CRC | 1=ACTIVE ✅ | (personal Allann) | **Autos Soler** |
| `act_930477373065306` 🆕 | INR | 1=ACTIVE | Inversiones Soler | **Cuenta sandbox** (test, 0 balance, 2 camps Traffic/Sales test) |

### Cuenta INR descubierta (act_930477373065306)
- **Name:** "unknown (Read-Only)"
- **Currency:** Indian Rupee
- **Timezone:** America/Costa_Rica
- **Balance:** 0 INR / Spent: 0
- **Campañas:** 2 (Traffic Campaign + Sales Campaign, ambas ACTIVE pero sin gasto)
- **Conclusion:** Probable cuenta de prueba creada al explorar Marketing API. Inofensiva, sin gastos. Considerar borrar o ignorar.

---

## 🎯 Cuándo usar cada token

### Para Glass + Autos (BMs Inversiones Soler)
```python
TOKEN = os.getenv('META_ACCESS_TOKEN')  # App Soler long-lived
```

### Para Esmeraldas (BM Farmacologia deportiva)
```python
TOKEN = os.getenv('META_ADS_TOKEN_INVERSIONES')  # App Soler Inversiones
```

### Para leadgen forms / lead retrieval
```python
TOKEN = os.getenv('META_ADS_TOKEN_INVERSIONES')  # tiene leads_retrieval
```

### Por defecto (gestion general)
```python
TOKEN = os.getenv('META_ACCESS_TOKEN')  # long-lived es el primario
```

---

## 📊 Insights validados con cada token

### Token Soler (long-lived) — Glass + Autos
- Glass: 35,614 impressions, 34 mensajes, $74 spent 30d
- Autos: 2,986 impressions, 10 conv, ₡1,497 30d

### Token Soler Inversiones — Esmeraldas optimo
- 152,318 impressions
- **330 messaging connections** ⭐
- 6,188 clicks
- ₡139,762 spent 30d
- CTR 4.06%
- 23 post_unlikes
- 144 welcome message views
- 1 lead capturado
- 1 registration via Meta Leads

---

## 🚀 Que se desbloquea ahora

Con AMBOS tokens disponibles:

1. ✅ Acceso completo a las 4 ad accounts (Glass+Esmeraldas+Autos+INR)
2. ✅ Read/write campañas en los 3 BMs
3. ✅ Gestión catálogos en BM Inversiones (Glass+Autos) Y BM Farmacologia (Esmeraldas)
4. ✅ leadgen forms via token Inversiones (cuando page permita)
5. ✅ Insights cross-account agregados

## ⚠️ Limitaciones persisten

- ❌ Conversaciones inbox (necesita `pages_messaging` en cualquier token)
- ❌ Instagram DMs (necesita `instagram_manage_messages`)
- ❌ WhatsApp Business API (necesita `whatsapp_business_messaging`)
- ❌ Webhook subscribe pages Autos/Inversiones (necesita `pages_messaging`)

Solución: agregar esos scopes en próxima regeneración (cualquiera de las 2 apps).

---

## 🛡️ Secretos guardados (.env)

```env
META_APP_ID=25746921918314942                  (Soler)
META_APP_SECRET=a5856fc9f23679afc29864a4e5ced9af
META_CLIENT_TOKEN=21896fc585b9c926577ec0ac91965773
META_APP_ID_INVERSIONES=950123147611259        (Soler Inversiones)
META_ACCESS_TOKEN=EAFt4s...long-lived
META_ADS_TOKEN=EAFt4s...same
META_ADS_TOKEN_INVERSIONES=EAANgIci0z...
META_ADS_ACCOUNT_GLASS=act_1101364862188478
META_ADS_ACCOUNT_ESMERALDAS=act_1868510380157902
META_ADS_ACCOUNT_AUTOS=act_2385776465260628
META_ADS_ACCOUNT_INR=act_930477373065306       (sandbox descubierto)
```

**App Secret para Soler Inversiones:** ❌ Aún no obtenido. Si quieres long-lived para esta app, hay que ir a `developers.facebook.com/apps/950123147611259/settings/basic/` y copiar el App Secret.

---

**Status:** ✅ Sistema dual de tokens operativo. Ambos validados con calls API reales.
