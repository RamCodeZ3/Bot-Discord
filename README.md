# 🤖 Bot de Bienvenidas y Despedidas

Este bot de Discord está diseñado para **dar la bienvenida y despedir a los usuarios** cuando entran o salen de un servidor.  
Los mensajes son **personalizables por cada servidor**, permitiendo a los administradores configurar saludos únicos.

---

## 🚀 Características
- ✅ Mensaje de presentación del bot.  
- ✅ Configuración de mensaje de **bienvenida**.  
- ✅ Configuración de mensaje de **despedida**.  
- ✅ Persistencia de configuraciones mediante **JSON** (los ajustes no se pierden al reiniciar el bot).  
- ✅ Uso de **slash commands** (`/comandos`).  

---
## 📂 Estructura del proyecto  
📦 Bot-Discord <br/>
┣ 📂 data <br/>
┃ ┗ 📜 settings.json # Configuración guardada en JSON <br/>
┣ 📂 src <br/>
┃ ┣ 📂 cogs <br/>
┃ ┃ ┗ 📜 __init__.py # Inicialización del paquete de cogs <br/>
┃ ┣ 📜 command.py # Comandos del bot <br/>
┃ ┣ 📜 event.py # Eventos de bienvenida y despedida <br/>
┃ ┣ 📜 function_json.py # Funciones para manejar JSON <br/>
┃ ┗ 📜 main.py # Archivo principal del bot <br/>
┣ 📜 .gitignore # Archivos/carpetas ignorados por Git <br/>
┣ 📜 README.md # Documentación del proyecto <br/>
┗ 📜 requirements.txt # Dependencias del proyecto <br/>

---

## 🛠️ Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/discord-welcome-bot.git
   cd discord-welcome-bot

2. Crear un entorno:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Linux/Mac
   venv\Scripts\activate      # En Windows

3. Crea un archivo .env en la raíz del proyecto con tu token:
   ```bash
   TOKEN = 'tu_token_aqui'
