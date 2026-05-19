# 🔍 Auditoria E2E CRM Soler — 18 mayo 2026 (noche)

Estado completo de todos los nodos n8n y funciones del sistema.

---

## 🌐 1. n8n CLOUD

| Item | Estado | Detalle |
|------|--------|---------|
| Servidor `/healthz` | ✅ OK | `{"status": "ok"}` |
| Webhook `/webhook/glass-soler` | ✅ HTTP 200 (302ms) | Workflow activo + responde |
| Webhook `/webhook/esmeraldas-soler` | ✅ HTTP 200 (279ms) | Workflow activo + responde |
| Webhook `/webhook/autos-soler` | ❌ HTTP 404 | **PENDIENTE IMPORTAR** JSON en `meta-config/` |
| Webhook `/webhook/inversiones-soler` | ❌ HTTP 404 | **PENDIENTE IMPORTAR** JSON en `meta-config/` |

**Score:** 2/4 negocios atendidos por n8n cloud.

### Workflows JSON listos para importar

`meta-config/n8n-workflow-autos-soler.json`:
- 7 nodos: Webhook → Set Extract → IF page_id → CRM Upsert → Bot Dispatch → Set Build → Send Meta
- 6 conexiones
- page_id filter: `100123132505557`
- Bot target: `localhost:5002/webhook` via tunnel
- Status: **inactive** (esperando import)

`meta-config/n8n-workflow-inversiones-soler.json`:
- Misma estructura
- page_id filter: `796480326889963`
- Bot target: `localhost:5003/webhook` via tunnel
- Status: **inactive** (esperando import)

### Workflows existentes en n8n cloud (no clonados a JSON aun)

Basado en sesiones previas:
- Glass Soler — Receive & Respond (activo)
- Esmeraldas Soler — Receive & Respond (activo)
- Cerebro Marketing IA (estado desconocido — requiere login)
- Agent 9 CRM Sync (estado desconocido — fix sortBy aplicado mes pasado)

---

## 🤖 2. BOTS PYTHON (4 instancias Flask)

| Bot | Puerto | Status | KB stats |
|-----|--------|--------|----------|
| 💎 Esmeraldas | 5000 | ✅ UP | 13 FAQs, 7 objeciones, 5 productos |
| 🛡️ Glass | 5001 | ✅ UP | 13 FAQs, 7 objeciones, 4 paquetes |
| 🚗 Autos | 5002 | ✅ UP | 13 FAQs, 7 objeciones, 4 servicios |
| 🏘️ Inversiones | 5003 | ✅ UP | 12 FAQs, 5 servicios |

### Endpoints REST verificados por cada bot

| Endpoint | Metodo | Auth | Funcion |
|----------|--------|------|---------|
| `/` | GET | — | Health + metadata |
| `/stats` | GET | secret | Stats conversaciones |
| `/chat` | POST | secret | Test directo enviar mensaje |
| `/webhook` | POST | secret | Receptor desde n8n |
| `/kb/reload` | POST | secret | Hot-reload KB JSON |
| `/leads/score` | GET | secret | Score de un user |
| `/leads/hot` | GET | secret | Lista hot leads (≥70) |
| `/leads/handoffs` | GET | secret | Handoffs disparados |
| `/leads/stats` | GET | secret | Aggregate stats |
| `/leads/score-message` | POST | secret | Manual scoring |
| `/leads/reset` | POST | secret | Reset user score |
| `/leads/enriched` | GET | secret | Datos extraidos (nombre/tel/etc) |
| `/leads/search` | GET | secret | Buscar por nombre o phone |
| `/leads/export` | GET | secret | Export CSV/JSON |
| `/reset/<user>` | POST | secret | Borrar historial |
| `/historial/<user>` | GET | secret | Ver historial |

**Total endpoints por bot: 16** = 64 endpoints REST a lo largo de los 4 bots.

### Datos actuales en producción

- 💎 Esmeraldas: 0 hot leads, 0 handoffs
- 🛡️ Glass: **3 hot leads**, **3 handoffs** (Carlos, Maria, Roberto desde tests)
- 🚗 Autos: 0 hot leads, **1 enriched** lead
- 🏘️ Inversiones: 0 hot leads, **2 enriched** leads

---

## ☁️ 3. ELENA MANAGED AGENT (Claude Console)

| Item | Valor |
|------|-------|
| Agent ID | `agent_01WSgH9Kp8GqD4MjwNcLXtV5` |
| Status | ✅ ACTIVO |
| Name | Elena - Grupo Soler |
| Model | claude-sonnet-4-5-20250929 (standard speed) |
| Tools | 3 (schedule_appointment, request_human_handoff, send_product_catalog) |
| Environment | env_01MD6aFXag86xp9QpG8hAbAE (elena-soler-env) |
| Sessions creadas | 3 (todas tests E2E) |
| Creado | 2026-05-18 19:06 UTC |

---

## 🖥️ 4. CRM NEXT.JS (auto-crm)

| Item | Estado |
|------|--------|
| Servidor :3000 | ❌ DOWN (no iniciado) |
| Tunnel cloudflare | ❌ DOWN |

**Accion:** Si necesitas operar via web/CRM, hay que arrancar `npx next dev` en `auto-crm/` y `cloudflared tunnel --url http://localhost:3000`.

### Paginas del CRM (cuando esta up)

| Ruta | Funcion |
|------|---------|
| `/` | Home dashboard + widget multi-business |
| `/leads` | Tabla hot leads filtrable |
| `/leads-kanban` | Kanban 7 columnas |
| `/analytics` | 5 widgets (trend/funnel/signals/heatmap/table) |
| `/performance` | Health/volume/cost/response |
| `/ads` | Meta Ads live dashboard |
| `/pipeline` | Deals tradicional |
| `/contacts` `/deals` `/conversations` `/activities` | CRUD tradicional |
| `/loyalty` | Generic loyalty (no bancario) |
| `/reports` `/settings` | Configuracion |

### APIs del CRM

- `GET /api/leads` (views: hot, handoffs, stats)
- `POST /api/leads/status` (cambiar estado manual kanban)
- `GET /api/leads/stream` (SSE 5s push)
- `GET /api/analytics?view=` (trend/funnel/signals/hours/table)
- `GET /api/performance/{health|volume|cost|response}`

---

## 🔧 5. SCRIPTS UTILITY (corriendo o disponibles)

| Script | Estado | Funcion |
|--------|--------|---------|
| `watchdog.py` | ✅ CORRIENDO | Auto-restart bots cada 60s |
| `watch-tokens.py` | ⏳ DISPONIBLE | Dispara al regenerar tokens |
| `auto_followup.py` | ⏳ DISPONIBLE | Recovery 4h+ inactividad |
| `deploy-pending-campaigns.py` | ⏳ ESPERANDO ADS TOKEN | Fire 6 campanas Meta |
| `extract-zolutium.py` | ⏳ ESPERANDO ZOLUTIUM TOKEN | Descarga GoHighLevel |
| `kb_trainer.py` | ⏳ DISPONIBLE | Analiza convs + sugiere mejoras |
| `create_elena_agent.py` | ✅ EJECUTADO | Elena Managed ya creada |
| `test_elena_e2e.py` | ✅ VERIFICADO | Test E2E OK |
| `enhance-glass-kb.py` | ✅ EJECUTADO | KB v2.0 con objeciones |
| `enhance-other-kbs.py` | ✅ EJECUTADO | +23 FAQs en 3 bots |

---

## 📊 6. MODULOS PYTHON COMPARTIDOS

| Modulo | Estado | Funciona |
|--------|--------|----------|
| `lead_scoring.py` | ✅ Activo | 35 patrones regex |
| `lead_enrichment.py` | ✅ Activo | Extrae 8 campos estructurados |
| `lead_endpoints.py` | ✅ Activo | Registra 9 endpoints REST |
| `notifications.py` | ✅ Activo | 4 canales (console/log/Slack/Telegram) |
| `conversation_store.py` | ✅ Disponible | SQLite persistence ready |
| `model_router.py` | ✅ Activo | Haiku/Sonnet routing (36% savings) |
| `ab_testing.py` | ✅ Activo | A/B framework + 3 experimentos |
| `csat_tracker.py` | ✅ Disponible | Customer satisfaction ratings |

---

## 📋 7. KNOWLEDGE BASES (v2.0)

| KB | FAQs | Objeciones | Productos/Servicios | Flujo venta | Tipos cliente |
|----|------|------------|---------------------|-------------|---------------|
| kb_glass_soler | 13 | 7 | 4 paquetes | 9 pasos | 5 perfiles |
| kb_esmeraldas | 13 | 7 | 5 productos | 9 pasos | 4 perfiles |
| kb_autos | 13 | 7 | 4 servicios | 5 pasos | 5 perfiles |
| kb_inversiones | 12 | 5 | 5 servicios | 5 pasos | 5 perfiles |

---

## 🚨 8. ACCIONES PENDIENTES DEL USUARIO

| # | Tarea | Bloquea | Prioridad |
|---|-------|---------|-----------|
| 1 | Importar 2 workflows JSON en n8n | Webhooks Autos+Inversiones funcionan | 🔴 Alta |
| 2 | Configurar webhooks Meta para pages Autos+Inversiones | Recepcion mensajes Meta | 🔴 Alta |
| 3 | Pagar factura Glass | Cuenta UNSETTLED → ACTIVE | 🔴 Alta |
| 4 | Habilitar Marketing API en app Soler + regenerar `META_ADS_TOKEN` | Deploy 6 campanas + Glass reactivate | 🔴 Alta |
| 5 | Regenerar `ZOLUTIUM_API_KEY` | Extract config GoHighLevel | 🟡 Media |
| 6 | Recargar saldos Esmeraldas (₡60k) + Autos (₡15k) | Reactivar campanas pausadas | 🟡 Media |
| 7 | Crear cuenta IG @inversionessoler | Atender DMs IG Inversiones | 🟡 Media |
| 8 | Vincular @autossoler IG Business a page Autos | Atender DMs IG Autos | 🟡 Media |
| 9 | Configurar `SLACK_WEBHOOK_URL` o `TELEGRAM_BOT_TOKEN` en .env | Notificaciones hot leads en celular | 🟢 Baja |
| 10 | Restart Claude Desktop (post fix MCP playwright) | Browser automation funciona de nuevo | 🟢 Baja |
| 11 | Arrancar CRM `npx next dev` + tunnel `cloudflared` | UI web del CRM accesible | 🟢 Baja (opcional) |

---

## 📈 9. METRICAS DEL SISTEMA

### Capacidad actual
- 4 bots respondiendo 24/7 mientras PC corra
- Watchdog reinicia automaticamente si caen
- ~2s latencia por mensaje (incluye Anthropic API)
- ~$0.0051 USD por conversacion (con router Haiku/Sonnet)
- Costo proyectado 100 convs/dia = $15/mes
- Costo proyectado 1000 convs/dia = $153/mes

### Volumen actual (datos audit)
- 6 leads totales en sistema (de tests)
- 3 hot leads (todos Glass)
- 3 handoffs disparados
- 3 sessions en Elena Managed
- 1 environment

---

## ✅ 10. CHECKLIST DE SALUD

- [x] n8n cloud servidor activo
- [x] 2 webhooks (Glass + Esmeraldas) respondiendo
- [ ] 2 webhooks (Autos + Inversiones) — PENDIENTE IMPORT
- [x] 4 bots Python UP
- [x] 64 endpoints REST funcionando
- [x] Watchdog corriendo
- [x] Elena Managed Agent activa con 3 tools
- [x] KBs v2.0 cargadas en los 4 bots
- [x] Modulos compartidos importados correctamente
- [ ] CRM Next.js corriendo — DOWN
- [ ] Cloudflare tunnel — DOWN
- [x] Repos GitHub separados (CRM-Soler + bac-loyalty-crm)
- [x] Backups locales actualizados
- [x] Drive sincronizado (docs index)

---

## 🎯 CONCLUSION

**Sistema operacional al 75%:**
- ✅ Backend bots + Elena Managed + n8n parcial funcionando perfectamente
- ⏳ Faltan 2 workflows n8n (Autos + Inversiones)
- ⏳ CRM web no esta corriendo (opcional, las APIs estan via bots)

**Para llegar al 100%:**
1. **Importar 2 JSON en n8n** (5 minutos, drag-drop en n8n cloud)
2. **Configurar webhooks Meta** en Developer Console (2 minutos)
3. **(Opcional)** Arrancar CRM Next.js + tunnel para UI web

**Lo que el sistema esta haciendo AHORA (sin intervencion):**
- Bots Elena listos para recibir mensajes via n8n (Glass+Esmeraldas) o test directo
- Watchdog vigilando cada 60s
- Elena Managed Agent disponible via Anthropic API

---

**Reporte generado:** 2026-05-18 ~20:13 CR
**Maintainer:** Allann Solis
