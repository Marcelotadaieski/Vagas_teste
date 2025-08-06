# Teste Técnico – Desenvolvedor Full Stack

## Descrição 
Aplicação web desenvolvida com Django para gerenciar vagas e candidatos, incluindo:
- Cadastro e listagem de vagas e candidatos
- Associação Many-to-Many entre candidatos e vagas
- Dashboard interativo com estatísticas
- Análise de dados com Pandas
- Visualização com Chart.js
- Interface responsiva com Bootstrap 5

## Tecnologias  
- Python 3.13.1
- Django 5.2.4
- Pandas  
- Chart.js  
- Bootstrap 5  

## Instalação  
```bash
git clone https://github.com/Marcelotadaieski/Vagas_teste.git
cd Vagas_teste
python3 -m venv venv
source venv/bin/activate        # (No macOS/Linux)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Acesso
Admin: http://127.0.0.1:8000/admin/
Dashboard: http://127.0.0.1:8000/dashboard/

Estrutura
Vagas_teste/
├── core/            
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│   └── templates/
│       └── core/
│           ├── base.html
│           ├── dashboard.html
│           ├── vaga_list.html
│           └── vaga_form.html
├── vaga_bauer/     
├── manage.py
├── requirements.txt
└── .gitignore

## Funcionalidades do Dashboard
- Total de vagas abertas e fechadas
- Número de candidatos por vaga
- Média de idade dos candidatos
- Setor com maior número de vagas abertas
- Visualização em tabela (Pandas) e gráficos (Chart.js)
