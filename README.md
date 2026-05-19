# 🛒 CRM Soler

Sistema CRM completo para administrar **las 4 marcas del Grupo Soler** en Costa Rica.

> **Proyecto separado** del BAC Loyalty CRM ([github.com/allansolis/bac-loyalty-crm](https://github.com/allansolis/bac-loyalty-crm) — Salesforce monitoring tool).

---

## 🎯 Que es

CRM operativo para vender, atender y administrar todas las redes y canales digitales de:

- 🛡️ **Glass Soler** — polarizado de seguridad vehicular
- 💎 **Esmeraldas Soler** — joyeria con esmeraldas naturales
- 🚗 **Autos Soler** — compra-venta de vehiculos
- 🏘️ **Inversiones Soler** — asesoria inmobiliaria

Atiende automaticamente **WhatsApp + Facebook Messenger + Instagram Direct** via Meta Webhooks + n8n + bot Elena (Claude Sonnet 4.5).

## 🏗️ Componentes

```
CRM-Soler/
├── auto-crm/                    Dashboard Next.js (puerto 3000)
│   ├── src/app/
│   │   ├── /                    Home con KPIs + widget multi-business
│   │   ├── /leads               Hot leads tabla
│   │   ├── /leads-kanban        Kanban 7 columnas (NEW→WON/LOST)
│   │   ├── /analytics           5 widgets: trend/funnel/signals/heatmap/table
│   │   ├── /performance         Health/volume/cost/response
│   │   ├── /ads                 Meta Ads live dashboard
│   │   ├── /pipeline /contacts /deals /conversations
│   │   ├── /loyalty /reports /settings
│   │   └── /api/*               14 endpoints REST (incluye SSE stream)
│   ├── data/                    SQLite DB
│   └── package.json
│
└── soler-elena-system/          Sistema bots Elena
    ├── bots/                    4 bots Flask Python (puertos 5000-5003)
    │   ├── bot.py              :5000 Esmeraldas
    │   ├── bot_glass.py        :5001 Glass
    │   ├── bot_autos.py        :5002 Autos
    │   ├── bot_inversiones.py  :5003 Inversiones
    │   ├── lead_scoring.py     scoring 35 patrones
    │   ├── lead_enrichment.py  extrae nombre/tel/vehiculo/etc
    │   ├── lead_endpoints.py   9 REST endpoints /leads/*
    │   ├── notifications.py    Slack/Telegram/log alerts
    │   ├── conversation_store.py SQLite persistence
    │   ├── model_router.py     Haiku/Sonnet smart routing
    │   ├── ab_testing.py       A/B framework
    │   └── csat_tracker.py     Customer satisfaction
    ├── knowledge-bases/         KBs JSON editables (v2.0)
    │   ├── kb_glass_soler.json (22 secciones, 7 objeciones)
    │   ├── kb_esmeraldas.json  (13 FAQs)
    │   ├── kb_autos.json       (13 FAQs)
    │   └── kb_inversiones.json (12 FAQs)
    ├── managed-agent/           Elena en Claude Console
    │   ├── elena-master-system-prompt.md
    │   ├── elena-agent-config.json
    │   ├── elena_mega_kb.json
    │   └── SETUP-CLAUDE-CONSOLE.md
    ├── meta-config/             Catalogos Meta + workflows n8n
    │   ├── campaign-pack.json   6 campanas listas para fire
    │   ├── n8n-workflow-autos-soler.json
    │   └── n8n-workflow-inversiones-soler.json
    ├── scripts/                 Utilidades
    │   ├── watchdog.py         Auto-restart bots
    │   ├── auto_followup.py    Recovery hot leads 4h+
    │   ├── deploy-pending-campaigns.py
    │   ├── extract-zolutium.py
    │   ├── kb_trainer.py       Analiza convs + sugiere mejoras
    │   ├── create_elena_agent.py
    │   └── test_elena_e2e.py
    └── docs/                    ~25 documentos
        ├── OPERATOR-GUIDE.md   ← Manual operativo
        ├── DIFERENCIACION-SOLER-vs-BAC-LOYALTY.md
        ├── BRIEF-DISENO-CREATIVOS-V2.md
        ├── IG-PLAN-INVERSIONES-30D.md
        ├── IG-POSTS-10-PRIMEROS.md
        ├── ARQUITECTURA-4-NEGOCIOS.md
        ├── N8N-AUDIT.md
        └── ZOLUTIUM-INTEGRATION.md
```

## 🚀 Quick start (PC nueva)

```bash
# 1. Clonar
git clone https://github.com/allansolis/CRM-Soler.git
cd CRM-Soler

# 2. CRM Next.js
cd auto-crm
npm install
cp .env.example .env.local  # editar tokens
npx next dev  # http://localhost:3000

# 3. Bots Elena
cd ../soler-elena-system
pip install flask anthropic python-dotenv truststore pip-system-certs
cp .env.example "C:\Users\Usuario\Desktop\Bot glass soler\.env"  # editar
python bots/bot.py            # :5000 Esmeraldas
python bots/bot_glass.py      # :5001 Glass
python bots/bot_autos.py      # :5002 Autos
python bots/bot_inversiones.py # :5003 Inversiones

# 4. Servicios background
python scripts/watchdog.py             # auto-restart
cloudflared tunnel --url http://localhost:3000  # tunel para n8n
```

## 📊 Capacidades

### Atencion automatica clientes
- 24/7 conversational AI con Claude Sonnet 4.5 + Haiku router (36% ahorro costos)
- Lead scoring auto en cada mensaje (35 patrones)
- Extraccion estructurada de datos (nombre, telefono, vehiculo, presupuesto, etc.)
- Notificaciones tiempo real Slack/Telegram cuando hot lead detectado
- Auto-followup recovery leads inactivos 4h+
- Handoff inteligente a operador humano

### Gestion operativa
- CRM con kanban + tabla + analytics + performance
- Dashboard live tiempo real (SSE 5s push)
- Pipeline tradicional + automatizado
- Meta Ads integrado (campaign-pack 6 campanas ready)
- A/B testing en saludos y respuestas
- Customer satisfaction tracking

### Infraestructura
- Watchdog auto-restart bots
- SQLite persistence (sobrevive restarts)
- Cloudflare quick tunnels
- Webhooks Meta para WhatsApp/Messenger/IG
- Integracion n8n cloud
- Backup auto local + Drive + GitHub

## 🤖 Las "dos Elenas" (importante distinguir)

| Elena local (bots Flask) | Elena Managed (Claude Console) |
|--------------------------|--------------------------------|
| 4 instancias separadas por bot | 1 agente master multi-marca |
| Identifica marca por puerto | Identifica por contexto/metadata |
| KB JSON local hot-reload | KB en system prompt + tools |
| Para WhatsApp/IG/Messenger via n8n | Para Web/API directa |
| Sonnet 4.5 + Haiku router 36% savings | Sonnet 4.5 + 3 custom tools |
| ID: localhost:5000-5003 | ID: `agent_01WSgH9Kp8GqD4MjwNcLXtV5` |

**Estrategia hibrida activa:** ambos sistemas corren en paralelo, cada uno optimizado para su canal.

## 🔑 Variables de entorno

Ver `soler-elena-system/.env.example` (template) y `auto-crm/.env.example` (CRM).

Claves principales:
- `ANTHROPIC_API_KEY` — para los bots
- `META_ACCESS_TOKEN` — para enviar mensajes Meta
- `META_ADS_TOKEN` — para Ads Manager (requiere ads_management)
- `ZOLUTIUM_API_KEY` — para sync con GoHighLevel
- `WEBHOOK_SECRET` — auth interna 4 bots
- `ELENA_MANAGED_AGENT_ID` — `agent_01WSgH9Kp8GqD4MjwNcLXtV5`
- `SLACK_WEBHOOK_URL` (opcional) — alertas
- `TELEGRAM_BOT_TOKEN` (opcional) — alertas

## 📈 Estado actual

```
✅ 4 bots Elena con lead scoring + enrichment + model router
✅ CRM Next.js 6 paginas (home, leads, kanban, analytics, performance, ads)
✅ Elena Managed Agent activa en Claude Console
✅ Watchdog auto-restart 60s
✅ Auto-followup 4h+
✅ Campaign Pack 6 listas
✅ A/B testing + CSAT + Notifications
✅ KB trainer + Conversation persistence SQLite
```

## ⏳ Pendientes manuales

1. Pagar factura Glass (act_1101364862188478)
2. Habilitar Marketing API en app Soler + regen ADS token
3. Regenerar ZOLUTIUM_API_KEY
4. Recargar saldos Esmeraldas + Autos
5. Crear @inversionessoler IG
6. Importar 2 workflows n8n (meta-config/*.json)
7. Configurar Slack webhook

Ver `soler-elena-system/docs/OPERATOR-GUIDE.md` para manual operativo completo.

## 🔗 Repos relacionados

- **CRM Soler** (este): https://github.com/allansolis/CRM-Soler — 4 negocios retail
- **BAC Loyalty CRM** (otro): https://github.com/allansolis/bac-loyalty-crm — Salesforce monitoring
- **skills-soler** (deprecated marketplace): https://github.com/allansolis/skills-soler — skills genericas

---

**Mantenedor:** Allann Solis
**Version:** 2.0 (extraido de skills-soler, refactor mayo 2026)
**Licencia:** Proprietary
