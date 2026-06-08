# Playwright E2E Testing with AI Integration & CI/CD Pipeline

Este repositório contém um projeto completo de automação de testes End-to-End (E2E) focado em qualidade de software moderna. O projeto utiliza o framework **Playwright** com **Python**, integrado à inteligência artificial do **Google Gemini API** para análise e validação dinâmica, além de uma esteira automatizada de **CI/CD** via **GitHub Actions**.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.11**
* **Playwright** (Automação de testes web)
* **Pytest** (Framework de testes e execução)
* **Google GenAI SDK** (Integração com o modelo Gemini)
* **GitHub Actions** (Automação do pipeline de CI/CD)
* **Python-dotenv** (Gerenciamento de variáveis de ambiente locais)

---

## ⚙️ Arquitetura do Projeto

O projeto adota boas práticas de desenvolvimento e organização para testes automatizados:

* **Page Object Model (POM):** Encapsulamento da lógica de interação com as páginas web para maior reusabilidade e manutenção do código.
* **AI-Powered Validation:** Utilização de IA generativa diretamente no fluxo de asserções para analisar cenários complexos (como análise de sentimento ou validação de conteúdo dinâmico).
* **DevSecOps Practices:** Gerenciamento seguro de chaves de API sensíveis utilizando o GitHub Secrets, evitando o vazamento de credenciais no código-fonte.

---

## 📦 Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Josalison/project_playwright.git](https://github.com/Josalison/project_playwright.git)
   cd project_playwright
