# 🚀 Crypto AI - AI-Powered Cryptocurrency Advisor Chatbot

![CryptoBuddy Logo](https://img.shields.io/badge/CryptoBuddy-AI%20Advisor-green?style=for-the-badge&logo=bitcoin)

## 📋 Project Overview

**CryptoBuddy** is an AI-powered cryptocurrency advisor chatbot that provides investment recommendations based on profitability and sustainability metrics. This project demonstrates fundamental AI decision-making through rule-based logic and conversational interfaces.

### 🎯 Assignment Context
- **Course**: PLP Academy - AI Development Track
- **Week**: 1 Assignment
- **Theme**: "Your First AI-Powered Financial Sidekick!"

## ✨ Features

### 🤖 Smart Analysis
- **Profitability Assessment**: Analyzes price trends and 24-hour changes
- **Sustainability Scoring**: Evaluates environmental impact and energy efficiency
- **Market Intelligence**: Considers market cap and stability factors
- **Personalized Recommendations**: Tailored advice based on user queries

### 💬 Conversational Interface
- Natural language processing using keyword matching
- Multiple query types supported
- Interactive chat experience
- Friendly, informative responses with emojis

### 📊 Cryptocurrency Database
Currently supports analysis of:
- **Bitcoin (BTC)** - Digital gold standard
- **Ethereum (ETH)** - Smart contract platform
- **Cardano (ADA)** - Proof-of-stake blockchain
- **Solana (SOL)** - High-speed blockchain
- **Polygon (MATIC)** - Layer 2 scaling solution

## 🛠️ Technology Stack

- **Language**: Python 3.7+
- **Architecture**: Rule-based chatbot
- **Libraries**: Built-in Python modules (no external dependencies)
- **Platform**: Compatible with Google Colab, Jupyter Notebook, or any Python IDE

## 🚀 Quick Start

### Installation
1. Clone the repository:
```bash
git clone https://github.com/abbgael/ai_assignment.git
cd ai_assignment
```

2. Run the chatbot:
```bash
python crypto.py
```

### Usage Examples

```
💬 You: Which crypto is trending up?
🤖 CryptoBuddy: 📈 TRENDING UP - PROFITABILITY FOCUS 📈

1. Cardano (ADA)
   🚀 24h Change: +4.2%
   💰 Current Price: $0.45
   📊 Market Cap: Medium

🎯 Hot pick: Cardano is showing strong momentum!
```

```
💬 You: What's the most sustainable coin?
🤖 CryptoBuddy: 🌱 SUSTAINABILITY CHAMPIONS 🌱

1. Polygon (MATIC)
   🌱 Sustainability Score: 9/10
   🟢 Energy Use: Low
   💡 Layer 2 scaling solution for Ethereum

💚 My top pick for eco-conscious investors: Polygon!
```

## 🧠 How It Works

### AI Decision-Making Process

1. **Query Analysis**: Natural language processing using keyword matching
2. **Intent Classification**: Categorizes user intent (sustainability, profitability, etc.)
3. **Data Processing**: Analyzes cryptocurrency metrics based on intent
4. **Recommendation Engine**: Applies scoring algorithms to rank options
5. **Response Generation**: Creates conversational, informative responses

### Key Algorithms

- **Sustainability Ranking**: `sorted(cryptos, key=sustainability_score, reverse=True)`
- **Profitability Analysis**: Combines price trends with 24-hour changes
- **Stability Assessment**: Identifies low-volatility options
- **Multi-criteria Decision Making**: Balances multiple factors for recommendations

## 📈 Data Structure

```python
crypto_db = {
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
    # ... more cryptocurrencies
}
```

## 🎨 Chatbot Personality

**CryptoBuddy** is designed to be:
- 🤝 **Friendly**: Welcoming and approachable tone
- 📚 **Educational**: Provides learning opportunities
- ⚠️ **Responsible**: Includes investment risk disclaimers
- 🎯 **Focused**: Specializes in crypto investment advice
- 🌟 **Engaging**: Uses emojis and conversational language

## 🔮 Future Enhancements

### Stretch Goals Implemented
- [x] Multiple cryptocurrency support
- [x] Detailed analysis metrics
- [x] Conversation history tracking
- [x] Help system

### Potential Improvements
- [ ] Real-time API integration (CoinGecko)
- [ ] Natural Language Processing with NLTK
- [ ] Machine learning-based predictions
- [ ] Portfolio management features
- [ ] Technical analysis indicators

## 📸 Screenshots

### Main Interface
```
🚀 Welcome to the crypto universe! 🌟

I'm CryptoBuddy, your AI-powered crypto advisor! 🤖💰

I can help you with:
• 📈 Price trend analysis
• 🌱 Sustainability recommendations  
• 💼 Investment advice based on your goals
• 📊 Market cap insights
• ⚡ Energy efficiency comparisons
```

### Sample Conversation
![Chat Example](screenshots/chat-example.png)

## ⚠️ Disclaimer

**IMPORTANT**: This chatbot is for educational purposes only. Cryptocurrency investments carry significant risks:

- 📉 **Volatility**: Crypto prices can fluctuate dramatically
- 💸 **Loss Risk**: You could lose your entire investment
- 🔍 **Research Required**: Always conduct thorough research
- 💡 **Not Financial Advice**: This tool provides educational information only

**Always consult with qualified financial advisors before making investment decisions.**

## 📚 Learning Outcomes

This project demonstrates:

### ✅ AI Fundamentals
- Rule-based decision making
- Pattern matching and classification
- Multi-criteria analysis
- Conversational AI basics

### ✅ Programming Skills
- Object-oriented design
- Data structure manipulation
- User interface development
- Error handling and validation

### ✅ Financial Technology
- Cryptocurrency market analysis
- Investment recommendation systems
- Risk assessment frameworks
- Sustainability metrics

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@abbgael](https://github.com/abbgael)
- Email: abgaelrehema@gmail.com

## 🙏 Acknowledgments

- PLP Academy for the inspiring assignment
- The cryptocurrency community for educational resources
- Open source developers for tools and inspiration

---

⭐ **Star this repository if you found it helpful!** ⭐

Made with ❤️ and ☕ for the PLP Academy AI Development Track
