# Personal Tax Advisor Agent - Terminal Interface

This terminal interface allows you to interact with your Personal Tax Advisor Agent directly from the command line, just like you're chatting with Claude Code.

## Quick Start

### Option 1: Interactive Mode (Recommended)
```bash
# Windows
tax-agent.bat

# Or directly with Python
python tax-agent-terminal.py
```

### Option 2: Single Question Mode
```bash
# Windows
tax-agent.bat --question "How should I structure my freelance transition?"

# Python
python tax-agent-terminal.py --question "Is Einzelunternehmen optimal for prop firm trading?"
```

## Features

### 1. **Interactive Chat Interface**
- Type questions naturally like in Claude Code
- Get comprehensive tax advice with sovereignty focus
- Conversation history tracking
- Save conversations to markdown files

### 2. **Specialized Analysis Types**
The agent can handle these specific areas:

| Analysis Type | Key Questions |
|--------------|---------------|
| **Freelance** | German freelance transition, Freiberufler vs. Gewerbe, VAT strategy |
| **Brazilian** | MEI compliance, 2-MEI split, cross-border taxation |
| **Citizenship** | Italian passport impact, EU tax residence, 183-day rule |
| **Trading** | Prop firm tax optimization, Einzelunternehmen assessment |
| **GmbH** | ICB Systems ownership formalization, profit distribution |
| **Sovereignty** | Freedom metrics, exit planning, state control minimization |

### 3. **Command Line Options**
```bash
# Interactive mode (default)
python tax-agent-terminal.py

# Ask a single question
python tax-agent-terminal.py --question "Your tax question here"

# Interactive mode explicitly
python tax-agent-terminal.py --interactive
```

### 4. **Built-in Commands**
While in interactive mode:
- `help` - Show all commands and sample questions
- `exit` - Exit the terminal
- `clear` - Clear the screen
- `history` - Show conversation history
- `save` - Save conversation to file
- `summary` - Show agent context summary
- `analysis` - List available analysis types

## Sample Questions to Try

1. **Freelance Transition**
   ```
   "How should I structure my €80,000 freelance income for maximum tax efficiency?"
   ```

2. **Brazilian MEI Compliance**
   ```
   "What's wrong with my current Brazilian MEI setup and how do I fix it?"
   ```

3. **Citizenship Impact**
   ```
   "How does my Italian citizenship approval change my tax planning options?"
   ```

4. **Prop Firm Trading**
   ```
   "Is my Einzelunternehmen the best structure for prop firm trading?"
   ```

5. **GmbH Ownership**
   ```
   "How should I formalize my 30% ownership in ICB Systems GmbH?"
   ```

6. **Sovereignty Focus**
   ```
   "What's my current sovereignty score and how can I improve it?"
   ```

## How It Works

The terminal interface:
1. Loads your Personal Tax Advisor Agent prompt from `wiki/outputs/2026-04-08-personal-tax-advisor-agent.md`
2. Integrates with your other tax analyses (sovereignty, trading, etc.)
3. Uses pattern matching to route questions to specialized handlers
4. Provides formatted, actionable responses with sovereignty focus
5. Maintains conversation history for reference

## Integration with Your Wiki

The agent references these key wiki pages:
- `wiki/outputs/2026-04-08-personal-tax-advisor-agent.md` - Core agent prompt
- `wiki/outputs/2026-04-08-german-self-employment-sovereignty-analysis.md` - Sovereignty principles
- `wiki/outputs/2026-04-08-prop-firm-trading-tax-analysis.md` - Trading optimization
- `wiki/dashboards/tax-planning-dashboard.md` - Overall tax planning

## Usage Examples

### Example 1: Quick Question
```bash
python tax-agent-terminal.py --question "How should I split my Brazilian MEI?"
```

### Example 2: Interactive Session
```bash
python tax-agent-terminal.py
Tax Agent> What's my sovereignty score?
Tax Agent> How can I improve it?
Tax Agent> save
Tax Agent> exit
```

### Example 3: Comprehensive Analysis
```bash
python tax-agent-terminal.py --question "Analyze my entire tax situation with sovereignty focus"
```

## Requirements

- Python 3.6+
- No additional packages required (uses standard library only)

## Files Created

- `tax-agent-terminal.py` - Main Python script
- `tax-agent.bat` - Windows batch file for easy execution
- `tax_agent_conversation_YYYYMMDD_HHMMSS.md` - Saved conversations (when using `save` command)

## Tips for Best Results

1. **Be Specific**: Include numbers (income amounts, percentages, etc.)
2. **Mention Jurisdictions**: Specify if question involves Germany, Brazil, EU, etc.
3. **State Sovereignty Priorities**: Mention if freedom/exit flexibility is key concern
4. **Ask Follow-ups**: The agent builds on previous conversation context
5. **Save Valuable Advice**: Use `save` command to keep important recommendations

## How I Can Access the Agent

As Claude Code, I can also interact with your tax agent by:
1. Reading the agent prompt file
2. Using the same analysis framework
3. Providing consistent advice
4. Updating the agent based on new information

This ensures you get the same quality tax advice whether chatting with me directly or using the terminal interface.

---

**Next Steps**: Run `tax-agent.bat` or `python tax-agent-terminal.py` to start chatting with your Personal Tax Advisor Agent!