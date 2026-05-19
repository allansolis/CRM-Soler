# 🔧 Meta CONFIG COMPLETO — 18 mayo 2026 noche

**Status:** ✅ ALL CONFIGURED — 2 apps, 4 ad accounts, WhatsApp test ready

---

## 🔑 CREDENCIALES COMPLETAS

### App 1: Soler (App ID 25746921918314942)
```
META_APP_ID=25746921918314942
META_APP_SECRET=a5856fc9f23679afc29864a4e5ced9af
META_CLIENT_TOKEN=21896fc585b9c926577ec0ac91965773
META_ACCESS_TOKEN=(long-lived, never expires, 10 scopes)
```
**Modo:** ✅ Publicada
**Empresa propietaria:** Inversiones Soler
**Domino:** allansolis.github.io
**Privacy:** https://allansolis.github.io/soler-legal/politica-privacidad.html

### App 2: Soler Inversiones (App ID 950123147611259) 🆕
```
META_APP_ID_INVERSIONES=950123147611259
META_APP_SECRET_INVERSIONES=f890a71d25f096140d3e83660d8830f3 ← NUEVO
META_CLIENT_TOKEN_INVERSIONES=b1a4cc61dbd1c86d36739ce8ef16b06b
META_THREADS_APP_ID=1245808824284459 (sub-app Threads)
META_ADS_TOKEN_INVERSIONES=(long-lived, never expires, 12 scopes con WhatsApp)
META_WA_TOKEN=(short-lived 60d, scope whatsapp_business_messaging)
```
**Modo:** 🚧 Sin publicar (sandbox/development)
**Cuenta autorizada:** 1868510380157902 (Esmeraldas)
**Icono:** Esmeraldas Soler logo

### WhatsApp Business API (Test sandbox 90 dias gratis) 🆕
```
META_WA_PHONE_ID_TEST=1071826282682496
META_WA_WABA_ID_TEST=2030634634524596
META_WA_TEST_PHONE_NUMBER=+15556336278
```
- **WABA name:** Test WhatsApp Business Account
- **Numero display:** +1 555-633-6278
- **Quality:** UNKNOWN (recien creada)
- **Tier:** TIER_250 (250 msgs/24h)
- **Template namespace:** 6be04bbc_211b_4747_8e39_b5919f20825c
- **Plantillas activas:** 1 (`hello_world` en en_US, APPROVED)

---

## 📊 SCOPES DISPONIBLES POR TOKEN

| Scope | META_ACCESS_TOKEN (Soler) | META_ADS_TOKEN_INVERSIONES | META_WA_TOKEN |
|-------|--------------------------|----------------------------|---------------|
| `catalog_management` | ✅ | ✅ | ✅ |
| `pages_show_list` | ✅ | ✅ | ✅ |
| `ads_management` | ✅ | ✅ | ✅ |
| `ads_read` | ✅ | ✅ | ✅ |
| `business_management` | ✅ | ✅ | ✅ |
| `pages_read_engagement` | ✅ | ✅ | ✅ |
| `pages_manage_metadata` | ✅ | ✅ | ✅ |
| `pages_manage_ads` | ✅ | ✅ | ✅ |
| `threads_business_basic` | ✅ | — | — |
| `leads_retrieval` | — | ✅ | ✅ |
| `whatsapp_business_management` | — | — | ✅⭐ |
| `whatsapp_business_messaging` | — | — | ✅⭐ |
| `public_profile` | ✅ | ✅ | ✅ |

**Falta para acceso completo:**
- `pages_messaging` (para inbox conversaciones)
- `instagram_basic` + `instagram_manage_messages` (para DMs IG)

---

## 🏢 4 AD ACCOUNTS

| Account ID | Currency | Status | BM Owner | Notas |
|------------|----------|--------|----------|-------|
| `act_1101364862188478` | USD | 3=UNSETTLED ⚠️ | Inversiones Soler | Glass Soler — pagar factura |
| `act_1868510380157902` | CRC | 9=GRACE | Farmacologia deportiva | Esmeraldas — recargar |
| `act_2385776465260628` | CRC | 1=ACTIVE ✅ | (personal) | Autos Soler |
| `act_930477373065306` | INR | 1=ACTIVE | Inversiones Soler | Sandbox sin uso |

---

## 📞 INFRA WHATSAPP

### Para testing inmediato (90 días gratis)
```bash
curl -X POST 'https://graph.facebook.com/v25.0/1071826282682496/messages' \
  -H 'Authorization: Bearer $META_WA_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "messaging_product": "whatsapp",
    "to": "TU_NUMERO_VERIFICADO",
    "type": "template",
    "template": {
      "name": "hello_world",
      "language": { "code": "en_US" }
    }
  }'
```

⚠️ **Antes de enviar:** El numero destinatario debe estar AGREGADO al WABA test en:
`developers.facebook.com/apps/950123147611259/wa-dev-console/`
→ "A" (destinatario) → Agregar tu numero personal

### Para producción
Agregar tu numero real WhatsApp Business (no el test):
- `developers.facebook.com/apps/950123147611259/wa-dev-console/` → Paso 5 "Añadir número de teléfono"
- Verificar via SMS/llamada
- Agregar método de pago (Paso 6)
- Migrar `META_WA_PHONE_ID_TEST` → `META_WA_PHONE_ID_PROD`

### Webhook URL para recibir mensajes
Configurar en: `developers.facebook.com/apps/950123147611259/wa-dev-console/` → Paso 3

URL sugerida: `https://allannsolis94.app.n8n.cloud/webhook/whatsapp-soler-inv`
Verify token: `glass_soler_verify_2026` (mismo que el actual)

Eventos suscribir: `messages, message_status`

---

## 🎯 PIPELINE COMPLETO DE CONEXIONES

```
┌─────────────────────────────────────────────────────────┐
│                    APP "SOLER"                          │
│             (App ID 25746921918314942)                  │
│                                                          │
│  ✅ Glass Soler (FB+IG+catalogo)                        │
│  ✅ Autos Soler (FB+catalogo)                           │
│  ✅ Inversiones Soler (FB)                              │
│  ❌ No WhatsApp scope                                   │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│              APP "SOLER INVERSIONES"                    │
│             (App ID 950123147611259)                    │
│                                                          │
│  ✅ Esmeraldas (FB+IG+catalogo, via BM Farmacologia)   │
│  ✅ WhatsApp Business (numero test +1 555 633 6278)    │
│  ✅ leads_retrieval (lead form ads)                    │
│  ✅ Threads sub-app (1245808824284459)                  │
└─────────────────────────────────────────────────────────┘
```

---

## 📦 ENV.LOCAL CONSOLIDADO

```env
# Bot
ANTHROPIC_API_KEY=sk-ant-api03-tfp_1QEH...
CLAUDE_MODEL=claude-sonnet-4-5-20250929
WEBHOOK_SECRET=Ok2XkP56Q-P503zT1dJWtgsS_V1b9NeRze9NOL_bDLQ

# Meta App Soler (long-lived)
META_APP_ID=25746921918314942
META_APP_SECRET=a5856fc9f23679afc29864a4e5ced9af
META_CLIENT_TOKEN=21896fc585b9c926577ec0ac91965773
META_ACCESS_TOKEN=EAFt4s...long-lived
META_ADS_TOKEN=EAFt4s...same

# Meta App Soler Inversiones (long-lived)
META_APP_ID_INVERSIONES=950123147611259
META_APP_SECRET_INVERSIONES=f890a71d25f096140d3e83660d8830f3
META_CLIENT_TOKEN_INVERSIONES=b1a4cc61dbd1c86d36739ce8ef16b06b
META_ADS_TOKEN_INVERSIONES=EAANg...long-lived
META_THREADS_APP_ID=1245808824284459

# WhatsApp Business Test
META_WA_TOKEN=EAANg...60d
META_WA_PHONE_ID_TEST=1071826282682496
META_WA_WABA_ID_TEST=2030634634524596
META_WA_TEST_PHONE_NUMBER=+15556336278

# Pages
META_PAGE_ID=860529027138846                  # Glass
META_ESMERALDAS_PAGE_ID=797310113463115
META_AUTOS_PAGE_ID=100123132505557
META_INVERSIONES_PAGE_ID=796480326889963

# Ad Accounts
META_ADS_ACCOUNT_GLASS=act_1101364862188478
META_ADS_ACCOUNT_ESMERALDAS=act_1868510380157902
META_ADS_ACCOUNT_AUTOS=act_2385776465260628
META_ADS_ACCOUNT_INR=act_930477373065306

# Catalogos
META_CATALOG_GLASS=1670886954032475
META_CATALOG_ESMERALDAS=944718051249202
META_CATALOG_AUTOS=955793357293894

# Pixel
META_PIXEL_GLASS=4073809872916511

# WhatsApp Pages (legacy via app Soler)
META_PHONE_NUMBER_ID=777414378791556
META_WABA_ID=786597210574223
```

---

## 🚀 SIGUIENTES PASOS POSIBLES

1. **Enviar mensaje WhatsApp test** (necesitas agregar tu numero al WABA test primero en dev console)
2. **Configurar webhook WhatsApp** → n8n cloud para recibir mensajes
3. **Crear plantillas WhatsApp custom** para los 4 negocios (greeting, follow-up, etc.)
4. **Migrar a numero production** (cuando tengas el WABA real verificado)
5. **Agregar numero personal Esmeraldas** (+506 8798 5656) al WABA
6. **Publicar app Soler Inversiones** (review process Meta)

---

**Fecha:** 2026-05-18 23:50 CR
**Maintainer:** Allann Solis
**Total credenciales documentadas:** 25+ variables
