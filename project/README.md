# Gerenciador de Faculdade

Este projeto é um gerenciador de faculdade que permite adicionar estudantes, cursos e disciplinas, além de inscrever estudantes em cursos e disciplinas.

## Tecnologias Utilizadas

- Python
- Selenium
- PyScript
- HTML/CSS

## Estrutura do Projeto

- `pages/`
  - `base_page.py`: Contém a classe base para todas as páginas.
  - `student_page.py`: Contém a classe para a página de estudantes.
  - `course_page.py`: Contém a classe para a página de cursos.
  - `discipline_page.py`: Contém a classe para a página de disciplinas.
- `tests/`
  - `test_workflow.py`: Contém os testes para o fluxo de trabalho de adicionar estudantes, cursos e disciplinas.

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. Crie e ative um ambiente virtual:
    cd project
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. pip install -r requirements.txt

4. Executando os Testes
    pytest tests/test_workflow.py