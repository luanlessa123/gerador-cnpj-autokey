# Gerador de CNPJ — AutoKey (Python)

## 🧩 Descrição

Gerador simples de CNPJ válido escrito em **Python** para uso com **AutoKey (AutoKey v2)**. O script cria a base do CNPJ (8 dígitos aleatórios + filial "0001"), calcula os dois dígitos verificadores conforme o algoritmo oficial e insere o resultado no campo de texto usando a API de teclado do AutoKey (`keyboard.send_keys`).

> 🧠 Este projeto foi **criado e documentado com auxílio de Inteligência Artificial (IA)**, utilizando ChatGPT (OpenAI).

## ⚙️ Como usar (AutoKey v2)

1. Abra o **AutoKey** no seu sistema Linux.
2. Crie um novo **Script** (Novo → Script).
3. Cole o conteúdo do arquivo `autokey/gerador-cnpj-autokey.py` no editor do AutoKey.
4. Salve o script e atribua uma **hotkey** (exemplo: `Ctrl + Alt + G`).
5. Vá a qualquer campo de texto e pressione a hotkey. O script irá gerar automaticamente um CNPJ e inserir no campo ativo.

### Observações técnicas
- O script gera a parte base do CNPJ como: 8 dígitos aleatórios + filial `0001`.
- Em seguida calcula o primeiro e o segundo dígitos verificadores usando os pesos apropriados e concatena tudo formando os 14 dígitos.
- O exemplo final usa `keyboard.send_keys(cnpj)` para enviar o número ao campo ativo dentro do AutoKey.

---

## ⚠️ Aviso de uso

Este gerador de CNPJ foi criado **exclusivamente para fins de teste, automação e desenvolvimento de software**.
**Não utilize CNPJs gerados em cadastros reais, sistemas oficiais, transações financeiras ou qualquer atividade ilegal.**

O objetivo é facilitar o preenchimento de formulários de teste e o desenvolvimento de scripts e automações que exigem dados fictícios.
