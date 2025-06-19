import re
import random
from datetime import datetime

class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.crypto_db = {
            "Bitcoin": {
                "symbol": "BTC",
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3,
                "current_price": 65000,
                "24h_change": 2.5,
                "description": "The original cryptocurrency and digital gold"
            },
            "Ethereum": {
                "symbol": "ETH",
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6,
                "current_price": 3500,
                "24h_change": 1.8,
                "description": "Smart contract platform powering DeFi and NFTs"
            },
            "Cardano": {
                "symbol": "ADA",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8,
                "current_price": 0.45,
                "24h_change": 4.2,
                "description": "Proof-of-stake blockchain focused on sustainability"
            },
            "Solana": {
                "symbol": "SOL",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7,
                "current_price": 145,
                "24h_change": 3.7,
                "description": "High-speed blockchain for dApps and DeFi"
            },
            "Polygon": {
                "symbol": "MATIC",
                "price_trend": "stable",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 9,
                "current_price": 0.85,
                "24h_change": -0.5,
                "description": "Layer 2 scaling solution for Ethereum"
            }
        }
        
        self.greetings = [
            "Hey there, crypto explorer! 🚀",
            "Welcome to the crypto universe! 🌟",
            "Ready to navigate the crypto waters? ⛵",
            "Let's find your perfect crypto match! 💎"
        ]
        
        self.conversation_history = []
    
    def greet(self):
        greeting = random.choice(self.greetings)
        intro = f"""
{greeting}

I'm {self.name}, your AI-powered crypto advisor! 🤖💰

I can help you with:
• 📈 Price trend analysis
• 🌱 Sustainability recommendations  
• 💼 Investment advice based on your goals
• 📊 Market cap insights
• ⚡ Energy efficiency comparisons

Just ask me questions like:
- "Which crypto is trending up?"
- "What's the most sustainable coin?"
- "Should I invest in Bitcoin?"
- "Show me all cryptos"

⚠️ DISCLAIMER: Crypto investments are risky! Always do your own research.

What would you like to know about crypto today?
        """
        print(intro)
        return intro
    
    def analyze_query(self, query):
        """Analyze user query and determine intent"""
        query_lower = query.lower()
        
        # Intent classification
        if any(word in query_lower for word in ['sustainable', 'green', 'eco', 'environment', 'energy']):
            return 'sustainability'
        elif any(word in query_lower for word in ['rising', 'trending', 'up', 'growing', 'profitable']):
            return 'profitability'
        elif any(word in query_lower for word in ['stable', 'safe', 'secure', 'reliable']):
            return 'stability'
        elif any(word in query_lower for word in ['show', 'list', 'all', 'display']):
            return 'list_all'
        elif any(word in query_lower for word in ['compare', 'vs', 'versus', 'difference']):
            return 'compare'
        elif any(word in query_lower for word in ['price', 'cost', 'value']):
            return 'price_info'
        elif any(crypto.lower() in query_lower for crypto in self.crypto_db.keys()):
            return 'specific_crypto'
        elif any(word in query_lower for word in ['help', 'what', 'how']):
            return 'help'
        else:
            return 'general'
    
    def get_sustainable_recommendations(self):
        """Recommend most sustainable cryptocurrencies"""
        sorted_cryptos = sorted(
            self.crypto_db.items(), 
            key=lambda x: x[1]['sustainability_score'], 
            reverse=True
        )
        
        response = "🌱 SUSTAINABILITY CHAMPIONS 🌱\n\n"
        
        for i, (name, data) in enumerate(sorted_cryptos[:3], 1):
            energy_emoji = "🟢" if data['energy_use'] == 'low' else "🟡" if data['energy_use'] == 'medium' else "🔴"
            response += f"{i}. {name} ({data['symbol']})\n"
            response += f"   🌱 Sustainability Score: {data['sustainability_score']}/10\n"
            response += f"   {energy_emoji} Energy Use: {data['energy_use'].title()}\n"
            response += f"   💡 {data['description']}\n\n"
        
        response += "💚 My top pick for eco-conscious investors: "
        response += f"{sorted_cryptos[0][0]}! It's leading the green crypto revolution!"
        
        return response
    
    def get_profitable_recommendations(self):
        """Recommend most profitable cryptocurrencies"""
        rising_cryptos = [
            (name, data) for name, data in self.crypto_db.items() 
            if data['price_trend'] == 'rising'
        ]
        
        # Sort by 24h change
        rising_cryptos.sort(key=lambda x: x[1]['24h_change'], reverse=True)
        
        response = "📈 TRENDING UP - PROFITABILITY FOCUS 📈\n\n"
        
        for i, (name, data) in enumerate(rising_cryptos, 1):
            trend_emoji = "🚀" if data['24h_change'] > 3 else "📈"
            response += f"{i}. {name} ({data['symbol']})\n"
            response += f"   {trend_emoji} 24h Change: +{data['24h_change']}%\n"
            response += f"   💰 Current Price: ${data['current_price']:,}\n"
            response += f"   📊 Market Cap: {data['market_cap'].title()}\n\n"
        
        if rising_cryptos:
            response += f"🎯 Hot pick: {rising_cryptos[0][0]} is showing strong momentum!"
        
        return response
    
    def get_stable_recommendations(self):
        """Recommend stable cryptocurrencies"""
        stable_cryptos = [
            (name, data) for name, data in self.crypto_db.items() 
            if data['price_trend'] == 'stable' or abs(data['24h_change']) < 2
        ]
        
        response = "⚖️ STABILITY FOCUSED PICKS ⚖️\n\n"
        
        for i, (name, data) in enumerate(stable_cryptos, 1):
            response += f"{i}. {name} ({data['symbol']})\n"
            response += f"   📊 Trend: {data['price_trend'].title()}\n"
            response += f"   💰 Current Price: ${data['current_price']:,}\n"
            response += f"   📈 24h Change: {data['24h_change']:+}%\n\n"
        
        if stable_cryptos:
            response += f"🛡️ Most stable option: {stable_cryptos[0][0]} for steady growth!"
        
        return response
    
    def list_all_cryptos(self):
        """Display all available cryptocurrencies"""
        response = "📋 ALL AVAILABLE CRYPTOCURRENCIES 📋\n\n"
        
        for i, (name, data) in enumerate(self.crypto_db.items(), 1):
            trend_emoji = "🚀" if data['price_trend'] == 'rising' else "📊"
            sustainability_emoji = "🌱" if data['sustainability_score'] >= 7 else "⚠️"
            
            response += f"{i}. {name} ({data['symbol']})\n"
            response += f"   💰 ${data['current_price']:,} ({data['24h_change']:+}%)\n"
            response += f"   {trend_emoji} Trend: {data['price_trend'].title()}\n"
            response += f"   {sustainability_emoji} Sustainability: {data['sustainability_score']}/10\n"
            response += f"   📝 {data['description']}\n\n"
        
        response += "Need specific advice? Ask me about profitability or sustainability! 🎯"
        return response
    
    def get_specific_crypto_info(self, query):
        """Get information about a specific cryptocurrency"""
        query_lower = query.lower()
        
        for name, data in self.crypto_db.items():
            if name.lower() in query_lower or data['symbol'].lower() in query_lower:
                trend_emoji = "🚀" if data['price_trend'] == 'rising' else "📊"
                energy_emoji = "🟢" if data['energy_use'] == 'low' else "🟡" if data['energy_use'] == 'medium' else "🔴"
                
                response = f"📊 {name} ({data['symbol']}) ANALYSIS 📊\n\n"
                response += f"💰 Current Price: ${data['current_price']:,}\n"
                response += f"{trend_emoji} 24h Change: {data['24h_change']:+}%\n"
                response += f"📈 Price Trend: {data['price_trend'].title()}\n"
                response += f"📊 Market Cap: {data['market_cap'].title()}\n"
                response += f"{energy_emoji} Energy Use: {data['energy_use'].title()}\n"
                response += f"🌱 Sustainability Score: {data['sustainability_score']}/10\n"
                response += f"📝 Description: {data['description']}\n\n"
                
                # Add recommendation
                if data['sustainability_score'] >= 7 and data['price_trend'] == 'rising':
                    response += "✅ RECOMMENDATION: Great choice! High sustainability + growth potential!"
                elif data['sustainability_score'] >= 7:
                    response += "✅ RECOMMENDATION: Excellent for eco-conscious long-term investing!"
                elif data['price_trend'] == 'rising':
                    response += "⚠️ RECOMMENDATION: Good for short-term gains, but consider environmental impact."
                else:
                    response += "⚠️ RECOMMENDATION: Proceed with caution. Do thorough research first."
                
                return response
        
        return "🤔 Sorry, I don't have information about that cryptocurrency. Try asking about Bitcoin, Ethereum, Cardano, Solana, or Polygon!"
    
    def get_help(self):
        """Provide help information"""
        return """
🆘 HOW TO CHAT WITH CRYPTOBUDDY 🆘

Ask me questions like:
• "Which crypto is trending up?" - For profitable picks
• "What's the most sustainable coin?" - For eco-friendly options  
• "Show me all cryptos" - To see everything available
• "Tell me about Bitcoin" - For specific crypto analysis
• "Which crypto is stable?" - For low-risk options

I analyze based on:
📈 Price trends (rising/stable)
🌱 Sustainability scores (1-10)
⚡ Energy efficiency (low/medium/high)
💰 Market capitalization
📊 24-hour price changes

Remember: This is educational only! 📚
Always do your own research before investing! 🔍
        """
    
    def process_query(self, query):
        """Main query processing logic"""
        if not query.strip():
            return "🤔 I didn't catch that. What would you like to know about crypto?"
        
        intent = self.analyze_query(query)
        self.conversation_history.append(f"User: {query}")
        
        if intent == 'sustainability':
            response = self.get_sustainable_recommendations()
        elif intent == 'profitability':
            response = self.get_profitable_recommendations()
        elif intent == 'stability':
            response = self.get_stable_recommendations()
        elif intent == 'list_all':
            response = self.list_all_cryptos()
        elif intent == 'specific_crypto':
            response = self.get_specific_crypto_info(query)
        elif intent == 'help':
            response = self.get_help()
        else:
            response = """
🤖 I'm here to help with crypto advice! Try asking:
• "Which crypto should I buy for long-term growth?"
• "What's the most eco-friendly cryptocurrency?"
• "Show me trending cryptos"
• "Tell me about Ethereum"

What crypto question can I help you with? 🚀
            """
        
        self.conversation_history.append(f"CryptoBuddy: {response}")
        return response
    
    def run_chat(self):
        """Main chat loop"""
        print("=" * 60)
        self.greet()
        print("=" * 60)
        
        while True:
            try:
                user_input = input("\n💬 You: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    farewell = """
🚀 Thanks for chatting with CryptoBuddy! 

Remember:
• Crypto markets are volatile 📈📉
• Only invest what you can afford to lose 💰
• Do your own research always! 🔍
• Stay updated on market trends 📊

Happy investing, and may your portfolio be ever green! 🌱💎

Goodbye! 👋
                    """
                    print(farewell)
                    break
                
                if not user_input:
                    print("🤔 Please ask me something about crypto!")
                    continue
                
                response = self.process_query(user_input)
                print(f"\n🤖 {self.name}: {response}")
                
            except KeyboardInterrupt:
                print("\n\n👋 Chat interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Oops! Something went wrong: {e}")
                print("Let's try again! 🔄")

# Function to run the chatbot
def main():
    """Initialize and run the CryptoBuddy chatbot"""
    bot = CryptoBuddy()
    bot.run_chat()

if __name__ == "__main__":
    main()
