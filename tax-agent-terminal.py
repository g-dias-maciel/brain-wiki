#!/usr/bin/env python3
"""
Tax Advisor Agent Terminal Interface

This script provides a terminal interface to interact with the Personal Tax Advisor Agent.
It loads the agent prompt and allows you to ask tax-related questions in a conversational format.

Usage:
    python tax-agent-terminal.py
    python tax-agent-terminal.py --question "Your tax question here"
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

# Add the current directory to the path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class TaxAgentTerminal:
    def __init__(self, wiki_root="wiki"):
        """Initialize the Tax Agent Terminal interface."""
        self.wiki_root = Path(wiki_root)
        self.agent_prompt_path = self.wiki_root / "outputs" / "2026-04-08-personal-tax-advisor-agent.md"
        self.tax_dashboard_path = self.wiki_root / "dashboards" / "tax-planning-dashboard.md"
        self.sovereignty_analysis_path = self.wiki_root / "outputs" / "2026-04-08-german-self-employment-sovereignty-analysis.md"
        self.prop_trading_analysis_path = self.wiki_root / "outputs" / "2026-04-08-prop-firm-trading-tax-analysis.md"

        # Load agent prompt and related documents
        self.agent_prompt = self._load_file(self.agent_prompt_path)
        self.tax_dashboard = self._load_file(self.tax_dashboard_path)
        self.sovereignty_analysis = self._load_file(self.sovereignty_analysis_path)
        self.prop_trading_analysis = self._load_file(self.prop_trading_analysis_path)

        # Extract key information from agent prompt
        self.agent_info = self._parse_agent_prompt()

        # Conversation history
        self.conversation_history = []

    def _load_file(self, filepath):
        """Load a file from the wiki."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"File not found: {filepath}"
        except Exception as e:
            return f"Error loading file: {str(e)}"

    def _parse_agent_prompt(self):
        """Parse the agent prompt to extract key information."""
        info = {
            'purpose': '',
            'focus_areas': [],
            'client_info': {},
            'sovereignty_insights': [],
            'sample_prompts': []
        }

        lines = self.agent_prompt.split('\n')
        in_purpose = False
        in_focus_areas = False
        in_client_info = False
        in_sovereignty_insights = False
        in_sample_prompts = False

        for line in lines:
            if '**Purpose**:' in line:
                info['purpose'] = line.split('**Purpose**:')[1].strip()
            elif '**Focus Areas**:' in line:
                info['focus_areas'] = [area.strip() for area in line.split('**Focus Areas**:')[1].split(',')]
            elif 'Your primary client is Gabriel Dias' in line:
                in_client_info = True
            elif '**Key Sovereignty Insights from Analysis**:' in line:
                in_sovereignty_insights = True
            elif '### For Specific Questions' in line:
                in_sample_prompts = True
            elif in_sample_prompts and '```' in line:
                in_sample_prompts = False
            elif in_sample_prompts and line.strip():
                info['sample_prompts'].append(line.strip())

        return info

    def get_context_summary(self):
        """Get a summary of the tax agent context."""
        summary = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                     PERSONAL TAX ADVISOR AGENT - TERMINAL                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

Purpose: {self.agent_info['purpose']}

Focus Areas:
{chr(10).join(f'  • {area}' for area in self.agent_info['focus_areas'])}

Key Sovereignty Principles:
  • "Free from state, or at least be free to leave whenever I want to"
  • Freiberufler offers superior sovereignty vs. Gewerbe
  • Italian citizenship transforms exit flexibility (passport pending)
  • Brazilian MEI currently non-compliant (R$8,500 > R$6,750 limit)
  • V0050 social security exemption available for Freiberufler

Available Analyses:
  • German Self-Employment Sovereignty Analysis
  • Prop Firm Trading Tax Optimization Analysis
  • Tax Planning Dashboard

Sample Questions:
  1. "How should I structure my freelance transition for maximum tax efficiency?"
  2. "What's the optimal way to split the Brazilian MEI for compliance?"
  3. "How does my Italian citizenship affect my German tax planning?"
  4. "Is Einzelunternehmen the best structure for prop firm trading?"
  5. "What are the tax implications of my informal GmbH ownership?"

Type 'help' for commands, 'exit' to quit.
"""
        return summary

    def process_question(self, question):
        """Process a tax question and generate a response."""
        # Add to conversation history
        self.conversation_history.append({
            'timestamp': datetime.now().isoformat(),
            'role': 'user',
            'content': question
        })

        # Generate response based on question type
        response = self._generate_response(question)

        # Add response to history
        self.conversation_history.append({
            'timestamp': datetime.now().isoformat(),
            'role': 'agent',
            'content': response
        })

        return response

    def _generate_response(self, question):
        """Generate a response based on the question."""
        question_lower = question.lower()

        # Check for specific question patterns
        if any(word in question_lower for word in ['freelance', 'freiberufler', 'self-employment']):
            return self._handle_freelance_question(question)
        elif any(word in question_lower for word in ['brazil', 'mei', 'brazilian']):
            return self._handle_brazilian_question(question)
        elif any(word in question_lower for word in ['italian', 'citizenship', 'passport', 'niederlassungserlaubnis']):
            return self._handle_citizenship_question(question)
        elif any(word in question_lower for word in ['prop firm', 'trading', 'einzelunternehmen']):
            return self._handle_trading_question(question)
        elif any(word in question_lower for word in ['gmbh', 'icb', 'ownership']):
            return self._handle_gmbh_question(question)
        elif any(word in question_lower for word in ['sovereignty', 'freedom', 'exit']):
            return self._handle_sovereignty_question(question)
        elif any(word in question_lower for word in ['tax', 'optimization', 'planning']):
            return self._handle_general_tax_question(question)
        else:
            return self._handle_general_question(question)

    def _handle_freelance_question(self, question):
        """Handle questions about German freelance transition."""
        response = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    GERMAN FREELANCE TRANSITION ANALYSIS                      ║
╚══════════════════════════════════════════════════════════════════════════════╝

Based on your question: "{question}"

KEY RECOMMENDATIONS:

1. **Business Structure**: Choose Freiberufler over Gewerbe for sovereignty
   • No trade tax (Gewerbesteuer) - saves ~15%
   • Simpler exit process (no Gewerbeabmeldung)
   • Less state control and reporting burden

2. **VAT Strategy**:
   • If projected revenue < €22,000: Use Kleinunternehmerregelung (no VAT filing)
   • If > €22,000 or high business expenses: Regular VAT (19%) to deduct input VAT

3. **Social Security**: Apply for V0050 exemption
   • 3-year freedom from German social system
   • Must prove sufficient private health insurance
   • Critical for sovereignty and cost reduction

4. **Expense Deductions** (maximize these):
   • Home office (proportional rent, utilities, internet)
   • Computer equipment and software
   • Professional education and courses
   • Business travel and conferences
   • Professional memberships and subscriptions

5. **Transition Timing**:
   • Coordinate with employment contract end date
   • Consider tax bracket implications
   • Plan cash flow for first 3-6 months

SOVEREIGNTY IMPACT:
• Freiberufler: 🟢 High exit flexibility, low state control
• Gewerbe: 🔴 Complex exit, high state control

ACTION PLAN:
1. Register as Freiberufler with Finanzamt
2. Apply for V0050 exemption with health insurance proof
3. Choose Kleinunternehmerregelung if eligible
4. Set up business expense tracking system
5. Consult tax advisor for specific deduction strategies

For detailed calculations, provide your projected freelance income and expenses.
"""
        return response

    def _handle_brazilian_question(self, question):
        """Handle questions about Brazilian MEI optimization."""
        response = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    BRAZILIAN MEI OPTIMIZATION ANALYSIS                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

Based on your question: "{question}"

CURRENT SITUATION:
• Revenue: R$8,500/month via mother's MEI
• MEI Limit: R$6,750/month (R$81,000/year)
• Status: NON-COMPLIANT (exceeds limit by R$1,750/month)
• Sovereignty Risk: 🔴 High (state exposure, potential penalties)

RECOMMENDED SOLUTION: 2-MEI Split Strategy

1. **Split Structure**:
   • MEI 1 (Mother): R$6,750/month (at limit)
   • MEI 2 (You or family member): R$1,750/month
   • Total: R$8,500/month (compliant)

2. **Implementation Steps**:
   a. Register second MEI (can be in your name or trusted family member)
   b. Split client contracts between two MEIs
   c. Maintain separate bank accounts for each MEI
   d. Issue separate invoices from each MEI

3. **German Tax Implications**:
   • Both MEI incomes must be declared in German tax return
   • Brazil-Germany tax treaty may provide relief
   • Consider permanent establishment risk if managed from Germany

4. **Alternative: Proper Entity** (if scaling beyond R$10,000/month):
   • Consider LTDA (limited liability company)
   • Higher compliance but better legal protection
   • More professional for international clients

SOVEREIGNTY CONSIDERATIONS:
• Current non-compliance creates state exposure risk
• 2-MEI split reduces audit risk and state scrutiny
• Proper documentation minimizes cross-border attribution risk

ACTION PLAN:
1. Immediately implement 2-MEI split to become compliant
2. Document business rationale for split (different services/clients)
3. Set up proper invoicing and accounting for both MEIs
4. Consult Brazilian accountant for optimal split structure
5. Update German tax advisor on new structure

For specific implementation details, provide your client structure and service offerings.
"""
        return response

    def _handle_citizenship_question(self, question):
        """Handle questions about Italian citizenship and residency."""
        response = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║               ITALIAN CITIZENSHIP & RESIDENCY OPTIMIZATION                   ║
╚══════════════════════════════════════════════════════════════════════════════╝

Based on your question: "{question}"

CURRENT STATUS:
• German: Niederlassungserlaubnis (permanent residence)
• Italian: Citizenship approved (March 2026), passport pending
• Sovereignty Impact: Italian passport is SINGLE MOST IMPACTFUL upgrade

IMMEDIATE ACTION: EXPEDITE ITALIAN PASSPORT
• Contact Italian consulate for fastest processing
• Target: 60-day issuance timeline
• Cost: Acceptable for sovereignty transformation

WITH ITALIAN PASSPORT (Projected Sovereignty):
• German Exit Flexibility: 9/10 (vs 5/10 currently)
• EU Mobility: 10/10 (27 countries + global visa-free)
• Tax Residence Options: 8/10 (multiple EU options)
• Overall Sovereignty: 8.75/10 (vs 3.5/10 currently)

TAX RESIDENCE STRATEGIES:

1. **German Tax Residence** (Current):
   • 183-day rule primary test
   • Center of vital interests in Germany
   • High taxes but established business base

2. **Portuguese NHR** (Non-Habitual Resident):
   • 10-year special tax regime
   • Foreign income potentially tax-free
   • Requires <183 days in Germany
   • Ideal for freelance income

3. **Malta**:
   • 15% corporate tax with refunds
   • Favorable for business income
   • EU member with English business environment

4. **Cyprus**:
   • 60-day rule for tax residence
   • Low corporate and personal taxes
   • Favorable for investment income

5. **Estonia** (e-Residency):
   • 0% corporate tax on retained profits
   • 20% tax on distributions only
   • Digital nomad friendly
   • Compliance complexity with German CFC rules

PRACTICAL STRATEGY: DUAL RESIDENCE
• Maintain Niederlassungserlaubnis for German business operations
• Establish tax residence in Portugal/Malta/Cyprus
• Keep <183 days in Germany per year
• Use Italian passport for EU freedom of movement

ACTION PLAN:
1. Expedite Italian passport (Week 1-2)
2. Research EU tax options (Portugal NHR, Malta, Cyprus)
3. Plan <183 days in Germany strategy
4. Open EU bank account (Revolut Business EU entity)
5. Consult EU tax specialist for cross-border planning

For specific country comparisons, provide your income sources and travel patterns.
"""
        return response

    def _handle_trading_question(self, question):
        """Handle questions about prop firm trading tax optimization."""
        response = f"""
╔══════════════════════════════════════════════════════════════════════════════╝
║                 PROP FIRM TRADING TAX OPTIMIZATION                           ║
╚══════════════════════════════════════════════════════════════════════════════╝

Based on your question: "{question}"

KEY FINDING: Einzelunternehmen is SUBOPTIMAL for prop firm trading

TAX TREATMENT ANALYSIS:

1. **Current Einzelunternehmen (Gewerbe)**:
   • Income Classification: Business income (Gewerbebetrieb)
   • Trade Tax: 14-17% effective rate
   • Income Tax: Progressive rates (14-45%)
   • Total Effective Rate: ~40-50%
   • Sovereignty Impact: 🔴 High state control, complex exit

2. **Alternative: Freiberufler** (If Possible):
   • Income Classification: Professional services income
   • Trade Tax: EXEMPT (saves ~15%)
   • Total Effective Rate: ~30-40%
   • Sovereignty Impact: 🟢 Lower state control, simpler exit
   • Likelihood for Trading: Low (trading rarely qualifies)

3. **Alternative: Personal Trading**:
   • Requirements: Occasional trading only
   • Tax: Capital gains tax (Abgeltungsteuer) 25% + solidarity
   • Sovereignty Impact: 🟢 High (no business registration)
   • Risk: Reclassification as business by tax office

RECOMMENDED HYBRID APPROACH:

Phase 1: Immediate Optimization (1 month)
1. Review Trading Scale: If <€1,000/month, consider personal trading
2. Attempt Freiberufler Argument: Frame as "financial analysis services"
3. Optimize Einzelunternehmen: Apply Kleinunternehmerregelung if <€22,000

Phase 2: Structural Optimization (1-3 months)
1. Evaluate Trading Volume: Keep separate from main freelance business
2. Sovereignty-Focused Structure: Maintain clean separation for exit
3. Tax Planning Integration: Coordinate with overall tax strategy

Phase 3: Long-term (3-12 months)
1. With Italian Passport: Consider EU-based trading entity
2. Scale Assessment: Re-evaluate if trading grows significantly

CRITICAL QUESTIONS FOR TAX ADVISOR:
1. "Based on my trading frequency/volume, what's the most likely classification?"
2. "What evidence supports Freiberufler classification for prop firm trading?"
3. "At what income level does GmbH become tax-efficient for trading?"

FINAL RECOMMENDATION:
• For Now: Optimize current Einzelunternehmen while exploring Freiberufler possibility
• Short-term: Maximize deductions, consider Kleinunternehmer VAT option
• Medium-term: Evaluate separation from main freelance business for sovereignty
• Long-term: With Italian passport, consider EU-based structure for maximum freedom

For specific advice, provide your monthly trading volume and frequency.
"""
        return response

    def _handle_gmbh_question(self, question):
        """Handle questions about ICB Systems GmbH ownership."""
        response = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    ICB SYSTEMS GMBH OWNERSHIP FORMALIZATION                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

Based on your question: "{question}"

CURRENT SITUATION:
• Company: ICB Systems GmbH (German software company)
• Your Stake: 30% informal ownership
• Status: Not documented, not formalized
• Sovereignty Risk: 🔴 High (legal vulnerability, state claim risk)

URGENCY: HIGH - Formalize before Italian passport obtained

FORMALIZATION OPTIONS:

1. **Direct Shareholding** (Simplest):
   • Register 30% ownership in commercial register
   • Become official Gesellschafter (shareholder)
   • Tax: Receive profit distributions, subject to personal income tax
   • Sovereignty: Medium (German corporate structure)

2. **Holding Structure** (More Complex):
   • Create holding company (GmbH or foreign entity)
   • Holding owns 30% of ICB Systems
   • You own holding company
   • Tax: Potential deferral benefits, more planning options
   • Sovereignty: Higher (separation layer, potential international holding)

3. **Profit Participation Rights** (Alternative):
   • Instead of shares, receive profit participation certificates
   • Similar economic rights without voting control
   • Tax: Treated as business income
   • Sovereignty: Simpler exit, less corporate entanglement

TAX IMPLICATIONS:

1. **Profit Distributions**:
   • Subject to 25% capital gains tax (Abgeltungsteuer) + solidarity
   • Can be offset by previous losses if any
   • Must be declared in annual tax return

2. **Salary vs. Dividends**:
   • Salary: Subject to income tax, social security contributions
   • Dividends: 25% flat tax, no social security
   • Optimal mix depends on overall income level

3. **Corporate Level**:
   • GmbH corporate tax: ~30% (15% corporate + 15% trade tax approx.)
   • After-tax profits available for distribution

SOVEREIGNTY CONSIDERATIONS:

1. **Current Informal Status**:
   • High legal vulnerability
   • No asset protection
   • Difficult to exit or sell stake
   • State could challenge ownership

2. **Formal German Structure**:
   • Legal protection for your stake
   • Clear exit mechanisms
   • Still subject to German corporate law
   • Exit requires formal process

3. **International Holding**:
   • With Italian passport: Consider EU holding company
   • Malta, Cyprus, Portugal options
   • More exit flexibility
   • Higher compliance complexity

ACTION PLAN:

Immediate (Week 1-2):
1. Document current informal agreement (emails, messages, understandings)
2. Consult German corporate lawyer for formalization options
3. Negotiate formal shareholder agreement with other owners

Short-term (Month 1):
1. Choose formalization structure (direct vs. holding)
2. Prepare necessary documents
3. Register ownership in commercial register

Medium-term (Month 2-3):
1. Set up profit distribution mechanism
2. Plan tax-optimal salary/dividend mix
3. Integrate with overall tax planning

Long-term (With Italian Passport):
1. Consider restructuring with EU holding company
2. Evaluate international expansion of ICB Systems
3. Plan eventual exit or sale strategy

CRITICAL QUESTIONS:
1. "What are the other owners' preferences for formalization?"
2. "What is the current valuation of ICB Systems?"
3. "Are there any existing shareholder agreements or articles of association?"
4. "What are the growth projections and profit expectations?"

For specific advice, provide details about company valuation and other owners' positions.
"""
        return response

    def _handle_sovereignty_question(self, question):
        """Handle questions about sovereignty and freedom-focused tax planning."""
        response = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    SOVEREIGNTY-FOCUSED TAX PLANNING                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

Based on your question: "{question}"

CORE SOVEREIGNTY OBJECTIVE:
"Free from state, or at least be free to leave whenever I want to"

KEY SOVEREIGNTY PRINCIPLES FROM ANALYSIS:

1. **Freiberufler vs. Gewerbe**:
   • Freiberufler: No trade tax, simpler exit, less state oversight
   • Gewerbe: Trade tax burden, complex exit, higher state control
   • Recommendation: Always prefer Freiberufler classification when possible

2. **State Control Minimization**:
   • Avoid business forms with high reporting requirements
   • Minimize interactions with tax authorities
   • Use digital/automated systems where possible
   • Keep business structures simple and transparent

3. **Exit Flexibility**:
   • Structure for quick unwinding if needed
   • Avoid long-term contracts with cancellation penalties
   • Maintain portable income streams
   • Keep assets mobile and internationally accessible

4. **Asset Protection**:
   • Diversify assets across jurisdictions
   • Use international banking options
   • Consider asset protection structures
   • Maintain emergency funds outside Germany

5. **International Mobility**:
   • Leverage Italian citizenship for EU freedom
   • Plan multiple residency options
   • Structure income for location independence
   • Minimize physical presence requirements

CURRENT SOVEREIGNTY SCORE: 3.5/10
• German Exit Flexibility: 5/10 (Niederlassungserlaubnis only)
• EU Mobility: 2/10 (Italian passport pending)
• Tax Residence Options: 3/10 (Limited to Germany)
• Asset Protection: 4/10 (German-centric)

WITH ITALIAN PASSPORT (Projected): 8.75/10
• German Exit Flexibility: 9/10
• EU Mobility: 10/10
• Tax Residence Options: 8/10
• Asset Protection: 8/10

SOVEREIGNTY-FOCUSED TAX STRATEGIES:

1. **German Operations**:
   • Register as Freiberufler (not Gewerbe)
   • Apply for V0050 social security exemption
   • Use Kleinunternehmerregelung if eligible
   • Maximize digital/remote operations

2. **International Structure**:
   • With Italian passport: Establish EU tax residence
   • Consider Portugal NHR for freelance income
   • Maintain German business address but not tax residence
   • Keep <183 days in Germany annually

3. **Asset Strategy**:
   • Move 30%+ assets outside Germany
   • Use EU-based banking (Revolut Business EU)
   • Consider cryptocurrency for portable value
   • Maintain emergency fund in stable currency

4. **Exit Planning**:
   • Develop 30-day Germany exit plan
   • Document all business processes for remote management
   • Secure international payment channels
   • Establish backup locations in EU

ACTION PLAN FOR MAXIMUM SOVEREIGNTY:

Week 1-2:
1. Expedite Italian passport process
2. Research Portugal NHR requirements
3. Open EU bank account

Month 1-3:
1. Register German Freiberufler business
2. Apply for V0050 exemption
3. Move initial assets outside Germany
4. Test remote work from Portugal/Spain

Month 4-6:
1. Establish EU tax residence
2. Achieve <183 days in Germany
3. Diversify income streams internationally
4. Create comprehensive exit plan

Month 7-12:
1. Full exit readiness (30-day capability)
2. Multiple EU residency options
3. International asset protection structure
4. Sovereign digital infrastructure

For specific sovereignty metrics, provide your current asset locations and travel patterns.
"""
        return response

    def _handle_general_tax_question(self, question):
        """Handle general tax optimization questions."""
        response = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    GENERAL TAX OPTIMIZATION ANALYSIS                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

Based on your question: "{question}"

COMPREHENSIVE TAX OPTIMIZATION FRAMEWORK:

1. **Income Stream Analysis**:
   • German employment: Fixed salary, high tax burden
   • German freelance: Target €80,000/year, Freiberufler preferred
   • Brazilian MEI: R$8,500/month, needs 2-MEI split
   • Prop firm trading: Supplementary income, tax structure optimization needed
   • ICB Systems GmbH: 30% informal ownership, urgent formalization needed
   • CAJU Wear GbR: Pre-launch, planning phase

2. **Jurisdictional Optimization**:
   • Germany: High taxes but established base
   • Brazil: Low MEI taxes but compliance issues
   • EU Options: Portugal NHR, Malta, Cyprus with Italian passport
   • International: Consider for future scaling

3. **Timing Optimization**:
   • Transition from employment to freelance: Coordinate tax years
   • Brazilian MEI split: Implement immediately for compliance
   • GmbH formalization: Complete before Italian passport
   • EU tax residence: Plan for next tax year

4. **Deduction Maximization**:
   • Home office: Proportional rent, utilities, internet
   • Business equipment: Computers, software, office supplies
   • Professional development: Courses, conferences, memberships
   • Travel expenses: Business-related travel
   • Vehicle expenses: If used for business

5. **Risk Management**:
   • Brazilian MEI non-compliance: Immediate split required
   • Informal GmbH ownership: Urgent formalization needed
   • Permanent establishment risk: Document remote work arrangements
   • Transfer pricing: Arm's length documentation for related parties

INTEGRATED TAX STRATEGY:

Phase 1: Foundation (1-3 months)
1. Register German Freiberufler business
2. Implement Brazilian 2-MEI split
3. Formalize ICB Systems GmbH ownership
4. Optimize prop firm trading structure

Phase 2: Optimization (4-6 months)
1. Obtain Italian passport
2. Research EU tax residence options
3. Establish international banking
4. Implement comprehensive expense tracking

Phase 3: Sovereignty (7-12 months)
1. Establish EU tax residence
2. Achieve <183 days in Germany
3. Diversify assets internationally
4. Create full exit readiness

KEY METRICS TO TRACK:
• Effective tax rate (target: <30%)
• Non-German revenue percentage (target: >30%)
• Exit readiness score (target: 80/100)
• State reporting burden (target: <10 hours/month)

PROFESSIONAL SUPPORT NEEDED:
1. German tax advisor (Freiberufler specialist)
2. Brazilian accountant (MEI compliance)
3. EU tax specialist (cross-border planning)
4. Corporate lawyer (GmbH formalization)

For specific calculations, provide your income projections and expense estimates.
"""
        return response

    def _handle_general_question(self, question):
        """Handle general questions not covered by specific categories."""
        response = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    TAX ADVISOR AGENT RESPONSE                                ║
╚══════════════════════════════════════════════════════════════════════════════╝

Based on your question: "{question}"

As your Personal Tax Advisor Agent with sovereignty focus, I analyze your question through multiple lenses:

1. **Tax Efficiency**: How to minimize your overall tax burden
2. **Compliance**: How to remain legally compliant in all jurisdictions
3. **Sovereignty**: How to maximize freedom from state control and exit flexibility
4. **Practicality**: How to implement recommendations with minimal disruption

GENERAL GUIDANCE:

For comprehensive tax advice, please provide:
• Specific income amounts and sources
• Current business structures and registrations
• Residency status and travel patterns
• Short-term and long-term business goals
• Risk tolerance and sovereignty priorities

AVAILABLE SPECIALIZED ANALYSES:

1. **German Freelance Transition**: Optimal structure, deductions, VAT strategy
2. **Brazilian MEI Optimization**: 2-MEI split, compliance, cross-border implications
3. **Italian Citizenship Impact**: EU tax residence options, mobility planning
4. **Prop Firm Trading**: Tax classification, structure optimization, sovereignty impact
5. **GmbH Ownership**: Formalization options, tax treatment, exit strategies
6. **Sovereignty-Focused Planning**: Freedom metrics, exit readiness, state control minimization

SAMPLE QUESTIONS FOR MORE SPECIFIC ADVICE:

• "What's the optimal business structure for my €80,000 freelance income?"
• "How should I split my Brazilian MEI to remain compliant?"
• "What EU country offers the best tax regime with my Italian passport?"
• "Is my current Einzelunternehmen optimal for prop firm trading?"
• "How do I formalize my 30% GmbH ownership tax-efficiently?"
• "What's my sovereignty score and how can I improve it?"

To get started, please ask a more specific question or provide details about your situation.
"""
        return response

    def get_help(self):
        """Get help information for the terminal interface."""
        help_text = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    TAX AGENT TERMINAL - HELP                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

COMMANDS:
  help          - Show this help message
  exit          - Exit the terminal interface
  clear         - Clear the screen
  history       - Show conversation history
  save          - Save conversation to file
  summary       - Show agent context summary
  analysis      - Show available analysis types

ANALYSIS TYPES:
  freelance     - German freelance transition optimization
  brazil        - Brazilian MEI optimization and compliance
  citizenship   - Italian citizenship and EU tax residence planning
  trading       - Prop firm trading tax optimization
  gmbh          - ICB Systems GmbH ownership formalization
  sovereignty   - Sovereignty-focused tax planning
  general       - General tax optimization advice

SAMPLE QUESTIONS:
  • "How should I structure my freelance transition?"
  • "What's wrong with my Brazilian MEI setup?"
  • "How does Italian citizenship help my tax planning?"
  • "Is Einzelunternehmen good for prop firm trading?"
  • "How do I formalize my GmbH ownership?"
  • "What's my sovereignty score and how to improve it?"

USAGE TIPS:
  • Be specific with income amounts and business details
  • Mention all relevant jurisdictions (Germany, Brazil, EU)
  • Include your sovereignty priorities
  • Ask follow-up questions for clarification
  • Save important conversations for reference

QUICK START:
  1. Type 'summary' to see your current tax context
  2. Ask a specific question about your tax situation
  3. Use 'analysis' to see available specialized analyses
  4. Type 'save' to save valuable recommendations

For command-line usage: python tax-agent-terminal.py --question "Your question here"
"""
        return help_text

    def show_history(self):
        """Show conversation history."""
        if not self.conversation_history:
            return "No conversation history yet."

        history_text = "╔══════════════════════════════════════════════════════════════════════════════╗\n"
        history_text += "║                    CONVERSATION HISTORY                                      ║\n"
        history_text += "╚══════════════════════════════════════════════════════════════════════════════╝\n\n"

        for i, entry in enumerate(self.conversation_history, 1):
            role = "You" if entry['role'] == 'user' else "Agent"
            timestamp = entry['timestamp'][11:19]  # Just time part
            history_text += f"[{timestamp}] {role}:\n"
            history_text += f"{entry['content']}\n"
            history_text += "-" * 80 + "\n"

        return history_text

    def save_conversation(self, filename=None):
        """Save conversation history to file."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"tax_agent_conversation_{timestamp}.md"

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("# Tax Agent Conversation\n\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

                for entry in self.conversation_history:
                    role = "## User" if entry['role'] == 'user' else "## Agent"
                    f.write(f"{role} ({entry['timestamp']})\n\n")
                    f.write(f"{entry['content']}\n\n")
                    f.write("---\n\n")

            return f"Conversation saved to {filename}"
        except Exception as e:
            return f"Error saving conversation: {str(e)}"

    def show_analysis_types(self):
        """Show available analysis types."""
        analysis_text = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    AVAILABLE ANALYSIS TYPES                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

1. FREELANCE ANALYSIS
   • German freelance transition optimization
   • Freiberufler vs. Gewerbe comparison
   • VAT strategy (Kleinunternehmerregelung)
   • V0050 social security exemption
   • Business expense maximization
   • Tax bracket management

2. BRAZILIAN ANALYSIS
   • MEI compliance optimization
   • 2-MEI split strategy implementation
   • Cross-border tax implications
   • Profit extraction strategies
   • Scaling beyond MEI limits

3. CITIZENSHIP ANALYSIS
   • Italian passport expedited processing
   • EU tax residence options (Portugal NHR, Malta, Cyprus)
   • Dual residence strategies
   • 183-day rule optimization
   • International mobility planning

4. TRADING ANALYSIS
   • Prop firm trading tax classification
   • Einzelunternehmen optimization
   • Freiberufler possibility exploration
   • Personal trading vs. business trading
   • Sovereignty impact assessment

5. GMBH ANALYSIS
   • ICB Systems ownership formalization
   • Shareholding vs. holding structures
   • Profit distribution optimization
   • Tax-efficient salary/dividend mix
   • Exit strategy planning

6. SOVEREIGNTY ANALYSIS
   • Freedom metrics calculation
   • State control minimization
   • Exit flexibility optimization
   • Asset protection strategies
   • International mobility planning

7. GENERAL TAX OPTIMIZATION
   • Integrated multi-jurisdiction planning
   • Timing optimization strategies
   • Deduction maximization
   • Risk management frameworks
   • Professional support planning

HOW TO USE:
• Ask questions mentioning key terms from above
• Be specific about which analysis type you need
• Provide relevant numbers (income, expenses, etc.)
• Mention your sovereignty priorities

EXAMPLE QUESTIONS:
• "Analyze my freelance transition for maximum sovereignty"
• "What's the optimal Brazilian MEI structure for compliance?"
• "How does Italian citizenship change my EU tax options?"
• "Is my current trading structure tax-optimal?"
• "How should I formalize my GmbH ownership?"
• "What's my current sovereignty score and how to improve it?"
"""
        return analysis_text

def main():
    """Main function for the terminal interface."""
    parser = argparse.ArgumentParser(description='Tax Advisor Agent Terminal Interface')
    parser.add_argument('--question', '-q', type=str, help='Ask a tax question directly')
    parser.add_argument('--interactive', '-i', action='store_true', help='Start interactive mode')
    args = parser.parse_args()

    # Create tax agent terminal
    agent = TaxAgentTerminal()

    if args.question:
        # Process single question from command line
        print(agent.get_context_summary())
        print("\n" + "="*80 + "\n")
        response = agent.process_question(args.question)
        print(response)

        # Ask if user wants to save
        save = input("\nSave this conversation? (y/n): ").lower()
        if save == 'y':
            result = agent.save_conversation()
            print(result)
    else:
        # Start interactive mode
        print(agent.get_context_summary())

        while True:
            try:
                user_input = input("\nTax Agent> ").strip()

                if not user_input:
                    continue

                if user_input.lower() == 'exit':
                    print("Exiting Tax Agent Terminal. Goodbye!")
                    break
                elif user_input.lower() == 'help':
                    print(agent.get_help())
                elif user_input.lower() == 'clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(agent.get_context_summary())
                elif user_input.lower() == 'history':
                    print(agent.show_history())
                elif user_input.lower() == 'save':
                    filename = input("Enter filename (or press Enter for default): ").strip()
                    if filename:
                        result = agent.save_conversation(filename)
                    else:
                        result = agent.save_conversation()
                    print(result)
                elif user_input.lower() == 'summary':
                    print(agent.get_context_summary())
                elif user_input.lower() == 'analysis':
                    print(agent.show_analysis_types())
                else:
                    response = agent.process_question(user_input)
                    print(response)

            except KeyboardInterrupt:
                print("\n\nExiting Tax Agent Terminal. Goodbye!")
                break
            except EOFError:
                print("\n\nExiting Tax Agent Terminal. Goodbye!")
                break
            except Exception as e:
                print(f"\nError: {str(e)}")
                print("Please try again or type 'help' for assistance.")

if __name__ == "__main__":
    main()