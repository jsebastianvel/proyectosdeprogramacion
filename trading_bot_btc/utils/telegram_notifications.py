# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 23:45:04 2025

@author: OMEN Laptop
"""

import requests
import os
from datetime import datetime

class TelegramNotifier:
    def __init__(self, token=None, chat_id=None):
        """
        Inicializa el notificador de Telegram
        :param token: Bot token de Telegram
        :param chat_id: ID del chat donde enviar mensajes
        """
        self.token = token or os.getenv('TELEGRAM_BOT_TOKEN')
        self.chat_id = chat_id or os.getenv('TELEGRAM_CHAT_ID')
        self.base_url = f"https://api.telegram.org/bot{self.token}"
        
    def send_message(self, message):
        """Envía un mensaje de texto simple"""
        try:
            url = f"{self.base_url}/sendMessage"
            data = {
                "chat_id": self.chat_id,
                "text": message,
                "parse_mode": "HTML"
            }
            response = requests.post(url, data=data)
            return response.json()
        except Exception as e:
            print(f"❌ Error enviando mensaje a Telegram: {str(e)}")
            return None

    def send_trade_signal(self, timeframe, signal, strength, price, additional_info=None):
        """Envía una señal de trading formateada"""
        emoji_map = {
            'buy': '🟢',
            'sell': '🔴',
            'valley_buy': '💚',
            'top_sell': '❤️',
            'hold': '⚪'
        }
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        emoji = emoji_map.get(signal, '⚠️')
        
        message = f"""
<b>🤖 Señal de Trading</b>
━━━━━━━━━━━━━━━
⏰ <b>Fecha:</b> {current_time}
📊 <b>Timeframe:</b> {timeframe}
{emoji} <b>Señal:</b> {signal.upper()}
💪 <b>Fuerza:</b> {strength:.2f}
💵 <b>Precio:</b> ${price:.2f}
"""
        
        if additional_info:
            message += f"\nℹ️ <b>Info adicional:</b>\n{additional_info}"
            
        return self.send_message(message)

    def send_summary(self, peso_buy, peso_sell, decision, orderbook=None):
        """Envía un resumen de la decisión final"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        emoji_decision = {
            "📈 LONG": "🚀",
            "📉 SHORT": "🔻",
            "⏳ WAIT": "⏳"
        }.get(decision, "❓")
        
        message = f"""
<b>📊 Resumen de Trading</b>
━━━━━━━━━━━━━━━
⏰ <b>Fecha:</b> {current_time}
📈 <b>Peso Compra:</b> {peso_buy:.2f}
📉 <b>Peso Venta:</b> {peso_sell:.2f}
{emoji_decision} <b>Decisión:</b> {decision}
"""
        
        if orderbook:
            message += f"""
📚 <b>Order Book:</b>
💰 Bid: ${orderbook['bid_price']:.2f}
💰 Ask: ${orderbook['ask_price']:.2f}
📊 Medio: ${orderbook['mid_price']:.2f}
"""
            
        return self.send_message(message)

    def send_error(self, error_message, context=None):
        """Envía una notificación de error"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        message = f"""
❌ <b>Error en el Bot</b>
━━━━━━━━━━━━━━━
⏰ <b>Fecha:</b> {current_time}
🔴 <b>Error:</b> {error_message}
"""
        
        if context:
            message += f"📝 <b>Contexto:</b> {context}"
            
        return self.send_message(message) 