# 🔎 Multi-Agent Research System

An AI-powered multi-agent research system that searches the web, extracts relevant information, generates a structured research report, and evaluates the final report using a critic agent.

## 🚀 Features

- 🔍 **Search Agent** — Searches the web for recent and relevant information using Tavily.
- 📖 **Reader Agent** — Scrapes and extracts useful content from web pages.
- ✍️ **Writer Chain** — Converts collected research into a structured report.
- 🧐 **Critic Chain** — Reviews the generated report and provides a score, strengths, and areas for improvement.
- ⚡ **LLM-powered workflow** — Uses Groq-hosted LLMs through LangChain.
- 🎨 **Streamlit UI** — Simple interface for running the complete research pipeline.

## 🏗️ Architecture

```text
                    User Query
                        │
                        ▼
                ┌───────────────┐
                │  Search Agent │
                └───────┬───────┘
                        │
                        ▼
                  Tavily Search
                        │
                        ▼
                ┌───────────────┐
                │  Reader Agent │
                └───────┬───────┘
                        │
                        ▼
                  URL Scraping
                        │
                        ▼
                ┌───────────────┐
                │  Writer Chain │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │  Critic Chain │
                └───────┬───────┘
                        │
                        ▼
                 Final Research
                     Report