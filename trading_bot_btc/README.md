# 🤖 Trading Bot BTC

Bot de trading automatizado para criptomonedas con análisis técnico, backtesting y notificaciones por Telegram.

## 📋 Características Principales

- Análisis técnico usando MACD en múltiples temporalidades
- Backtesting con interfaz gráfica
- Notificaciones por Telegram
- Análisis del libro de órdenes
- Visualización de datos y resultados
- Gestión de riesgo dinámica
- Manejo robusto de errores
- Sistema de logging
- Tests automatizados

## 🛠️ Tecnologías Utilizadas

### Lenguajes y Frameworks
- Python 3.8+
- Streamlit (Interfaz web)
- Pytest (Testing)

### Análisis de Datos y Trading
- pandas: Manipulación de datos
- pandas_ta: Indicadores técnicos
- numpy: Cálculos numéricos
- ccxt: Integración con exchanges

### Visualización
- matplotlib: Gráficos técnicos
- plotly: Gráficos interactivos
- Streamlit: Dashboard web

### APIs y Comunicación
- ccxt: API de exchanges
- python-telegram-bot: Notificaciones
- python-dotenv: Variables de entorno

### Testing y Calidad
- pytest: Framework de testing
- pytest-cov: Cobertura de tests
- black: Formateo de código
- flake8: Linting

## 🚀 Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/yourusername/trading_bot_btc.git
cd trading_bot_btc
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
- Copiar `.env.example` a `.env`
- Agregar tus claves API y token de Telegram

## 📁 Estructura del Proyecto

### Archivos Ejecutables
- `main.py`: Script principal del bot
- `app_streamlit.py`: Interfaz web
- `run_backtest.py`: Backtesting por línea de comandos
- `test_dependencies.py`: Verificación de dependencias

### Módulos Principales

#### 1. Estrategia (`strategy/`)
- `macd_strategy.py`: Implementación de estrategia MACD
  - Cálculo de señales
  - Umbrales dinámicos
  - Ajuste por volatilidad

#### 2. Backtesting (`backtesting/`)
- `engine.py`: Motor de backtesting
  - Simulación de operaciones
  - Gestión de capital
- `metrics.py`: Métricas de rendimiento
  - Win rate
  - Drawdown
  - Profit factor

#### 3. Utilidades (`utils/`)
- `api_data.py`: Interacción con exchanges
  - Datos históricos
  - Orderbook
- `error_handler.py`: Manejo de errores
  - Excepciones personalizadas
  - Decoradores de retry
- `telegram_notifications.py`: Notificaciones
  - Alertas de trading
  - Reportes

#### 4. Visualización (`visual/`)
- `macd_plot.py`: Gráficos técnicos
  - Visualización MACD
  - Señales de trading

#### 5. Tests (`tests/`)
- `test_strategy.py`: Pruebas de estrategia
- `test_error_handler.py`: Pruebas de errores
- `conftest.py`: Fixtures de pytest

## 🔧 Configuración

### Variables de Entorno
```env
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

### Parámetros de Trading
- Temporalidades: 15m, 30m, 1h, 4h, 1d, 3d
- Umbrales dinámicos por timeframe
- Pesos de señales configurables

## 📊 Uso

### Bot de Trading
```bash
python main.py
```

### Backtesting
```bash
# Línea de comandos
python run_backtest.py

# Interfaz web
streamlit run app_streamlit.py
```

### Tests
```bash
pytest tests/
```

## 📈 Funcionamiento

1. **Obtención de Datos**
   - Datos históricos en múltiples timeframes
   - Análisis del orderbook
   - Indicadores técnicos

2. **Análisis**
   - Cálculo de MACD
   - Señales por timeframe
   - Fuerza de señales
   - Ajuste por volatilidad

3. **Toma de Decisiones**
   - Evaluación multi-timeframe
   - Ponderación de señales
   - Umbrales dinámicos
   - Gestión de riesgo

4. **Notificaciones**
   - Alertas de trading
   - Reportes de rendimiento
   - Errores y advertencias

## 🤝 Contribución

1. Fork el repositorio
2. Crear rama feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

## 📝 Licencia

Distribuido bajo la licencia MIT. Ver `LICENSE` para más información.

## 📧 Contacto

Tu Nombre - [@tutwitter](https://twitter.com/tutwitter) - email@example.com

Link del Proyecto: [https://github.com/yourusername/trading_bot_btc](https://github.com/yourusername/trading_bot_btc) 